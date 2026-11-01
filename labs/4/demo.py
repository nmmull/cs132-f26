import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, RadioButtons
from matplotlib.collections import LineCollection
from lab4 import *

#############################
# MATPLOTLIB CONFIGURATIONS #
#############################

# set up subplots
fig, axes = plt.subplot_mosaic(
    [['main', 'log'],
     ['main', 'shape'],
     ['main', '.']],
    width_ratios=[3.5, 1.5],
    height_ratios=[2, 2, 1])

# make room in plot for sliders
fig.subplots_adjust(left=0.25, bottom=0.25, right=0.75)

# settings
axes['main'].set_xlim((-6, 6))
axes['main'].set_ylim((-6, 6))
axes['main'].set_aspect('equal')
axes['main'].set_autoscale_on(False)
axes['main'].xaxis.set_tick_params(labelbottom=False)
axes['main'].yaxis.set_tick_params(labelleft=False)
axes['main'].set_xticks([])
axes['main'].set_yticks([])
axes['main'].set_title("3D Graphics Demo")
axes['shape'].set_title("Shapes")
axes['log'].axis('off')

###############
# WIRE FRAMES #
###############

cube = [[(-1, -1, -1), (1, -1, -1)],
        [(1, -1, -1), (1, 1, -1)],
        [(1, 1, -1), (-1, 1, -1)],
        [(-1, 1, -1), (-1, -1, -1)],
        [(-1, -1, -1), (-1, -1, 1)],
        [(1, -1, -1), (1, -1, 1)],
        [(1, 1, -1), (1, 1, 1)],
        [(-1, 1, -1), (-1, 1, 1)],
        [(-1, -1, 1), (1, -1, 1)],
        [(1, -1, 1), (1, 1, 1)],
        [(1, 1, 1), (-1, 1, 1)],
        [(-1, 1, 1), (-1, -1, 1)]]

pyramid = [[(-1, -1, -1), (-1, -1, 1)],
           [(-1, -1, 1), (1, -1, 1)],
           [(1, -1, 1), (1, -1, -1)],
           [(1, -1, -1), (-1, -1, -1)],
           [(-1, -1, -1), (0, 1, 0)],
           [(-1, -1, 1), (0, 1, 0)],
           [(1, -1, 1), (0, 1, 0)],
           [(1, -1, -1), (0, 1, 0)]]

def mk_circle(r, n, z):
    out = []
    for i in range(n):
        out.append(((r * np.cos(2 * np.pi * i / n), r * np.sin(2 * np.pi * i / n), z),
                    (r * np.cos(2 * np.pi * (i + 1) / n), r * np.sin(2 * np.pi * (i + 1) / n), z)))
    return out

def mk_wheel_edge(r, n, z1, z2):
    out = []
    for i in range(n):
        out.append(((r * np.cos(2 * np.pi * i / n), r * np.sin(2 * np.pi * i / n), z1),
                    (r * np.cos(2 * np.pi * i / n), r * np.sin(2 * np.pi * i / n), z2)))
    return out

def mk_wheel_face(r1, r2, n, z):
    out = []
    for i in range(n):
        out.append(((r1 * np.cos(2 * np.pi * i / n), r1 * np.sin(2 * np.pi * i / n), z),
                    (r2 * np.cos(2 * np.pi * i / n), r2 * np.sin(2 * np.pi * i / n), z)))
    return out

wheel = mk_circle(3, 50, 1) + \
    mk_circle(1, 50, 1) + \
    mk_circle(3, 50, -1) + \
    mk_circle(1, 50, -1) + \
    mk_wheel_edge(3, 50, 1, -1) + \
    mk_wheel_edge(1, 50, 1, -1) + \
    mk_wheel_face(1, 3, 50, 1) + \
    mk_wheel_face(1, 3, 50, -1)

guide_axes = [[(-0.75, 0, 0), (0.75, 0, 0)],
              [(0, -0.75, 0), (0, 0.75, 0)],
              [(0, 0, -0.75), (0, 0, 0.75)]]

shapes = {'cube': guide_axes + cube,
          'pyramid': guide_axes + pyramid,
          'wheel': guide_axes + wheel,
          extra_credit_name: guide_axes + extra_credit_shape}

# the shape being viewed
base_shape = shapes['cube']

###################
# TRANSFORMATIONS #
###################

# dictionary of global parameters
# updated by the sliders
global_params = { 'tx' : 0.0,  # x-axis translation
                  'ty' : 0.0,  # y-axis translation
                  'tz' : 0.0,  # z-axis translation
                  'rx' : 0.0,  # roll rotation
                  'ry' : 0.0,  # pitch rotation
                  'rz' : 0.0 } # yaw rotation

def mk_transform():
    p = global_params
    return transform_matrix(p['tx'], p['ty'], p['tz'], p['rx'], p['ry'], p['rz'])

def mk_full_transform(shape):
    p = global_params
    return full_transform(p['tx'], p['ty'], p['tz'], p['rx'], p['ry'], p['rz'], shape)

###########
# DISPLAY #
###########

lc = LineCollection(
    mk_full_transform(base_shape),
    linewidth=1,
    colors=(['r', 'g', 'b'] + (len(base_shape) - 3) * ['C0']))

s = axes['main'].add_collection(lc)

def update_curr_shape():
    s.set(segments=mk_full_transform(base_shape))

def set_curr_shape(shape):
    global base_shape
    base_shape = shape
    update_curr_shape()
    s.set(colors=['r', 'g', 'b'] + (len(base_shape) - 3) * ['C0'])

#######
# LOG #
#######

def log():
    return f"""
Transformation:
--------------

{mk_transform()}

"""

log_text = axes['log'].text(0, 0, log(), name='Courier', fontsize=9)
update_log = lambda: log_text.set(text=log())

###########
# SLIDERS #
###########

slider_position = lambda index: [0.25, 0.20 - 0.03 * index, 0.45, 0.03]
slider = lambda name, pos, r: Slider(
    ax=fig.add_axes(slider_position(pos)),
    label=name,
    valmin=-r,
    valmax=r,
    valinit=0.0,
    valstep=0.1)

theta_slider_x = slider('roll', 0, 7.0)
theta_slider_y = slider('pitch', 1, 7.0)
theta_slider_z = slider('yaw', 2, 7.0)
trans_slider_x = slider('x', 3, 5.0)
trans_slider_y = slider('y', 4, 5.0)
trans_slider_z = slider('z', 5, 5.0)

def set_update(pname, slider):
    def update(val):
        global_params[pname] = val
        update_curr_shape()
        update_log()
        fig.canvas.draw_idle()
    slider.on_changed(update)

updates = [('rx', theta_slider_x),
           ('ry', theta_slider_y),
           ('rz', theta_slider_z),
           ('tx', trans_slider_x),
           ('ty', trans_slider_y),
           ('tz', trans_slider_z)]

# connect sliders to functions
for name, slider in updates:
    set_update(name, slider)

#################
# RADIO BUTTONS #
#################

shape_radio = RadioButtons(axes['shape'] , list(shapes.keys()))

def draw_shape(label):
    set_curr_shape(shapes[label])
    fig.canvas.draw()

# connect radio buttons to functions
shape_radio.on_clicked(draw_shape)

#######
# FIN #
#######

plt.show()
# DO NOT ADD ANYTHING AFTER THIS LINE
