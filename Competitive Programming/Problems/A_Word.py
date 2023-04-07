word = input() 
upper = 0
lower = 0

for _ in word:
    if _.isupper() == True:
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(word.upper())
else:
    print(word.lower())