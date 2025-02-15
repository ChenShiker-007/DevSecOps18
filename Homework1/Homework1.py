


# Question 1 ##

# def find_divisors(n):
#     divisors = [n]
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             divisors.append(i)
#     return sorted(divisors) #הדפסה_מסודרת_באמצעות_SORT
#
# #קבלת_מספר_מהמשתמש
# num = int(input('Insert a number: '))
#
# ##קריאה_לפונקציה_והדפסת_המחלקים
# result = find_divisors(num)
# print("Divisors:", ", ".join(map(str, result)))



# # Question 2 ##
# Please enter number #1 : 5
# Please enter number #2 (avg=5. Sum=5): 15
# Please enter number #3 (avg=10. Sum=20): -1
# Thank you. Goodbye.
#
#

def collect_numbers():
    count = 0  # מונה_את_כמות_המספרים_שהוזנו
    total_sum = 0  # סכום_המספרים_שנקלטו

    while True:
        if count == 0:
            user_input = input(f"Please enter number #{count + 1}: ")
        else:
            avg = total_sum / count  # חישוב_ממוצע
            user_input = input(f"Please enter number #{count + 1} (avg={avg:.2f}. Sum={total_sum}): ")

        num1 = int(user_input)  # המרת_הקלט_למספר_שלם

        if num1 < 0:  #יציאה_אם_המספר_שלילי
            break

        count += 1
        total_sum += num1

    print("Thank you. Goodbye.")


#קריאה_לפונקציה
collect_numbers()



