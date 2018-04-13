


Reference image
![](celadon_vase_03.jpeg)

Default material  

**celadon_glaze_001** {2018-04-13 16:51}
![](celadon_glaze_001.png)
Render time: 0:00:20.183531

![](celadon_glaze_ss_01.png)

Add some color to diffuse

**celadon_glaze_002** {2018-04-13 16:57}
![](celadon_glaze_002.png)
Render time: 0:00:20.045838
Too smooth but highlights are sharper

Roughen diffuse

**celadon_glaze_003** {2018-04-13 17:11}
![](celadon_glaze_003.png)
Render time: 0:00:20.356762

Try differnt glossy shader types

Sharp

**celadon_glaze_004** {2018-04-13 17:13}
![](celadon_glaze_004.png)
Render time: 0:00:20.082703
Too glossy

Beckmann

**celadon_glaze_005** {2018-04-13 17:14}
![](celadon_glaze_005.png)
Render time: 0:00:20.434412
Better but glossy highlight needs to be sharper

Lower glossy roughness

**celadon_glaze_006** {2018-04-13 17:17}
![](celadon_glaze_006.png)
Render time: 0:00:20.392772
Better

Make mix use more of diffuse

**celadon_glaze_007** {2018-04-13 17:18}
![](celadon_glaze_007.png)
Render time: 0:00:20.221339
Better

Try using Layer Weight for mix factor

**celadon_glaze_008** {2018-04-13 17:22}
![](celadon_glaze_008.png)
Render time: 0:00:20.346465

![](celadon_glaze_ss_02.png)

Facing instead of Fresnel

**celadon_glaze_009** {2018-04-13 17:24}
![](celadon_glaze_009.png)
Render time: 0:00:20.525302
This is much darker around back edges

Lower Layer Weight Blend value

**celadon_glaze_010** {2018-04-13 17:26}
![](celadon_glaze_010.png)
Render time: 0:00:20.299810

Make both glossy and diffuse less rough

**celadon_glaze_011** {2018-04-13 17:28}
![](celadon_glaze_011.png)
Render time: 0:00:20.267659
This has shapened up highlight

Pick the colors off reference image

**celadon_glaze_012** {2018-04-13 17:34}
![](celadon_glaze_012.png)
Render time: 0:00:20.231184
Not bad!

![](celadon_vase_03.jpeg)

Final node setup

![](celadon_glaze_ss_03.png)

Could use a geometry pointedness input node to mix a lighter shade to give the look of a breaking glaze on sharp edges or play with a Voronoi texture for crazing.
