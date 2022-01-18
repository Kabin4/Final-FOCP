print("Stop! Who would cross the Bridge of Death! Must answer me these questions three, 'ere the other side he see.")
Extract_name = input("What is your name? \n") # asking the first question

if Extract_name.capitalize() == "Arthur": # checking wether the name is kings name or not 
    print("My liege! You may pass!")
else:
    get_quest = input("What is your quest? \n ")  # asking the third question

    if "grail" in get_quest.lower(): # changing the get_quest in to lower form and using in function to check wether the word contin grail or not 
        get_colour = input("What is your favourite colour? \n ")

        if get_colour[0].capitalize() == Extract_name[0].upper(): # checking the first alphabet of the name and color   
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of the Eternal Peril.")

    else :
        print("Only those who seek the Grail may pass.")
    
