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

if __name__ == '__main__':
    # demo_simple()    
    demo_ani()