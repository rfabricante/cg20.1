import csv

class CsvParser:
    
    def __init__(self, vertices_path, faces_path):
        self.vertices_path = vertices_path
        self.faces_path = faces_path

    
    def vertices_to_dict(self):
        vertices = {}
        with open(self.vertices_path, newline='') as arquivo_csv:
            reader = csv.reader(arquivo_csv, delimiter=',')
            for row in reader:
                vertices[row[0].strip()] = (int(row[1]), int(row[2]), int(row[3]))
        
        return vertices

    def faces_to_dict(self):
        faces = {}
        with open(self.faces_path, newline='') as arquivo_csv:
            reader = csv.reader(arquivo_csv, delimiter=',')
            for row in reader:
                faces[row[0].strip()] = ([row[1].strip(), row[2].strip(), row[3].strip()], self.color_parser(row[4].strip()))

        return faces

    def color_parser(self, color):
        return color if (color[0]=='#') else ("#" + color)

    