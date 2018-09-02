#列表冒泡排序
nums=[5, 2, 1, 4, 3]
for i in range(len(nums)-1):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)