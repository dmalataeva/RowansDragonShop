'''
Name: Deniza Malataeva
Date: January 14, 2015
Description: A dragon pet store.
> allows to enter as customer or administrator
> protected shopkeeper account
> allows the shopkeeper to change price and position (sold\on sale)
> allows shopkeepers to add/remove pets from the database
> shopkeepers can also view animals that are unavailable to the general public
> presents details on the shop's profit
> saves all data to file UPON PROPER EXIT
> can view a list of animals, as well as divide them by species
> allows customers to view information about a pet and its diet + say 'hello' to it
> gives information about the differences between 3 main species
Known Issues: when inputting an action choice in certain menus, the program cannot process strings,
thus mistakes or deliberate mistyping will bring up an error.
'''

# IMPORTANT INFORMATION!!! ========================<>

# Shopkeeper login:
# CadburyRowan

# Shopkeeper password:
# flightfright

#===================================================================================================

#------------------------------------------<<<<IMPORTS>>>>------------------------------------------
from RowansClass import Pet
import os
#---------------------------------------------------------------------------------------------------

# opens the database file to extract total number of pets
file=open("Database.txt","r")
dragoncount=int(file.readline()) # this number will be used multiple times throughout the program
file.close() # later procedures with the file will require a different file mode so we close it
# also prevents the file from damage in event of unexpected program crash

#-----------------------------------------<<<<FUNCTIONS>>>>-----------------------------------------

def Shopkeeper(): # called upon entering shopkeeper account
    cls()
    print("Login:")
    login=input()
    cls()
    print("Password:")
    password=input()
    if login=="CadburyRowan" and password=="flightfright":
        account=True
    else:
        account=False
    return account #returns boolean variable stating if shopkeeper is verified

def cls(): # made for the most convenience
    os.system ('cls')

def leave(file): # called upon exiting the shop
    cls()
    print("We hope you are satisfied with our service and wide range of goods.")
    print("Please come back again!")
    input()
    file.close() #closes file
    exit()       

def petsdata(dragoncount): # main function which extracts data from Database.txt
    fileline=[]            # and converts it into instances in an array
    dragon=[]
    file=open("Database.txt")
    dragoncount=int(file.readline()) 
    for i in range (0,dragoncount):
        fileline.append(file.readline())
        fileline[i]=fileline[i].split("*")
        fc=10
        for word in fileline[i]:
            if fc==10:
                name=word
                fc=fc-1
            elif fc==9:
                species=word
                fc=fc-1
            elif fc==8:
                breed=word
                fc=fc-1
            elif fc==7:
                gender=word
                fc=fc-1
            elif fc==6:
                age=word
                fc=fc-1
            elif fc==5:
                origin=word
                fc=fc-1
            elif fc==4:
                diet=word
                fc=fc-1
            elif fc==3:
                hostility=word
                fc=fc-1
            elif fc==2:
                price=word
                fc=fc-1
            elif fc==1:
                sold=word.rstrip("\n") # gets rid of the 'next line' char
                fc=fc-1
        dragon.append(Pet(name,species,breed,gender,age,origin,diet,hostility,price,sold))  
    file.close()
    return dragon #returns a ready array
            
def listallpets(dragon,dragoncount,listtype): # prints out a list of pets based on a category (or attribute)
    if listtype==1: #pets on sale
        for i in range (0,dragoncount):
            if (dragon[i].getSold())=="Y":
                print(dragon[i].getName())        
    elif listtype==2: #dragons
        for i in range (0,dragoncount):
            if (dragon[i].getSpecies())=="dragon":
                print(dragon[i].getName())
    elif listtype==3: #wyverns
        for i in range (0,dragoncount):
            if (dragon[i].getSpecies())=="wyvern":
                print(dragon[i].getName())
    elif listtype==4: #drakes
        for i in range (0,dragoncount):
            if (dragon[i].getSpecies())=="drake":
                print(dragon[i].getName()) 
    elif listtype==5: #all pets
        for i in range (0,dragoncount):
            print(i+1,">",dragon[i].getName())
    elif listtype==6: #sold
        for i in range (0,dragoncount):
            if (dragon[i].getSold())=="N":
                print(dragon[i].getName())
    
def talk(dragon,dragoncount,i): #identifies species of pet and corresponding response
        if dragon[i].getSpecies()=="dragon":
            cls()
            print("~~Rr-rr-r-rawrg!")
            print("Translation:'hi!'")
            print()
            input("Continue...")
        elif dragon[i].getSpecies()=="wyvern":
            cls()
            print("~~Wree-argh!")
            print("Translation:'sup?'")
            print()
            input("Continue...")
        elif dragon[i].getSpecies()=="drake":
            cls()
            print("~~Kraa-a-aokh!")
            print("Translation:'ha!'")
            print()
            input("Continue...") 
        else: #in case of a mistake
            cls()
            print("Pet species unrecognised. Translator not working.")
            print()
            print("Continue...")    

def profit(dragon,dragoncount,listtype): # calculates and presents a number for profits
    total=float(0)
    if listtype==1: # total estimated profit
        for i in range (0,dragoncount):
            amount=(dragon[i].getPrice())
            amount=float(amount)
            total=total+amount
    elif listtype==2: # profit from not yet sold animals
        for i in range (0,dragoncount):
            if dragon[i].getSold()=="Y":
                amount=(str(dragon[i].getPrice()))
                amount=float(amount)
                total=total+amount
    elif listtype==3: # existing profit
        for i in range (0,dragoncount):
            if dragon[i].getSold()=="N":
                amount=(str(dragon[i].getPrice()))
                amount=float(amount)
                total=total+amount   
    return total #returns a single float number


#-------------------------------------------<<<<MAIN>>>>--------------------------------------------

print("Hello and welcome to Cadbury Rowan's Dragon Shop!")
print("Here is where you can buy your very own tamable dragon!")
print()
print()
input("Continue...")
while True: # convenient way of returning
    cls()
    print("Please select one of the following actions:")
    print()
    print("1) enter as customer")
    print("2) enter as administrator")
    print("3) exit")
    choice=input()
    if choice=="":
        None
    elif int(choice)==1:
        person=1
        break
    elif int(choice)==2:
        account=Shopkeeper() #verification
        cls()
        if account==True:
            print("Welcome back Mr. Rowan.")
            input("Continue...")
            person=2
            break
        else:
            print("The system does not recognize the self-proclaimed administrator.")
    elif int(choice)==3:
        leave(file)
        
dragon=[]
dragon=petsdata(dragoncount) # initializes databas

if person==1: # CUSTOMER      
    while True: # convenient way of returning
        cls()
        print("The shop currently sells drakes, wyverns and ancient dragons.")
        print("To find out more about the difference between these, enter '?'.")
        print("To find out more about a pet just enter its name (case sensitive!)")
        print("To exit the shop enter '!'.")
        print()
        listtype=1
        listallpets(dragon,dragoncount,listtype)
        choice=input()
        if choice=="":
            None
        elif choice=="!":
            leave(file)
        elif choice=="?": # lists pets according to their species
            cls()
            print("What are drakes,wyverns and ancient dragons (or wyrms)?")
            print()
            print("Dragons are magical reptiles that can fly and often are larger than the average human.")
            print("The first dragon was tamed thousands of years ago, so the species are often called 'ancient wyrms'.")
            print("Dragons often possess magical abilities and a unique colour,")
            print("according to the natural element they were born in. Most can breathe fire.")
            print("Of the three, ancient wyrms develop a distinct attitude and outstanding intelligence.")
            print("Here is a list of dragons currently available:")
            listtype=2
            listallpets(dragon,dragoncount,listtype)
            print()
            print("Wyverns are slender, snake-like magical reptiles that are drawn to shiny things.")
            print("Not seldom wyverns are known to guard mountains of treasure.")
            print("They have cold bodies and are smaller than dragons.")
            print("Here is a list of wyverns currently available:")
            listtype=3
            listallpets(dragon,dragoncount,listtype)
            print()
            print("Drakes are the smallest of the three, but are also the most violent.")
            print("Most breeds are two-legged and have small wings.")
            print("Drakes do not have magical powers. Instead, they possess a tough shell,")
            print("which makes them a good option for riding into battle.")
            print("Here is a list of drakes currently available:")
            listtype=4
            listallpets(dragon,dragoncount,listtype)
            print()
            print("Nonetheless, the term 'dragon' is used interchangeably and worldwide.")
            input("Continue...")
        else: # brings up all information about pet (if it is on sale)
            cls()
            for i in range (0,dragoncount):
                if dragon[i].getName()==choice:
                    dragon[i].AboutMe()
                    print()
                    print(dragon[i].Diet())
                    print()
                    print("If you want to say hi to our pet, please enter 'speak'!")
                    more=input("Continue...")
                    if str(more)=="speak":
                        talk(dragon,dragoncount,i)
                    
                
elif person==2: # SHOPKEEPER
    while True: # convenient way of returning
        cls()
        print("What would you like to do today?")
        print()
        print("1) manage pets")
        print("2) view accounting details")
        print("3) exit")
        choice=input()
        if choice=="":
            None
        elif int(choice)==3:
            leave(file)
        elif int(choice)==1:
            while True: # convenient way of returning
                cls()
                print("To show pets currently on sale enter '1'.")
                print("To show sold pets enter '2'.")
                print("To change data enter '3'.")
                print("To go back enter '!'.")
                print()
                listtype=5
                listallpets(dragon,dragoncount,listtype)
                choice=input()
                if choice=="":
                    None
                elif choice=="!":
                    break
                elif int(choice)==1:
                    cls()
                    print("On sale:")
                    listtype=1
                    listallpets(dragon,dragoncount,listtype)
                    print()
                    input("Continue...")
                elif int(choice)==2:
                    cls()
                    print("Already sold:")
                    listtype=6
                    listallpets(dragon,dragoncount,listtype)
                    print()
                    input("Continue...")
                elif int(choice)==3:
                    cls()
                    print("To change a pet's shop position or price, enter 'change'.")
                    print("If you want to eliminate a pet from the shop's database forever,")
                    print("please enter 'goodbye'.")
                    print("However, if you want to add a completely new member to the family, please enter 'new'.")
                    print()
                    entry=input()
                    if entry=="goodbye":
                        cls()
                        print("Which pet do you want to eliminate?")
                        delete=input()
                        for i in range (0,dragoncount):
                            if dragon[i].getName()==delete:
                                dragon.pop(i)
                                dragoncount=dragoncount-1
                                break
                        file=open("Database.txt","w") # re-writes file without eliminated pet
                        file.write(str(dragoncount)+"\n")
                        for i in range (0,dragoncount):
                            line=(str(dragon[i].getName())+"*"+str(dragon[i].getSpecies())+"*"+str(dragon[i].getBreed())+"*"+str(dragon[i].getGender())+"*"+str(dragon[i].getAge())+"*"+str(dragon[i].getOrigin())+"*"+str(dragon[i].getDiet())+"*"+str(dragon[i].getHostility())+"*"+str(dragon[i].getPrice())+"*"+str(dragon[i].getSold()))
                            file.write(line+"\n")
                        file.close()
                        cls()
                        print("Farewell. We will miss",delete,".")
                        input("Continue...")
                    elif entry=="new":
                        cls()
                        print("Please enter a name:")
                        name=input()
                        cls()
                        print("Now enter the reptile's species:")
                        species=input()
                        cls()
                        print("Its breed:")
                        breed=input()
                        cls()
                        print("Whether its male or female:")
                        gender=input()
                        cls()
                        print("How old is this pet:")
                        age=input()
                        cls()
                        print("Where is he/she brought from:")
                        origin=input()
                        cls()
                        print("Common diet items:")
                        diet=input()
                        cls()
                        print("Hostility rate from 1 to 10:")
                        hostility=input()
                        cls()
                        print("Price for this fella:")
                        price=input()
                        cls()
                        print("And finally, is he/she available for sale ('Y' or 'N'):")
                        sold=input()
                        dragon.append(Pet(name,species,breed,gender,age,origin,diet,hostility,price,sold))
                        dragoncount=dragoncount+1
                        file=open("Database.txt","w")
                        file.write (str(dragoncount)+"\n") # re-writes file with newly added pet
                        for i in range (0,dragoncount):
                            line=(str(dragon[i].getName())+"*"+str(dragon[i].getSpecies())+"*"+str(dragon[i].getBreed())+"*"+str(dragon[i].getGender())+"*"+str(dragon[i].getAge())+"*"+str(dragon[i].getOrigin())+"*"+str(dragon[i].getDiet())+"*"+str(dragon[i].getHostility())+"*"+str(dragon[i].getPrice())+"*"+str(dragon[i].getSold()))
                            file.write(line+"\n")
                        file.close()
                        cls()
                        input("Let us welcome an addition!")
                    elif entry=="change":
                        cls()
                        print("To change an existing pet's position in the shop")
                        print("simply enter its name and new position. (on sale = 'Y', already sold = 'N')")
                        print()
                        print("For example, 'Smaug Y'.")
                        print("We do not have Smaug in our shop by the way.")
                        print()
                        print("Otherwise, to change its price, again, enter its name and new price.")
                        print("'Smaug 1000000'")
                        print("Sorry, Tolkien.")
                        print()
                        entrychange=input()
                        entrypos=[]
                        entrypos=entrychange.split()
                        if entrypos[1]=="Y" or entrypos[1]=="N":
                            for i in range (0,dragoncount):
                                if dragon[i].getName()==entrypos[0]:
                                    dragon[i].sold=entrypos[1]
                                    break
                            cls()
                            print("Position of",entrypos[0],"successfully changed to",entrypos[1],".")
                        else:
                            for i in range (0,dragoncount):
                                if dragon[i].getName()==entrypos[0]:
                                    dragon[i].price=entrypos[1]
                                    break
                            cls()
                            print("Price of",entrypos[0],"successfully changed to",entrypos[1],".")
                        file=open("Database.txt","w")
                        file.write (str(dragoncount)+"\n") # re-writes file to save all changes
                        for i in range (0,dragoncount):
                            line=(str(dragon[i].getName())+"*"+str(dragon[i].getSpecies())+"*"+str(dragon[i].getBreed())+"*"+str(dragon[i].getGender())+"*"+str(dragon[i].getAge())+"*"+str(dragon[i].getOrigin())+"*"+str(dragon[i].getDiet())+"*"+str(dragon[i].getHostility())+"*"+str(dragon[i].getPrice())+"*"+str(dragon[i].getSold()))
                            file.write(line+"\n")  
                        file.close()
                        print()
                        input("Continue...")
                        
        elif int(choice)==2:
            cls()
            print("Pets sold:")
            listtype=6
            listallpets(dragon,dragoncount,listtype)
            print()
            print("Pets on sale:")
            listtype=1
            listallpets(dragon,dragoncount,listtype)
            print()
            print("Profit:")
            print("From sold dragons:")
            listtype=3
            print(str(profit(dragon,dragoncount,listtype)))
            print("From dragons to be sold:")
            listtype=2
            print(str(profit(dragon,dragoncount,listtype)))
            print("TOTAL:")
            listtype=1
            print(str(profit(dragon,dragoncount,listtype)))   
            print()
            input("Continue...")

#===================================================================================================

# Dragon species and references taken from:
# http://dragcave.wikia.com/wiki/Dragon_Types

# With special help from:
# Mr. Rivard
# https://docs.python.org/3/
# http://stackoverflow.com/

#===================================================================================================
