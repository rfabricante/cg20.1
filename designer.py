import tkinter as tk


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
            multiplier = 15
            x = self.canvasWidth + self.vertices[vertices[i]][0]*multiplier
            y = self.canvasHeight - self.vertices[vertices[i]][1]*multiplier
            coords.append([x, y])
        
        self.canvas.create_polygon(coords, fill=color)
        self.canvas.pack(fill=tk.BOTH)

    def draw(self): 
        for f, v in self.faces.items():
            print(f"drawing face {f} with vertices {v}")
            self.draw_form(v[0], v[1])
    
