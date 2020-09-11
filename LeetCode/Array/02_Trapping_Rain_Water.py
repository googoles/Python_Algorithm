from typing import List

# 문제풀이 Stack 이용
# 1. 깊이를 잰다. (어떻게?)
# 1.1 갑자기 높아지면 그 전의 높이만큼 + 1
# 1.2 but 그 다음 칸의 높이 고려해서 채워준다.
#

# class Solution:
#     def trap(self, height: List[int]) -> int:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

water = 0

for i in range(1, len(height)):

    left = height[i]

    for j in range(i):

        left = max(left,height[j])

    right = height[i]

    for j in range(i+1,len(height)):

        right = max(right,height[j])

    water = water + (min(left,right)-height[i])

print(water)

        # return water

# a = Solution
# print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# class Solution:
#     def trap(self, height: List[int]) -> int:
#
#         water = 0
#
#         for i in range(1, len(height)):
#
#             left = height[i]
#
#             for j in range(i):
#                 left = max(left, height[j])
#
#             right = height[i]
#
#             for j in range(i + 1, len(height)):
#                 right = max(right, height[j])
#
#             water = water + (min(left, right) - height[i])
#
#         return water


# input : [0,1,0,2,1,0,1,3,2,1,2,1] height
# output : 6

