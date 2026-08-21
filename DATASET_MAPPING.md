# Dataset mapping

Final folders:

```text
dataset/
├── plastic/
├── paper/
├── metal/
├── organic/
├── glass/
└── e-waste/
```

Sources:

1. Recyclable Waste Image Dataset — CC BY 4.0
   https://data.mendeley.com/datasets/h5pxbsdz4m/1
   Includes paper, cardboard, plastic, metal and glass.

2. Custom Bangladeshi E-Waste Image Dataset — CC BY 4.0
   https://data.mendeley.com/datasets/77383kmdnw/1
   Includes battery waste, keyboard, light bulb, mobile, mouse and PCB,
   which can be mapped to `e-waste`.

3. Waste Classification Dataset — CC BY 4.0
   https://data.mendeley.com/datasets/n3gtgm9jxj/3
   Includes an organic class.

Important: these sources are primarily classification-style datasets.
A real multi-object detector needs bounding-box annotations. Do not treat
class folders as bounding-box labels.
