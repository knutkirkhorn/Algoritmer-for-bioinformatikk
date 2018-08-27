"""
Script made for computing the Longest Common Subsequence of two strings. Mainly used with DNA strings.
"""


class LCS:

    @staticmethod
    def __f(s, r):
        if s == r:
            return 1
        else:
            return 0

    # TODO: rename => ? find_with_dp ?
    @staticmethod
    def compute_dp_matrix(s, r):
        """
        Static method for returning the LCS of two strings with DP(dynamic programming???)
        :param s: the first string to compare.
        :param r: the second string to compare.
        :return: how long the LCS is of the two strings.
        """

        # Initialize the array
        a = []
        b = []
        for i in range(0, len(s) + 1):
            a.append([])
            b.append([])
            for j in range(0, len(r) + 1):
                a[i].append([])
                b[i].append([])

        a[0][0] = 0  # Set the start to 0

        # Initialize the start of S
        for i in range(1, len(s) + 1):  # TODO: + 1?
            a[i][0] = 0

        # Initialize the start of R
        for j in range(1, len(r) + 1):
            a[0][j] = 0

        # Compute the rest of the elements in the array
        for i in range(1, len(s) + 1):
            for j in range(1, len(r) + 1):
                s_i = s[i-1]
                r_j = r[j-1]

                a[i][j] = max(a[i-1][j], a[i][j-1], a[i-1][j-1] + LCS.__f(s_i, r_j))

                if a[i][j] == a[i-1][j]:
                    b[i][j] = 0
                elif a[i][j] == a[i][j-1]:
                    b[i][j] = 1
                elif a[i][j] == a[i-1][j-1] + 1:
                    b[i][j] = 2

        return a, b

    @staticmethod
    def print_lcs(b, s, i, j, result):
        if i == 0 or j == 0:
            return result

        if b[i][j] == 2:
            result = s[i] + result
            return LCS.print_lcs(b, s, i - 1, j - 1, result)
        elif b[i][j] == 0:
            return LCS.print_lcs(b, s, i-1, j, result)
        else:
            return LCS.print_lcs(b, s, i, j-1, result)

    @staticmethod
    def find_with_backtrack(s, r):
        b = LCS.compute_dp_matrix(s, r)
        i = len(b)
        j = len(b[0])
        return LCS.print_lcs(b, s, i, j, "")

    @staticmethod
    def find_without_backtrack(s, r):
        # TODO: is this using a recursive LCS?
        return s, r

    @staticmethod
    def find_all_lcs(s, r):
        return s, r
