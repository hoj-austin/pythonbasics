"""
Scipt for playing with classes - Object Oriented Programming
"""

class Aircraft: # because planes and helicopters are awesome
    airspace = 'troposphere' #class variable shared in all instances

    def __init__(self, wingType, hours, vne, passengers):
        self.wingType = wingType
        self.hours = hours
        self.vne = vne #Vne is the never exceed velocity - don't fly your plane faster than this!
        self.passengers = passengers

    def aircraftType(self):
        if self.wingType == 'rotary':
           print('The aircraft is a helicopter')
        elif self.wingType == 'fixed':
            print('The aircraft is an aeroplane')
        else: 
            print('The aircraft type is unknown')

    # def maintenance