import time

from astar import astar
from utilities import faces, moves, end


def demo_complete_shake(shake, start):
    # execute complete shake
    for i in range(len(shake)):
        start = shake[i](start)

    print("This is start")
    demo_print_cube(start)
    print("")
    print("")

    t = time.time()
    test = astar(start, end, moves)
    elapsed = time.time() - t

    for elem in test:
        demo_print_cube(elem)
        print(elem['Move'], end="")
        print("")
    print("Time elapsed -> ", elapsed)
    print("")
    print("")


def demo_step_by_step(shake, start):
    # execute shake step by step
    for i in range(len(shake)):  #
        print("Iteration number:", i + 1)
        start = shake[i](start)
        print("This is start")
        demo_print_cube(start)
        print("")
        print("")

        t = time.time()
        test = astar(start, end, moves)
        elapsed = time.time() - t

        for elem in test:
            demo_print_cube(elem)
            print(elem['Move'], end="")
            print("")
        print("Time elapsed -> ", elapsed)
        print("")
        print("")


def demo_test_printer(shakes, start):
    iteration = 0
    for shake in shakes:
        iteration = iteration + 1
        print("########################")
        print("Iteration number -> ", iteration)

        print("Shaking")
        for i in range(len(shake)):
            start = shake[i](start)

        print("Solving")
        test = astar(start, end, moves)

        for face in faces:
            start[face] = end[face].copy()


def demo_print_cube(start):
    for face in faces:
        print(face, ': [ ', end="")
        for j in range(4):
            print(start[face][j], ' ', end="")
        print("]", end="")
    print(end="")


def demo_test_single_moves(start):
    for move in moves:
        print('Move:', move.__name__)
        for face in faces:
            start[face] = end[face].copy()
        demo_print_cube(start)
        move(start)
        demo_print_cube(start)
        tmp = astar(start, end, moves)
        for i in range(len(tmp)):
            print(tmp[i])
        print("\n\n")
