import random
import sys
def validate_email(email_id): 
    # Function to validate the email id
    """this function will check the main id"""
    if (email_id.count("@") == 1) and (len(email_id[:email_id.index("@")]) >= 2) and (email_id[email_id.index("@")+1:] == "pop.ac.uk"):
        return True

def extract_name(email_id): # Function to extract the name from the email id
    return email_id[:email_id.index("@")].capitalize()

def check_network_error(): # Function to create network crash
    """this function is used for erroe""" 
    if random.choice([i for i in range(10)]) == 1:
        print("*** NETWORK ERROR ***")
        raise AssertionError


def list_of_data(data):
    """this function is used to store tha data in list"""
    list_1 = ("The library is closed today.")
    if data == 1:
        return list_1
    list_2 =  ("WiFi is excellent across the campus.")
    if data == 2:
        return list_2
    list_3 = ("Your deadline has been extended by two working da")
    if data == 3:
        return list_3
    list_4= ("Teekee is open until 9 PM this morning.")
    if data == 4:
        return list_4
    list_5 =("Hmm.", "Oh, yes, I see.", "Tell me more", "Mmmm.", "Yes", "You should try woking on this system.", "That is interesting")
    if data == 5 :
        return random.choice(list_5)     


def answering(answer):
    if "library" in answer.lower():
        print(list_of_data(1))

    elif "wifi" in answer.lower():
        print(list_of_data(2))

    elif "deadline" in answer.lower():
        print(list_of_data(3))

    elif "coffee" in answer.lower():
        print(list_of_data(4))

    elif "fee" in answer.lower():
        print(list_of_data(5)) 
   
    elif any(char in answer.lower() for char in ["bye", "exit", "goodbye", "help"]):
        exit()

    else:
        print(list_of_data(5))
print("Welcome to our Pop Chat \nOne of our operators will be pleased to help you today.\n")
email_id = input("Please enter your Poppleton email address: ")
validate_email(email_id)
if validate_email(email_id) != True:
    sys.exit("{} is invalid at pop.ac.uk. \nPlease Try Again! \nExiting........".format(email_id))

Operator_Name = random.choice(["kabin","Siri", "Google", "Shayam", "Depsnon", "loki"])
name = extract_name(email_id)
print("Hi, {}! Thank you, and Welcome to PopChat! \nMy name is {}, and it will be my pleasure to help you.".format(name, Operator_Name))

def greeting(name):
    sys.exit("Thanks, {}, for using PopChat. See you again soon!".format(name))

while True:
    try:
        check_network_error()

        answer = input("---> ")
        answering(answer)

    except AssertionError as e:
        greeting(name)  

