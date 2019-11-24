# -*- coding: utf-8 -*-

class Scramble:

    # ULB -> URB -> URF -> ULFの順
    U_FACE = ["w", "w", "w", "w"]
    F_FACE = ["g", "g", "g", "g"]
    R_FACE = ["r", "r", "r", "r"]
    B_FACE = ["b", "b", "b", "b"]
    L_FACE = ["o", "o", "o", "o"]
    D_FACE = ["y", "y", "y", "y"]

    # キューブを定義する
    u_face = U_FACE
    f_face = F_FACE
    r_face = R_FACE
    b_face = B_FACE
    l_face = L_FACE 
    d_face = D_FACE

    def __init__(self):

        self.u_face = Scramble.U_FACE
        self.f_face = Scramble.F_FACE 
        self.r_face = Scramble.R_FACE
        self.b_face = Scramble.B_FACE
        self.l_face = Scramble.L_FACE
        self.d_face = Scramble.D_FACE

    def is_solved(self):

        return self.u_face == Scramble.U_FACE \
               and self.f_face == Scramble.F_FACE \
               and self.r_face == Scramble.R_FACE \
               and self.b_face == Scramble.B_FACE \
               and self.l_face == Scramble.L_FACE \
               and self.d_face == Scramble.D_FACE

    def move_u(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_b_face = self.b_face[:]
        tmp_l_face = self.l_face[:]

        tmp_u_face[0] = self.u_face[3]
        tmp_u_face[1] = self.u_face[0]
        tmp_u_face[2] = self.u_face[1]
        tmp_u_face[3] = self.u_face[2]

        tmp_f_face[0] = self.r_face[0]
        tmp_f_face[1] = self.r_face[1]

        tmp_r_face[0] = self.b_face[0]
        tmp_r_face[1] = self.b_face[1]

        tmp_b_face[0] = self.l_face[0]
        tmp_b_face[1] = self.l_face[1]

        tmp_l_face[0] = self.f_face[0]
        tmp_l_face[1] = self.f_face[1]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.b_face = tmp_b_face
        self.l_face = tmp_l_face

    def move_r(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_b_face = self.b_face[:]
        tmp_d_face = self.d_face[:]

        tmp_u_face[1] = self.f_face[1]
        tmp_u_face[2] = self.f_face[2]

        tmp_f_face[1] = self.d_face[1]
        tmp_f_face[2] = self.d_face[2]

        tmp_r_face[0] = self.r_face[3]
        tmp_r_face[1] = self.r_face[0]
        tmp_r_face[2] = self.r_face[1]
        tmp_r_face[3] = self.r_face[2]

        tmp_b_face[0] = self.u_face[2]
        tmp_b_face[3] = self.u_face[1]

        tmp_d_face[1] = self.b_face[3]
        tmp_d_face[2] = self.b_face[0]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.b_face = tmp_b_face
        self.d_face = tmp_d_face

    def move_f(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_l_face = self.l_face[:]
        tmp_d_face = self.d_face[:]

        tmp_u_face[2] = self.l_face[1]
        tmp_u_face[3] = self.l_face[2]

        tmp_f_face[0] = self.f_face[3]
        tmp_f_face[1] = self.f_face[0]
        tmp_f_face[2] = self.f_face[1]
        tmp_f_face[3] = self.f_face[2]

        tmp_r_face[0] = self.u_face[3]
        tmp_r_face[3] = self.u_face[2]

        tmp_l_face[1] = self.d_face[0]
        tmp_l_face[2] = self.d_face[1]

        tmp_d_face[0] = self.r_face[3]
        tmp_d_face[1] = self.r_face[0]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.l_face = tmp_l_face
        self.d_face = tmp_d_face

    def move_b(self):

        tmp_u_face = self.u_face[:]
        tmp_r_face = self.r_face[:]
        tmp_b_face = self.b_face[:]
        tmp_l_face = self.l_face[:]
        tmp_d_face = self.d_face[:]

        tmp_u_face[0] = self.r_face[1]
        tmp_u_face[1] = self.r_face[2]

        tmp_r_face[1] = self.d_face[2]
        tmp_r_face[2] = self.d_face[3]

        tmp_b_face[0] = self.b_face[3]
        tmp_b_face[1] = self.b_face[0]
        tmp_b_face[2] = self.b_face[1]
        tmp_b_face[3] = self.b_face[2]

        tmp_l_face[0] = self.u_face[1]
        tmp_l_face[3] = self.u_face[0]

        tmp_d_face[2] = self.l_face[3]
        tmp_d_face[3] = self.l_face[0]

        self.u_face = tmp_u_face
        self.r_face = tmp_r_face
        self.b_face = tmp_b_face
        self.l_face = tmp_l_face
        self.d_face = tmp_d_face

    def move_l(self):

        tmp_u_face = self.u_face[:]
        tmp_f_face = self.f_face[:]
        tmp_b_face = self.b_face[:]
        tmp_l_face = self.l_face[:]
        tmp_d_face = self.d_face[:]

        tmp_u_face[0] = self.b_face[2]
        tmp_u_face[3] = self.b_face[1]

        tmp_f_face[0] = self.u_face[0]
        tmp_f_face[3] = self.u_face[3]

        tmp_b_face[1] = self.d_face[3]
        tmp_b_face[2] = self.d_face[0]

        tmp_l_face[0] = self.l_face[3]
        tmp_l_face[1] = self.l_face[0]
        tmp_l_face[2] = self.l_face[1]
        tmp_l_face[3] = self.l_face[2]

        tmp_d_face[0] = self.f_face[0]
        tmp_d_face[3] = self.f_face[3]

        self.u_face = tmp_u_face
        self.f_face = tmp_f_face
        self.b_face = tmp_b_face
        self.l_face = tmp_l_face
        self.d_face = tmp_d_face

    def move_d(self):

        tmp_f_face = self.f_face[:]
        tmp_r_face = self.r_face[:]
        tmp_b_face = self.b_face[:]
        tmp_l_face = self.l_face[:]
        tmp_d_face = self.d_face[:]

        tmp_f_face[2] = self.l_face[2]
        tmp_f_face[3] = self.l_face[3]

        tmp_r_face[2] = self.f_face[2]
        tmp_r_face[3] = self.f_face[3]

        tmp_b_face[2] = self.r_face[2]
        tmp_b_face[3] = self.r_face[3]

        tmp_l_face[2] = self.b_face[2]
        tmp_l_face[3] = self.b_face[3]

        tmp_d_face[0] = self.d_face[3]
        tmp_d_face[1] = self.d_face[0]
        tmp_d_face[2] = self.d_face[1]
        tmp_d_face[3] = self.d_face[2]

        self.f_face = tmp_f_face
        self.r_face = tmp_r_face
        self.b_face = tmp_b_face
        self.l_face = tmp_l_face
        self.d_face = tmp_d_face

    def move_u_rev(self):
        self.move_u()
        self.move_u()
        self.move_u()

    def move_r_rev(self):
        self.move_r()
        self.move_r()
        self.move_r()

    def move_f_rev(self):
        self.move_f()
        self.move_f()
        self.move_f()

    def move_b_rev(self):
        self.move_b()
        self.move_b()
        self.move_b()

    def move_l_rev(self):
        self.move_l()
        self.move_l()
        self.move_l()

    def move_d_rev(self):
        self.move_d()
        self.move_d()
        self.move_d()

    def move_u2(self):
        self.move_u()
        self.move_u()

    def move_r2(self):
        self.move_r()
        self.move_r()

    def move_f2(self):
        self.move_f()
        self.move_f()

    def move_b2(self):
        self.move_b()
        self.move_b()

    def move_l2(self):
        self.move_l()
        self.move_l()

    def move_d2(self):
        self.move_d()
        self.move_d()


if __name__ == "__main__":

    from pprint import pprint

    s = Scramble()
    s.move_u()
    s.move_f()
    s.move_r_rev()
    s.move_b()
    s.move_l()
    s.move_d_rev()

    pprint(s.u_face)
    pprint(s.f_face)
    pprint(s.r_face)
    pprint(s.b_face)
    pprint(s.l_face)
    pprint(s.d_face)
