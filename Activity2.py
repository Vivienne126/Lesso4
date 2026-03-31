def factor(number):
    print(f"The factors of {number} are:")
    for i in range(1,number+1):
        if number%i==0:
            print(i)

number=int(input("Enter your number to find factors"))

factor(number)