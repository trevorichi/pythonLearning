isRunning = True

def print_welcome():
    print("Welcome to the Capsule Hotel!")
    return input("\nHow many capsules are available today?: ")

def print_menu():
    print("1. Check In")
    print("2. Check Out")
    print("3. View Guests")
    print("4. Exit")
    
num_of_capsules = print_welcome()
num_of_capsules = int(num_of_capsules)

capsules = [None] * num_of_capsules

def check_in():
    print("Guest Check In")
    print("==========================\n\n")
    guest_name = input("Enter your name: ")
    
    capsule_number = int(input("Capsule # [1-" + str(num_of_capsules)+"]"))
    
    if capsules[capsule_number-1] == None:
        capsules[capsule_number-1] = guest_name
        print("Success :)")
        print(guest_name + " is booked in capsule #" + str(capsule_number))
    else:
        print("Sorry that is taken\n\n")
        
    
def check_out():
    print("Guest Check Out")
    print("==========================\n\n")
    capsule_being_checked_out = int(input("Capsule # [1-100]: "))
    if capsules[capsule_being_checked_out-1] == None:
        print("Error :(, that capsule is unoccupied")
    elif capsules[capsule_being_checked_out-1] != None:
        print("Success, checkout complete")
        capsules[capsule_being_checked_out-1] = None
    else:
        print("Unknown Error, trev u a dumbo")
    
    
     
def view_guests():
    for i in range(len(capsules)):
        print(str(i) + ":" + str(capsules[i]))



print("There are currently " + str(num_of_capsules) + " capsules available! \n")

while(isRunning):
    
    print_menu()        
    choice = int(input("\nWhat would you like to do?[1-4]: "))
        
    if choice==1:
        check_in()
    elif choice==2:
        check_out()
    elif choice==3:
        view_guests()
    elif choice==4:
        print("Goodbye!")
        isRunning = False
        
  
    
    
    
    
    