import os
import re
import shutil
import argparse
from datetime import datetime


# The main interpreter. It mostly replaces the tags written as <mytag/>
# with the relevant parts of code. Static website, bla bla bla.
class StaticGenerator:
    root = os.getcwd()  # Root directory
    components = {}
    templates = {}
    args = {}

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", dest="file", default="all", help="Files to be generated")

        self.args = parser.parse_args()

    def run(self):
        self.load_resources()
        self.build_posts()
        self.build_home()

    # I load the resources by creating dictionaries with html content inside.
    def load_resources(self):
        print("Loading up components:")
        for obj in os.listdir("src/components"):
            print(" - " + obj)
            name = os.path.splitext(obj)[0]
            self.components[name] = open(f"{self.root}/src/components/{obj}").read()

        print("Loading up templates:")
        for obj in os.listdir("src/templates"):
            print(" - " + obj)
            name = os.path.splitext(obj)[0]
            self.templates[name] = open(f"{self.root}/src/templates/{obj}").read()

        print("Loaded resources successfully.")

    # After loading up the resources, I can compile them progressively.
    # Sometimes, components may be inside components and I have to loop
    # until there are no more components.
    def build_posts(self):
        print("Beginning to process the posts!")

        # Latest build is also in /view
        if os.path.isdir(f"{self.root}/view/"):
            shutil.rmtree(f"{self.root}/view/")

        os.mkdir(f"{self.root}/view/")

        # Posts are like "projects" - they can contain html, css and js files.
        for post in os.listdir("post/"):

            # If we specify a file using the -f flag, we will skip other posts
            if self.args.file != 'all' and self.args.file != post:
                print(f" - '{post}' skipped.")
                continue

            # Only one html allowed. Multiple css and js files can be imported.
            objects = {
                "html": "Empty",
                "css": [],
                "js": []
            }

            # Iterate through all the post objects and place them selectively
            for obj in os.listdir(f"post/{post}/"):
                if obj.find(".html") == -1 and obj.find(".css") == -1 and obj.find(".js") == -1 and obj != "meta.txt":
                    continue

                content = open(f"{self.root}/post/{post}/{obj}").read()

                if obj.find(".html") != -1:
                    objects["html"] = content
                elif obj.find(".css") != -1:
                    objects["css"].append(content)
                elif obj.find(".js") != -1:
                    objects["js"].append(content)
                elif obj == "meta.txt":
                    metadata = content.splitlines()
                    objects["title"] = metadata[0]
                    objects["date"] = metadata[1]

            # Replacing all the tags in a somewhat recursive (but not actually) manner.
            output = self.templates["post"].replace("<mycontent/>", objects["html"])
            while tags := re.findall("<my([a-z]+)(\(.+\))?\/>", output):
                for tag in tags:
                    html_tag = "<my" + tag[0] + tag[1] + "/>"
                    stripped_tag = tag[0]

                    arguments = tag[1].removeprefix("(")
                    arguments = arguments.removesuffix(")")

                    if arguments:
                        arguments = arguments.split("|")

                    if stripped_tag == "script":
                        to_replace = ""
                        for script in objects["js"]:
                            to_replace += f"<script>{script}</script>\n"
                            
                        output = output.replace(html_tag, to_replace)
                    elif stripped_tag == "style":
                        to_replace = ""
                        for style in objects["css"]:
                            to_replace += f"<style>{style}</style>\n"
                            
                        output = output.replace(html_tag, to_replace)
                    elif stripped_tag == "title":
                        output = output.replace(html_tag, objects["title"])
                    elif stripped_tag == "date":
                        output = output.replace(html_tag, objects["date"])
                    else:
                        component_content = self.components[stripped_tag]
                        i = 1
                        for arg in arguments:
                            component_content = component_content.replace(f"${i}$", arg)
                            i += 1
                        
                        output = output.replace(html_tag, component_content)
            
            with open(f"{self.root}/view/{post}.html", "w") as file:
	            file.write(output)

            print(f" - '{post}' processed!")

        print("Finished processing the posts.")

    # I build special pages separately.
    def build_home(self):
        print("Building home page.")

        output = self.templates["home"]
        while tags := re.findall("<my([a-z]+)(\(.+\))?\/>", output):
            for tag in tags:
                html_tag = "<my" + tag[0] + tag[1] + "/>"

                stripped_tag = tag[0]

                arguments = tag[1].removeprefix("(")
                arguments = arguments.removesuffix(")")

                if arguments:
                    arguments = arguments.split("|")

                if stripped_tag == "script" or stripped_tag == "style":
                    output = output.replace(html_tag, "")
                elif stripped_tag == "posts":
                    post_links = {}

                    # When generating post links, I will need their meta file.
                    print("Feed:")                    
                    for post in os.listdir("post/"):
                        for obj in os.listdir(f"post/{post}/"):
                            if obj == "meta.txt":
                                content = open(f"{self.root}/post/{post}/{obj}").read()
                                print(f" - {post}")
                                metadata = content.splitlines()
                                post_links[int(metadata[2])] = f'<p><a href="/view/{post}.html" class="fs-5 text-dark">{metadata[0]}</a> <span class="fs-6 text-muted">- on {metadata[1]}</span></p>'
                                break
                    
                    ordered_post_links = dict(sorted(post_links.items(), reverse=True))
                    posts_html = ""
                    
                    for timestamp, content in ordered_post_links.items():
                        posts_html += content
                    
                    output = output.replace(html_tag, posts_html)
                else:
                    component_content = self.components[stripped_tag]
                    i = 1
                    for arg in arguments:
                        component_content = component_content.replace(f"${i}$", arg)
                        i += 1
                    
                    output = output.replace(html_tag, component_content)
        
        # I won't bother with looping through a folder just for one page.
        # I will write html, js and css in the source file.
        if os.path.isfile(f"{self.root}/index.html"):
            os.remove(f"{self.root}/index.html")
        
        with open(f"{self.root}/index.html", "w") as file:
	            file.write(output)

        print("Built home page.")


if __name__ == "__main__":
    generator = StaticGenerator()
    generator.run()