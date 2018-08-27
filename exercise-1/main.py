"""
Exercise 1 - Algorithms for bioinformatics
"""


from LCS import LCS

s = "AGCTTAGC"
r = "TCGGATG"

lcs_matrices = LCS.compute_dp_matrix(s, r)
a = lcs_matrices[0]
b = lcs_matrices[1]

LCS.print_tables(a, b, s, r)

# TODO:
# Task 1 - Compute the LCS DP matrix for LCS(ATTCGGTTA, TAGTGATG)
s = "ATTCGGTTA"
r = "TAGTGATG"
matrix = LCS.compute_dp_matrix(s, r)

# Task 2 - Find the LCS without using a backtrack matrix

# Task 3 - Find all LCSs for a S and R
