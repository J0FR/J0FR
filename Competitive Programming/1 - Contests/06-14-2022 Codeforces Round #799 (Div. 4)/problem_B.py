# No paso

import sys

test_cases = int(sys.stdin.readline())

for i in range(test_cases):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    counter = {}
    
    for _ in lst:
        num = lst.count(_)
        counter[_] = num
    
    set = False
                
    for _ in range(1, len(lst)):
        if lst[_ - 1] == lst[_]:
            lst.pop(_ - 1)
            lst.pop(_)
            break
        
        
    
    print(lst)
    