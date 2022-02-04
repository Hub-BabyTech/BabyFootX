#!/usr/bin/env python3

from matplotlib import pyplot as plt 
from matplotlib.patches import Circle
import matplotlib.cm as cm

f = open("data.txt", "r")
# data = f.read()
x = []
y = []
j = 0
# print(f.read())
img = plt.imread('images/stade.jpg')

fig, ax = plt.subplots(1)
ax.imshow(img)
ax.axis('off')

i = 0
for line in f.readlines():
    if j == 0:
        x += [int(line)]
        j=1
    else:
        j=0
        y+= [int(line)]
        print("x :", x[-1], "y :", -y[-1])
        # circ = Circle((x[-1]/1920*750, -y[-1]/1080*584), 15, color="#FFA50012")
        # ax.add_patch(circ)
        # circ = Circle((x[-1]/1920*750, -y[-1]/1080*584), 7, color="#FFA50032")
        # ax.add_patch(circ)
        # circ = Circle((x[-1]/1920*750, -y[-1]/1080*584), 3, color="#FFA50064")
        # ax.add_patch(circ)
        circ = Circle((x[-1]/640*750, -y[-1]), 4, color=cm.hsv(i/200))
        ax.add_patch(circ)
        # if len(y) >=2:
        #     plt.plot([x[-2]/640*750, x[-1]/640*750], [-y[-2], -y[-1]], cm.hsv(i/200))
    i+=1
    if i == 200:
        i = 0
    # print(line)


# plt.imshow(img)
# ax.axis("off")
plt.show()

# plt.plot(x,y,"-gs")

# print("X : ", x, "\nY : ", y)

# plt.title("Nuage de points")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig('points.png')
plt.show()