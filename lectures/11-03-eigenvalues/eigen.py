import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, RadioButtons
from matplotlib.collections import LineCollection

#############################
# MATPLOTLIB CONFIGURATIONS #
#############################

# set up subplots
fig, axes = plt.subplot_mosaic(
    [['main', 'matrix'],
     ['main', 'matrix'],
     ['main', 'matrix']],
    width_ratios=[3.5, 1.5])

# make room in plot for sliders
fig.subplots_adjust(left=0.25, bottom=0.25, right=0.75)

# settings
axes['main'].set_xlim((-1, 1))
axes['main'].set_ylim((-1, 1))
axes['main'].set_aspect('equal')
axes['main'].set_autoscale_on(False)
axes['main'].axhline(0, color='black', linewidth=0.5)
axes['main'].axvline(0, color='black', linewidth=0.5)
axes['main'].xaxis.set_tick_params(labelbottom=False)
axes['main'].yaxis.set_tick_params(labelleft=False)
axes['main'].set_xticks([])
axes['main'].set_yticks([])
axes['main'].set_title("Eigenvector Demo")
axes['matrix'].set_title("Matrices")

a = np.array([
    [2.0, -1.0],
    [1.0, 0.0]])

simple = a @ np.diag([2 ** 0.01, 3 ** 0.01]) @ np.linalg.inv(a)

shear = np.array([
    [1, 0.01],
    [0, 1]])

scale = np.array([
    [1.02, 0],
    [0, 0.98]])

rotate = np.array([
    [np.cos(0.01), -np.sin(0.01)],
    [np.sin(0.01), np.cos(0.01)]])

contract = np.array([
    [0.98, 0],
    [0, 0.98]])

fib = np.array([
    [1., 1],
    [1, 0]])

_, d, v = np.linalg.svd(np.array([[1., 1], [1, 0]]))

def mpow(a):
    return lambda k, x: np.linalg.matrix_power(a, k) @ x

def fib_like(k, x):
    return np.dot(v.T * (d ** (k * 0.08)), v) @ x

functions = {
    "simple" : mpow(simple),
    "shearing" : mpow(shear),
    "scaling" : mpow(scale),
    "rotation" : mpow(rotate),
    "contraction" : mpow(contract),
    "fibonacci" : mpow(fib),
    "fibonacci-like" : fib_like}

base_function = functions['simple']

global_params = { 'time' : 0 }

a = np.array([[x, y] for x in np.arange(-2, 2, 0.1) for y in np.arange(-2, 2, 0.1)]).T

# stole this from the internet and modified
s, = axes['main'].plot(*zip(*a.T), marker='.', color='r', ls='', markersize=1)

def update_curr():
    data = np.hstack([a] + [base_function(i, a) for i in range(global_params['time'])])
    # s.set_data(base_function(global_params['time'], a))
    s.set_data(data)

def set_curr_func(f):
    global base_function
    base_function = f
    update_curr()

###########
# SLIDERS #
###########

slider_position = lambda index: [0.25, 0.20 - 0.03 * index, 0.45, 0.03]
slider = lambda name, pos, mx: Slider(
    ax=fig.add_axes(slider_position(pos)),
    label=name,
    valmin=0,
    valmax=mx,
    valinit=0,
    valstep=1)

power_slider = slider('time', 0, 200)

def set_update(pname, slider):
    def update(val):
        global_params[pname] = val
        update_curr()
        fig.canvas.draw_idle()
    slider.on_changed(update)

updates = [('time', power_slider)]

# connect sliders to functions
for name, slider in updates:
    set_update(name, slider)

#################
# RADIO BUTTONS #
#################

shape_radio = RadioButtons(axes['matrix'] , list(functions.keys()))

def matrices(label):
    set_curr_func(functions[label])
    fig.canvas.draw()

# connect radio buttons to functions
shape_radio.on_clicked(matrices)

#######
# FIN #
#######

plt.show()
