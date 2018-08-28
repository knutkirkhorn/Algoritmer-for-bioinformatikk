"""
Exercise 1 - Algorithms for bioinformatics
"""


from LCS import LCS

# TODO: use these ?
# s = "AGCTTAGC"
# r = "TCGGATG"

# lcs_matrices = LCS.compute_dp_matrix(s, r)

# LCS.print_tables(lcs_matrices, s, r)

# print(LCS.find_with_backtrack(s, r))
# print(LCS.find_with_backtrack(r, s))
# matrices = LCS.compute_dp_matrix("ABCDGH", "AEDFHR")
# LCS.print_tables(matrices[0], matrices[1], "ABCDGH", "AEDFHR")

# TODO:
# Task 1 - Compute the LCS DP matrix for LCS(ATTCGGTTA, TAGTGATG)
s = "ATTCGGTTA"
r = "TAGTGATG"
matrices = LCS.compute_dp_matrix(s, r)  # Compute the matrices
LCS.print_tables(matrices, s, r)  # Print the matrix

# Task 2 - Find the LCS without using a backtrack matrix

# Task 3 - Find all LCSs for a S and R
