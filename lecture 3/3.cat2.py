# define main function
def main():
    # Call get_number() to get a valid positive integer and pass it to meow()
    meow(get_number())

# define get_number function
def get_number():
    #start an infinite loop to get user input
    while True:
        # n is variable to get value from user
        n = int(input("What's n?"))
        # if n is greater than 0, return n
        if n > 0:
            return n
        
# define meow function
def meow(n):
    # loop n times and print "meow" each time
    for _ in range(n):
        print("meow")

# call main function to execute the program
main()