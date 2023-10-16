# in terminal, navigate to the file folder
# type python3
# type "from functions_practice import hello" to import the function
# type "hello()" to run the function
def hello():
    print("Hello, Earthling!")



# in terminal, navigate to the file folder
# type python3
# type "from functions_practice import pack" to import the function
# type "my_pack = pack("pb&j", "kettle chips", "green tea")" to call the function with some sample arguments and store the result in a variable called my_pack
# Type "print(my_pack)" to print the contents of the my_pack variable.
def pack(sandwich, chips, drink):
    print("I am packing a", sandwich, "some", chips, "and a", drink)
    return[sandwich, chips, drink]



# in terminal, navigate to the file folder
# type python3
# type "from functions_practice import eat_lunch" to import the function

# what's for lunch? define my lunch items and then eat_lunch>>>
# type "my_lunch = ["sandwich", "chips", "apple"]" and then "eat_lunch(my_lunch)" to call the function with some sample arguments 
# ~or~
# type "eat_lunch(["apple", "sandwich", "chips", "drink"])" to call the function with some sample arguments

# "My lunchbox is empty!"
# call it separately with an empty array "empty_lunch = []", then the lunchbox is empty: "eat_lunch(empty_lunch)""
# ~or~
# oh no! an empty lunchbox! type "eat_lunch([])" to skip lunch.

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print("First I eat the", lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I eat", item)