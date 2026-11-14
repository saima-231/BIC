Text = input()
k = int(input())
d = int(input())

count = {}

for a in range(4**k):
    pattern = ""
    n = a

    for j in range(k):
        pattern += "ACGT"[n % 4]
        n = n // 4

    count[pattern] = 0

    for i in range(len(Text) - k + 1):
        word = Text[i:i+k]
        mismatch = 0

        for j in range(k):
            if word[j] != pattern[j]:
                mismatch += 1

        if mismatch <= d:
            count[pattern] += 1

maximum = max(count.values())

for pattern in count:
    if count[pattern] == maximum:
        print(pattern, end=" ")
