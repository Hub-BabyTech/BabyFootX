#!/usr/bin/env python3

from matplotlib import pyplot as plt 

f = open("data.txt", "r")
# data = f.read()
x = []
y = []
j = 0
# print(f.read())
for line in f.readlines():
    if j == 0:
        x += [int(line)]
        j=1
    else:
        j=0
        y+= [int(line)]
    # print(line)

plt.plot(x,y,"-gs")

print("X : ", x, "\nY : ", y)

plt.title("Nuage de points")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('points.png')
plt.show()