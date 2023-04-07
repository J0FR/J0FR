# https://codeforces.com/problemset/problem/116/A

cases = int(input())
train_states = [0]

for _ in range(cases):
    going_out, coming = map(int, input().split())
    last = train_states[_]
    train_states.append((last - going_out) + coming)

print(max(train_states))

