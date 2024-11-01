#calculator
def calculator():

    import math
    operator = input("Enter a operator ('+', '-', '/', '*'): ")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))

    def addition():
        if operator == "+":
            sum_of_input = num1 + num2
            print(f"The sum is {sum_of_input}")

    def subtraction():
        if operator == "-":
            subtract_result = num1 - num2
            print(f"The result of your subtaction is {subtract_result}")

    def multiplication():
        if operator == "*":
            multiply_results = num1 * num2
            print(f"Your multiplication resulted in {multiply_results}")

    def division():
        if operator == "/" :
            if num2 > 0:
                divided = num1 / num2
                print(f"Your diviison resulted in {divided}")
        elif num2 == "0":
            print("You cant divide by zero...sorry try again")
            



        
    addition()
    subtraction()
    multiplication()
    division()

calculator()

#shopping list 
your_list = []

def add_to_shoppin_list():
    needed_items = input("What is needed?: ")
    your_list.append(needed_items)
def print_list():
    formated_list = "\n".join(your_list)
    print("\nYour Shopping List:")
    print(formated_list)
def remove_from_list():
   while True:
    remove_it = input("Would you like to remove last item or add another item?: ")
    if remove_it in ["yes", "y", "1", "Yes", "YES"]:
       if your_list:
          your_list.pop()
          print("Last item removed.")
       else:
          print("The list may be empty")
    elif remove_it in ["no", "n", "2", "add"]:
       add_to_shoppin_list()
       ready_to_print = input("Ready to print your list")
    if ready_to_print in ["yes", "y", "1","Yes", "YES"]:
       print_list()
       
    are_you_done = input("Are you done with your list")
    if are_you_done in  ["yes", "y", "1","Yes", "YES"]:
       break
    elif are_you_done in ["no", "n", "2", "No"]:
       add_to_shoppin_list()





add_to_shoppin_list()
remove_from_list()
print_list()