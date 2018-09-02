# items=[1,[2,[3,[4,[5]]]]]
# def tell(l):
#     for item in l:
#         if type(item) is not list:
#             print(item)
#         else:
#             tell(item)
# tell(items)


# 找一个从小到大排列的整型数字列表
# nums=[1,33,5,8,9,5,2,555,66,]
# for item in nums:
#     if item==10:
#         print('find it')
#         break
# else:
#     print('not exists')


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def foo(n, nums):
    a = len(nums) // 2
    if n > nums[a]:
        nums = nums[a + 1:]
        foo(n, nums)
    elif n < nums[a]:
        nums = nums[:a]
        foo(n, nums)
    else:
        print("找到了")


foo(10, nums)
