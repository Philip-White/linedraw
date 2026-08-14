import linedraw
from pathlib import Path

folder_path = Path('what_to_draw')

for item in folder_path.glob("*"):

    if item.is_file():
        #print(f'linedraw/img_output/{item.name[:3]}.png')
        linedraw.input_path = str(item)
        linedraw.contour_simplify = 1
        linedraw.hatch_size = 8
        #!we are overriding the var set in linedraw.py
        linedraw.export_path = f'img_output/{item.name[:3]}.png'
        linedraw.show_bitmap = True
        #linedraw.draw_contour = True
        #linedraw.draw_hatch = False
        #linedraw.hatch_size = 1
        lines = linedraw.sketch(str(item))

