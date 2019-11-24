# -*- coding: utf-8 -*-


class Solver:

    def move(self, strings, scramble):

        for m in strings:
            if m == "U":
                scramble.move_u()
            elif m == "R":
                scramble.move_r()
            elif m == "F":
                scramble.move_f()
            elif m == "B":
                scramble.move_b()
            elif m == "L":
                scramble.move_l()
            elif m == "D":
                scramble.move_d()
            elif m == "U'":
                scramble.move_u_rev()
            elif m == "R'":
                scramble.move_r_rev()
            elif m == "F'":
                scramble.move_f_rev()
            elif m == "B'":
                scramble.move_b_rev()
            elif m == "L'":
                scramble.move_l_rev()
            elif m == "D'":
                scramble.move_d_rev()
            elif m == "U2":
                scramble.move_u2()
            elif m == "R2":
                scramble.move_r2()
            elif m == "F2":
                scramble.move_f2()
            elif m == "B2":
                scramble.move_b2()
            elif m == "L2":
                scramble.move_l2()
            elif m == "D2":
                scramble.move_d2()

