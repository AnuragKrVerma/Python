# Fizz Buzz problem

for i in range(1 , 100 + 1):
    if(i % 15 == 0 ):
        print(i , " FizzBuzz")
    elif(i % 3 == 0):
        print(i , " Fizz")
    elif(i % 5 == 0):
        print(i , " Buzz")
    else:
        print(i)
    