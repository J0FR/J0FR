case = input()

print(f"{case[0] if case[0].isupper() == True else case[0].swapcase()}{case[1:]}")