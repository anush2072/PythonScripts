# // i is the starting index and j is the ending index. i must be passed as 0 and j as n-1
# minPalPartion(str, i, j) = 0 if i == j. // When string is of length 1.
# minPalPartion(str, i, j) = 0 if str[i..j] is palindrome.

# // If none of the above conditions is true, then minPalPartion(str, i, j) can be 
# // calculated recursively using the following formula.
# minPalPartion(str, i, j) = Min { minPalPartion(str, i, k) + 1 +
#                                  minPalPartion(str, k+1, j) } 
#                            where k varies from i to j-1