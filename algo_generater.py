# -*- coding: utf-8 -*-


class AlgoGenerater:

    LENGTH = 4
    TURN = ("U", "R", "F", "B", "L", "D", 
            "U'", "R'", "F'", "B'", "L'", "D'",
            "U2", "R2", "F2", "B2", "L2", "D2")
    IGNORE = {"U": ["U", "D", "D'", "D2"],
              "R": ["R", "L", "L'", "L2"],
              "F": ["F", "B", "B'", "B2"],
              "B": ["B", "F", "F'", "F2"],
              "L": ["L", "R", "R'", "R2"],
              "D": ["D", "U", "U'", "U2"],
	      "U'": ["U'", "D", "D'", "D2"],
	      "R'": ["R'", "L", "L'", "L2"],
	      "F'": ["F'", "B", "B'", "B2"],
	      "B'": ["B'", "F", "F'", "F2"],
	      "L'": ["L'", "R", "R'", "R2"],
	      "D'": ["D'", "U", "U'", "U2"],
	      "U2": ["U2", "D", "D'", "D2"],
	      "R2": ["R2", "L", "L'", "L2"],
	      "F2": ["F2", "B", "B'", "B2"],
	      "B2": ["B2", "F", "F'", "F2"],
	      "L2": ["L2", "R", "R'", "R2"],
	      "D2": ["D2", "U", "U'", "U2"]}

    algo = []

    def generate(self):

        import itertools

        pures = list(itertools.product(AlgoGenerater.TURN, repeat=AlgoGenerater.LENGTH))
        for pure in pures:
            pre_turn = ""
            is_validate = True
            for turn in pure:
                if pre_turn is not "" and turn in AlgoGenerater.IGNORE[pre_turn]:
                    is_validate = False
                pre_turn = turn    
                    
            if is_validate:
                self.algo.append(pure)

if __name__ == "__main__":

    from pprint import pprint

    a = AlgoGenerater()
    a.generate()
   
