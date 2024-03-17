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
    for k in d1:
        print(f'Name: {k} Address: {d1[k]}')
        
    # ask the user what they would like to do and loop back to question
while True: 
    option = input("What would you like to do? Add/Quit ")
    # if add option
    if option == "Add" or option == "add":
        #add name & address
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        d1[name] = address
        # if quit option
    elif option == "Quit" or option == "quit":
        #solve error or show updates
        break
        
if not d1:
    print("You never even used my Adress Book bro..")
else: 
    print(show_dict())








# EXCERCISE 2



# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a set of times they are available ('HH:MM' 24-hour). Create a function that will take in any number of sets of available times (*remember \*args*) and return a set of times where everyone can meet.

person1 = {'09:00', '10:30', '11:30', '12:00', '13:00', '14:30'}
person2 = {'09:30', '10:00', '10:30', '12:00', '14:30', '16:00'}
person3 = {'09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00'}
person4 = {'11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00'}
# Available Times: '12:00' and '14:30'

    
# create an empty list of available times to meet
# avail_time: []


#create a function
def sim_time(*people):
    #empty set
    empty_set = set()
    # looping through index of people for length of tuple  
    for index in range(len(people)):
        # index is the first 
        if index == 0:
            #add to set as base comparison
            empty_set = people[index]
        # otherwise
        else:
            #compare our set with the rest of set
            empty_set = empty_set & people[index]
    return empty_set
            
print(sim_time(person1, person2, person3, person4))