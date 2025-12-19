import os
import platform
import subprocess

import numpy as np

from IPython.display import Image

from matplotlib.patches import Rectangle
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt

SYSTEM = platform.system()


def shift_coordinate(state):
    x, y = state
    return x - .5, y - .5


def set_up_GBG(w, h, jarntorget, chalmers, home):
    fig = plt.figure(figsize=(6, 9))
    gs = GridSpec(4, 3, figure=fig)
    
    ax = fig.add_subplot(gs[1:, :])
    ax.set_aspect(w/h)
    ax.set_title('WindyGothenburg')
    ax.set_xlim(-.5, w + .5)
    ax.set_ylim(-.5, h + .5)
    ax.hlines(range(h+1), -.5, w+1, color='grey', linewidth=.5)
    ax.vlines(range(w+1), -.5, h+1, color='grey', linewidth=.5)
    ax.annotate('JT', shift_coordinate(jarntorget), fontname='Segoe UI Emoji', fontsize=25, color='r')
    ax.add_patch(Rectangle(shift_coordinate((0, h)), 2, 1, color='grey'))
    ax.annotate('P', shift_coordinate(chalmers), fontname='Segoe UI Emoji', fontsize=25, color='b')
    ax.annotate('H', shift_coordinate(home), fontname='Segoe UI Emoji', fontsize=25, color='g')
    ax.add_patch(Rectangle(shift_coordinate((w, h)), 1, 1, color='grey'))
    ax.add_patch(Rectangle(shift_coordinate((2, h)), w-2, 1, color='b'))   
    grid_world = ax

    ax = fig.add_subplot(gs[0, :])
    ax.grid(True)
    ax.set_xlabel('Episode')
    ax.xaxis.set_label_position('top') 
    ax.xaxis.tick_top()
    ax.set_ylabel('Average Reward')
    ax.set_ylim(-2, 8)
    scatter_plot = ax
    
    return fig, grid_world, scatter_plot


def argmax_Q(Q, state):
    max_q = float("-inf")
    argmax_q = None
    for a, q in Q[state].items():
        if q > max_q:
            max_q = q
            argmax_q = a
    return argmax_q


def plot_Q(ax, Q, w, h):
    x = y = np.arange(0, h + 1, 1)
    X, Y = np.meshgrid(x, y)
    V = np.array([max(Q[(i, j)].values()) for j in range(h+1) for i in range(w+1)])
    V = V.reshape(X.shape)
    Q_contours = ax.contourf(X, Y, V, levels=20, vmin=-10, vmax=90, cmap='RdYlGn', alpha=.5)
    labels = ax.clabel(Q_contours, inline=True, fontsize=10)
    symbls = {'north': 6, 'east': 5, 'south': 7, 'west': 4}
    policy_markers = [ax.scatter(*x, color='g', marker=symbls[argmax_Q(Q, x)]) for x in Q.keys()]
    return Q_contours, labels, policy_markers


def plot_pos(ax, pos):
    return ax.annotate('$😴$',shift_coordinate(pos), fontname='Segoe UI Emoji', fontsize=25)


def clear_plot(contours, labels, policy_markers):
    for c in contours.collections:
        c.remove()
    for l in labels:
        l.remove()
    for m in policy_markers:
        m.remove()


def plot_average_r(ax, avg_r, eps):
    return ax.plot(eps, avg_r, 'b.')
