import tkinter as tk

global_vertices = {
    'v1': (-2, 22), 
    'v20': (-2, 3), 
    'v2': (3, 22), 
    'v21': (0, 3), 
    'v3': (5, 22), 
    'v22': (4, 3), 
    'v4': (10, 22), 
    'v23': (8, 3), 
    'v5': (4, 20), 
    'v24': (10, 3), 
    'v6': (-2, 18), 
    'v25': (0, 0), 
    'v7': (3, 18), 
    'v26': (8, 0), 
    'v8': (5, 18), 
    'v27': (4, -1), 
    'v9': (10, 18), 
    'v28': (2, -2), 
    'v10': (4, 16), 
    'v29': (6, -2), 
    'v11': (3, 14), 
    'v30': (4, 20), 
    'v12': (5, 14), 
    'v31': (4, 16), 
    'v13': (0, 12), 
    'v32': (4, 12), 
    'v14': (4, 12), 
    'v33': (0, 8), 
    'v15': (8, 12), 
    'v34': (8, 8), 
    'v16': (-2, 8), 
    'v35': (0, 3), 
    'v17': (0, 8), 
    'v36': (4, 3), 
    'v18': (8, 8), 
    'v37': (8, 3), 
    'v19': (10, 8), 
    'v38': (4, -1),
}

global_faces = {
    'f1': ('v1','v2','v7'), 
    'f25': ('v18','v23','v22'), 
    'f49': ('v12','v32','v15'), 
    'f2': ('v2','v3','v5'), 
    'f26': ('v18','v24','v23'), 
    'f50': ('v12','v11','v32'), 
    'f3': ('v2','v5','v7'), 
    'f27': ('v18','v19','v24'), 
    'f51': ('v11','v13','v32'), 
    'f4': ('v3','v8','v5'), 
    'f28': ('v20','v21','v25'), 
    'f52': ('v15','v34','v19'), 
    'f5': ('v5','v8','v7'), 
    'f29': ('v21','v22','v25'), 
    'f53': ('v15','v32','v18'), 
    'f6': ('v3','v4','v8'), 
    'f30': ('v22','v26','v25'), 
    'f54': ('v32','v33','v34'), 
    'f7': ('v6','v7','v11'),
    'f31': ('v22','v23','v26'), 
    'f55': ('v32','v13','v33'), 
    'f8': ('v7','v10','v11'), 
    'f32': ('v23','v24','v26'), 
    'f56': ('v13','v16','v32'), 
    'f9': ('v7','v8','v10'), 
    'f33': ('v25','v27','v28'), 
    'f57': ('v19','v34','v24'), 
    'f10': ('v8','v12','v10'), 
    'f34': ('v25','v26','v27'), 
    'f58': ('v34','v23','v24'), 
    'f11': ('v10','v12','v11'), 
    'f35': ('v26','v29','v27'), 
    'f59': ('v34','v22','v23'), 
    'f12': ('v8','v9','v12'), 
    'f36': ('v27','v28','v29'), 
    'f60': ('v34','v33','v36'), 
    'f13': ('v11','v12','v14'), 
    'f37': ('v4','v3','v8'), 
    'f61': ('v33','v35','v36'), 
    'f14': ('v13','v11','v14'), 
    'f38': ('v3','v30','v8'), 
    'f62': ('v33','v20','v35'), 
    'f15': ('v12','v15','v14'), 
    'f39': ('v3','v2','v30'), 
    'f63': ('v33','v16','v20'), 
    'f16': ('v13','v17','v16'), 
    'f40': ('v2','v7','v30'), 
    'f65': ('v24','v37','v26'), 
    'f17': ('v13','v14','v17'), 
    'f41': ('v2','v1','v7'), 
    'f65': ('v37','v36','v26'), 
    'f18': ('v14','v18','v17'), 
    'f42': ('v30','v7','v8'), 
    'f66': ('v36','v25','v26'), 
    'f19': ('v14','v15','v18'), 
    'f43': ('v9','v8','v12'), 
    'f67': ('v36','v35','v25'), 
    'f20': ('v15','v19','v18'), 
    'f44': ('v8','v31','v12'), 
    'f68': ('v35','v20','v25'), 
    'f21': ('v16','v17','v20'), 
    'f45': ('v8','v7','v31'), 
    'f69': ('v26','v38','v29'), 
    'f22': ('v17','v21','v20'), 
    'f46': ('v7','v11','v31'), 
    'f70': ('v26','v25','v38'), 
    'f23': ('v17','v22','v21'), 
    'f47': ('v7','v6','v11'), 
    'f71': ('v25','v28','v38'), 
    'f24': ('v17','v18','v22'), 
    'f48': ('v31','v11','v12'), 
    'f72': ('v38','v28','v29'),
}

class Designer:
    def __init__(self, root, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.canvasWidth = 50
        self.canvasHeight = 500 - 50
        self.canvas = tk.Canvas(root,  width = 500, height = 500)      
        
    
    def draw_form(self, vertices):
        for i in range(0, len(vertices)):
            if i != len(vertices) - 1:
                j = i + 1
            else: 
                j = 0    
            self.canvas.create_line(self.vertices[vertices[i]][0]*15 + self.canvasWidth, self.canvasHeight - self.vertices[vertices[i]][1]*15, self.canvasWidth + self.vertices[vertices[j]][0]*15, self.canvasHeight - self.vertices[vertices[j]][1]*15, width = 3)
        
        self.canvas.pack()


        # x_values = []
        # y_values = []
        
        # x_values.append(self.vertices[vertices[0]][0])
        # y_values.append(self.vertices[vertices[0]][1])

        # x_values.append(self.vertices[vertices[1]][0])
        # y_values.append(self.vertices[vertices[1]][1])

        # plt.plot(x_values, y_values, marker = '.')

        # x_values = []
        # y_values = []

        # x_values.append(self.vertices[vertices[1]][0])
        # y_values.append(self.vertices[vertices[1]][1])

        # x_values.append(self.vertices[vertices[2]][0])
        # y_values.append(self.vertices[vertices[2]][1])

        # plt.plot(x_values, y_values, marker = '.')

        # x_values = []
        # y_values = []

        # x_values.append(self.vertices[vertices[2]][0])
        # y_values.append(self.vertices[vertices[2]][1])

        # x_values.append(self.vertices[vertices[0]][0])
        # y_values.append(self.vertices[vertices[0]][1])

        # plt.plot(x_values, y_values, marker = '.')

    def draw(self): 
        for f, v in self.faces.items():
            print(f"drawing face {f} with vertices {v}")
            self.draw_form(v)
        # plt.plot([1, 1], [2, 5], marker = 'o')    
        # plt.show()    
    

if __name__ == "__main__":
    root = tk.Tk()  
    root.title('abacaxi')
    d = Designer(root, global_vertices, global_faces)
    d.draw()
    root.mainloop() 
    
    
    