from node import Node, compute_conf
from utilities import moves, opposite_moves


def create_nodes(start, end):
    dummy_node = Node(None, start)
    # Create start and end node
    start_node = Node(dummy_node, start)
    start_node_inverse = Node(dummy_node, end)
    end_node = Node(None, end)
    end_node_inverse = Node(None, start)
    return start_node, start_node_inverse, end_node, end_node_inverse


def choose_node(current_node, open_list, closed_list):
    current_index = 0
    for index, item in enumerate(open_list):
        if item.f < current_node.f:
            current_node = item
            current_index = index

    # Pop current off open list, add to closed list
    open_list.pop(current_index)
    closed_list.append(current_node)
    return current_node


def find_dict_match(open_list, closed_list, last_list, open_list_inverse, closed_list_inverse, last_list_inverse,
                    branches):
    flag = False
    middle_node = Node()
    middle_node_inverse = Node()
    middle_node.g = 8
    middle_node_inverse.g = 8
    if branches <= 1:
        for i in open_list + closed_list:
            for j in open_list_inverse + closed_list_inverse:
                if i.new_position == j.new_position:
                    flag = True
                    if i.g + j.g < middle_node.g + middle_node_inverse.g:
                        middle_node = i
                        middle_node_inverse = j
    else:
        for i in last_list:
            for j in open_list_inverse:
                if i.new_position == j.new_position:
                    flag = True
                    if i.g + j.g < middle_node.g + middle_node_inverse.g:
                        middle_node = i
                        middle_node_inverse = j

        for j in last_list_inverse:
            for i in open_list:
                if i.new_position == j.new_position:
                    flag = True
                    if i.g + j.g < middle_node.g + middle_node_inverse.g:
                        middle_node = i
                        middle_node_inverse = j

    return flag, middle_node, middle_node_inverse


def find_path_astar(middle_node, middle_node_inverse):
    path_astar = []
    path_direct = []

    path_nodes_direct = []
    path_nodes_inverse = []
    path_nodes = []

    current = middle_node
    while current.parent is not None:
        path_nodes_direct.append(current)
        path_direct.append(current.new_position)
        path_direct[-1]['Move'] = current.move.__name__
        current = current.parent

    path_inverse = []
    current = middle_node_inverse.parent
    while current.parent is not None:
        path_nodes_inverse.append(current)
        path_inverse.append(current.new_position)
        path_inverse[-1]['Move'] = current.move.__name__
        current = current.parent

    path_astar.extend(path_direct[::-1])
    path_astar.extend(path_inverse)

    path_nodes.extend(path_nodes_direct[::-1])
    path_nodes.extend(path_nodes_inverse)


    return path_astar


def compare_paths(path_astar, path_direct, path_inverse):
    list_of_path = [path_astar, path_direct, path_inverse]
    list_of_len = [len(path_astar), len(path_direct), len(path_inverse)]
    value = min(i for i in list_of_len if i > 0)
    smaller_path = list_of_path[list_of_len.index(value)]
    return smaller_path


def generate_children(current_node, children, is_start):
    for move in moves:
        generate = True
        # Create new node
        if not is_start:
            for avoid_move in opposite_moves[moves.index(current_node.move)]:
                if move == avoid_move:
                    generate = False

        if generate:
            parent_new_node = current_node
            new_position_new_node = compute_conf(parent_new_node.new_position, move)
            new_node = Node(parent_new_node, new_position_new_node, move)

            # Append
            children.append(new_node)

    is_start = False
    return is_start, children


def append_children(children, open_list, closed_list, current_node, flag_direction, child_number):
    '''
    flag_direction: if 1 is used an heuristic, otherwise is used Breadth-First Search,
                    note that flag_direction could be different in the two directions.
    '''
    last_list = []
    for child in children:

        is_new_child = True

        # Create the f, g, and h values
        child.g = current_node.g + 1
        if flag_direction:
            child.h = 0
        else:
            child.h = child.compute_h()
        child.f = child.g + child.h

        # Child is on the closed list
        for closed_child in closed_list:
            if child.new_position == closed_child.new_position:
                if child.g >= closed_child.g:
                    del child
                    is_new_child = False
                else:
                    del closed_child
                break

        if is_new_child:
            # Child is already in the open list
            for open_node in open_list:
                if child.new_position == open_node.new_position:
                    if child.g >= open_node.g:
                        del child
                        is_new_child = False
                    else:
                        del open_node
                break

        if is_new_child:
            child_number = child_number + 1
            # Add the child to the open list
            open_list.append(child)
            last_list.append(child)

    return open_list, last_list, child_number


def astar_loop(start, end, moves):
    start_node, start_node_inverse, end_node, end_node_inverse = create_nodes(start, end)

    open_list = []
    closed_list = []
    last_list = []

    open_list_inverse = []
    closed_list_inverse = []
    last_list_inverse = []

    # Add the start node
    open_list.append(start_node)
    open_list_inverse.append(start_node_inverse)

    # Paths
    path_astar = []
    path_direct = []
    path_inverse = []

    is_start = True
    is_start_inverse = True

    child_number = 0
    child_number_inverse = 0
    branches = 0
    # Loop until you find the end
    while len(open_list) > 0 or len(open_list_inverse) > 0:
        current_node = open_list[0]
        current_node_inverse = open_list_inverse[0]

        current_node = choose_node(current_node, open_list, closed_list)
        current_node_inverse = choose_node(current_node_inverse, open_list_inverse, closed_list_inverse)

        flag, middle_node, middle_node_inverse = find_dict_match(open_list, closed_list, last_list,
                                                                 open_list_inverse, closed_list_inverse,
                                                                 last_list_inverse,
                                                                 branches)

        if flag:
            path_astar = find_path_astar(middle_node, middle_node_inverse)
            return path_astar

        # Generate children
        children = []
        children_inverse = []
        is_start, children = generate_children(current_node, children, is_start)
        is_start_inverse, children_inverse = generate_children(current_node_inverse, children_inverse, is_start_inverse)

        branches = branches + 1

        # Loop through children
        open_list, last_list, child_number = append_children(children, open_list, closed_list, current_node, 0,
                                                             child_number)

        # Loop through children_inverse
        open_list_inverse, last_list_inverse, child_number_inverse = append_children(children_inverse,
                                                                                     open_list_inverse,
                                                                                     closed_list_inverse,
                                                                                     current_node_inverse, 1,
                                                                                     child_number_inverse)


def astar(start, end, moves):
    return astar_loop(start, end, moves)
