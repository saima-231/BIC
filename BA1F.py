Genome = input()

skew = 0
values = [0]

for i in Genome:
    if i == 'G':
        skew += 1
    elif i == 'C':
        skew -= 1

    values.append(skew)

minimum = min(values)

for i in range(len(values)):
    if values[i] == minimum:
        print(i, end=" ")
