from moves import f, f2, fp, u, u2, up, r, r2, rp


colors = ['w', 'b', 'g', 'o', 'y', 'r']
# class and list to print colors in terminal
"""
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[38;2;255;165;0m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


colors = [Colors.END + 'w' + Colors.END,
          Colors.BLUE + 'b' + Colors.END,
          Colors.GREEN + 'g' + Colors.END,
          Colors.ORANGE + 'o' + Colors.END,
          Colors.YELLOW + 'y' + Colors.END,
          Colors.RED + 'r' + Colors.END]
"""

faces = ["L", "F", "R", "B", "U", "D"]


moves = [f, f2, fp, u, u2, up, r, r2, rp]
opposite_moves = [[f, fp, f2], [f, fp, f2], [f, fp, f2],
                  [u, up, u2], [u, up, u2], [u, up, u2],
                  [r, rp, r2], [r, rp, r2], [r, rp, r2]]


end = {"F": [colors[0], colors[0], colors[0], colors[0]],  # w
       "D": [colors[1], colors[1], colors[1], colors[1]],  # b
       "U": [colors[2], colors[2], colors[2], colors[2]],  # g
       "R": [colors[3], colors[3], colors[3], colors[3]],  # o
       "B": [colors[4], colors[4], colors[4], colors[4]],  # y
       "L": [colors[5], colors[5], colors[5], colors[5]]}  # r
