text = input()
k = int(input())

profile = []
for i in range(4):
    profile.append(list(map(float, input().split())))

best_kmer = ""
best_prob = -1

for i in range(len(text) - k + 1):
    kmer = text[i:i+k]
    prob = 1

    for j in range(k):
        if kmer[j] == 'A':
            prob *= profile[0][j]
        elif kmer[j] == 'C':
            prob *= profile[1][j]
        elif kmer[j] == 'G':
            prob *= profile[2][j]
        else:
            prob *= profile[3][j]

    if prob > best_prob:
        best_prob = prob
        best_kmer = kmer

print(best_kmer)
