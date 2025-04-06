"""
sort012.py
by Paul Renaud
4/6/2025
IvyTech SDEV220
Given an unsorted list of 0s, 1s, and 2s, change the list to be sorted.
This one counts how many of each, and then simply creates a new list.

I was originally counting them manually in a pass through the list,
but then I remembered the count function exists.
"""

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        arr[:] = [0]*arr.count(0) + [1]*arr.count(1) + [2]*arr.count(2)
      
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1]
print(arr)
Solution.sort012(Solution, arr)
print(arr)
