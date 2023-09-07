def dani():
    num = int(input("Enter a number: "))
    sum = 0
    temp=num
    while temp> 0:
        digit = temp % 10
        sum += digit ** 3
        # sum += digit ** 4
        temp //= 10
    if num == sum:
        print("it is an Armstrong number")
    else:
        print("it is not an Armstrong number")
dani()
      