Title: Parametric Surfaces in Blender
Date: 2014-08-03 22:00
Tags: make, think, blender
Category: think
Author: elfnor

The [Blender](http://www.blender.org/) 3D modeling and rendering package has an add-on for mathematically defined surfaces. It is enabled via the Extra Objects add-on under `File > User Preferences> Addons`.

The `XYZ Math Surface` can be used to construct meshes for parametric surfaces. The parametric surface is defined by three functions of two variables $u$ and $v$:

$$
x = X(u,v)
$$
$$
y = Y(u,v)
$$
$$
z = Z(u,v)
$$

The [documentation page](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/Add_3d_Function_Surface) for the add-on has a number of example surfaces, but there are a lot more interesting named surfaces out there.

Its fairly easy to enter any formulae you find for a parametric 3D surface into Blender and save it as an `Operator Preset`. I've uploaded my collection of saved presets to a github [repo](https://github.com/elfnor/blender_XYZ_surface_presets). I haven't included every named surface out there, just ones I think might make interesting images. 

Here are a couple of images produced using the XYZ Math Surface add-on.

##Dini##

![Dini Surface](images/dini_01.png)

##Twisted Torus##

![twisted torus](images/twisted_torus_02.png)

##Stereosphere##

A stereosphere is the projection of a plane grid onto a sphere with the projection lines going through the top pole of the sphere. In the following image there is a point source light at the north pole of the stereosphere (the light is represented by the yellow dot). This light then does a stereographic projection of the sphere back onto the plane producing the grid present on the ground plane.
 
![stereosphere](images/stereosphere_01.png)

----------------------------------


