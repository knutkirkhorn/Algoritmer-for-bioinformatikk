from unittest import TestCase

from LCS import LCS


class TestLCS(TestCase):
    s = "AGCTTAGC"
    r = "TCGGATG"
    expected_solution = "ATG"  # TODO: replace with all solutions, e.g. CTG, TAG...? aswell

    def test_some_lcss(self):
        # S = "SSSS" and R = "SS" => LCS = "SS"
        lcs_1 = LCS.find("SSSS", "SS", True)
        expected_solution_1 = "SS"
        self.assertEqual(lcs_1, expected_solution_1)

        # S = "ABCDGH" and R = "AEDFHR" => LCS = "ADH"
        lcs_2 = LCS.find("ABCDGH", "AEDFHR", True)
        expected_solution_2 = "ADH"
        self.assertEqual(lcs_2, expected_solution_2)

        # S = "AGGTAB" and R = "GXTXAYB" => LCS = "GTAB"
        lcs_3 = LCS.find("AGGTAB", "GXTXAYB", True)
        expected_solution_3 = "GTAB"
        self.assertEqual(lcs_3, expected_solution_3)

    def test_empty_strings(self):
        s = ""
        r = ""

        solution = LCS.find(s, r, True)
        expected_solution = ""

        self.assertEqual(solution, expected_solution)

    def test_switching_s_and_r(self):
        lcs = LCS.find(self.s, self.r, True)
        lcs_switched = LCS.find(self.r, self.s, True)

        # TODO: test with all elements when done?
        self.assertEqual(len(lcs), len(lcs_switched))

    def test_same_with_and_without_backtrack(self):
        lcs_with = LCS.find(self.s, self.r, True)
        lcs_without = LCS.find(self.s, self.r, False)

        self.assertEqual(lcs_with, lcs_without)

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
        solution = LCS.find(self.s, self.r, True)

        self.assertEqual(solution, self.expected_solution)

    def test_without_backtrack(self):
        length = LCS.find(self.s, self.r)

        # self.assertEqual(length, 3)  # TODO:

    def test_find_all_sqsssTODO(self):
        all_TODO_name = LCS.find_with_backtrack_test(self.s, self.r)

        # self.assertEqual(all_TODO_name, "todo_insert_array")  # TODO
