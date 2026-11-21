from itertools import product

k = int(input())
dna = input().split()

best_pattern = ""
best_distance = float('inf')

for p in product("ACGT", repeat=k):
    pattern = ''.join(p)
    total = 0

    for text in dna:
        min_dist = float('inf')

        for i in range(len(text) - k + 1):
            dist = sum(a != b for a, b in zip(pattern, text[i:i+k]))
            min_dist = min(min_dist, dist)

        total += min_dist

    if total < best_distance:
        best_distance = total
        best_pattern = pattern

print(best_pattern)
