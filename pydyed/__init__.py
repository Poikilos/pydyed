#!/usr/bin/env/python
"""
Provide a Python API for the "dyed" mod for Minetest by Poikilos:
<https://github.com/poikilos/dyed>.

The primary use case is Poikilos' fork of mcimport:
<https://github.com/poikilos/>.

NOTE: In this module, colorapi refers to colorapi by ArionasMC.
"""
mc_colorapi_colors = [
# translate https://github.com/ArionasMC/ColorAPI/raw/master/ColorAPI/src/me/amc/colorapi/Colors.java
    'white',
    'orange',
    'magenta',  # "Magneta" [sic] in ArionasMC's code
    'light_blue',
    'yellow',
    'green',  # "Lime"
    'pink',
    'dark_grey',  # "Grey"
    'grey',  # "LightGray"
    'cyan',
    'violet',  # "Purple" (appearance differs in MC)
    'blue',
    'brown',
    'dark_green',  # "Green"
    'red',
    'black'
]

mt_poikilos_dyed_lookup = {
    'white': 0,
    'orange': 1,
    'magenta': 2,  # "Magneta" [sic]
    'light_blue': 3,
    'yellow': 4,
    'green': 5,  # "Lime"
    'pink': 6,
    'dark_grey': 7,  # "Gray" in MC
    'grey': 8,  # "LightGray" in MC
    'cyan': 9,
    'violet': 10,  # "Purple" (appearance differs in MC)
    'blue': 11,
    'brown': 12,
    'dark_green': 13,  # "Green"
    'red': 14,
    'black': 15
}

mc_ArionasMC_colorapi_lookup = {
    'white': 0,
    'orange': 1,
    'magenta': 2,  # "Magneta" [sic]
    'light_blue': 3,
    'yellow': 4,
    'green': 5,  # "Lime"
    'pink': 6,
    'dark_grey': 7,  # "Gray" in MC
    'grey': 8,  # "LightGray" in MC
    'cyan': 9,
    'violet': 10,  # "Purple" (appearance differs in MC)
    'blue': 11,
    'brown': 12,
    'dark_green': 13,  # "Green"
    'red': 14,
    'black': 15
}
