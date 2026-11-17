import os, sys
def get_even(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result
def total(items):
    t=0
    for i in items:
        t = t + i
    return t
