# Q1: 两数之和
def twoSum(nums, target):
    result = []
    hashmap = {}  # 创建哈希表
    for idx, num in enumerate(nums):
        hashmap[num] = idx  # 键：数值，值：索引
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in hashmap and hashmap[diff] != idx:
            result.append(idx)
            result.append(hashmap[diff])
            return result


# Q169: 多数元素
def majorityElement1(nums):  # 法1：排序法
    nums.sort()
    half = len(nums) // 2
    return nums[half]


def majorityElement2(nums):  # 法2：哈希表法
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] = hashmap[num] + 1  # hashmap.get(num) + 1
    half = len(nums) // 2
    for key in hashmap.keys():
        if hashmap[key] > half:
            return key
    # 多数元素不存在
    return -1


# Q448: 找到所有数组中消失的数字
def findDisappearedNumbers(nums):
    counter = set(nums)  # 集合：元素不重复
    result = []
    for i in range(1, len(nums) + 1):
        if i not in counter:
            result.append(i)
    return result


# Q283: 移动零
def moveZeros(nums):
    n = len(nums)
    slow, fast = 0, 0  # 双指针
    while fast < n:
        if nums[slow] != 0 and nums[fast] == 0:
            slow = fast  # 把slow指到待替换位置
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
    return nums


# Q136: 只出现一次的数字
def singleNumber(nums):
    x = 0
    for num in nums:
        x ^= num  # ^为异或操作，a ^ a = 0, a ^ 0 = a
    return x


# Q121: 买卖股票的最佳时机
def maxProfit(prices):
    minprice = float('inf')
    maxprofit = 0
    for price in prices:  # 直接遍历法
        minprice = min(minprice, price)
        maxprofit = max(maxprofit, price - minprice)
    return maxprofit


# Unsolved list
# 1. 动态规划


if __name__ == "__main__":
    # Q1
    # a = twoSum([2, 7, 11, 15], 9)
    # print(a)

    # Q169
    # a = majorityElement2([2, 2, 1, 1, 1, 2, 2])
    # print(a)

    # Q448
    # a = findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    # print(a)

    # Q283
    # a = moveZeros([0, 1, 0, 3, 12])
    # print(a)

    # Q136
    # a = singleNumber([2, 4, 4, 5, 5])
    # print(a)

    # Q121
    a = maxProfit([7, 1, 5, 3, 6, 4])
    print(a)

