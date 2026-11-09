Text = input()
k = int(input())

count = {}

for i in range(len(Text) - k + 1):
    word = Text[i:i+k]
    count[word] = count.get(word, 0) + 1

maximum = max(count.values())

for word in count:
    if count[word] == maximum:
        print(word, end=" ")
