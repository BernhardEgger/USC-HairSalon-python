#helpful to parse binary data: https://docs.python.org/3/library/struct.html
#this decodes the following file format:
#NumofStrand(int)
#NumOfVertices(int) Vertex1(3 float) Vertex2(3 float) Vertex3(3 float) ...
#NumOfVertices(int) Vertex1(3 float) Vertex2(3 float) Vertex3(3 float) ...
#...
#...

import struct
import numpy as np
fin = open ("strands00001.data", "rb")
num_of_strands = struct.unpack('i', fin.read(4))[0]
hair = []
#print("num_of_strands: ", num_of_strands)
for i in range(num_of_strands):
  num_of_vertices = struct.unpack('i', fin.read(4))[0]
  #print("num_of_vertices: ", num_of_vertices)
  strand = []
  for j in range(num_of_vertices):
    vertex_x = struct.unpack('f', fin.read(4))[0]
    vertex_y = struct.unpack('f', fin.read(4))[0]
    vertex_z = struct.unpack('f', fin.read(4))[0]
    vertex = [vertex_x, vertex_y, vertex_z]
    #print("vertex: ", vertex)
    strand.append(vertex)
  hair.append(strand)
  #print(len(strand), num_of_vertices)
#print(len(hair), num_of_strands)
#print(hair)
