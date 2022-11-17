# Q461: 汉明距离
def hammingDistance(x, y):
    return bin(x ^ y).count('1')


if __name__ == "__main__":
    # Q461
    a = hammingDistance(1, 4)
    print(a)
