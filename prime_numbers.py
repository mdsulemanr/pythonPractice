def prime_eratosthenes(n):
    not_prime=[]
    prime_num = []
    for i in range(2, n+1):
        if i not in not_prime:
            prime_num.append(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
    return prime_num


print(prime_eratosthenes(100))