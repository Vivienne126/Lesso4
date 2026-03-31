n=int(input("Enter a number"))

digits=len(str(n))

result_number=0

temp=n

while temp>0:
    digit=temp%10
    result_number+=digit**digits
    temp//=10

if n==result_number:
    print(f"{n} is a amstrong number")
else:
    print(f"{n} is not a  amstrong number")
