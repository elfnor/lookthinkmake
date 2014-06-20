Title: Notes on Pelican and markdown
Date: 2014-06-14 22:00
Tags: make
Category: make
Author: elfnor

I'm now using Pelican to generate this blog from content stored in plain tect files. It's installation is well explained on the [Pelican](http://docs.getpelican.com/en/3.1.1/getting_started.html) website and many blogs ([the one I used](http://www.circuidipity.com/pelican.html)). I used the method where you set up a virtualenv and install pelican into that.

The only problem I had was that after I'd cloned the standard themes from github:

```sh
git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
```
I couldn't get the path to the themes `~/pelican-themes` to work in the `pelicanconf.py` file. The hack solution was to copy all the theme folders and files from `~/pelican-themes/` to `~/virtualenvs/lookthinkmake/lib/python2.7/site-packages/pelican/themes/`  and use the following line in `pelicanconf.py`. 

```python
THEME = 'pelican-bootstrap3'
```
where the folder of the desired theme is specified.

To restart a devlopment session:

```sh
cd ~/lookthinkmake
source ~/virtualenvs/lookthinkmake/bin/activate
make devserver
```
and point firefox to `localhost:8000`. 

I also swapped this version of [`server.py`](https://github.com/robulouski/pelican/blob/301268f67f1a6751a3c9ac51d099fae10b808f8b/pelican/server.py) for the one in `~/virtualenvs/lookthinkmake/lib/python2.7/site-packages/pelican/` to fix some `Broken Pipe Errors`.


Markdown
=======

Try [dillinger](http://dillinger.io/) for an online markdown editor with real time viewer. 

The use of references for links looks like good practice.

A good [cheat sheet](http://plutowski.com/).

Tables kind of work without a plugin, layout may be theme dependent.

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

Pygments
=======

For the `pelican-bootstrap3` theme. There are some settings that can be added to the `pelicanconf.py` file. See [here](https://github.com/DandyDev/pelican-bootstrap3). In particular:

```sh
PYGMENTS_STYLE = 'manni'
```
changes the pygments css. Most themes have the pygments css built in.

Some random python to test this on:

```python
"""
document comment
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

#short unnecessry comment
soup = BeautifulSoup(urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=78').read())

for row in soup('table', {'class' : 'spad'})[0].tbody('tr'):
  tds = row('td')
  print(tds[0].string, tds[1].string)
  # will print date and sunrise
```

Themes
======

I'm still settling on a theme for the blog.

* pelican-simplegrey
* pelican-bootstrap3
* pelican-octopress

pelican-simplegrey with recent posts on right side bar would be great

Blogs I like the __look__ of:

* <http://matija.suklje.name/5th-incarnation-of-hooks-humble-homepage>
    * layout is good but don't like the colour of code blocks (inline or blocks).  
* <http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/>  
    * again I'd choose a different (light-grey) colour for the code blocks.  


Flow Text around image
------------------

Use html in markdown file.

	<img align="left" style="margin: 0px 20px" alt="parasled" src="/images/parasled.jpg?w=121" width="278" height="686" /></a>

To Work Out
=========

I'm still trying to work out:  

* how to flow text around an image  

* zotero citations?  
* math notation (latex?)
* how to get full articles on 1st page - done using pelican-simplegrey them
* add an archive page to pelican-simplegrey-efh theme. Lots of other themes have them

<http://andresjruiz.com/theming-pelican-with-a-little-boostrap.html>

This site has an all category

<http://pirsquared.org/blog/pelican-tags-vs-categories.html>


