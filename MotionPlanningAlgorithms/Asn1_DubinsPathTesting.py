import matplotlib.pyplot as plt
from Asn1_DubinsPath import cos, sin, pi, returnDubinsPath

x1 = 145
y1 = 715
psi1 = 0
x2 = 345
y2 = 125
psi2 = 0
R = 25

xtrajectory, ytrajectory, pathDistance = returnDubinsPath(x1, y1, psi1, x2, y2, psi2, R)

#Plot results
length = 35
width = 10

if pathDistance is not None:
    plt.figure("Dubin's path - CCC")
    plt.arrow(x1, y1, length * cos(psi1), length * sin(psi1), fc="b", ec="b", head_width=width, head_length=width)
    plt.arrow(x2, y2, length * cos(psi2), length * sin(psi2), fc="r", ec="r", head_width=width, head_length=width)
    plt.plot(xtrajectory, ytrajectory, color = "k")
    plt.xlim(0, 1000)
    plt.ylim(0, 1000) 
    plt.show()