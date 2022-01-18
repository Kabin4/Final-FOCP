from math import radians
from statistics import mean
print("Swallow Speed Analysis: Version 1.0")
reading_list = [] # List for storing the readings
while True:
        reading = input("Enter the Next Reading : ")  # asking to inter the data
        if reading == "":
            break

        elif "E" in reading.upper(): # changing the alphabet into upper case 
            reading_in_km = float(reading[1:]) # slicing the inital value of the enter data and converting into float 
            reading_in_miles = reading_in_km 
            reading_list.append(reading_in_miles)
            print("Reding saved")

        elif "U" in reading.upper():
            reading_in_miles  = float(reading[1:]) # slicing the inital value of the enter data and converting into float 
            reading_in_km = reading_in_miles * 1.60934
            reading_list.append(reading_in_km)  # entering the data inside the empty list
            print("Reding saved")
        else:
            print("wrong input")    
if reading_list == []:
    print("No readings entered. Nothing to do.")
    
else :
    max_reading_km = max(reading_list)
    min_reading_km = min(reading_list)
    avg_reading_in_km = mean(reading_list)

    max_reading_mile = max(reading_list)/1.61
    min_reading_mile = min(reading_list)/1.61
    avg_reading_mile = mean(reading_list)/1.61
    print("\nResults Summary")

    print("%d Reading analyzed"%(len(reading_list))  
    if len(reading_list) <=1 
    else "%d Readings analyzed.\n"%(len(reading_list)))

    print(f"Max Reading : {max_reading_mile:.1f} MPH, {max_reading_km:.1f} KPH")
    print(f"Min Reading : {min_reading_mile:.1f} MPH, {min_reading_km:.1f} KPH")
    print(f"Average Reading : {avg_reading_mile:.1f} MPH, {avg_reading_in_km:.1f} KPH")