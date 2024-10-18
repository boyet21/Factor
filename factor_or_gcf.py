
def factors(number):
    factoring=[]
    for i in range(1,number+1):
        if number%i==0:
            factoring.append(i)
    return factoroing

def gcf(a,b):
    lcf=1
    smaller = min(a,b)
    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            lcf=i
    return lcf