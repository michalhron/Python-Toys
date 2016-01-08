def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


def getNextPrime(n):
        nCopy = n+1
        while not isPrime(nCopy):
            nCopy+=1
        return nCopy
        
def NextPrimeDist(n):
        steps =1
        nCopy = n+1
        while not isPrime(nCopy):
            steps +=1
            nCopy+=1
        return steps
        


        
        
def fact(x):
    #if len(str(x)) > 15:
    #    raise ValueError("May be too long")
    divisor = 2
    remainder = x
    factors = [1]
    while not isPrime(remainder):
        while remainder % divisor == 0:
            factors.append(divisor)
            remainder /= divisor
        else: 
            divisor = getNextPrime(divisor)
    if remainder not in factors and isPrime(remainder):
        factors.append(remainder)
    
    return factors
        
        
        
    
    
def defact(list):
    result = 1
    for i in list:
        result *= i
    return result
    
    
    
    