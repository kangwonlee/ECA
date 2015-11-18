import unittest

import eigenanalysis as ea
import linear_algebra as la


class TestEigenAnalysis(unittest.TestCase):
    def test_power_method(self):
        A = [[-2.0, -1.0],
             [-1.0, -3.0]]

        lamda1, x1 = ea.power_method(A)
        Ax1 = la.multiply_matrix_vector(A, x1)

        self.assertEqual(len(Ax1), len(A))

        for x1i, Ax1i in zip(x1, Ax1):
            self.assertAlmostEqual(Ax1i, lamda1 * x1i)


if "__main__" == __name__:
    unittest.main()