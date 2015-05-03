# Programmer: Brian Elliott, Taylor Boyd
# Started DATE, Last Updated 4/29/15
# Language: Python 3.4, PyCharm Editor

# Importing various modules and packages needed for the program
import math
import DecayClass
import time as time
import matplotlib.pyplot as plt
import sys


def main():  # defining the main function of the program
    choice = input("\nWelcome to the Radioactive Decay Modeling program!\n"
                   "This program will plot the decay per day of the\n"
                   "Phosphorus-32 and the Chromium-51 Isotopes until\n"
                   "They each a safe activity level!\n"
                   "If you would like to model one of the isotopes,\n"
                   "simply enter any value except 1 or press 'Enter'\n"
                   "If you would like to exit this program, input 1\n"
                   "\n"
                   "Made By: Brian Elliott and Taylor Byrd\n"
                   "=====================\n"
                   "Enter Decision: ")
    if choice == "1":
        sys.exit(0)
    half_phosphorus = 14.262  # days
    half_chromium = 27.7025  # days
    disposal_constant = 37.00  # disposal constant of the radioactive isotopes
    decay_constant = 0.693  # decay constant of the radioactive isotope
    isotope, mass, percent, initial_activity, percent_mass = get_info()
    # setting various variables by calling the get_info function
    days_to_decay = GetDays(half_phosphorus, half_chromium, disposal_constant, decay_constant,
                               # finding the days to decay of the chosen isotope
                               isotope, initial_activity, percent_mass)
    safe_activity = Safe_Activity_Level(isotope, initial_activity, decay_constant, days_to_decay, half_phosphorus,
                         half_chromium)  # Calculating the safe activity level for the isotope
    activity, counter = NewIsotopeActivity(decay_constant, half_chromium, half_phosphorus, initial_activity, safe_activity,
                                       isotope)
    # finding the activity of the isotope each day until it reaches its safe level

    check = True  # starting boolean decision structure for data validation
    while check:  # validation check
        plot_choice = input("Please Enter 1 to plot your decay automatically, or 2 to process manual decay\n"
                            "=====================\n"
                            "Enter Decision: ")  # Asking user if they would rather use automatic or manual decay
        if plot_choice == "1":  # check users method choice
            auto_plot(counter, activity)  # calls the auto decay function
            check = False  # fixes validation
        if plot_choice == "2":  # Does the same as the first check for the manual function
            manual_plot(counter, activity)
            check = False


def get_info():  # Function to get various variables for the program
    isotope = (DecayClass.Decay().get_isotope())  # getting the isotop name from the decayclass file
    mass = (DecayClass.Decay().get_mass())  # getting the mass in kg
    percent = (DecayClass.Decay().get_percent())  # getting the percent of the mass made up by the isotope
    initial_activity = (DecayClass.Decay().get_activity())  # the intial activity of the radioactive isotope in kBq
    percent_mass = mass * percent  # simple math to find the mass of the radioactive isotope

    return isotope, mass, percent, initial_activity, percent_mass  # returning values for use in the program


def GetDays(half_phosphorus, half_chromium, disposal_constant, decay_constant,
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


def Safe_Activity_Level(isotope, initial_activity, decay_constant, days_to_decay, half_phosphorus,
         half_chromium):  # finding the safe level of the isotope for each isotope
    if isotope == "Chromium-51":  # checking for the isotope type
        safe_activity_level = initial_activity * math.exp(
            -((decay_constant * days_to_decay) / half_chromium))  # solving for the safe activity level of the isotope
        return safe_activity_level  # returning the safe activity level of the isotope
    if isotope == "Phosphorus-32":  # same code as above for phosphorus
        safe_activity_level = initial_activity * math.exp(-((decay_constant * days_to_decay) / half_phosphorus))
        return safe_activity_level


def NewIsotopeActivity(decay_constant, half_chromium, half_phosphorus, initial_activity, safe_activity,
                   isotope):  # function to compute the activity level of the isotope over days
    activity = float(initial_activity)  # setting initial activity
    counter = 1
    counter_list = [1]
    activity_list = [activity]  # preparing a list to store the activity level data
    if isotope == "Chromium-51":  # checking the isotope type
        while activity > safe_activity:  # while the activity is greater than the safe activity level, run this code
            activity *= math.exp(
                -(decay_constant / half_chromium))  # set the activity equal to the decay of the previous days activity
            activity_list.append(
                activity)  # adding that days activity to the activity list and formatting it
            counter += 1
            counter_list.append(int(counter))
        return activity_list, counter_list  # returning the activity list
    if isotope == "Phosphorus-32":  # same as above for the phosphorus isotope
        while activity > safe_activity:
            activity *= math.exp(-(decay_constant / half_phosphorus))
            activity_list.append(activity)
            counter += 1
            counter_list.append(int(counter))
        return activity_list, counter_list


def auto_plot(counter, activity):
    plt.ion()  # needed to haave the decay appear on the graph over time
    for i in range(max(counter)):  # looping through the day count
        plt.bar(counter[i], activity[i])  # update the data with the radioactivity level at the counter day
        plt.title('Radioactive Isotope Decay Per Day')  # setting the title for the plot
        plt.xlabel('Day')  # setting the x-axis title
        plt.ylabel('Radioactivity in kBq')  # setting the y-axis title
        plt.draw()  # redraw the canvas with the new values
        time.sleep(0.1)  # tell the graph to wait this long in seconds before continuing with a new bar
    plt.ioff()  # turning off the auto editing system.
    plt.show()  # display the finished graph to the user
    print("Final Activity\t\tTime For Safe Disposal")
    print(format(min(activity),',.2f'),"kBq", "\t\t\t",max(counter), "Days")
    final_check()



def manual_plot(counter, activity):
    print("Press 'Enter' to process the isotope decay manually.\n"
          "Each time you press 'Enter', a day of decay will be simulated\n"
          "=====================\n")
    n = 0
    while n <= (max(counter) - 1):
        pause = input()
        print("At day", counter[n], "The radioactivity of your isotope is:\n"
              , activity[n], "kBq")
        n += 1

    print("Final Activity\t\tTime For Safe Disposal")
    print(format(min(activity),',.2f'),"kBq", "\t\t\t",max(counter), "Days")
    final_check()


def final_check():
    final = input("\nThank you for using our program! If you would like to run another model\n"
                  "please input 1 below, if you would like to exit, enter any value or just\n"
                  "press 'Enter'\n"
                  "=====================\n"
                  "Enter Decision: ")
    if final == "1":
        main()
    else:
        sys.exit(0)


main()  # calling the main function to run the program