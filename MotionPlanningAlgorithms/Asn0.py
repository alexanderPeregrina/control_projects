#Assignment 0
#Review of Python

#Imports and Definitions
import numpy as np
import matplotlib.pyplot as plt
cos = np.cos
sin = np.sin
atan2 = np.arctan2

#Random points
x1 = 500
y1 = 200
psi1 = 0.45
x2 = 1000
y2 = 430
psi2 = -1.35

length = 40
width = 15

#Plotting
fig = plt.figure("Configuration Space")
grid = np.load('cspaceRoadmap.npy')
plt.imshow(grid, cmap='binary', origin = 'lower')
plt.arrow(x1, y1, length * cos(psi1), length * sin(psi1), fc="b", ec="b", head_width=width, head_length=width)
#TODO: Plot arrow for x2, y2 and psi2 (similar to above), in red color ("r")
plt.arrow(x2, y2, length * cos(psi2), length * sin(psi2), fc="r", ec="r", head_width=width, head_length=width)
    
plt.xlabel('X-axis $(m)$')
plt.ylabel('Y-axis $(m)$')

#Determine angle psi3 between <x1,x2> and <y1,y2> (atan2(dy,dx)), and plot the arrow on <x1,y1>
psi3 = atan2(y2-y1, x2-x1)
plt.arrow(x1, y1, length * cos(psi3), length * sin(psi3), fc="g", ec="g", head_width=width, head_length=width)

#Configuration Space - for a point use grid[y][x]
print(grid[754][345])
print(grid[345][229])
#TODO: print grid at x = 1455, y = 765
print(grid[765][1455])
print(grid.shape)
print("--------------------------")
plt.show()

#Trees
class treeNode():
    def __init__(self, locationX, locationY):
        self.locationX = locationX                #X Location
        self.locationY = locationY                #Y Location  
        self.children = []                        #children list   
        self.parent = None                        #parent 
        
#Tree Traversal - Recursive DFS
def DFS(node):
    print(node.locationX, node.locationY)
    for child in node.children:
        DFS(child)

A = treeNode(45, 67)
B = treeNode(100,100)
A.children.append(B)
B.parent = A


C = treeNode(145,254)
B.children.append(C)
C.parent = B   

D = treeNode(65,65)
C.children.append(D)
D.parent = C

print("Depth First Search")
DFS(A)
