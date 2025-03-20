class Prime:
    def __init__(self, number):
        if not self.isPrime(number):
            raise ValueError("Not a Prime Number")
        self.number = number

    def __repr__(self):
        return f"Prime({self.number})"
    
    def __str__(self):
        return str(self.number)
    
    def __add__(self, step):
        return Prime(self.nextPrime(step))
    
    def __iadd__(self, step):
        self.number = self.nextPrime(step)
        return self

    def __len__(self, N, M):
        return len(self.genPrimeBet(N, M))
    
    #tests if number prime or not
    def isPrime(self, n):
        if n == 2: return True
        return not 1 in [int(n % i == 0) for i in range(2, n) if n > 2]
    
    #calculating next prime
    def nextPrime(self, step):
        temp = self.number
        while True:
            temp += 1
            if self.isPrime(temp): 
                step -= 1
            if step == 0: return temp
        
    #generate list of prime numbers less than
    def genPrimeLt(self, limit):
        return [i for i in range(2,limit+1) if self.isPrime(i)]

    #generate list of prime numbers greater than
    def genPrimeGt(self, limit):
        return [i for i in range(limit, 100) if self.isPrime(i)]

    #generate list of prime numbers within a range
    def genPrimeBet(self, N, M):
        return [i for i in range(N, M) if self.isPrime(i)]
    

a = Prime(7)
print(a)
print(a.__repr__())

print(a.genPrimeLt(50))
print(a.genPrimeGt(50))
print(a.genPrimeBet(20,70))

print(a + 4)
print(a)
a += 4
print(a)