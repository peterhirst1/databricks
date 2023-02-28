# Databricks notebook source
import matplotlib.pyplot as plt
import numpy as np



# COMMAND ----------

#creates y axis from -1 to 1 with 5 increments evenly spaced
y = np.linspace(-1,1,5)
# creates an x axis from 0-4
x = np.arange(5)
fig = plt.figure()
ax = fig.subplots()
#creates new line plot
y2 = np.linspace(-2,2,5)
#these plot the lines
line1 = ax.plot(x,y)
line2 = ax.plot(x,y2)


# COMMAND ----------

number_rows = 3
number_columns = 2
fig2 = plt.figure()
ax2 = fig2.subplots(number_rows, number_columns)
#in square bracket is which gragh its in 
ax2[2,1].plot(x,y)

ax2[0,1].plot(x,y)

# COMMAND ----------

#for different types of graphs 
y1 = np.arange(0,110,10)
y2 = np.random.random(11)
x = np.arange(11)

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x,y1)
ax[0,1].scatter(x,y2)
ax[1,0].bar(x,y1)
ax[1,1].barh(x,y1)

# COMMAND ----------

x = np.arange(0,4*np.pi, 0.05)
ycos = np.cos(x)
ysin = np.sin(x)

fig, ax = plt.subplots()
#set colour, line type and label
ax.plot(x, ycos, 'b-', label="cos(x)")
ax.plot(x, ysin, 'r--', label="sin(x)")

ax.set_title("Trigonometric functions")
ax.set_xlabel("0 to 4pi")
ax.set_ylabel("cos(x) and sin(x)")
ax.legend()

# COMMAND ----------

fig, ax = plt.subplots(1,2)

ax[0].axhline(0.3, color='red')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=10)
ax[0].axhline(0.6, linestyle=':', xmin=0.25, xmax=0.75, color='orchid')
ax[0].axhline(0.7, xmin=0.25, xmax=0.75, color=(0.1,0.2, 0.5, 0.3))

ax[1].axvline(0.3, color='red')
ax[1].axvline(0.4, linestyle='--', color='blue')
ax[1].axvline(0.5, color='cyan', linewidth=10)
ax[1].axvline(0.6, linestyle=':', ymin=0.25, ymax=0.75, color=('orchid'))
ax[1].axvline(0.7, ymin=0.25, ymax=0.75, color=(0.1,0.2, 0.5, 0.3))
#set x-axis and y-axis limits
ax[0].set_ylim([0.1, 0.9])
ax[1].set_xlim([0.1, 0.9])

#set title to figure and subplots
fig.suptitle("horizontal and vertical lines", fontsize=14)
ax[0].set_title("horizontal lines", fontstyle='italic')
ax[1].set_title("vertical lines",color='green',fontname='Ariel')

# COMMAND ----------

x = np.array([2,4,6,7,4,2,5,7,8,9,4,2,1])
y = np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])

fig, ax = plt.subplots(1,3)
ax[0].scatter(x,y)
ax[0].set_title('default')

ax[1].scatter(x,y, 50, marker='+')
ax[1].set_title('size = 50, style = +')

crosses = ax[2].scatter(x, y, 200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, 50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------

#3D 
z = np.array([0,1,4,3,5,1,2,5,7,5,9,8,5])
y = np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])
fig = plt.figure()
ax = np.array([fig.add_subplot(1, 3, 1, projection='3d'),
              fig.add_subplot(1, 3, 2, projection='3d'),
              fig.add_subplot(1, 3, 3, projection='3d')])

ax[0].scatter(x,y,z)
ax[0].set_title('default')

ax[1].scatter(x, y, z, s=50, marker='+')
ax[1].set_title('size = 50, style = +')

crosses = ax[2].scatter(x, y, z, s=200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, z, s=50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------

people = ["student A", "student B"]
studentA = np.array([90,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange(len(studentA))

fig, ax = plt.subplots(1,2)

ax[0].bar(x, studentA, width=0.3)
ax[1].bar(x, studentB, width=0.3)

for i in range(len(ax)):
    ax[i].set_ylim([0, 100])
    ax[i].set_title(people[i])
    ax[i].set_xlabel("exercise")
    ax[i].set_ylabel("mark (%)")
    ax[i].set_xticks([0,1,2,3])
    ax[i].set_xticklabels(["ex1", "ex2", "ex3", "ex4"])
    
fig.tight_layout()


# COMMAND ----------

fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/2, studentA, width, label='student A')
s2bars = ax.bar(x + width/2, studentB, width, label='student B')

# COMMAND ----------

people = ["student A", "student B"]
studentA = np.array([90,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange(len(studentA))
width=5
fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/2, studentA, width, label='student A', linewidth=3)
s2bars = ax.bar(x + width/2, studentB, width, label='student B', linewidth=3)


ax.set_ylim([0, 100])
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_xticks([0,1,2,3])
ax.set_xticklabels(["one", "two", "three", "four"])
ax.set_title("graph")
ax.legend()

for i in range(len(studentA)):
    if studentA[i] < 50:
        s1bars[i].set_edgecolor('red')
    if studentB[i] < 50:
        s2bars[i].set_edgecolor('red')

# COMMAND ----------


