"""
Leetcode 2366: Minimum Replacements to Sort the Array
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

You are given a 0-indexed integer array nums. In one operation you can replace
any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1]
with 2 and 4 and convert nums to [5,2,4,7].

Return the minimum number of operations to make an array that is sorted in non
decreasing order.


Constraints:
  1 <= nums.length <= 10^5
  1 <= nums[i] <= 10^9
"""


from typing import List


def minimumReplacement(nums: List[int]) -> int:
	steps = 0
	upper_bound = nums[-1]  # The largest number we can place at the current pos
	for i in range(len(nums) - 1, -1, -1):
		# Calculate number of replacements needed to be within upper_bound
		num_replacements = (nums[i] + upper_bound - 1) // upper_bound
		# Update upper bound based on number of replacements we did on nums[i]
		upper_bound = nums[i] // num_replacements
		steps += num_replacements - 1 # Add number of steps taken; replacements - 1
	return steps


# Test cases
test_cases = [[3, 9, 3], [1, 2, 3, 4, 5], [12, 9, 7, 6, 17, 19, 21]]
test_case_expected = [2, 0, 6]

print()
print("Testing Report")
print("-" * 48)
num_passed = 0
for i in range(len(test_cases)):
	output = minimumReplacement(test_cases[i])

	print("minimumReplacement(" + str(test_cases[i]) + "):", output)
	print("\\" + "-" * (11 + len(str(test_cases[i]))) + "Expected:", test_case_expected[i])

	if (output == test_case_expected[i]):
		print("Test case", i + 1, "passed!")
		num_passed += 1
	else:
		print("Test case", i + 1, "failed!")
	print()

print("Test cases passed:", str(num_passed / len(test_cases) * 100) + "%")
print("-" * 48)