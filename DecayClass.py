#
# Programmer: Brian Elliott, Taylor Boyd
# Started DATE, Last Updated DATE
# Language: Python 3.4, PyCharm Editor
#


import scipy
import numpy
import matplotlib


class Decay:
    def __init__(self):  # initializing variables for use
        self.__isotope = "isotope"  # name of the isotope that is being investigated
        self.__mass = 0  # mass of material containing the radioactive isotope
        self.__percent = 0  # percent of the weight that is made up by the isotope
        self.__initial_activity = 0  # Initial radioactivity of the material
        self.__half_phosphorus = 14.262  # days
        self.__half_chromium = 27.7025  # days
        self.__disposal_constant = 37.00  # disposal constant of the radioactive isotopes
        self.__decay_constant = 0.693  # decay constant of the radioactive isotope

    def activity_per_day(self):  # will contain all mathematical calculations for finding half life
        print("Placeholder for equation")  # placeholder for equations

    def get_isotope(self):  # gets the name of the isotope
        self.__isotope = str(input("Are we investigating\n- Phosphorus-32\nor\n- Chromium-51\n"
                                   "=====================\n"
                                   "Enter Name: "))  # asks for user input for the isotopse
        while self.__isotope != "Phosphorus-32" and self.__isotope != "Chromium-51":
            # checks for the isotope given to match
            self.__isotope = str(input("That is not a valid input, Please choose either\n"
                                       "- Phosphorus-32\nor\n- Chromium-51\n"
                                       "=====================\n"
                                       "Enter Name: "))
        else:  # returns the isotope value to the main file to be displayed to the user
            return self.__isotope

    def get_mass(self):  # Obtaining the total mass of the isotope and material
        check = 0  # check set to loop through the try and except
        while check == 0:
            try:  # start the try
                self.__mass = float(  # Getting the mass input from the user
                    input(
                        "What is the total mass on the material and isotope that we are investigating?\n"
                        "(in kg)\n"
                        "=====================\n"
                        "Enter Value: "))
            except Exception as Err:  # trapping error if the user inputs a invalid input
                print("An unexpected value was entered\n",
                      Err)  # printing error to user
            else:  # if the number is valid, check if greater than 0
                if self.__mass > 0:
                    check = 1  # adjust check to stop the while loop
        return self.__mass  # return the user input value for mass

    def get_percent(self):
        print("placeholder")