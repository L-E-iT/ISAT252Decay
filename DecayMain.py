#
# Programmer: Brian Elliott, Taylor Boyd
# Started DATE, Last Updated DATE
# Language: Python 3.4, PyCharm Editor
#

# Importing various modules and packages needed for the program
import math
import DecayClass
import time
import scipy
import numpy
import matplotlib


def main():  # defining the main function of the program
    half_phosphorus = 14.262  # days
    half_chromium = 27.7025  # days
    disposal_constant = 37.00  # disposal constant of the radioactive isotopes
    decay_constant = 0.693  # decay constant of the radioactive isotope
    isotope, mass, percent, initial_activity, percent_mass = get_info()
    # setting various variables by calling the get_info function
    days_to_decay = days_decay(half_phosphorus, half_chromium, disposal_constant, decay_constant,
                               # finding the days to decay of the chosen isotope
                               isotope, initial_activity, percent_mass)
    print(format(days_to_decay, ',.2f'))  # printing out the days for testing
    safe_activity = safe(isotope, initial_activity, decay_constant, days_to_decay, half_phosphorus,
                         half_chromium)  # Calculating the safe activity level for the isotope
    print(format(safe_activity, ',.2f'))  # printing out the safe activity for testing
    activity = activity_level(decay_constant, half_chromium, half_phosphorus, initial_activity, safe_activity,
                              isotope)  # finding the activity of the isotope each day until it reaches its safe level
    print(activity)  # printing out the safe activity for testing


def get_info():  # Function to get various variables for the program
    isotope = (DecayClass.Decay().get_isotope())  # getting the isotop name from the decayclass file
    mass = (DecayClass.Decay().get_mass())  # getting the mass in kg
    percent = (DecayClass.Decay().get_percent())  # getting the percent of the mass made up by the isotope
    initial_activity = (DecayClass.Decay().get_activity())  # the intial activity of the radioactive isotope in kBq
    percent_mass = mass * percent  # simple math to find the mass of the radioactive isotope

    return isotope, mass, percent, initial_activity, percent_mass  # returning values for use in the program


def days_decay(half_phosphorus, half_chromium, disposal_constant, decay_constant,
               isotope, initial_activity, percent_mass):  # finding the days that it takes for the isotope to decay
    print(percent_mass)  # printing percent mass for testing
    if isotope == "Chromium-51":  # checking for the isotope type
        days_to_decay = -(half_chromium / decay_constant) * math.log(
            disposal_constant / (
                initial_activity / percent_mass))
        # code to solve for the number of days it will take for the isotope to decay
        return days_to_decay  # returning the value
    if isotope == "Phosphorus-32":  # same code as above for the phosphorus isotope
        days_to_decay = -(half_phosphorus / decay_constant) * math.log(
            disposal_constant / (initial_activity / percent_mass))
        return days_to_decay


def safe(isotope, initial_activity, decay_constant, days_to_decay, half_phosphorus,
         half_chromium):  # finding the safe level of the isotope for each isotope
    if isotope == "Chromium-51":  # checking for the isotope type
        safe_activity_level = initial_activity * math.exp(
            -((decay_constant * days_to_decay) / half_chromium))  # solving for the safe activity level of the isotope
        return safe_activity_level  # returning the safe activity level of the isotope
    if isotope == "Phosphorus-32":  # same code as above for phosphorus
        safe_activity_level = initial_activity * math.exp(-((decay_constant * days_to_decay) / half_phosphorus))
        return safe_activity_level


def activity_level(decay_constant, half_chromium, half_phosphorus, initial_activity, safe_activity,
                   isotope):  # function to compute the activity level of the isotope over days
    activity = initial_activity  # setting initial activity
    activity_list = [format(activity, ',.2f')]  # preparing a list to store the activity level data
    if isotope == "Chromium-51":  # checking the isotope type
        while activity > safe_activity:  # while the activity is greater than the safe activity level, run this code
            activity *= math.exp(
                -(decay_constant / half_chromium))  # set the activity equal to the decay of the previous days activity
            activity_list.append(
                format(activity, ',.2f'))  # adding that days activity to the activity list and formatting it
        return activity_list  # returning the activity list
    if isotope == "Phosphorus-32":  # same as above for the phosphorus isotope
        while activity > safe_activity:
            activity *= math.exp(-(decay_constant / half_phosphorus))
            activity_list.append(format(activity, ',.2f'))
        return activity_list


main()  # calling the main function to run the program