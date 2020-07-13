#Adapted from ImportanceOfBeingErnest answer on Stackoverflow https://stackoverflow.com/questions/42192133/embedding-matplotlib-live-plot-data-from-arduino-in-tkinter-canvas
from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.geometry('1200x700+200+100')
root.title('This is my root window')
root.state('zoomed')
root.config(background='#fafafa')

xar = []
yar = []

style.use('ggplot')
fig = plt.figure(figsize=(14, 4.5), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(0, 100)
line, = ax1.plot(xar, yar, 'r', marker='o')

def animate(i):
    yList = []
    pullData = open("last_list.csv","r").read()
    dataList = pullData.split('\n')
    dataList.pop(0)
    for eachLine in dataList:
        if len(eachLine) > 0:
            y, x = eachLine.split(',')
            yList.append(int(float(y)))
            xList = list(range(len(yList)))
    ax1.clear()
    ax1.plot(xList,yList)


plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().grid(column=1, row=1)
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False)

root.mainloop()

