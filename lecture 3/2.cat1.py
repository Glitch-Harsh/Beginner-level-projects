#start an infinite loop 
while True:
    # n is variable to get value from user
    n = int(input("What's n? "))
    #check if n is greater than 0
    if n > 0:
        # if yes exit the loop
        break

# loop n times
# and print "meow" each time
for _ in range(n):
    print("meow")