def is_prime(num):
    #Prime -> returns True
    #not Prime -> return False
    
    if num == 2:
        return True
    elif num > 2:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    else:
        return "Invalid Number"

print("Enter a number:", end=" ")
num = int(input())
print(is_prime(num))