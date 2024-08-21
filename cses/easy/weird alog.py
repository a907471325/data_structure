
n = input()
n = int(n)
res_list = [str(n)]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    res_list.append(str(n))
print(" ".join(res_list))