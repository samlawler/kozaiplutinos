import sys
import numpy as np
import random


class TestParticle:
    def __init__(self):  # Attributes defined
        self.SemiMajorAxis = 0
        self.Eccentricity = 0
        self.Inclination = 0
        self.Ω = 0
        self.ω = 0
        self.M = 0


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

    def GetData(self):
         #  Data =  str(self.SemiMajorAxis) + " " + str(self.Eccentricity) + " " + str(
         #     self.Inclination) + " " + str(self.Ω) + " " + str(self.ω) + " " + str(self.M % 360)
        Data = str(0.0) + " " + str(self.SemiMajorAxis) + " " + str(self.Eccentricity) + " " + str(self.Inclination) + " " + str(self.Ω) + " " + str(self.ω) + " " + str(self.M % 360)
        return Data


if __name__ == '__main__':
    NumberOfData = sys.argv[1]

    file = 0
    for file in np.arange(1, 11):
        TextFile = open("TestParticle" + str(file) + ".in", "w")
        TextFile.write("# TP  Time  Semi-major-Axis  Eccentricity  Inclination  Omega  omeaga  M" + "\n")
        line = 0
        while line < int(NumberOfData):
            TestParticle20 = TestParticle()
            TestParticle20.GenerateData()
            Data = TestParticle20.GetData()
            TextFile.write(str(line) + " " + str(Data) + '\n')
            line += 1

