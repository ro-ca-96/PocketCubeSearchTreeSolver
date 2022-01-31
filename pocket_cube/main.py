from demos import *
from moves import *
from utilities import end


if __name__ == '__main__':
    start = {}

    for face in faces:
        start[face] = end[face].copy()

    shakes = [
        [f, u, r, up, f, u, f, rp, f, rp, u, fp, up, r, r],
        [u, fp, rp, u,  rp, up, f, f, u, f, r, f, f, r, r, up, r],
        [u, u, fp, up, r, u, u, rp, u, u, r, r, f, f, r, up, r, r, f, f, u, u],
        [u, r, up, r, up, r, f, f, rp, f, f, r, f, r, r, f, u],
        [u, u, rp, u, f, u, u, rp, f, f, u, u, r, r, u, u, f, f, up, f, f, up],
        [f, up, rp, fp, r, u, f, u, u, rp, u, u, fp, u, u, fp, up],
        [rp, up, fp, r, u, r, r, f, r, u, f, u, u, fp, r, up],
        [up, rp, f, f, rp, f, f, u, u, r, up, r, f, f, u, u, f, up, f],
        [r, f, rp, u, u, f, r, r, fp, up, f, u, u, fp, r, r, u, r, r],
        [u, u, fp, r, u, u, f, f, r, fp, rp, f, r, f, f, r, r, u, u, f, f]]

    # demo_step_by_step(shakes[0], start)
    for i in range(len(shakes)):
        demo_complete_shake(shakes[i], start)
