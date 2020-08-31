import bisect
nums = [5,2,6,1]
sorted_nums = []
ans = []
for n in nums[::-1]:
    index = bisect.bisect_left(sorted_nums,n)
    bisect.insort(sorted_nums,n)
    ans.append(index)
# triangle = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# n = len(triangle)
# f = [[0] * n for _ in range(n)]
# f[0][0] = triangle[0][0]
#
# for i in range(1, n):
#     f[i][0] = f[i - 1][0] + triangle[i][0]
#     for j in range(1, i):
#         f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
#     f[i][i] = f[i - 1][i - 1] + triangle[i][i]
#
# print(min(f[- 1]))
