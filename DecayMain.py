#
# Programmer: Brian Elliott, Taylor Boyd
# Started DATE, Last Updated DATE
# Language: Python 3.4, PyCharm Editor
#

import DecayClass

def main():
    RadioDecay = DecayClass.Decay()
    get_info()


def get_info():
    print(DecayClass.Decay().get_isotope())
    print(DecayClass.Decay().get_mass(),"kg")
    print(DecayClass.Decay().get_percent(),"percent in decimal")
    print(DecayClass.Decay().get_activity(),"kBq")


main()