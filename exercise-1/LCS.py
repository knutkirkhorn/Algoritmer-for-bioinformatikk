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

                # Insert values for the backtrack matrix
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
            result = result + s[i]
            return LCS.print_lcs(b, s, i - 1, j - 1, result)
        elif b[i][j] == 0:
            return LCS.print_lcs(b, s, i-1, j, result)
        else:
            return LCS.print_lcs(b, s, i, j-1, result)

    @staticmethod
    def find_with_backtrack(s, r):
        b = LCS.compute_dp_matrix(s, r)[1]
        i = len(s)
        j = len(r)
        return LCS.print_lcs(b, s, i, j, "")

    @staticmethod
    def find_without_backtrack(s, r):
        # TODO: is this using a recursive LCS?
        return s, r

    @staticmethod
    def find_all_lcs(s, r):
        return s, r

    @staticmethod
    def print_tables(a, b, s, r, only_a=True):
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

        if only_a is False:
            print("")
            print("Backtrace matrix:")
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
                    print("є [ _, _, _, _, _, _, _, _]")
                else:
                    print('{} {}'.format(s[i - 1], b[i]))
