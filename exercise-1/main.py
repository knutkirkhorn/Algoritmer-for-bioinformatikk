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
