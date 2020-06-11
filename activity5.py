# Name: Yaow Hui Chong
# Course Name: ISQA3900 - 850
# Date: 06/08/2020
# Descriptiion: This program allows users to read from and write to an .csv file and also manually input
#

import csv


def read_csv():
    try:
        file = input("Enter the csv filename containing trip data: ")
        with open(file) as csvfile:
            trip_read = csv.reader(csvfile, delimiter=',')
            print("Trips:")
            i = 1
            for row in trip_read:

                print(str(i) + ". Miles: " + (row[0]) + "     Gallons of Gas: " + str(row[1]) + "       Mpg: " + str(row[2]))
                i += 1
    except FileNotFoundError:
        print("Trips not read from file - file not found: ", file)

def write_csv():
    with open(file, 'w', newline='') as csvfile:
        trip_write = csv.writer(csvfile, delimeter=' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        for i in range (0, len(trip)):
            trip_write.writerow(trip[i])
        print()
        print("Trips saved to file: trips.csv")

# display a title

print("The Miles Per Gallon program")
print()


read = str(input("Would you like to read trips from a file? (y/n): "))
if read.lower() == "y":
    read_csv()

    choice = str(input("Would you like to enter trip data? (y/n): "))
    if choice.lower() == "y":
        try:
            miles_driven= float(input("Enter miles driven:\t\t"))
            gallons_used = float(input("Enter gallons of gas used:\t"))
            mpg = miles_driven / gallons_used
            mpg = round(mpg, 2)
            trip =[miles_driven, gallons_used, mpg]
            trip.append([miles_driven, gallons_used, mpg])
            i = 0
            for i in range(0, len(trip)):
                print(str(i + 1) + ". Miles: " + (trip[int(i)].miles_driven) + "     Gallons of Gas: " + str(trip[int(i)].gallons_used) + "       Mpg: " + str(trip[int(i)].mpg) + "\n")
                i += 1
            print()
        except ValueError:
            print("Enter numeric values only. Try again.")


    cont = str(input("Would you like to continue? (y/n): "))
    while cont.lower() == "y":
        try:
            miles_driven= float(input("Enter miles driven:\t\t"))
            gallons_used = float(input("Enter gallons of gas used:\t"))
            mpg = miles_driven / gallons_used
            mpg = round(mpg, 2)
            trip = trip.append([miles_driven, gallons_used, mpg])
            for i in range(0, len(trip)):
                print.row(str(i+1) + ". Miles: " + str(trip[i][miles_driven]) + "     Gallons of Gas: " + str(
                    trip[i][gallons_used]) + "       Mpg: " + str(trip[i][mpg]))

        except ValueError:
            print("Enter numeric values only. Try again.")

    print()
    write.csv()

else:
    print("Bye")