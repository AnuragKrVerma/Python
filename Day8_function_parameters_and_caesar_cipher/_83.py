# prime number checker
def prime_checker(number):
    t = True
    for i in range(2 , number):
        if number % i == 0:
            t = False
            break
    if t :
        print(f"{number} is a Prime number")
    else:
        print(f"{number} is not a Prime number")


n = int(input("Check the number: "))
prime_checker(number = n)