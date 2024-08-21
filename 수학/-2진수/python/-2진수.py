n = int(input())
if n == 0:
    print("0")
else:
    answer = ""
    while n != 0:
        remainder = n % -2
        n //= -2

        if remainder < 0:
            remainder += 2
            n += 1
        
        answer = str(remainder) + answer

    print(answer)
