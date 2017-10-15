# 求阶乘
def recursion_01(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * recursion_01(n-1)


# 菲波那切数列
def recursion_02(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursion_02(n-1)+recursion_02(n-2)


# 判断是否回文字符串
# 判断头尾，缩小规模
def recursion_03(n):
    # 奇数
    if len(n) == 1:
        return True
    if len(n) == 0:
        return True
    if n[0] == n[-1]:
        x = len(n)
        return recursion_03(n[1:x-1])
    else:
        return False


# 二分查找
def recursion_04(n,x):
    mid = int(len(x))/2
    if n == x[mid]:
        return True
    if n< x[mid]:
        return recursion_04(n,x[0:mid])
    if n> x[mid]:
        return recursion_04(n,x[mid+1,-1])
    if n < x[0]:
        return False
    if n> x[-1]:
        return False


# 判断一个数是偶数还是奇数
def recursion_05(n):
    if n == 0:
        return True

# 放苹果
def recoursion_06(m,n):
    if m == 0:
        return True
    if n == 0:
        return True
    if n > m:
        return recoursion_06(m,m)
    else:
        return recoursion_06(m,n-1)+recoursion_06(m-n,n)





