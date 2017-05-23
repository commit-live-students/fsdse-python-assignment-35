from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        self.assertEqual(True, solution([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
        self.assertEqual(False, solution([1, 2, 3, 4, 5], [6, 7, 8, 9]))
