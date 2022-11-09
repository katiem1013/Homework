# exercise 1
list_1 = ['mix', 'apple', 'rovio']
list_2 = ['xyz', 'xanadu']
print(sorted(list_2), sorted(list_1))

# exercise 2
words = ["xxx", "aaa", "r5t6yy", "g", "wow"]

amount_of_words = 0
for i in words:
    if (len(i) >= 2) and (i[-1] == i[0]):
        amount_of_words += 1
        print(amount_of_words, i)

# exercise 3
attempts = 3

while attempts > 0:
    password = input("Please enter password: ")
    attempts -= 1

    if password == "password":
        print("Welcome")
        break
    else:
        print("wrong password ")
        print(attempts, " attempts remaining")

else:
    print("you lost")

# exercise 4
for rows in range(10):
    for i in range(rows):
        print('*', end=' ')
    print('')