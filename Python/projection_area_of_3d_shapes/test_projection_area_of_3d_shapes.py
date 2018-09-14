import unittest
import projection_area_of_3d_shapes

"""
We write a couple of unittest here to learn unittesting.
"""


class ProjectionAread3dShapesTest(unittest.TestCase):
    def test_with_zero_elements(self):
        self.assertEqual(Solution().projectionArea([[1, 0], [0, 2]]), 8)


if __name__ == '__main__':
    unittest.main()
