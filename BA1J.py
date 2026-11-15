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

    reverse = ""

    for letter in pattern:
        if letter == 'A':
            reverse += 'T'
        elif letter == 'T':
            reverse += 'A'
        elif letter == 'C':
            reverse += 'G'
        else:
            reverse += 'C'

    reverse = reverse[::-1]

    total = 0

    for i in range(len(Text) - k + 1):
        word = Text[i:i+k]

        mismatch1 = 0
        mismatch2 = 0

        for j in range(k):
            if word[j] != pattern[j]:
                mismatch1 += 1

            if word[j] != reverse[j]:
                mismatch2 += 1

        if mismatch1 <= d:
            total += 1

        if mismatch2 <= d:
            total += 1

    count[pattern] = total

maximum = max(count.values())

for pattern in count:
    if count[pattern] == maximum:
        print(pattern, end=" ")
