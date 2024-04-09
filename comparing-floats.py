first_number = float(input())
second_number = float(input())
epsilon_val = float(input())

print("first_number: ", first_number)
print("second_number: ", second_number)
print("epsilon_val: ", epsilon_val)
delta = abs(first_number - second_number)
print("delta: ", delta)

if delta < 0.001:
    print("equal")
    exit()
if delta < epsilon_val:
    print("close enough")
    exit()
else:
    print("not close")
