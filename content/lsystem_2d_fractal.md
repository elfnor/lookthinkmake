Title: Generative Art Examples - Fractals on a Plane
Date: 2016-02-14 22:00
Tags: make, think, blender, sverchok, structuresynth
Category: think
Author: elfnor
Status: draft

![koch vase](/images/koch_vase_render_01_003.png)

I've made some changes and improvements to the *Generative Art* node in Sverchok. This node uses a simple *xml* file to define a set of rules to produce geometry. This node is very strongly based on [Structure Synth]() and can produce [Lindermayer Systems (lsystems)]() and fractals as well as more random and interesting creations. 

This post is hopefully the first in a series of examples and demos for the *Generative Art* node. For some examples I've also given a link to an *eisenscript* version to be used in [StructureSynth](). These are not always exactly equivalent due to some differences between the two implementations but should help those who are more familiar with *eisenscript* make the transition to the *xml* format.

Sverchok is available on [github](https://github.com/nortikin/sverchok). Download the zip version and install like any other Blender addon.

The documentation for the node is [here](local md copy).

## Koch Snowflake

![koch snowflake](/images/ga_koch_snowflake.png)

```xml
<rules max_depth="100">
    <rule name="entry">
        <call transforms="ty 0.5*3**0.5" rule="R1"/>
        <call transforms="rz 120 ty 0.5*3**0.5" rule="R1"/>
        <call transforms="rz 240 ty 0.5*3**0.5" rule="R1"/>
    </rule>
    
    <rule name="R1" max_depth="4" successor="unit">
        <call transforms="tx -1 ty 0 sa 1.0/3.0" rule="R1"/>
        <call transforms="tx -0.25 ty 0.25*3**0.5 rz 60 sa 1.0/3.0" rule="R1"/>      
        <call transforms="tx 0.25 ty 0.25*3**0.5 rz -60 sa 1.0/3.0" rule="R1"/>
        <call transforms="tx 1 ty 0 sa 1.0/3.0" rule="R1"/>

    </rule>
    <rule name="unit">
        <instance transforms="tx -1.5 s 3 0.5 0.1" shape="s0"/>
    </rule>
</rules>

```

[xml](), [nodes in json](), [eisenscript](), [info]()

## T-Square

![t square](/images/ga_tsquare_2d.png)

```xml
<rules max_depth="100">
    <rule name="entry">
        <call rule="R1"/>
    </rule>
    
    <rule name="R1" max_depth="5">
        <instance  transforms="sz 0.1" shape="s1"/>
        <call transforms="tx 0.5 ty 0.5 sx 0.5 sy 0.5" rule="R1"/>
        <call transforms="tx -0.5 ty -0.5 sx 0.5 sy 0.5" rule="R1"/>
        <call transforms="tx 0.5 ty -0.5 sx 0.5 sy 0.5" rule="R1"/>
        <call transforms="tx -0.5 ty 0.5 sx 0.5 sy 0.5" rule="R1"/>
    </rule>

</rules>
```

[xml](), [nodes in json](), [eisenscript](), [info]()




---------------------------------------------------------------------------------

