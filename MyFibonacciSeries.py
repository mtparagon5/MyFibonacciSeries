
# first we'll ask for input from the user
# to determine the length of the series
# that should be created
def get_series_length():
    # Here we'll use a try/except blocks 
    # to account for user entering a non-integer
    while True:
        # here we'll try to get an integer 
        # from the user
        try:
            series_length = int(input(
                "How many numbers in the " + 
                "Fibonacci series would you " +
                "like to display? "))
            # we want to make sure we get a number > 0
            if series_length <= 0:
                print("Hmm...it seems you entered a value " + u"\u2264" + " 0. Try again!")
                continue
                
        # if the user provides a non-integer
        # this will catch the error and ask
        # the user for valid input
        except ValueError:
            print("Please enter a valid integer")
            #continue will allow the loop to kepp going
            continue
        # once we get a valid input, we for the function
        # to return it
        else:
            return series_length
            

#get_series_length()

# next we'll generate the list of numbers in the Fibonacci 
# the user designated


# Next we'll create a function that will generate 
# a fibonacci series the length of the user's input

# define the function
def get_fib_series(length):
    # create an empty list
    list = []
    
    # each number in the range(users input)
    for l in range(length):
        # if the # is 0 -> add 0 to the list
        if l == 0:
            list.append(0)
        
        # else if the # is 1 -> add 1 to the list
        elif l == 1:
            list.append(1)
            
        # else add the sum of the two previous
        # numbers in the sequence
        else:
            # eg. list[3] = list[0] + list[1] = 1
            fib_value = list[l-2] + list[l-1]
            list.append(fib_value)
    # once the loop is finished, return the list        
    return list

# here you'll notice an Out[#]: because it's being computed
# as an output
#get_fib_series(get_series_length())

# next, we'll create a function that can display the
# sequence to the user

# initiate function name
def display_fib_series(fib_numbers):
    # for each number in the created list of 
    # fibonacci numbers, print them to the user
    for nums in fib_numbers:
        print(nums)

# unlike the above example, here we won't see the out[]:
# this is because our function has printed the list
#display_fib_series(get_fib_series(get_series_length()))

# finally we'll write a function that will put them
# all together. this will allow the program to be run 
# by calling a simple function as opposed to imbedding
# them each time.

def main():
    series_length = get_series_length()
    series = get_fib_series(series_length)
    display_fib_series(series)

main()