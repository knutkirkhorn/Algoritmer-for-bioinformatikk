"""
Exercise 1 - Algorithms for bioinformatics
"""


from LCS import LCS

# TODO: fix this code below
s = "AGCTTAGC"
r = "TCGGATG"

longest_common_subs = LCS.compute_dp_matrix(s, r)
print('LCS: {}'.format(longest_common_subs))
#TODO: print(LCS.print_lcs(LCS.find_with_backtrack(s, r)))
