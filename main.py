import tkinter as tk
import sys
import csv_parser as parser
import designer as designer


if __name__ == "__main__":
    root = tk.Tk()  
    root.title('Trabalho 1')
    csv_parser = parser.CsvParser(sys.argv[1], sys.argv[2])
 
    vertices = csv_parser.vertices_to_dict()
    faces = csv_parser.faces_to_dict()
    d = designer.Designer(root, vertices, faces)
    d.scale(10)
    d.vertical_skew(1)
    d.draw()
    root.mainloop()