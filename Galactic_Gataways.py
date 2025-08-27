print("test print")
print("second test print")
print("Lim is bad")
print("yes")


print("poo")
import random
import datetime
def force_number(message, lower, upper):
    while True:#infinite loop
        try:
            num = int(input(message))
            if num >= lower and num <= upper:#sets a condition for the number
                break#beaks loop is condition above is met
            else:
                print("Error, Invalid number")
        except:
            print("Error, only type in numbers")
    return num
def force_name(message, lower, upper):
    while True: #infinite loop
        name = str(input(message)).title()#asking for users name and storing it capitalising the first letter
        if len(name) >= lower and len(name) <= upper and name.isalpha():  #sets a condition for the name 
            break#beaks loop is condition above is met
        else:
            print("Invalid name")
    return name#returns a valid name back to veriable
def force_cellphone_number(message, lower, upper):
    while True:#infinite loop
        cell = str(input(message))
        if len(cell) >= lower and len(cell) <= upper and cell.isnumeric():#sets a condition for the cellphone number
            break#beaks loop is condition above is met
        else:
            print(f"ERROR! Please enter between a {lower} - {upper}")
    return cell
def main_menu():
    destination_names = ['Mars Colonization Mission','Jupiter Moon Excursion (Europa)','Saturn Rings Cruise','Venus Cloud City Tour']
    print("Welcome to Galactic Getaways!")
    while True:
        print("Please select a destination from the following options:\n1. Mars Colonization Mission\n2. Jupiter Moon Excursion (Europan)\n3. Saturn Rings Cruise\n4. Venus Cloud City Tour\n0. Exit")
        choice = force_number("Please enter your choice:", 1, 4)
        if choice <= 1 and choice >= 4:
            booking_destination = destination_names[choice - 1]
            return booking_destination, choice
        else:
            break
    date_time = datetime.datetime.now()
    first_name = force_name("Please enter your first name: ", 2, 15)
    last_name = force_name("Please enter your last name: ",0, 28)   
    cellphone_nunber = force_cellphone_number("Please enter your phone number:",9,12)
    random_num = random.randint(1000, 9999)
    booking_codes = ['MAR','EUR','SAT','VEN'] 
    unique_code = booking_codes[choice - 1] + str(random_num)
    print("*** Confirmed Booking***")
    print(f"First Name: {first_name}")
    print(f"Last Name:  {last_name}")
    print(f"Cellphone Number: {cellphone_nunber}")
    print(f"Destination: {destination_names[choice - 1]}")
    print(f"Booking code: {unique_code}")
    print(f"Date and time of booking: {date_time}")
    print("*** End of Confirmed Booking ***") 
    outFile=open("booking_confirmation.txt", "w")
    outFile.write(f"First name: {first_name}\n")
    outFile.write(f"Last name: {last_name}\n")
    outFile.write(f"Phone number: {cellphone_nunber}\n")
    outFile.write(f"Booking code: {unique_code}\n")
    outFile.write(f"Date of booking:{date_time}")
    outFile.close()
    print("PROGRAM ENDS****")
main_menu()









        
