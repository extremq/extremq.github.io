import os, re
from datetime import datetime
import shutil

# The main interpreter. It mostly replaces the tags written as <mytag/>
# with the relevant parts of code. Static website, bla bla bla.
class StaticGenerator:
    root = os.getcwd() # Root directory
    components = {}
    templates = {}

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

        build_name = datetime.utcnow().strftime("%Y-%m-%d--%H-%M-%S")
        os.mkdir(f"{self.root}/output/{build_name}")
        # Posts are like "projects" - they can contain html, css and js files.
        for post in os.listdir("post/"):

            # Only one html allowed. Multiple css and js files can be imported.
            objects = {
                "html": "Empty",
                "css": [],
                "js": []
            }

            # Iterate through all the post objects and place them selectively
            for obj in os.listdir(f"post/{post}/"):
                content = open(f"{self.root}/post/{post}/{obj}").read()

                if obj.find(".html") != -1:
                    objects["html"] = content
                elif obj.find(".css") != -1:
                    objects["css"].append(content)
                elif obj.find(".js") != -1:
                    objects["js"].append(content)
            
            # Replacing all the tags in a somewhat recursive (but not actually) manner.
            output = self.templates["post"].replace("<mycontent/>", objects["html"])
            while tags := re.findall("<my[a-z]+/>", output):
                for tag in tags:
                    stripped_tag = tag.removeprefix("<my")
                    stripped_tag = stripped_tag.removesuffix("/>")
                    if stripped_tag == "script":
                        to_replace = ""
                        for script in objects["js"]:
                            to_replace += f"<script>{script}</script>\n"
                            
                        output = output.replace(tag, to_replace)
                    elif stripped_tag == "style":
                        to_replace = ""
                        for style in objects["css"]:
                            to_replace += f"<style>{style}</style>\n"
                            
                        output = output.replace(tag, to_replace)
                    else:
                        output = output.replace(tag, self.components[stripped_tag])

            # I store past builds
            path = f"{self.root}/output/{build_name}/{post}"
            os.mkdir(path)

            with open(f"{path}/{post}.html", "w") as file:
	            file.write(output)
            
            # Latest build is also in /view
            if os.path.isdir(f"{self.root}/view/"):
                shutil.rmtree(f"{self.root}/view/")

            os.mkdir(f"{self.root}/view/")
            
            with open(f"{self.root}/view/{post}.html", "w") as file:
	            file.write(output)

            print(f" - '{post}' processed!")

        print("Finished processing the posts.")

    # I build special pages separately.
    def build_home(self):
        print("Building home page.")

        output = self.templates["home"]
        while tags := re.findall("<my[a-z]+/>", output):
            for tag in tags:
                stripped_tag = tag.removeprefix("<my")
                stripped_tag = stripped_tag.removesuffix("/>")
                
                if stripped_tag == "script" or stripped_tag == "style":
                    output = output.replace(tag, "")
                else:
                    output = output.replace(tag, self.components[stripped_tag])
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