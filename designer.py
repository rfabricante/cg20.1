import tkinter as tk
import numpy


class Designer:
    def __init__(self, root, vertices, faces, width=1920, height=1080):
        self.vertices = vertices
        self.faces = faces
        self.canvasWidth = width*0.5
        self.canvasHeight = height*0.5
        self.canvas = tk.Canvas(root,  width = width, height = height)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        
    
    def draw_form(self, vertices, color):
        coords = []
        for i in range(0, len(vertices)):
            x = self.canvasWidth + self.vertices[vertices[i]][0]
            y = self.canvasHeight - self.vertices[vertices[i]][1]
            coords.append([x, y])
        
        self.canvas.create_polygon(coords, fill=color)
        self.canvas.pack(fill=tk.BOTH)

    def draw(self):
        face_list = list(self.faces.items()) 
        for f, v in face_list:
            print(f"drawing face {f} with vertices {v[0]}")
            self.draw_form(v[0], v[1])

    def scale(self, amount=5):
        matrix = [[amount,      0,      0],
                  [     0, amount,      0],
                  [     0,      0,      1]]

        self._transform(matrix)

    def vertical_skew(self, amount=5): 
        matrix = [[     1,      0,      0],
                  [amount,      1,      0],
                  [     0,      0,      1]]

        self._transform(matrix)
    
    def _transform(self, matrix): 
        for k, v in self.vertices.items():
            print(f"transforming vertice {k} with value {v}")
            self.vertices[k] = numpy.matmul(matrix, v)
            


    
