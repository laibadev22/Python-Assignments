def get_odds(num):
    result=[]
    for i in num:
        if i%2!=0:
            result.append(i)
    return result

def get_even(num):
    result=[]
    for i in num:
        if i%2 == 0:
            result.append(i)
    return result
def get_prime(num):
    result=[]
    for n in num:
        if n <=1:
            continue
        prime = True
        for i in range(2,n):
            if n%i==0:    
                prime = False
                break
        if prime:                 
            result.append(n)
    return result

numbers=[]
for i in range(10):
    num= int(input("Enter Number: "))
    numbers.append(num)

odd=get_odds(numbers)
even=get_even(numbers)
prime=get_prime(numbers)

if odd:
    print("odd",odd)
else:
    print("odd: Not Found")    
if even:
    print("Even",even)
else:
    print("Even: Not Found")    
if odd:
    print("Prime",prime)
else:
    print("Prime: Not Found")    
