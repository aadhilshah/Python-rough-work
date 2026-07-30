num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("fizzBuzz")
elif num%5==0:
    print("buzz")
elif num%3==0:
    print("Fizz")
else:
    print(num)