def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

# 测试代码
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # 输出应为 [0, 1]