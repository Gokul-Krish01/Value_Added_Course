c = int(input("value : "))

if c <= 1:
    print("1")
else:
    n = 2
    p = 0
    while p < c:
        is_prime = True
        if n % 2 == 0 or n % 3 == 0:
                is_prime = False
        else:
                i = 5
                while i * i <= n:
                    if n % i == 0 or n % (i + 2) == 0:
                        is_prime = False
                        break
                    i += 6

        if is_prime:
            print(n)
            p += 1

        n += 1
