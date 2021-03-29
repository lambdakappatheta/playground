#!/usr/bin/env python3


import unittest


class TestComprehension(unittest.TestCase):


    def test_comprehension_flat(self):

        # nested loop, flat list

        got = [(i, j) for i in range(4) for j in range(i)]

        want = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)] 

        self.assertEqual(got, want)

        # corresponds to

        lis = []
        for i in range(4):
            for j in range(i):
                lis.append((i, j))

        self.assertEqual(lis, want)


    def test_comprehension_nested(self):

        # nested loop, nested list

        got = [[(i, j) for j in range(i)] for i in range(4)]

        want = [[], [(1, 0)], [(2, 0), (2, 1)], [(3, 0), (3, 1), (3, 2)]]

        self.assertEqual(got, want)

        # corresponds to

        outer = []
        for i in range(4):
            inner = []
            for j in range(i):
                inner.append((i, j))
            outer.append(inner)

        self.assertEqual(outer, want)


if __name__ == "__main__":
    unittest.main()

