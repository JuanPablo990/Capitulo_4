import Amplitudes as am
import unittest
class Test_Amplitudes(unittest.TestCase):

    def test_(self):
        v1 = [[[-3,-1]],[[0,-2]],[[0,1]],[[2,0]]]
        self.assertEqual(am.probabilidad(v1,2), 0.05263157894736841)

if __name__ == "__main__":
    unittest.main()