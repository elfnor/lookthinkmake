Title: Structure Synth meets Sverchok - Generative Art inside Blender
Date: 2015-03-08 22:00
Tags: make, think, blender, sverchok
Category: think
Author: elfnor
Status: draft


![Nouveau Dr Seuss](/images/seuss_nouveu_11.png)

After using the ["Matrix Iterate"]({filename}simple_sverchok_05.md) node to generate some of the simpler structures from [Structure Synth](http://structuresynth.sourceforge.net/). I started to think about how to implement more of Structure Synth directly in Blender. It turned out to be remarkably simple using a scripted node and some existing python code.

Structure Synth uses a domain specific langauge called eisenscript to define a design grammar to construct 3D structures. Here's the eisenscript for a structure with 6 spirals.

```
set maxdepth 400

r0

rule r0 {
  3 * { rz 120  } R1
  3 * { rz 120 } R2
}

rule R1 {
  { x 1.3 rx 1.57 rz 6 ry 3 s 0.99} R1
  { s 4 } sphere
}

rule R2 {
  { x -1.3 rz 6 ry 3 s 0.99} R2
  { s 4 }  sphere
}
```

![matrix iterate sample image](/images/matrix_iterate_13.png)


An eisenscript consists of a list of rules. Each rule contains a set of instructions. That instruction can either be to place an object or to call another rule. That call can be to to the rule doing the calling in a recursive fashion. Each instruction also has an associated transform to scale rotate or move the current coordinate system. The original eisenscript also allowed transforms on the colour and transparency of the object.

The above structure can be easily implemented in Sverchok using the "Matrix Iterate" node as shown in the [previous post]({filename}simple_sverchok_05.md). 

The interesting bit is that each rule can have multiple definitions that are called randomly according to the weight assigned to each rule definintion. This allows structures with random branches and other complexities. This random choice of rule is bit harder to implement directly in Sverchok nodes but I'm thinking about it...

In the meantime searching the web, I couldn't find anyone who had included a parser for eisenscript files in Blender (there is one in [MeshLab](http://meshlab.sourceforge.net/)), but I did find that [LittleGrasshopper](http://github.prideout.net/) had written some [python scripts](http://prideout.net/blog/?p=72) to work with RenderMan. 

He uses an xml form of eisenscript to define the design grammar. The above script looks like this in Little Grasshopper's xml:

```xml
<rules max_depth="400">
    <rule name="entry">
        <call count="3" transforms="rz 120" rule="R1"/>
        <call count="3" transforms="rz 120" rule="R2"/>
    </rule>
    <rule name="R1">
        <call transforms="tx 1.3 rx 1.57 rz 6 ry 3 sa 0.99" rule="R1"/>
        <instance transforms="sa 4" shape="sphere"/>
    </rule>
    <rule name="R2">
        <call transforms="tx -1.3 rz 6 ry 3 sa 0.99" rule="R2"/>
        <instance transforms="sa 4" shape="sphere"/>
    </rule>
</rules>
```

From Little Grasshopper's post

>Every description must contain at least one rule named entry; this is the starting point for the evaluator. Note the mini-language used for specifying transformations. It’s a simple string consisting of translations, rotations, and scaling operations. For example, ```tx n```  means “translate n units along the x-axis”, ```ry theta```  means “rotate theta degrees about the y-axis”, and ```sa f``` means “scale all axes by a factor of f“.

In Little Grasshopper's code he provides a module (GenerativeArt.py) that parses the above type of xml strings and outputs a list of matrices and the name of the object to place at the location, scale and rotation defined by the matrix. This code is beautifully separated from any code used to implement or render the geometry and is perfect to incorporate in Sverchok.

The module ```GenerativeArt.py``` has two dependencies, ```elementtree``` for parsing the xml and ```euclid``` for the matrix multiplication. I replaced ```elementtree``` with ```xml.etree.cElementTree``` avaliable in the standard python included with Blender, and replaced ```euclid``` with the Blender ```mathutils``` module. 

From there all we need is a simple "Scripted Node" in Sverchok with the following code:

```python
from mathutils import Matrix
from sverchok.data_structure import Matrix_listing

import GenerativeArt_Blender as GenerativeArt
import GA_xml

import imp

max_mats = 5000

def sv_main(rseed=21):

    in_sockets = [['s', 'rseed', rseed]]
       
    imp.reload(GA_xml)
       
    tree = GA_xml.Library["Default"]
    shapes = GenerativeArt.Evaluate(tree, seed = rseed)
    
    shapes = shapes[:max_mats]
            
    mats = [matrix for name, matrix in shapes] 
    names = [name for name, matrix in shapes]   
        
    mat_out =  Matrix_listing(mats)
    
    #convert names to integer list
    iddict = {k:v for v,k in enumerate(set(names))}
    mask = [iddict[k] for k in names]
    
    out_sockets = [
        ['m', 'matrices', mat_out],
        ['s', 'mask', [mask]]
    ]

    return in_sockets, out_sockets
```

See [here](http://sverchok.readthedocs.org/en/latest/nodes/generator/scripted_intro.html) if you need help working with the "Scripted Node" in Sverchok.

That was too simple and it just works! It's fast too. Before doing this I played around trying to implement the object generation directly in Blender python and had trouble getting fast enough code, let alone getting lost in ```bpy.ops``` and ```bpy.context``` calls.

To use the GA node in Blender first install the Sverchok addon. Download the GA code from [github](). Then load the three python files as separate text blocks into a blend file. Add a "Scripted Node" to Sverchok node tree. On the node select the ```GA_node.py``` code from the lower drop down. Then click the plugin icon to the right of this field. The node should turn blue with one input and two outputs. Wire the matrices output to a "Viewer Draw" node and you should see some geometry as below.

![GA node diagram](/images/generative_art_node_for_blog.blend.png)

The node has one input "rseed" which is used to set the random number generator. For a rule set that includes multiple definitions of rules, changing this will change the stucture. 

The Library of xml rule sets is stored in the ```GA_xml.py``` module. This allows you to easily change the rule set. In the last line of code ```Library["Default"] = Library["Tree"]``` change ```Tree``` to any of the other examples. You can also change the rules or add new ones. The geometry should change in the 3D View after clicking the "Update Node Tree" button in the Sverchok panel.

If the rule set defines different objects in the instances, the node will put out a mask to use in Sverchok. The objects can be called anything in the xml. ```GenerativeArt_Blender.py``` passes them to the node as strings. The node then converts these to integers (that is (0, 1) for two different objects, (0, 1, 2) for three objects etc.). This mask can be used as input to a "Mask List" node to separate the matrices into two lists as shown below. This is simple for two objects but is a bit more complicated but doable for more.

![GA node diagram with mask list](/images/generative_art_node_OK_02.blend.png)

My computer chokes if I try to feed too many matrices into Sverchok. I've put a hard limit in the node at 5000 matrices. Feel free to change this depending on you and your computer's ability to cope with lockups and crashes.

The code is available [here on github]().

-----------------------------------------------------------------------------------







