#
# Programmer: Brian Elliott, Taylor Boyd
# Started DATE, Last Updated DATE
# Language: Python 3.4, PyCharm Editor
#


import scipy
import numpy
import matplotlib
import math
import time


class Decay:
    def __init__(self):  # initializing variables for use
        self.__isotope = "isotope"  # name of the isotope that is being investigated
        self.__mass = 0  # mass of material containing the radioactive isotope
        self.__percent = 0  # percent of the weight that is made up by the isotope
        self.__initial_activity = 0  # Initial radioactivity of the material

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

    def get_percent(self):  # gets the percent of the mass made up by the isotope
        check = 0  # set up check for the percent check
        while check == 0:  # check statement for the percentage input
            try:  # error handling for the percent input
                self.__percent = float(input("What is the total percent mass of the material made up by the isotope?\n"
                                             "(in decimal percent, ex: 1 = 100%, .5 = 50%)\n"
                                             "====================\n"
                                             "Enter Value: "))
                # Input statement for the percent value of the percent mass of the material from the isotope
            except Exception as Err:
                print("An unexpected value was entered\n",
                      Err)  # trap and print error if applicable
            else:  # executes if there is no error
                if self.__percent > 0:  # checks the the percentage given is greater than 0
                    check = 1  # adjusts check so that it will not run again
        return self.__percent  # returns the percent to the main program in decimal format

    def get_activity(self):  # gets the initial radioactivity of the isotope in kBq's, should be positive
        check = 0  # sets up the check
        while check == 0:  # sets up the while loop for the check
            try:  # starting the try/except error catch
                self.__initial_activity = float(input("What is the initial radioactivity of the isotope?\n"
                                                      "(In kBq)\n"
                                                      "====================\n"
                                                      "Enter Value: "))
                # Input for the initial activity from the user
            except Exception as Err:  # checks to make sure the input was valid and so the program will not crash
                print("An unexpected value was entered\n",
                      Err)  # inform user if the program has crashed
            else:  # if there was no error
                if self.__initial_activity > 0:  # checking to make sure the value entered was above 0
                    check = 1  # set check to 1 to stop loop
        return self.__initial_activity  # return the initial activity value

