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
            row.append(sum(m[j] == x for m in motifs) / len(motifs))
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


best_motifs = [s[:k] for s in dna]

for i in range(len(dna[0]) - k + 1):
    motifs = [dna[0][i:i+k]]

    for j in range(1, t):
        p = profile(motifs)
        motifs.append(most_probable(dna[j], p))

    if score(motifs) < score(best_motifs):
        best_motifs = motifs

print(*best_motifs)
