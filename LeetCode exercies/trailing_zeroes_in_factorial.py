'''
Given an integer n, return the number of trailing zeroes in n factorial n!
'''

# Brute force approach
def trailing_zeros(n:int) -> int:
    def find_Factorial(num):
        if num == 1:
            return 1
        return num * find_Factorial(num-1)
    
    def trailing_zeroes(num):
        cnt = 0
        while num % 10 == 0:
            cnt += 1
            num = num // 10
        return cnt
    
    fact = find_Factorial(n)
    cnt = trailing_zeroes(fact)
    return cnt

print(trailing_zeros(5))
print(trailing_zeros(50))

# Optimal approach
#???