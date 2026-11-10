Genome = input()
k = int(input())
L = int(input())
t = int(input())

result = []

for i in range(len(Genome) - L + 1):
    window = Genome[i:i+L]

    for j in range(len(window) - k + 1):
        word = window[j:j+k]

        if window.count(word) >= t:
            if word not in result:
                result.append(word)

for word in result:
    print(word, end=" ")
