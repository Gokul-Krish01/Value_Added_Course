n = int(input("value: "))
a=0 
b=1
count = 0
if n <= 0:
    print("-ve value")
elif n == 1:
    print(a)
else:
    print("series:")
    while count < n:
        print(a)
        v = a + b
        a = b
        b = v
        count += 1
