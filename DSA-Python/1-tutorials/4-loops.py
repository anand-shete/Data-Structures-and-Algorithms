# if elif else conditional
score = 85
if score > 90:
    print("Outstanding student")
elif score < 80:
    print("He can do better")
else:
    print("Score is average")
print()



# range(start, stop, step)
# start (optional): start integer (inclusive, defaults to 0)
# stop (required): end integer (exclusive)
# step (optional): increment or decrement integer (defaults to 1)
# loop from start to stop-1 (+ve step) or start to stop+1 (-ve step)



# for loop
# move in -ve direction with step 1, start at 10 end at 0+1 = 1
for i in range(10, 0, -1):
    print(i, end=' ')
print()



# element based for loop
nums = [12, 34, 45, 23, -4]
for num in nums:
    print(num, end=' ')
print('\n')



# while loop
n = 5126
print('reversed:', end=' ')
while n > 0:
    print(n % 10, end="")
    n //= 10
print('\n')




# break
while i in range(10):
    if i == 3:
        break
    print(i, end=',')
    i += 1
print('\n')



# continue
for i in range(1,5+1):
    if i == 2:
        continue
    print(i, end=" ")
    i+=1
print('\n')



# match case
status_code = 500
match status_code:
    case 200:
        print("success")
    case 400:
        print("Client error")
    case 500:
        print("Internal server error")
    case _:
        print("God knows the status_code, not me")
print()


    
# An else block appended immediately after a for loop or while loop will execute only if the loop finishes naturally without encountering a break statement
target = 5
nums = [1, 2, 3, 4]

for x in nums:
    if x == target:
        print("Found target")
        break
else:
    print("loop did not execute break") 