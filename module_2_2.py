first = 45
second = 42
third = 74
if first == second and second == third and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)