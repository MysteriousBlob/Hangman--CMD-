'''
TRIGGER WARNING!

The following code... 
Works.

Nothing less,
Nothing more!

View at your own disgression
'''

from math import floor

xscale = 2
yscale = 1
'''
Class line, created in order to make stuff more abstract.

It does not make stuff readable tho...

Line types:
    0 - linear
    1 - horizontal
    2 - vertical
    3 - circular (Future)
    4 - Quadratic (Future)
    5 - Cubic (Future)
'''
class Line():
    def __init__(self, begX, begY, endX, endY, shiftX = 0, shiftY = 0) -> None:
        if begX != endX and begY != endY:
            self.type = 0

            self.begX = begX + shiftX
            self.begY = begY + shiftY
            self.endX = endX + shiftX
            self.endY = endY + shiftY

            self.gradient = (self.endY - self.begY) / (self.endX - self.begX)
            self.origin = self.begY - self.gradient * self.begX

        elif begX != endX and begY == endY:
            self.type = 1

            self.origin = begY + shiftY
            self.begX = begX + shiftX
            self.endX = endX + shiftX

        # elif begX == endX and begY != endY: #Temporary in case of future development
        else:
            self.type = 2

            self.origin = begX + shiftX
            self.begY = begY + shiftY
            self.endY = endY + shiftY


    
    def formula(self) -> None:
        if self.type == 0:
            print(f"y = {self.gradient}x + {self.origin}")

        elif self.type == 1:
            print(f"x = {self.origin}")

        # elif self.type == 2: #Temporary in case of future development
        else:
            print(f"y = {self.origin}")

'''
Honestly, After wasting 10 hours on this...

I REALLY DON'T KNOW HOW IT WORKS!

I MEAN AT ALL!

I AM TRYING MY HARDEST TO EXPLAIN THE MATH IN THE COMMENTS
'''
def render_line(line:Line, ascii_render:list) -> str:
    if line.type == 0: # Linear line handling
        if len(ascii_render) <= line.endY: # Size management (2D vertical expension)
            for i in range(len(ascii_render) - 1, line.endY):
                ascii_render.append("")

        for row in range(line.begY, line.endY + 1): # Iterate over each available row
            row_edit = "" # Python is dumb... This complicates things! (The edited row is stored here)
            flag = False # Flag in order to conserve time (True if line was outputted)
            target = floor((row - line.origin)/line.gradient) # The position of the point where line intersects (Floored)

            if len(ascii_render[row]) <= line.endX: # In case the line is bigger than existing render X dimension
                for column in range(0, len(ascii_render[row])):
                    if column == target and not flag:
                        row_edit += "■"
                        flag = True # Flag set true to stop wasting time
                    else:
                        row_edit += ascii_render[row][column] # Copies the existing render
                
                for column in range(len(ascii_render[row]), line.endX + 1):
                    if column == target and not flag:
                        row_edit += "■"
                        flag = True
                    elif not flag:
                        row_edit += " "
                    else:
                        break

            else:
                for column in range(0, len(ascii_render[row])):
                    if column == target and not flag:
                        row_edit += "■"
                        flag = True
                    else:
                        row_edit += ascii_render[row][column]

            ascii_render[row] = row_edit # Saves the new render of the row

    elif line.type == 1: # Horizontal line handling
        if len(ascii_render) <= line.origin * yscale: 
            for i in range(len(ascii_render) - 1, line.origin * yscale):
                ascii_render.append("")

        row_edit = "" 

        if len(ascii_render[line.origin * yscale]) <= line.endX * xscale: 
            for column in range(0, len(ascii_render[line.origin * yscale]), xscale):
                if column >= line.begX * xscale and line.endX * xscale >= column:
                    row_edit += "■" + " " * (xscale - 1)
                else:
                    row_edit += ascii_render[line.origin * yscale][column] + " " * (xscale - 1)
            
            for column in range(len(ascii_render[line.origin * yscale]), line.endX * xscale + 1, xscale):
                if column >= line.begX * xscale and line.endX * xscale >= column:
                    row_edit += "■" + " " * (xscale - 1)
                else:
                    row_edit += " " * xscale

        else:
            for column in range(0, len(ascii_render[line.origin * yscale]), xscale):
                if column >= line.begX * xscale and line.endX * xscale >= column:
                    row_edit += "■" + " " * (xscale - 1)
                else:
                    row_edit += ascii_render[line.origin * yscale][column] + " " * (xscale - 1)

        ascii_render[line.origin * yscale] = row_edit
    
    elif line.type == 2: # Vertical line handling
        if len(ascii_render) <= line.endY:
            for i in range(len(ascii_render) - 1, line.endY):
                ascii_render.append("")

        for row in range(line.begY, line.endY + 1):
            row_edit = "" 
            flag = False 

            if len(ascii_render[row]) <= line.origin:
                for column in range(0, len(ascii_render[row])):
                    if column == line.origin and not flag:
                        row_edit += "■"
                        flag = True
                    else:
                        row_edit += ascii_render[row][column]
                
                for column in range(len(ascii_render[row]), line.origin + 1):
                    if column == line.origin and not flag:
                        row_edit += "■"
                        flag = True
                    elif not flag:
                        row_edit += " "
                    else:
                        break

            else:
                for column in range(0, len(ascii_render[row])):
                    if column == line.origin and not flag:
                        row_edit += "■"
                        flag = True
                    else:
                        row_edit += ascii_render[row][column]

            ascii_render[row] = row_edit # Saves the new render of the row

    return ascii_render

def renderer(lines:list) -> list:
    ascii_render = []
    for line in lines:
        ascii_render = render_line(line, ascii_render)
    
    return ascii_render

head = [Line(begX=0, begY=0, endX=10, endY=0), Line(begX=0, begY=0, endX=10, endY=0, shiftY=10), Line(begX=0, begY=0, endX=0, endY=10), Line(begX=0, begY=0, endX=0, endY=10, shiftX=10)]

for i in renderer(head):
    print(i)