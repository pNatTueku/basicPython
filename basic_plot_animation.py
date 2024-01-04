import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# create functions and test

def demo_simple():

    # ref: http://mathworld.wolfram.com/HeartCurve.html
    t = np.linspace(0, 2 * np.pi, 180) # linear space
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    plt.plot(x, y)
    plt.show()

def demo_ani():

    def update_line(num):
        chart.set_data(data[..., :num])
        return chart,

    # ref: http://mathworld.wolfram.com/HeartCurve.html
    t = np.linspace(0, 2 * np.pi, 180) # linear space
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    data = np.vstack((x, y)) # 2x180
    fig = plt.figure()

    plt.xlim(np.min(x), np.max(x))
    plt.ylim(np.min(y), np.max(y))

    chart, = plt.plot([], [])
    ani = animation.FuncAnimation(fig, update_line, interval = 10) # set speed to 10 milliseconds
    plt.show()

def demo1():
    # heart
    # t = np.linspace(0, 2 * np.pi, 180)
    # x = 16 * np.sin(t) ** 3
    # y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    # butterfly: https://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)
    t = np.linspace(0, 5 * np.pi, 180 * 5)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
    plot_ani(x, y, lw = 3, interval = 10)

def plot_ani(x, y, color = "green", interval = 20, lw = 2):
    def update_line(num):
        chart.set_data(data[..., :num])
        return chart,

    # ref: http://mathworld.wolfram.com/HeartCurve.html
    data = np.vstack((x, y))  # 2 x 180
    fig = plt.figure()
    padding = 1.1
    plt.xlim(np.min(x) * padding, np.max(x) * padding)
    plt.ylim(np.min(y) * padding, np.max(y) * padding)
    chart, = plt.plot([], [], color = color, linewidth = lw)
    ani = animation.FuncAnimation(fig, update_line, interval = interval, frames = x.size, repeat = False)
    # required ffmpeg
    # ani.save("ani_demo2.mp4")
    plt.show()

if __name__ == '__main__':
    # demo_simple()    
    # demo_ani()
    demo1()