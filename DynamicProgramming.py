# Q70: 爬楼梯
def climbStairs(n):
    res = [1, 2]
    if n <= 2:
        return n
    for i in range(2, n):
        res.append(res[-1] + res[-2])  # 斐波那契数列
    return res[-1]


# Q338: 比特位计数
def countBits1(num):  # 哈希表法
    if num == 0:
        return [0]
    result = [0]
    hashmap = {0: 0}  # 0值单独考虑
    for i in range(1, num+1):
        if i & (i-1) == 0:  # 二进制上存在进位
            pre = i  # pre仅存放最高位1其余位0的数
            count = 1
        else:
            count = 1 + hashmap[i-pre]
        hashmap[i] = count
        result.append(count)
    return result


if __name__ == "__main__":
    # Q70
    # a = climbStairs(4)
    # print(a)

    # Q338
    a = countBits1(2)
    print(a)
