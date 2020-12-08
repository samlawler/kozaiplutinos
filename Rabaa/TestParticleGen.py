__author__ = "Rabaa"
__copyright__ = "Copyright 2020"
__version__ = "1.0.1"
__maintainer__ = "Rabaa"
__email__ = "beborabaa@gmail.com"

import sys
import numpy as np
import random


NumberOfFiles = 10 # Number of files the user wants, could be modified

# Class: TestParticle
# Functions: Default Constructor, GenerateData, GetData
class TestParticle:
    def __init__(self):  # Attributes defined
        self.SemiMajorAxis = 0
        self.Eccentricity = 0
        self.Inclination = 0
        self.Ω = 0
        self.ω = 0
        self.M = 0

    # GenerateData:
    # Expects: Nothing
    # Will do: Set Random values within the Kozai Resonance range to the 6 orbital elements attributes with 9 figures
    def GenerateData(self):
        # Getting SMA
        Numerator = random.randint(38442157982, 40442157982)
        Denominator = 1000000000
        self.SemiMajorAxis =  Numerator / Denominator

        # Getting Eccentricity
        Numerator = random.randint(0, 700000000)
        Denominator = 1000000000
        self.Eccentricity = Numerator / Denominator

        # Getting Inclination
        Numerator = random.randint(0, 90000000000)
        Denominator = 1000000000
        self.Inclination = Numerator / Denominator

        # Getting Libration Amplitude
        Numerator = random.randint(0, 90000000000)
        Denominator = 1000000000
        LibrationAmp = Numerator / Denominator

        # Getting phi
        Numerator = random.randint(0, 1000000000)
        Denominator = 1000000000
        RandomNumber = Numerator / Denominator

        Φ = np.pi + np.sin(2.*np.pi*RandomNumber)*LibrationAmp

        # Getting Mean Anomaly
        Numerator = random.randint(0, 360000000000)
        Denominator = 1000000000
        Numerator = random.randint(0, 1000000000)
        Denominator = 1000000000
        Ran = Numerator / Denominator
        self.M = Ran * 2. * 2. * np.pi * 180. / np.pi

        # Getting Ascending Node
        Numerator = random.randint(0, 360000000000)
        Denominator = 1000000000
        self.Ω = 0  # Numerator / Denominator

        #Getting omega
        λN = 350.7630  # λN as of 1 Jan 2021
        self.ω = (1./float(2) * ((Φ * (180. / np.pi)) - float(3) * self.M) - self.Ω + λN) % ((2.*np.pi) * 180. / np.pi)
    # GetData:
    # Expects: Nothing
    # Will do: Orders the 6 Attribute elements preceeded by 0.0, indicating the start time ot testparticles in a string format, and return it to the caller function
    def GetData(self):
         #  Data =  str(self.SemiMajorAxis) + " " + str(self.Eccentricity) + " " + str(
         #     self.Inclination) + " " + str(self.Ω) + " " + str(self.ω) + " " + str(self.M % 360)
        Data = str(0.0) + " " + str(self.SemiMajorAxis) + " " + str(self.Eccentricity) + " " + str(self.Inclination) + " " + str(self.Ω) + " " + str(self.ω) + " " + str(self.M % 360)
        return Data

# Main
if __name__ == '__main__':
    NumberOfData = sys.argv[1] # User to specify the number of the Test Particles he wants the code to create

    file = 0
    for file in np.arange(1, NumberOfFiles + 1): # Will create the number of files the user chooses
        TextFile = open("TestParticle" + str(file) + ".in", "w") # Creating a file 
        TextFile.write("# TP  Time  Semi-major-Axis  Eccentricity  Inclination  Omega  omeaga  M" + "\n")
        line = 0
        while line < int(NumberOfData):
            TestParticle20 = TestParticle() # Create the test particle
            TestParticle20.GenerateData() # Generate the fine tuned random data
            Data = TestParticle20.GetData() # get the string of attributes into "Data" variable
            TextFile.write(str(line) + " " + str(Data) + '\n') # Write the data into the file
            line += 1

