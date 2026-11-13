Pattern = input()
Text = input()
d = int(input())

for i in range(len(Text) - len(Pattern) + 1):
    word = Text[i:i+len(Pattern)]

    count = 0

    for j in range(len(Pattern)):
        if Pattern[j] != word[j]:
            count += 1

    if count <= d:
        print(i, end=" ")
