"""
Exercise 1 - Algorithms for bioinformatics
"""


from LCS import LCS


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

# Task 3 - Find all solutions for LCS(AGCTTAGCTG, TCGGATG)
print("\nTask 3:")
s = "AGCTTAGCTG"
r = "TCGGATG"
print("All solutions to LCS(AGCTTAGCTG, TCGGATG):\n{}".format(LCS.find_all(s, r)))
