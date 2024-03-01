# Develop a user-friendly program that acts as an address book. The program should have the following functionalities:
# 1. Upon starting the program, create an empty dictionary to store names and addresses.
# 2. Allow the user to add people to the address book. For each entry, prompt the user to input a name and its corresponding address. Store these as key-value pairs in the dictionary.
# 3. Provide a clear and straightforward menu for the user, including options to add a new entry or quit the program.
# 4. Implement a loop that allows users to continue adding entries until they explicitly choose to quit.
# 5. When the user decides to quit, break out of the loop and display the collected information. Print out the names and addresses of everyone in the address book in a well-formatted manner.
# 6. Consider adding error handling to handle unexpected inputs gracefully. For instance, if the user provides invalid input when prompted for a name or address, handle the error and ask for the information again.
# 7. Provide a user-friendly and informative message when the program terminates, summarizing the data entered and thanking the user for using the address book.


d1 = {} # create an empty dictionary

def show_dict():
    print("Thank you for contributing to Adonai's Address Book!\nHere is what you've added this time:")
    for key in d1:
        print(f'{name}: {address}')
# ask the user what they would like to do and loop back to question
while True: 
    option = input("What would you like to do? Add/Quit ")
    if option == "Add":
        name = input("Enter Name: ")
        address = input("Enter {name}'s Address: ")
        d1[name] = address
    elif option == "Quit":
        if not d1:
            print("You never even used my Adress Book bro...")
        else:
            show_dict()
    break
#not sure why 



person1 = {'09:00', '10:30', '11:30', '12:00', '13:00', '14:30'}
person2 = {'09:30', '10:00', '10:30', '12:00', '14:30', '16:00'}
person3 = {'09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00'}
person4 = {'11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00'}
# Available Times: '12:00' and '14:30'

avail_time: []
    
def sim_time(*people):
    while element in *people:
        for time in *people:
            i == i
            avail_time.append()