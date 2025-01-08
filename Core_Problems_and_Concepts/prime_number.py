def prime_number(n):
    square_root_n = n ** 0.5
    print(int(square_root_n))
    if n < 2:
        return False
    for i in range(2,int(square_root_n)+1):
        print(i)
        if n%i == 0:
            return False
    return True

print(prime_number(7))


