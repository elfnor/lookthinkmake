Title: Symmetry Group Links and Notation
Date: 2014-07-18 22:00
Tags: make, think, symmetrytile
Category: think
Slug: Symmetry Group Links and Notation
Author: elfnor

There are many great resources on the 17 plane symmetry groups.

I made great use of a couple of online apps while writing my [Symmetry Tile plug-in.]({filename}/symmetry_tile_docs.md)

##Morenaments##

![morenaments]({filename}/images/morenaments.png)

This great java applet can either be used [here online](http://www.morenaments.de/euc/applet) or [downloaded](http://www.morenaments.de/euc/) as a `jar` file and run locally.

It allows you to draw on a canvas that automatically completes the choosen symmetry group.Be sure to investigate the menu on the top-right. Selecting tile and/or cell under the grid menu will show these on the pattern canvas and help with seeing the structure underlying a particular symmetry. Look in the manual under help for more information. Be sure to try dragging the coloured dots in the tile view around. These can show how the same symmetry pattern can have different shaped cell or tile.

##Kali##

![kali]({filename}/images/kali.png)

This online java applet can be used [here](http://www.scienceu.com/geometry/handson/kali/). Its much easier to do straight lines in this app. It uses the orbifold notation for the symmetry groups.

##Books##

The two books I consulted the most while working on this plug-in were:  

*  ["Handbook of Regular Patterns: An Introduction to Symmetry in Two Dimensions" by Peter S. Stevens](http://www.amazon.com/Handbook-Regular-Patterns-Introduction-Dimensions/dp/0262690888)  
*  ["Designing Tessalations: The Secret of Interlocking Patterns" by Jinny Beyer](http://www.amazon.com/Designing-Tessellations-Secrets-Interlocking-Patterns/dp/0809228661/)

All of these references use different notations and descriptions for the symmetry groups. I've summarised them in the folowing table for easy reference. The Symmetry Tile plug-in uses the notation in the left most column.

##Notation for Symmetry Groups##

| Crystallography | full | Terrazo       | Jinny Beyer's description         | Orbifold | Peter S. Stevens's description                            |
|-----------------|------|---------------|-----------------------------------|----------|-----------------------------------------------------------|
| p1              | p1   | Gold Brick    | Translation                       | o        | Two Nonparallel Translations                              |
| p2              | p211 | Hither & Yon  | Midpoint or Half-Turn Rotation    | 2222     | Four Half-Turns                                           |
| pm              | p1m1 | Wings         | Mirror                            | **       | Two Parallel Mirrors                                      |
| pg              | p1g1 | Card Tricks   | Glide                             | xx       | Two Parallel Glide Refelections                           |
| pgg             | p2gg | Honey Bees    | Double Glide                      | 22x      | Two Perpendicular Glide Reflections                       |
| pmm             | p2mm | Prickly Pear  | Double Mirror                     | *2222    | Reflections in Four Sides of a Rectangle                  |
| pmg             | p2mg | Lightning     | Glided Staggered Mirror           | 22*      | A Mirror and a Perpendicular Reflection                   |
| cm              | c1m1 | Crab Claws    | Staggered Mirror                  | *x       | A Reflection and a Parallel Glide Reflection              |
| cmm             | c2mm | Spider Web    | Staggered Double Mirror           | 2*22     | Perpendicular Mirrors and Perpendicular Glide Reflections |
| p4              | p4gm | Pinwheel      | Pinwheel or Quarter-Turn Rotation | 442      | Quarter-Turns                                             |
| p3m1            | p3m1 | Winding Ways  | Mirror and Three Rotations        | *333     | Reflections in an Equilateral Triangle                    |
| p3              | p3   | Storm at Sea  | Three Rotation                    | 333      | Three Rotations through 120°                              |
| p4g             | p4gm | Primrose Path | Mirrored Pinwheel                 | 4*2      | Reflections of Quarter-Turns                              |
| p4m             | p4mm | Sunflower     | Traditional Block                 | *442     | Reflections on the Sides of a 45°-45°-90° Triangle        |
| p6              | p6   | Whirlpool     | Six Rotation                      | 632      | Sixfold Rotation                                          |
| p31m            | p31m | Monkey Wrench | Three Roatations and a Mirror     | 3*3      | Refections of 120° Turns                                  |
| p6m             | p6mm | Turnstile     | Kalieidoscope                     | *632     | Refections in the Sides of a 30°-60°-90° Triangle         |

----------------
