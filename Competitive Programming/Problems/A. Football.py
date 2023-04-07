# https://codeforces.com/problemset/problem/96/A

# Option 1
caso = input()
size = len(caso)
seguido = 0
flag = caso[0]
 
for _ in range(size):
    if caso[_] == flag:
        seguido += 1
        if seguido >= 7:
            print("YES")
            break
    else:
        seguido = 1
        flag = caso[_]
else:
    print("NO")

# Option 2
caso = input()
cero = "0000000"
uno = "1111111"
 
if cero in caso or uno in caso:
    print("YES")
else:
    print("NO")