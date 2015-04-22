#
# Programmer: Brian Elliott, Taylor Boyd
# Started DATE, Last Updated DATE
# Language: Python 3.4, PyCharm Editor
#

class Decay:

    def __init__(self):
        self.__isotope = "isotope" # name of the isotope that is being investigated
        self.__mass = 0 # mass of material containing the radioactive isotope
        self.__percent = 0 # percent of the weight that is made up by the isotope
        self.__initial_activity = 0 # Initial radioactivity of the material
        self.__half_phosphorus = 14.262 # days
        self.__half_chromium = 27.7025 # days
        self.__disposal_constant = 37.00 # disposal constant of the radioactive isotopes
        self.__decay_constant = 0.693 # decay constant of the radioactive isotope

    def activity_per_dat(self):
        print("Placeholder for equation")

    def get_info(self):
        self.__isotope = str(input("Are we investigating\n- Phosphorus-32\nor\n- Chromium-51\n"))
        return self.__isotope

