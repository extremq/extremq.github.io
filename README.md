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
To use components, you must first create a file inside the `components/` folder and then, inside your templates (or even other component files) you will need to type
```
<mycomponent/>
```
and it will simply be replaced with the contents of the file. It's also recursive, so you can have a component inside another component.

Components also support arguments. To create such component, you will need to provide some argument placeholders as such:

`link.html`
```
<a href="$$1$$">$$2$$</a>
```
`home.html`
```
My github is <mylink(https://github.com/extremq|Extremq)/>.
```
The format is `<my` + Component name (name of file) + `(argument1|argument2|argument3...)` (optional) + `/>`.

In the `.env` file there will always be a `__DATE__` that's always updated when the site is generated. You can use any environment variable in the html using this format:
```
__MYVAR__
```  
Make sure to write it in this way inside the `.env` file:
```
MYVAR='cheese'
```
After you're done with that, you can choose to render only that page or all the pages by using `python ./build.py --file name-of-folder` or `python ./build.py --f name-of-folder`. Providing no flags will generate all the pages instead.