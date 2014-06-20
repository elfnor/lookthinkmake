Title: Pelican and markdown cheat-sheet
Date: 2014-06-19 22:00
Tags: pelican, markdown
Category: think
Author: elfnor

A Pelican blog consists of:  

* __markdown__ text files containing __content__
* __ jinga2__ html template files defining the pages __layout__
* __CSS__ style file that determine how the page elements __look__

These elements are processed by the Pelican python software to produce the static html pages that make up this blog.

Lots of blogs have very good information on installing Pelican. Many also have the markdown codes used in text files to define what parts of the text are code blocks, what parts are quotes. But I couldn't find a post that described where and how to edit the CSS style files that determine how the the different elements look on the finished blog.

I'll try and write that post. 

A warning: I'm fairly new and no expert on html or CSS and most of this information comes from poking pelican themes and seeing what happens. I'll try and test my conclusions on more than one theme, but mostly I'll be fiddling with the pelican-simplegrey theme.

In-line Code
---------

This is text such as `this` that is normally used for a short piece of code in a a paragraph. 


It might also be used when a variable name or file name `~\file.txt` is referred to in a paragraph.

	This is text such as `this` that is normally...

The static html produced by Pelican is:  

```html
<p>This is text such as <code>this</code> that is normally used for a short piece of code in a a paragraph. </p>
```

This format of the in-line code element is given by a piece of CSS such as this, included in the theme `main.css` or `style.css` file

```css
code {
  font-family: 'Source Code Pro', monospace;
  font-size: 0.9em;
  font-style: normal;
  letter-spacing: 0.015em;
}
```


[http://www.krisyu.org/blog/posts/2013/06/markdown-and-latex-reference]


