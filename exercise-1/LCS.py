"""
Script made for computing the Longest Common Subsequence of two strings.
Used with DNA strings in the course. And it is also used in the UNIX command `diff` and in `git`.
"""


class LCS:

    @staticmethod
    def __f(s, r):
        if s == r:
            return 1
        else:
            return 0

    @staticmethod
    def compute_dp_matrix(s, r):
        """
        Static method for returning the LCS matrices of two strings with DP(dynamic programming).
        :param s: the first string to compare.
        :param r: the second string to compare.
        :return: matrix for the LCS DP matrix and a backtrack matrix.
        """

        # Initialize the arrays
        a = []
        b = []
        for i in range(0, len(s) + 1):
            a.append([])
            b.append([])
            for j in range(0, len(r) + 1):
                a[i].append([])
                b[i].append([])

        a[0][0] = 0  # Set the start to 0
        b[0][0] = 0

        # Initialize the start of S
        for i in range(1, len(s) + 1):
            a[i][0] = 0
            b[i][0] = 0

        # Initialize the start of R
        for j in range(1, len(r) + 1):
            a[0][j] = 0
            b[0][j] = 0

        # Compute the rest of the elements in the array
        for i in range(1, len(s) + 1):
            for j in range(1, len(r) + 1):
                s_i = s[i - 1]
                r_j = r[j - 1]

                a[i][j] = max(a[i - 1][j], a[i][j - 1], a[i - 1][j - 1] + LCS.__f(s_i, r_j))

                # Insert values for the backtrack matrix
                if a[i][j] == a[i-1][j]:
                    b[i][j] = 0
                elif a[i][j] == a[i][j-1]:
                    b[i][j] = 1
                elif a[i][j] == a[i-1][j-1] + 1:
                    b[i][j] = 2

        return a, b

    @staticmethod
    def __print_lcs(b, s, i, j, result):
        if i == 0 or j == 0:
            return result

        if b[i][j] == 2:
            result = s[i - 1] + result
            return LCS.__print_lcs(b, s, i - 1, j - 1, result)
        elif b[i][j] == 0:
            return LCS.__print_lcs(b, s, i - 1, j, result)
        else:
            return LCS.__print_lcs(b, s, i, j - 1, result)

    @staticmethod
    def __print_lcs_without_backtrack(a, s, i, j, result):
        if i == 0 or j == 0:
            return result

        if a[i][j] == a[i-1][j]:
            return LCS.__print_lcs_without_backtrack(a, s, i - 1, j, result)
        elif a[i][j] == a[i][j-1]:
            return LCS.__print_lcs_without_backtrack(a, s, i, j - 1, result)
        elif a[i][j] == a[i-1][j-1] + 1:
            result = s[i - 1] + result
            return LCS.__print_lcs_without_backtrack(a, s, i - 1, j - 1, result)

    @staticmethod
    def find(s, r, with_backtrack=False):
        """
        Static method for returning a single solution to LCS(s, r)
        :param s: the first string to compare.
        :param r: the second string to compare.
        :param with_backtrack: if the computation is going to use a backtrack matrix. Default value is False.
        :return: A single solution of the LCS(s, r).
        """
        matrices = LCS.compute_dp_matrix(s, r)
        i = len(s)
        j = len(r)

        if with_backtrack:
            b = matrices[1]
            return LCS.__print_lcs(b, s, i, j, "")
        else:
            a = matrices[0]
            return LCS.__print_lcs_without_backtrack(a, s, i, j, "")

    @staticmethod
    def __print_all_lcss_without_backtrack(a, s, r, i, j, result, results):
        if i == 0 or j == 0:
            # TODO: temp?
            exists = False
            for i in range(0, len(results)):
                if results[i] == result:
                    exists = True
                    break
            if not exists:
                results.append(result)

            return results

        if a[i][j] == a[i - 1][j]:
            LCS.__print_all_lcss_without_backtrack(a, s, r, i - 1, j, result, results)
        if a[i][j] == a[i][j - 1]:
            LCS.__print_all_lcss_without_backtrack(a, s, r, i, j - 1, result, results)
        if a[i][j] == a[i - 1][j - 1] + 1 and LCS.__f(s[i - 1], r[j - 1]) == 1:
            result = s[i - 1] + result
            LCS.__print_all_lcss_without_backtrack(a, s, r, i - 1, j - 1, result, results)

    @staticmethod
    def find_all(s, r):
        """
        Static method for returning all solutions to the LCS(s, r).
        :param s: the first string to compare.
        :param r: the second string to compare.
        :return: an array of all solutions to LCS(s, r).
        """
        a = LCS.compute_dp_matrix(s, r)[0]
        i = len(s)
        j = len(r)
        array = []
        LCS.__print_all_lcss_without_backtrack(a, s, r, i, j, "", array)
        return array

    @staticmethod
    def print_tables(matrices, s, r, only_a=True):
        a = matrices[0]
        b = matrices[1]

        # Print dp matrix
        # Print R
        print("DP matrix:")
        r_formatted = "   є "
        for i in range(0, len(r)):
            if i > 0:
                r_formatted += " "
            r_formatted += " " + r[i]

        print(r_formatted)

        # Print S and rest of table
        for i in range(0, len(a)):
            if i == 0:
                print("є {}".format(a[i]))
            else:
                print('{} {}'.format(s[i - 1], a[i]))

        if not only_a:
            print("\nBacktrack matrix:")
            # Print backtrack matrix
            # Print R
            r_formatted = "   є "
            for i in range(0, len(r)):
                if i > 0:
                    r_formatted += " "
                r_formatted += " " + r[i]

            print(r_formatted)

            # Print S and rest of table
            for i in range(0, len(b)):
                if i == 0:
                    print("є {}".format(b[i]))
                else:
                    print('{} {}'.format(s[i - 1], b[i]))
