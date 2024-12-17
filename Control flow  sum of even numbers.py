#Write a program to sum all even numbers from 1 to 50 using a loop.
even_sum = 0
for num in range (1,51):
    if num % 2 == 0:
        print(f"The even numbers from 1 to 50 are : {num}")
        even_sum += num
print(f"The sum of all even numbers from 1 to 50 is:{even_sum}")