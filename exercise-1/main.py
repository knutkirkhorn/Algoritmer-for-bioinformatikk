"""
Exercise 1 - Algorithms for bioinformatics
"""


from LCS import LCS

# TODO: use these ?
# s = "AGCTTAGC"
# r = "TCGGATG"
# TODO : print(LCS.find_with_backtrack_test(s, r))
# print("S: {}, R: {} =>".format(s, r))
# print(LCS.find(s, r, True))
# print(LCS.find(s, r))
# print("")

# lcs_matrices = LCS.compute_dp_matrix(s, r)

# LCS.print_tables(lcs_matrices, s, r)

# print(LCS.find_with_backtrack(s, r))
# print(LCS.find_with_backtrack(r, s))
# matrices = LCS.compute_dp_matrix("ABCDGH", "AEDFHR")
# LCS.print_tables(matrices[0], matrices[1], "ABCDGH", "AEDFHR")

# Task 1 - Compute the LCS DP matrix for LCS(ATTCGGTTA, TAGTGATG)
print("Task 1:")
s = "ATTCGGTTA"
r = "TAGTGATG"
matrices = LCS.compute_dp_matrix(s, r)  # Compute the matrices
LCS.print_tables(matrices, s, r)  # Print the matrix
print("Computed LCS with backtrack matrix: {}".format(LCS.find(s, r, True)))

# Task 2 - Find the LCS without using a backtrack matrix
print("\nTask 2:")
print("Computed LCS without backtrack matrix: {}".format(LCS.find(s, r, False)))

# Task 3 - Find all LCSs for LCS(AGCTTAGCTG, TCGGATG)
print("\nTask 3:")
s = "AGCTTAGCTG"
r = "TCGGATG"
print(LCS.find_with_backtrack_test(s, r))
