__author__ = "Rabaa"
__copyright__ = "Copyright 2020"
__version__ = "1.0.1"
__maintainer__ = "Rabaa"
__email__ = "beborabaa@gmail.com"

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
from os import path




NumberOfFiles = 500 # Number of files the code will read from, could be modified

# Function: DrawGraph
# Expects: Nothing
# Will do: Draw graph consisting of all test particles from the sequential files or test particles, that came from ResonanceCheck
def DrawGraph():
    Index0, SMA0, Ecc0, Inc0, Node0, ArgPeri0, MeanAnom0, Name0, AverageSMA0, AverageEcc0, AverageInc0, LibrationCenter0, LibrationAmp0, KozaiCenter0, KozaiAmp0 = np.genfromtxt(
                "Num_1_500ktp_TPCheck_1.out", unpack=True) # Reading the first file


    for file in range(2,NumberOfFiles + 1): # reading and appending all other files to the first attributes
        if (path.exists("Num_1_500ktp_TPCheck_" + str(file + 1) + ".out")):
            Index1, SMA1, Ecc1, Inc1, Node1, ArgPeri1, MeanAnom1, Name1, AverageSMA1, AverageEcc1, AverageInc1, LibrationCenter1, LibrationAmp1, KozaiCenter1, KozaiAmp1 = np.genfromtxt(
                "Num_1_500ktp_TPCheck_" + str(file + 1) + ".out", unpack=True)
            Index0 = np.append(Index0, Index1)
            SMA0 = np.append(SMA0, SMA1)
            Ecc0 = np.append(Ecc0, Ecc1)
            Inc0 = np.append(Inc0, Inc1)
            Node0 = np.append(Node0, Node1)
            ArgPeri0 = np.append(ArgPeri0, ArgPeri1)
            MeanAnom0 = np.append(MeanAnom0, MeanAnom1)
            Name0 = np.append(Name0, Name1)
            AverageSMA0 = np.append(AverageSMA0, AverageSMA1)
            AverageEcc0 = np.append(AverageEcc0, AverageEcc1)
            AverageInc0 = np.append(AverageInc0, AverageInc1)
            LibrationCenter0 = np.append(LibrationCenter0, LibrationCenter1)
            LibrationAmp0 = np.append(LibrationAmp0, LibrationAmp1)
            KozaiCenter0 = np.append(KozaiCenter0, KozaiCenter1)
            KozaiAmp0 = np.append(KozaiAmp0, KozaiAmp1)


    IsItKozai = np.zeros(len(Index0)) + 1 # Array of the status of each test particle. "0": Not Resonance, "1": Resonance but not Kozai, "2": Resonance and Kozai

    for i in range(0, len(Index0)):
        if (LibrationCenter0[i] == -999) | (LibrationCenter0[i] == 0):
            LibrationCenter0[i] = False
            IsItKozai[i] = 0
        else:
            LibrationCenter0[i] = True
            IsItKozai[i] = 1
        if (KozaiCenter0[i] == -999) | (KozaiCenter0[i] == 0):
            KozaiCenter0[i] = False
        else:
            KozaiCenter0[i] = True
            IsItKozai[i] = 2


    print(len(Index0)) # Will print the number of overall test particles examined by the code
    sns.set_style('dark')
    palette = sns.color_palette("mako", as_cmap=True)
    sns.set_palette("dark", 10)
    sns.relplot(x=SMA0, y=Ecc0, hue=IsItKozai, style=IsItKozai, size=IsItKozai, sizes=(40, 10))
    plt.show() # Show the graph

# Main function
if __name__ == '__main__':
    DrawGraph()
