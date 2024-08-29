# !/usr/bin/python3
# encoding:utf-8

# def test(x):
#     low,high,ans = 0, x, -1;
#     while low <= high:
#         mid = ( low + high)// 2
#         if mid * mid <= x:
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans

# print(5)
x = 13
if x == 0:
    res = 0
else :
	C,x0 = float(x),float(x)
	while True:
		xi = 0.5 * (x0 + C / x0)
		if abs(x0 - xi) < 1e-7:
			break
		x0 = xi
	res = int(x0)
print(res)