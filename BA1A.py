def PatternCount(Text, Pattern):
    count = 0
    k = len(Pattern)

    for i in range(len(Text) - k + 1):
        if Text[i:i+k] == Pattern:
            count = count + 1

    return count


Text = input()
Pattern = input()

print(PatternCount(Text, Pattern))
