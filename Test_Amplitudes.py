import Amplitudes as am
import unittest
class Test_Amplitudes(unittest.TestCase):

    def test_probabilidad(self):
        v1 = [[[-3,-1]],[[0,-2]],[[0,1]],[[2,0]]]
        self.assertEqual(am.probabilidad(v1,2), 0.05263157894736841)

    def test_probabilidad_transicion(self):
        v1 = [[[-2, -1]], [[0, -2]], [[0, 1]], [[2, 0]]]
        v2 = [[[-8, -1]], [[0, -2]], [[0, 1]], [[2, 0]]]
        self.assertEqual(am.probabilidad_transicion(v1,v2), [[[0.8077806958015602, -0.18641092980036003]]])
if __name__ == "__main__":
    unittest.main()