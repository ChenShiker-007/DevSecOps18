


# Question 1 ##

def find_divisors(n):
    divisors = [n]
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors) #הדפסה_מסודרת_באמצעות_SORT

# קבלת מספר מהמשתמש
num = int(input('Insert a number: '))

# קריאה_לפונקציה_והדפסת_המחלקים
result = find_divisors(num)
print("Divisors:", ", ".join(map(str, result)))



# # Question 2 ##
# Please enter number #1 : 5
# Please enter number #2 (avg=5. Sum=5): 15
# Please enter number #3 (avg=10. Sum=20): -1
# Thank you. Goodbye.
#
#
# # num = input('Insert a positive number: ')
# # while()


