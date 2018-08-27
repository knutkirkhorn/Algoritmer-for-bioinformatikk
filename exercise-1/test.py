from unittest import TestCase

from LCS import LCS


class TestLCS(TestCase):
    s = "AGCTTAGC"
    r = "TCGGATG"
    expected_solution = "CTG"

    def test_testing(self):
        length = LCS.find_with_backtrack("SSSS", "SS")

        expected_solution = "SS"

        self.assertEqual(length, expected_solution)

    def test_compute_dp_matrix(self):
        matrices = LCS.compute_dp_matrix(self.s, self.r)
        a = matrices[0]
        b = matrices[1]

        expected_matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 2],
                           [0, 0, 1, 1, 1, 1, 1, 2], [0, 1, 1, 1, 1, 1, 2, 2], [0, 1, 1, 1, 1, 1, 2, 2],
                           [0, 1, 1, 1, 1, 2, 2, 2], [0, 1, 1, 2, 2, 2, 2, 3], [0, 1, 2, 2, 2, 2, 2, 3]]
        expected_backtrack_matrix = [[[], [], [], [], [], [], [], []], [[], 0, 0, 0, 0, 2, 1, 1],
                                     [[], 0, 0, 2, 1, 0, 0, 2], [[], 0, 2, 0, 0, 0, 0, 0], [[], 2, 0, 0, 0, 0, 2, 0],
                                     [[], 0, 0, 0, 0, 0, 0, 0], [[], 0, 0, 0, 0, 2, 0, 0], [[], 0, 0, 2, 1, 0, 0, 2],
                                     [[], 0, 2, 0, 0, 0, 0, 0]]

        self.assertEqual(a, expected_matrix)
        # TODO: check if this is correct
        self.assertEqual(b, expected_backtrack_matrix)

    def test_find_dp_backtrack_solution(self):
        solution = LCS.find_with_backtrack(self.s, self.r)

        self.assertEqual(solution, self.expected_solution)

    def test_without_backtrack(self):
        length = LCS.find_without_backtrack(self.s, self.r)

        #self.assertEqual(length, 3)  # TODO:

    def test_find_all_sqsssTODO(self):
        all_TODO_name = LCS.find_all_lcs(self.s, self.r)

        #self.assertEqual(all_TODO_name, "todo_insert_array")  # TODO
