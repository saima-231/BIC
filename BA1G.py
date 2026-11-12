p = input()
q = input()

count = 0

for i in range(len(p)):
    if p[i] != q[i]:
        count += 1

print(count)
