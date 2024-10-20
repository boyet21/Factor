
def factors(number):
    factoring=[]
    for i in range(1,number+1):
        if number%i==0:
            factoring.append(i)
    return factoring

def lcf(num1,num2):
    lcf=1
    smaller = min(num1,num2)
    for i in range(1,smaller+1):
        if num1%i==0 and num2%i==0:
            lcf=i
    return lcf