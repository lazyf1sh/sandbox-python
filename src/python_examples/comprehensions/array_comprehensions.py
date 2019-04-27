import unittest


class MyTest2(unittest.TestCase):
    """

    """
    def test1(self):

        var = [item * 2 for item in [1, 2, 3]]

        self.assertEqual(var[0], 2)
        self.assertEqual(var[1], 4)
        self.assertEqual(var[2], 6)
