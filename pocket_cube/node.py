from utilities import faces
from heuristic import compute_h_manhattan
from moves import dm, f


def eq_conf(child, parent):
    # child and parent are dictionaries
    # creating two new set in order to compare them
    child_set = set(tuple(row) for row in child.values())
    parent_set = set(tuple(row) for row in parent.values())
    return child_set == parent_set


def compute_conf(parent, move):
    # input: parent(dictionary) and move()
    # output: child(dictionary) configuration
    child = {}
    # in order to not overwrite the parent dictionary
    for face in faces:
        child[face] = parent[face].copy()
    return move(child)


class Node:
    def __init__(self, parent=None, new_position=None, move=dm):  # new_position is the new config. of the cube (dict.)
        self.parent = parent
        self.new_position = new_position
        self.move = move
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other_conf):
        is_eq = list(self.new_position.values()) == list(other_conf.new_position.values())
        return is_eq

    def compute_itself(self):
        return compute_conf(self.parent.new_position, self.move)

    def compute_h(self):
        if self.g < 4:
            return compute_h_manhattan(self.new_position)
        else:
            return 0
