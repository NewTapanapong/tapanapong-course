"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    person = ("tapanapong", 19, "sattahip", "chonburi")  
    hobbies = []
    while True:
        print("Tnformation")
        print("Name:",person[0])
        print('age: ',person[1])
        print('city: ',person[2])
        print('country: ',person[3])
        print("hobbies: ",hobbies)
        print('1,Add new hobbies 2,Remove hobbies 3,Update age 4,thank you')
        x = int(input('you pass choice'))     

        if x==1:
            hobbi = input("You hobbies")
            hobbies.append(hobbi)
        elif x==2:
            del hobbies[0]
        elif x==3:
            age= int(input("Insert new age"))
            person_list = list(person)
            person_list[1] = age
            person = tuple(person_list)
        elif x==4:
            print('thank you')
            break


if __name__ == "__main__":
    personal_info_manager()