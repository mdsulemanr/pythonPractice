def prime_eratosthenes(n):
    not_prime=[]
    for i in range(2, n+1):
        if i not in not_prime:
            print(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
print(prime_eratosthenes(100))