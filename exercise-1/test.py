from unittest import TestCase

from LCS import LCS


class TestLCS(TestCase):
    s = "ATTCGGTTA"
    r = "TAGTGATG"

    def test_testing(self):
        length = LCS.find_all_lcs("SSSS", "SS")

        self.assertEqual(length, 2)

    def test_compute_dp(self):
        length = LCS.find_dp(self.s, self.r)

        self.assertEqual(length, 3) # TODO:

    def test_without_backtrack(self):
        length = LCS.find_without_backtrack(self.s, self.r)

        self.assertEqual(length, 3) # TODO:

    def test_find_all_sqsssTODO(self):
        all_TODO_name = LCS.find_all_lcs(self.s, self.r)

        self.assertEqual(all_TODO_name, "todo_insert_array")
