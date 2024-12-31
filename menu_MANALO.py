import os


username = input("Please enter your name: ")  
print(f"Hi there, {username}!")  
#ASK THE USER FOR THE PROGRAM
start_prog = input("Would you like to initiate the program? YES/NO: ")  

#SHOW THE MENU
def show_menu():
    print("-------------------------------------------------------------------------------------------------")
    print(f"Greetings, {username}! WELCOME to PYTHON PRINT FUNCTION DEMONSTRATION")
    print("Ang print() command ay ginagamit para magpakita ng mensahe o data sa screen.")
    print("")    
    print("\t\t\t----OPTIONS FOR PRINTING IN PYTHON----\t\t\t")
    print("\t\t\t1. BASIC PRINT USAGE")
    print("\t\t\t2. STRING CONCATENATION IN PRINTING")  
    print("\t\t\t0. RETURN TO MAIN MENU")  
    
#FUNCTION DEMONSTRATING SOMETGING SOMETHING
def basic_printing():
    print("DEMONSTRATION:")
    print("")
    print("\tINTRO TO PYTHON")
    print("\tSPORTS")
    print("\tSOCIAL RESPONSIBILITY")
    print("")
    print("CODE EXAMPLE:")
    print("")
    print('\tprint("INTRO TO PYTHON")')
    print('\tprint("SPORTS")')    
    print('\tprint("SOCIAL RESPONSIBILITY")')
    print("0. Back")  #BACK AGAIN

#STRING
def string_concat_print():
    print("Pagsasama ng mga variable x at y sa bagong variable na z:")
    print("DEMONSTRATION:")
    print("")
    print("\tPythonRocks")
    print("")
    print("CODE EXAMPLE:")
    print("")
    print('\tx = "Python"')
    print('\ty = "Rocks"')
    print("\tz = x + y")
    print("\n0. Back")  #BACK TO MENU

#MENU FOR VARIABLES
def variable_menu():
    print("Ang mga variable ay ginagamit para mag-imbak ng data sa Python.")
    print("Awtomatikong gumagawa ang Python ng variable kapag nag-assign ka ng value dito.")
    print("")
    print("\t---------------------------------------------------")
    print("\t\t\tVARIABLES MENU")
    print("")
    print("\t1. STRING CONCATENATION WITH VARIABLES")  
    print("\t2. EXPLANATION OF VARIABLES")  
    print("\t0. RETURN TO MAIN") 


def add_numbers():
    num1 = eval(input("Input the first number: ")) 
    num2 = eval(input("Input the second number: "))  
    print(num1, " + ", num2, " = ", num1 + num2)   

#FUNCTION
def variable_explanation():
    print("CODE EXAMPLE:")
    print("")
    print('num1 = eval(input("Input the first number: "))')
    print('num2 = eval(input("Input the second number: "))') 
    print('print(num1," + ", num2," = ", num1 + num2)')  #SHOW RESULTS

#MAIN PROGRAM
continue_program = True
if start_prog.lower() == "yes":
    while continue_program:
        os.system('cls') 
        print("--------MAIN MENU-------")
        print("1. PRINTING IN PYTHON")  
        print("2. VARIABLES IN PYTHON")  
        print("3. EXIT")  
        print("------------------------")
        user_choice = input("Select an option by entering its number: ")  
        
        if user_choice == "1":
            while True:
                os.system('cls')
                show_menu()  #MENU SA PRINT
                printing_option = input("Choose a printing topic: ")
            
                if printing_option == "0":  #BALIK SA MENU
                    break
                elif printing_option == "1":  #BASIC PRINT
                    os.system('cls')
                    basic_printing()
                    back_option = input("Press Enter to go back: ")
                
                elif printing_option == "2":  #CONCATENATION
                    os.system('cls')
                    string_concat_print()
                    back_option = input("Press Enter to go back: ")
                else:
                    print("Invalid choice, try again.")  #PAG MALI YUNG INPUT

        elif user_choice == "2":
            while True:  
                os.system('cls')
                variable_menu()  #SHOW MENU IN VARIABLES
                variable_option = input("Select a number for more details: ")
                
                if variable_option == "1":  #HOW TO USE VARIABLES
                    os.system('cls')
                    add_numbers()
                    back_option = input("Press Enter to go back: ")
                
                elif variable_option == "2":  #EXPLAINATION
                    os.system('cls')
                    variable_explanation()
                    back_option = input("Press Enter to go back: ")
                
                elif variable_option == "0":  #BACK TO MENU
                    break

        elif user_choice == "3":  #EXIT
            print("Exiting the program. Goodbye!")
            continue_program = False
        else:
            print("Invalid input, please try again.")  #PAG MALI YUNG INPUT
else:
    print("Program not initiated.")  #IF DI NAG SSTART YUNG PROGRAM