def div_by_3_and_4_gen(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter a value for n: "))

for number in div_by_3_and_4_gen(n):
    print(number)
