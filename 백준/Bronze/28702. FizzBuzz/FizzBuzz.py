I1 = input()
I2 = input()
I3 = input()

i = int
if I1.isdigit():
    i = int(I1) + 3
elif I2.isdigit():
    i = int(I2) + 2
elif I3.isdigit():
    i = int(I3) + 1

answer = i
if not i % 3 and not i % 5:
    answer = "FizzBuzz"
elif not i % 3:
    answer = "Fizz"
elif not i % 5:
    answer = "Buzz"

print(answer)