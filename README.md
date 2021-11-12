# Status
![https://github.com/extremq/extremq.github.io/actions/workflows/generate-site.yaml](https://github.com/extremq/extremq.github.io/workflows/generate-site/badge.svg)
# Introduction
This is my personal website in which I will be posting different articles about various topics I like most. 
# How is it done
I am generating a static website using my own interpreter. It can be found in `build.py` and it employs the idea of using components to reuse html snippets (check `src/components`). You can read about it on the blog itself, [here](https://extremq.github.io/view/how-i-built-this-site.html).
# How to use
First, create a folder in `post`. The name of the folder will be the link of the generated page.  
Then, create a `.html` file and a `meta.txt` file.  
In the `.html` you should write your article and inside the `meta.txt` you will need to format the info as such:
```
Title of article
Date of article
UTC Timestamp of article in seconds
```
After you're done with that, you can choose to render only that page or all the pages by using `python ./build.py --file name-of-folder` or `python ./build.py --f name-of-folder`. Providing no flags will generate all the pages instead.