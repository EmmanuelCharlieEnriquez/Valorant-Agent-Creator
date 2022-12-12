name = []
skills = []
role = []
weapon = []

def menu():
    print("\n--------------------------")
    print("|    Welcome Player!     |")
    print("--------------------------")
    print("1. Create Agent")
    print("2. View Agent")
    print("3. Delete Agent")
    print("4. Update Agent")
    print("5. Exit")

def create():
    a_name = input("What is your Agents Name? : ")
    a_skills = input("What Skill do you like to have your Agent? : ")
    a_role = input("What is your Agents Role? : ")
    a_weapon = input("What is your agents weapon? : ")
    
    name.append(a_name)
    skills.append(a_skills)
    role.append(a_role)
    weapon.append(a_weapon)
    print("\nInput SuccessFully!")
    
def view():
    if len(name) == 0:
        print("\nNo Data To View!")
    else:
     for i in range(len(name)):       
        print("\n",[i], "\nName: ",name[i], "\nSkills: ",skills[i], "\nRole: ", role[i], "\nWeapon: ", weapon[i])
        
def delete():
    if len(name) == 0:
        print("\nNo Data Available!")
    else:
        view()
        index = int(input("\nEnter Index To Delete: "))
        del name[index]
        del skills[index]
        del role[index]
        del weapon[index]
        print("\nSuccessfully Deleted!")

def update():
    if len(name) == 0:
        print("\nNo Data Available!")
    else:
        view()
        print()
        index = int(input("Enter Index that you want to Update: "))
        name[index] = input("Enter New Agent Name: ")
        skills[index] = input("Enter New Agent Skill: ")
        role[index] = input("Enter new Agent Role: ")
        weapon[index] = input("Enter new Weapon: ")
        print("\nSuccessfully Updated.")
        
menu()
option = int(input("\nEnter choice: "))

while option != 5:
    if option == 1:
        create()
    
    elif option == 2:
        view()
        
    elif option == 3:
        delete()
        
    elif option == 4:
        update()
        
    elif option == 5:
        exit
        
    else:
        print("Invalid Input!")
        
    menu()
    option = int(input("Enter choice: "))