import numpy as np
import math

from utilities import *

default_corners = {
    # using frozensets because sets cannot be used as keys in a dictionary
    #  frozensets are immutable sets
    frozenset((colors[0], colors[5], colors[2])): [  # wrg
        frozenset((colors[0], colors[2], colors[3])),
        frozenset((colors[0], colors[5], colors[1])),
        frozenset((colors[4], colors[2], colors[5]))],
    frozenset((colors[0], colors[3], colors[2])): [  # wog
        frozenset((colors[0], colors[1], colors[3])),
        frozenset((colors[0], colors[5], colors[2])),
        frozenset((colors[4], colors[3], colors[2]))],
    frozenset((colors[0], colors[5], colors[1])): [  # wrb
        frozenset((colors[0], colors[2], colors[5])),
        frozenset((colors[0], colors[1], colors[3])),
        frozenset((colors[4], colors[5], colors[1]))],
    frozenset((colors[0], colors[3], colors[1])): [  # wob
        frozenset((colors[0], colors[5], colors[1])),
        frozenset((colors[0], colors[3], colors[2])),
        frozenset((colors[4], colors[3], colors[1]))],
    frozenset((colors[4], colors[2], colors[3])): [  # ygo
        frozenset((colors[4], colors[5], colors[2])),
        frozenset((colors[4], colors[3], colors[1])),
        frozenset((colors[0], colors[2], colors[3]))],
    frozenset((colors[4], colors[2], colors[5])): [  # ygr
        frozenset((colors[4], colors[1], colors[5])),
        frozenset((colors[4], colors[2], colors[3])),
        frozenset((colors[0], colors[2], colors[5]))],
    frozenset((colors[4], colors[1], colors[3])): [  # ybo
        frozenset((colors[4], colors[2], colors[3])),
        frozenset((colors[4], colors[1], colors[5])),
        frozenset((colors[0], colors[1], colors[3]))],
    frozenset((colors[4], colors[1], colors[5])): [  # ybr
        frozenset((colors[4], colors[3], colors[1])),
        frozenset((colors[4], colors[5], colors[2])),
        frozenset((colors[0], colors[1], colors[5]))]
}


def create_corners(conf):
    corners = {
        frozenset((conf["F"][0], conf["L"][0], conf["U"][1])): np.array([0, 0, 1]),  # wrg
        frozenset((conf["F"][1], conf["R"][1], conf["U"][0])): np.array([1, 0, 1]),  # wog
        frozenset((conf["F"][2], conf["L"][1], conf["D"][0])): np.array([0, 0, 0]),  # wrb
        frozenset((conf["F"][3], conf["R"][0], conf["D"][1])): np.array([1, 0, 0]),  # wob
        frozenset((conf["B"][0], conf["U"][2], conf["R"][3])): np.array([1, 1, 1]),  # ygo
        frozenset((conf["B"][1], conf["U"][3], conf["L"][2])): np.array([0, 1, 1]),  # ygr
        frozenset((conf["B"][2], conf["D"][3], conf["R"][2])): np.array([1, 1, 0]),  # ybo
        frozenset((conf["B"][3], conf["D"][2], conf["L"][3])): np.array([0, 1, 0])   # ybr
    }
    return corners


def manhattan_distance(corners, subject_corner):
    coords = np.array([], dtype=np.int64).reshape(0, 3)
    distances = np.array([], dtype=np.int64).reshape(0, 3)

    subject_coords = corners[subject_corner]

    neighbors = default_corners[subject_corner]

    # extract the neighbors's coordinates
    for neighbor in neighbors:
        coords = np.vstack([coords, corners[neighbor]])
        # coords = np.concatenate((coords, corners[neighbor]), axis=0)

    # compute distance between subject_corner and its neighbors
    for i in range(len(neighbors)):
        distances = np.append(distances, (
                    abs(subject_coords[0] - coords[i][0]) + abs(subject_coords[1] - coords[i][1]) + abs(
                subject_coords[2] - coords[i][2])))
    return distances


def compute_h_manhattan(conf):
    corners = create_corners(conf)
    distances = np.array([], dtype=np.int64).reshape(0, 3)
    for subject_corner in default_corners:
        distances = np.append(distances, manhattan_distance(corners, subject_corner))
    return np.sum(distances) / 72


def compute_h_cube(new_position):  # (node):
    # compute the heuristic:
    # for every list/face find the color with maximum frequency
    #   and assign as score the number of occurrences of the color
    # node is a dictionary
    h = 24.0
    h -= child_node_h(new_position)  # (node.new_position)
    return h


def child_node_h(new_position):
    h = 0
    for face in faces:
        h += max(count_colors(new_position[face]))
    h = math.floor(h)  # if you prefer, .ceil(h)
    return h


def count_colors(face):
    occurrences_of_colors = []
    for color in colors:
        occurrences_of_colors.append(face.count(color))
    return occurrences_of_colors
