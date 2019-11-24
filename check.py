# -*- coding: utf-8 -*-

import pprint
from solver import Solver
from scramble import Scramble
from algo_generater import AlgoGenerater

class Check:

    def check(self):

        a = AlgoGenerater()
        a.generate()

        comp_scramble_file = open("2x2x2scramble.txt")
        comp_scramble_list = comp_scramble_file.readlines()

        s = Solver()

        for comp_scramble in comp_scramble_list:
            sc = Scramble()
            comp_scrambles = comp_scramble.rstrip('\n').split(" ")
            s.move(comp_scrambles, sc)

            for algo_list in a.algo:
                s.move(algo_list, sc)

                if sc.is_solved():
                    pprint.pprint(algo_list)
                    break

                sc.clear()
                s.move(comp_scrambles, sc)

            if sc.is_solved():
                pprint.pprint(comp_scramble.rstrip('\n'))
            else:
                pprint.pprint("Fail")
   

if __name__ == "__main__":

   c = Check()
   c.check()
