Pattern = input()
Genome = input()

for i in range(len(Genome) - len(Pattern) + 1):
    if Genome[i:i+len(Pattern)] == Pattern:
        print(i, end=" ")
