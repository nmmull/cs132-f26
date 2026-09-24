import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, RadioButtons
from matplotlib.colors import to_rgba

#########
# SETUP #
#########

fig, axes = plt.subplot_mosaic(
    [['main', 'shape'],
     ['main', 'presets'],
     ['main', 'text']],
    width_ratios=[3.5, 1.5],
    height_ratios=[1, 2, 2]
)

# make room in plot for sliders
fig.subplots_adjust(left=0.25, bottom=0.25, right=0.75)

# configurations
axes['main'].set_xlim((-6, 6))
axes['main'].set_ylim((-6, 6))
axes['main'].set_aspect('equal')
axes['main'].grid(True)
axes['main'].set_autoscale_on(False)
axes['main'].axhline(0, color='black', linewidth=0.5)
axes['main'].axvline(0, color='black', linewidth=0.5)
axes['text'].axis('off')

# titles
axes['main'].set_title("2D Matrix Transformations")
axes['shape'].set_title('Shapes')
axes['presets'].set_title('Preset Matrices')

##########
# SHAPES #
##########

unit_square = np.array(
    [[0., 0],
     [1, 0],
     [1, 1],
     [0, 1]])

# taken from Professor Mark Crovella's material
music_note = np.array(
    [[193,47],
     [140,204],
     [123,193],
     [99,189],
     [74,196],
     [58,213],
     [49,237],
     [52,261],
     [65,279],
     [86,292],
     [113,295],
     [135,282],
     [152,258],
     [201,95],
     [212,127],
     [218,150],
     [213,168],
     [201,185],
     [192,200],
     [203,214],
     [219,205],
     [233,191],
     [242,170],
     [244,149],
     [242,131],
     [233,111]])/150.0

centered_square = np.array(
    [[1., 1],
     [-1, 1],
     [-1, -1],
     [1, -1]])

polygon = np.array(
    [[4., 1],
     [1, 2],
     [0, 0],
     [2, 1]]) - 3.0

base_shape = unit_square

# draw the base shape
s, = axes['main'].fill(base_shape.T[0], base_shape.T[1])
s.set_facecolor(to_rgba('blue', 0.3))
s.set_edgecolor(to_rgba('blue', 1.0))
s.set_linewidth(2.0)

# copy of base shape to transform
trans_shape = np.copy(base_shape)
t, = axes['main'].fill(trans_shape.T[0], trans_shape.T[1])
t.set_facecolor(to_rgba('red', 0.3))
t.set_edgecolor(to_rgba('red', 1.0))
t.set_linewidth(2.0)

update_base_shape = lambda: s.set_xy(base_shape)
update_trans_shape = lambda: t.set_xy((rotation @ transform @ trans_shape.T).T)

###################
# TRANSFORMATIONS #
###################

# global first tranformation
transform = np.array(
    [[1., 0],
     [0, 1]])

# global second transformation (rotation)
rotation = np.array(
    [[1., 0],
     [0, 1]])

# preset matrices
fbf = lambda a, b, c, d: np.array([[float(a), b], [c, d]])
id_mat = fbf(1, 0, 0, 1)
dil_mat = fbf(3, 0, 0, 3)
con_mat = fbf(0.75, 0, 0, 0.75)
hor_scl_mat = fbf(3, 0, 0, 1)
ver_scl_mat = fbf(1, 0, 0, 3)
hor_shr_mat = fbf(1, 1, 0, 1)
ver_shr_mat = fbf(1, 0, 1, 1)
ref_x_mat = fbf(1, 0, 0, -1)
ref_y_mat = fbf(-1, 0, 0, 1)
ref_xey_mat = fbf(0, 1, 1, 0)
ref_xeny_mat = fbf(0, -1, -1, 0)
ref_org_mat = fbf(-1, 0, 0, -1)
proj_x_mat = fbf(1, 0, 0, 0)
proj_y_mat = fbf(0, 0, 0, 1)

#######
# LOG #
#######

def log():
    return fr"""1st Transform
A = [[a, b]
    [c, d]]

{transform}

2nd Transform (rotation)
B = [[cos($\theta$), -sin($\theta$)]
    [sin($\theta$),  cos($\theta$)]]

{rotation}
"""

log_text = axes['text'].text(0, 0, log(), name='Courier', fontsize=9)
update_log = lambda: log_text.set(text=log())

axes['main'].text(-5.7, -5.7, r"$\{B(Ax): x \in$Shape$\}$", name='Courier', fontsize=9)

###########
# SLIDERS #
###########

slider_position = lambda index: [0.25, 0.20 - 0.03 * index, 0.45, 0.03]
a_slider = Slider(
    ax=fig.add_axes(slider_position(0)),
    label="a",
    valmin=-4.0,
    valmax=4.0,
    valinit=1.0,
    valstep=0.1)
b_slider = Slider(
    ax=fig.add_axes(slider_position(1)),
    label="b",
    valmin=-4.0,
    valmax=4.0,
    valinit=0.0,
    valstep=0.1)
c_slider = Slider(
    ax=fig.add_axes(slider_position(2)),
    label="c",
    valmin=-4.0,
    valmax=4.0,
    valinit=0.0,
    valstep=0.1)
d_slider = Slider(
    ax=fig.add_axes(slider_position(3)),
    label="d",
    valmin=-4.0,
    valmax=4.0,
    valinit=1.0,
    valstep=0.1)
theta_slider = Slider(
    ax=fig.add_axes(slider_position(4)),
    label=r"$\theta$",
    valmin=-7.0,
    valmax=7.0,
    valinit=0.0,
    valstep=0.1)

def set_update(lam, slider):
    def update(val):
        lam(slider.val)
        update_trans_shape()
        update_log()
        fig.canvas.draw_idle()
    slider.on_changed(update)

def update_index(index):
    def out(val):
        transform[index] = val
    return out

def update_rotate(theta):
    rotation[0, 0] = np.cos(theta)
    rotation[0, 1] = -np.sin(theta)
    rotation[1, 0] = np.sin(theta)
    rotation[1, 1] = np.cos(theta)

# connect sliders to functions
set_update(update_index((0, 0)), a_slider)
set_update(update_index((0, 1)), b_slider)
set_update(update_index((1, 0)), c_slider)
set_update(update_index((1, 1)), d_slider)
set_update(update_rotate, theta_slider)

#################
# RADIO BUTTONS #
#################

shape_radio = RadioButtons(axes['shape'] , (
    'unit square',
    'centered square',
    'music note',
    'polygon'))

presets_radio = RadioButtons(axes['presets'], (
    'identity',
    'dilation',
    'contraction',
    'hor. scaling',
    'hor. shearing',
    'vert. shearing',
    'reflect thr. $x_1$',
    'reflect thr. $x_2$',
    'reflect thr. $x_1 = x_2$',
    'reflect thr. $x_1 = -x_2$',
    'project $x_1$-axis',
    'project $x_2$-axis'))

def presets(label):
    d = {'identity': id_mat,
         'dilation': dil_mat,
         'contraction': con_mat,
         'hor. scaling': hor_scl_mat,
         'vert. scaling': ver_scl_mat,
         'hor. shearing': hor_shr_mat,
         'vert. shearing': ver_shr_mat,
         'reflect thr. $x_1$': ref_x_mat,
         'reflect thr. $x_2$': ref_y_mat,
         'reflect thr. $x_1 = x_2$': ref_xey_mat,
         'reflect thr. $x_1 = -x_2$': ref_xeny_mat,
         'reflect thr. origin': ref_org_mat,
         'project $x_1$-axis': proj_x_mat,
         'project $x_2$-axis': proj_y_mat}
    global transform
    transform = np.copy(d[label])
    a_slider.set_val(transform[0, 0])
    b_slider.set_val(transform[0, 1])
    c_slider.set_val(transform[1, 0])
    d_slider.set_val(transform[1, 1])
    theta_slider.reset()
    update_trans_shape()
    fig.canvas.draw()

def shapes(label):
    d = {'unit square': unit_square,
         'music note': music_note,
         'centered square': centered_square,
         'polygon': polygon}
    new_shape = d[label]
    global base_shape, trans_shape
    base_shape = new_shape
    trans_shape = new_shape
    update_base_shape()
    update_trans_shape()
    fig.canvas.draw()

# connect radio buttons to functions
presets_radio.on_clicked(presets)
shape_radio.on_clicked(shapes)

#######
# FIN #
#######

plt.show()
