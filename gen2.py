def even_num_gen(n):
    for num in range(0, n + 1, 2):
        yield num

n = int(input("Enter a value for n: "))

even_num= even_num_gen(n)
even_num_list = list(even_num)

result = ', '.join(map(str, even_num_list))

print("Even numbers between 0 and", n, "in comma-separated form:")
print(result)
