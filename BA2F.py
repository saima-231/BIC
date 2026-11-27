import random

k, t = map(int, input().split())
dna = [input() for _ in range(t)]

def score(motifs):
    total = 0
    for j in range(k):
        column = [m[j] for m in motifs]
        total += len(column) - max(column.count(x) for x in "ACGT")
    return total


def profile(motifs):
    matrix = []

    for x in "ACGT":
        row = []
        for j in range(k):
            count = 1
            for m in motifs:
                if m[j] == x:
                    count += 1
            row.append(count / (len(motifs) + 4))
        matrix.append(row)

    return matrix


def most_probable(text, matrix):
    best = text[:k]
    best_prob = -1

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        prob = 1

        for j in range(k):
            prob *= matrix["ACGT".index(pattern[j])][j]

        if prob > best_prob:
            best_prob = prob
            best = pattern

    return best


best_overall = None

for run in range(1000):

    motifs = []

    for text in dna:
        i = random.randint(0, len(text) - k)
        motifs.append(text[i:i+k])

    best_motifs = motifs[:]

    while True:
        p = profile(motifs)
        motifs = [most_probable(text, p) for text in dna]

        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]
        else:
            break

    if best_overall is None or score(best_motifs) < score(best_overall):
        best_overall = best_motifs[:]

print(*best_overall)
