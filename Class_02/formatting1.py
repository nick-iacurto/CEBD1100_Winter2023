first = "Nick"
last = "Iacurto"

print("{} {}".format(first, last))

print("First name is {1} and last name is {0}".format(first, last))

print(f"First name is {first} and last name is {last}")

print("{:04d}".format(42))

# the formatting... before . is width of value, after the . is rounding to places
print('price is ${:10.2f}'.format(1.699))