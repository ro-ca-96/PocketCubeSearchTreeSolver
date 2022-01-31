import utilities as ut


def move_execution(child_in, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out):
    child_out = {}
    for face in ut.faces:
        child_out[face] = child_in[face].copy()

    for i in range(len(list_of_faces_in)):
        child_in[list_of_faces_in[i]][list_of_colors_in[i]] = child_out[list_of_faces_out[i]][list_of_colors_out[i]]

    return child_in


def dummy_move(child):
    return child


def f(child):
    list_of_faces_in = ["U", "U", "R", "R", "D", "D", "L", "L", "F", "F", "F", "F"]
    list_of_colors_in = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3]
    list_of_faces_out = ["L", "L", "U", "U", "R", "R", "D", "D", "F", "F", "F", "F"]
    list_of_colors_out = [0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 3, 1]

    child = move_execution(child, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out)
    return child


def f2(child):
    child = f(child)
    child = f(child)
    return child


def fp(child):
    list_of_faces_out = ["U", "U", "R", "R", "D", "D", "L", "L", "F", "F", "F", "F"]
    list_of_faces_in = ["L", "L", "U", "U", "R", "R", "D", "D", "F", "F", "F", "F"]
    list_of_colors_in = [0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 3, 1]
    list_of_colors_out = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3]

    child = move_execution(child, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out)
    return child


def u(child):
    list_of_faces_in = ["L", "L", "F", "F", "R", "R", "B", "B", "U", "U", "U", "U"]
    list_of_colors_in = [0, 2, 0, 1, 1, 3, 0, 1, 0, 1, 2, 3]
    list_of_faces_out = ["F", "F", "R", "R", "B", "B", "L", "L", "U", "U", "U", "U"]
    list_of_colors_out = [1, 0, 1, 3, 0, 1, 2, 0, 2, 0, 3, 1]

    child = move_execution(child, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out)
    return child


def u2(child):
    child = u(child)
    child = u(child)
    return child


def up(child):
    list_of_faces_out = ["L", "L", "F", "F", "R", "R", "B", "B", "U", "U", "U", "U"]
    list_of_colors_out = [0, 2, 0, 1, 1, 3, 0, 1, 0, 1, 2, 3]
    list_of_faces_in = ["F", "F", "R", "R", "B", "B", "L", "L", "U", "U", "U", "U"]
    list_of_colors_in = [1, 0, 1, 3, 0, 1, 2, 0, 2, 0, 3, 1]

    child = move_execution(child, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out)
    return child


def r(child):
    list_of_faces_in = ["F", "F", "U", "U", "B", "B", "D", "D", "R", "R", "R", "R"]
    list_of_faces_out = ["D", "D", "F", "F", "U", "U", "B", "B", "R", "R", "R", "R"]
    list_of_colors_in = [1, 3, 0, 2, 0, 2, 1, 3, 0, 1, 2, 3]
    list_of_colors_out = [1, 3, 3, 1, 0, 2, 2, 0, 2, 0, 3, 1]

    child = move_execution(child, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out)
    return child


def r2(child):
    child = r(child)
    child = r(child)
    return child


def rp(child):
    list_of_faces_in = ["D", "D", "F", "F", "U", "U", "B", "B", "R", "R", "R", "R"]
    list_of_faces_out = ["F", "F", "U", "U", "B", "B", "D", "D", "R", "R", "R", "R"]
    list_of_colors_in = [1, 3, 3, 1, 0, 2, 2, 0, 2, 0, 3, 1]
    list_of_colors_out = [1, 3, 0, 2, 0, 2, 1, 3, 0, 1, 2, 3]

    child = move_execution(child, list_of_faces_in, list_of_colors_in, list_of_faces_out, list_of_colors_out)
    return child
