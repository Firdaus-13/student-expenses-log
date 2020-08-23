def example():
    
    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        test4word = int(input("Enter an Integer Number: "))

        try:
            test4num = int(input("Enter another Integer bigger than that :" ))

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        # When successfully converted to an integer,
        # the loop will end.
        else:
            print("In range of ", test4word, "to", test4num, ",the numbers that can be divided by 3:", test4num*60*60, "seconds in your mobile!")
            break

# The function is called
example()