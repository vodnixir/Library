# y = int(input())
# r = int(input())
# b = int(input())
# x = b + (r * 10) + (y * 100)
# res = x // 1000
# print(res)
#
#

# s = input()
# n = int(s)
# cnt = 0
# while n > 0:
#     s = str(n)
#     found = False
#     for i in range(len(s)):
#         # print(f"s = {s}, s[{i}] = {s[i]}")
#         if int(s[i]) & 1:
#             found = True
#             break
#     if found:
#         n = int(s) - 1
#     else:
#         n = int(s) // 2
#     cnt += 1
# print(cnt)

# s = input()
# cnt = 0
# while int(s) > 0:
#     found = False
#     for i in range(len(s)):
#         if int(s[i]) & 1:
#             found = True
#             break
#     if found:
#         s = str(int(s) - 1)
#     else:
#         s = str(int(s) // 1)
#     cnt += 1
# print(cnt)




# cnt = int(input())
# ints = [0] * cnt
# for i in range(cnt):
#     ints[i] = int(input())
# tmp = ints.copy()
# for i in range(cnt):
#     tmp = ints.copy()
#     for j in range(cnt):
#         if i != j:
#             if tmp[i] < ints[j]:
#                 tmp[i] = 0
#                 break
#             elif tmp[i] > ints[j]:
#                 tmp[i] += ints[j]
#     # if tmp[i] == ints[i]:
#     #     tmp[i] = 0
#
#     if tmp[i] > 0:
#         print(1)
#     else:
#         print(0)

# k = int(input())
# n = int(input())
# pred = n % k
# next = k - pred
# if next > pred:
#     print(pred)
# else:
#     print(next)

# a = int(input())
# b = int(input())
# if (a + b) % 3 != 0:
#     print(-1)
# else:
#     k1 = 0
#     k2 = 0
#     while a + b > 0:
#         if a > b:
#             k1 += 1
#             a -= 2
#             b -= 1
#         elif a < b:
#             k2 += 1
#             b -= 2
#             a -= 1
#         else:
#             k1 += 1
#             k2 += 1
#             a -= 3
#             b -= 3
#     if a == 0 and b == 0:
#         print(k1)
#         print(k2)
#     else:
#         print(-1)



# a = int(input())
# b = int(input())
# t = int(input())
# tmp1 = t % a
# tmp2 = t % b
# if a - tmp1 > b - tmp2:
#     print(1)
# if a - tmp1 < b - tmp2:
#     print(2)
# else:
#     if a>b:
#         print(2)
#     elif b<a:
#         print(1)
#     else:
#         print(0)

# t = int(input())
# r = int(input())
# l = int(input())
# p1 = int(input())
# p2 = int(input())
# p3 = int(input())
# cnt = 0
# m = r * l
# if t < m:
#     while True:
#         t += p1
#         cnt +=1
#         if t >= m:
#             break
#         t += p2
#         cnt += 1
#         if t >= m:
#             break
#         t += p3
#         cnt += 1
#         if t >= m:
#             break
# print(cnt)

# M = int(input())
# N = int(input())
# if M > (((N + 1) * N ) // 2):
#     print(0)
# else:
#     while M > 0:
#         if N == M:
#             print(N)
#             M = 0
#         elif (M - N) > 0:
#             M -= N
#             print(N)
#         N -= 1

# n = int(input())
# k = int(input())
# cnt = 0
# now = 0
# k %= n
# while True:
#     now += k
#     now %= n
#     cnt += 1
#     if (n-now) % n<= cnt:
#         print(cnt)
#         break

# n = int(input())
# k = int(input())
# en = 0
# for i in range(n):
#     a = int(input())
#     while a > 1 and a -(a//2) > k:
#         a //= 2
#         en += k
#     en += a - 1
# print(en)

# def compare(i, v0, d3, d4) :
#     if v0[0] - i[0] == 0 and (v0[0] - d4[0] == 0):
#         if not ((v0[1] - i[1] > 0 and (v0[1] - d4[1] > 0)) or (v0[1] - i[1] < 0 and (v0[1] - d4[1] < 0))):
#             return False
#         elif not((v0[0] - i[0] > 0 and (v0[0] - d4[0] > 0)) or (v0[0] - i[0] < 0 and (v0[0] - d4[0] < 0))) :
#             return False
#         if (v0[0] - i[0]) * (d3[1] - d4[1]) == (d3[0] - d4[0]) * (v0[1] - i[1]) :
#             return True
#     return False
#
# n = int(input())
# v = list()
# edges = list()
# v.append((int(input()), int(input())))
# for i in range(1, n):
#     v.append((int(input()), int(input())))
#     edges.append((1, i+1))
#     for j in range(0, len(edges) - 1):
#         if compare(v[i], v[0], v[edges[j][0] - 1], v[edges[j][1] - 1]):
#             if abs(v[0][0] - v[i][0]) > abs(v[0][0] - v[edges[j][1] - 1][0]):
#                 edges[-1] = (edges[j][1], i + 1)
#             elif abs(v[0][0] - v[i][0]) < abs(v[0][0] - v[edges[j][1] - 1][0]):
#                 edges[j] = (i + 1, edges[j][1])
#             else:
#                 if abs(v[0][1] - v[i][1]) > abs(v[0][1] - v[edges[j][1] - 1][1]):
#                     edges[-1] = (edges[j][1], i + 1)
#                 else:
#                     edges[j] = (i + 1, edges[j][1])
# print(n-1)
# for x in edges:
#     print(x[0], x[1])

# import math
#
# a, b, c = map(float, input().split())
# print(a, b, c)
# if a == 0 and b == 0:
#     print(-1)
#     exit()
# d = b * b - 4.0 * a * c
# a2 = a * 2.0
# if d < 0:
#     print(0)
#     exit()
# q = math.sqrt(d)
# x1 = (-b - q)/a2
# x1 = round(x1,10)
# if d == 0:
#     print(1, x1)
#     exit()
# x2 = (-b + q)/a2
# x2 = round(x2,10)
# if x1 > x2:
#     print(2, x2, x1)
#     exit()
# print(2, x1, x2)



# РАЗЛОЖЕНИЕ НА СЛАГАЕМЫЕ

# import time
#
# def isPrime(num):
#     if num == 1 or num == 2 or num == 3:
#         return True
#     if num > 1:
#         for i in range(2,int(num/2)+1):
#             if (num % i) == 0:
#                 return False
#             else:
#                 return True
#     else:
#         return False
#
# def f(a, n, p, src):
#     if n:
#         for i in range(n, 0, -1):
#             if i <= p and isPrime(i):
#                 f(a + [i], n - i, i, src)
#     else:
#         print(src,'= ', end='')
#         print(*a, sep=' + ')
#
#
# n = int(input())
# btm = time.time()
# f([], n, n, n)
# etm = time.time()
# print("Время выполнения:", round(1000.0 * (etm-btm)), "миллисекунд")



# ИЗ ДЕСЯТИЧНОЙ СИСТЕМЫ В ДВОИЧНУЮ
# cnt = int(input())
# nums = [0] * cnt
# for i in range(0, cnt):
#     # print(f"cnt = {cnt}, i = {i}")
#     nums[i] = int(input())
# for el in nums:
#     res = ""
#     num = el
#     while True:
#         num2 = num // 2
#         rest = num % 2
#         res = str(rest) + res
#         if num2 == 0:
#             break
#         num = num2
#     print(res)
#



# ДЕСЯТИЧНАЯ В ШЕСТНАДЦАТЕРИЧНУЮ
# def intToHex(num):
#     if num < 10:
#         return str(num)
#     elif num == 10:
#         return 'A'
#     elif num == 11:
#         return 'B'
#     elif num == 12:
#         return 'C'
#     elif num == 13:
#         return 'D'
#     elif num == 14:
#         return 'E'
#     elif num == 15:
#         return 'F'
#     return '*'
#
# cnt = int(input())
#
# nums = [0] * cnt
# for i in range(0, cnt):
#     # print(f"cnt = {cnt}, i = {i}")
#     nums[i] = int(input())
# base = 16
# for el in nums:
#     res = ""
#     num = el
#     while True:
#         num2 = num // base
#         rest = num % base
#         res = intToHex(rest) + res
#         if num2 == 0:
#             break
#         num = num2
#     print(res)


# cnt = int(input())
# nums = [0] * cnt
# for i in range(0, cnt):
#     nums[i] = int(input())
# for el in nums:
#     a = hex(el) # в 16ричную но в начале 0х
#     a = a[2::] # взять сиволы начиная со второго(0 - based) (чтобы не было 0х в начале) (извлекаем) (substring)
#     a.upper()  # делаем caps (abcdef в ABCDEF)
#     # print(hex(el)[2::].upper()) # все за раз (для понтов)
#     print(a)



# ИЗ ДЕСЯТИЧНОЙ В ЛЮБУЮ
# def intToBase(num):
#     if num < 10:
#         return str(num)
#     return chr(65 + num - 10)
#
# while True:
#     num, base = map(int, input().split())
#     res = ""
#     while True:
#         num2 = num // base
#         rest = num % base
#         res = intToBase(rest) + res
#         if num2 == 0:
#             break
#         num = num2
#     print(res)

# ВВОД КОЛИЧЕСТВА СТРОК И САМИХ СТРОК В ЦЕЛОЧИСЛЕННЫЙ МАССИВ

# def decToRim(n, res):
#     if n >= 1000:
#         n -= 1000
#         res += "M"
#     elif n >= 900:
#         n -= 500
#         res += "D"
# if n > 0:
#     res = decToRim(n, res)
# return res

# def decToRim(s, res):
#     if len(s) > 4:
#         return res
#     if len(s) == 4:
#         base = "M"
#         n = int(s[0])
#         while n > 0:
#             res += base
#             n -= 1
#         s = s[1::]
#         res = decToRim(s, res)
#         return res
#     if len(s) == 3:
#         base = "C"
#         base5 = "D"
#         base10 = "M"
#     elif len(s) == 2:
#         base = "X"
#         base5 = "L"
#         base10 = "C"
#     elif len(s) == 1:
#         base = "I"
#         base5 = "V"
#         base10 = "X"
#     elif len(s) == 0:
#         return res
#
#     n = int(s[0])
#     if n == 0:
#         pass
#     elif n <= 3:
#         while n > 0:
#             res += base
#             n -= 1
#     elif n == 4:
#         res += base + base5
#     elif n == 5:
#         res += base5
#     elif n <= 8:
#         res += base5
#         while n > 5:
#             res += base
#             n -= 1
#     else:
#         res = res + base + base10
#     s = s[1::]
#     res = decToRim(s, res)
#     return res
#
#
#
# cnt = int(input())
# nums = []
# for i in range(cnt):
#     nums.append(input())
#
# for num in nums:
#     res = ""
#     res = decToRim(num, res)
#     print(res)














