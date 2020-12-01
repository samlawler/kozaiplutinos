# ---- Author/Instructor: Samantha Lawler ---- #
# ---- CoAuthor/Student: Mriana Yadkoo ---- #
# ---- Student Email: mriana.saeed1997@gmail.com / May699@uregina.ca ---- #
# ---- Copyrights: Fall 2020 ---- #

# Used Modules
import numpy as np
import rebound
import sys

# Conversion tools
deg2rad = np.pi / 180.0  # (degrees to radians)
rad2deg = 180.0 / np.pi  # (radians to degrees)

# User to call the test particals files by using terminal, each file takes a one argument
runnum = int(sys.argv[1])

# Hint: The binary files and the check files contain similar test particles orbital elements,
# 	but except the binary files have the planets` orbital elements as the first four indices,
# 	and we need to remove them in order to do the comparesion.

# ############################# Adding Planets and Test Particles By Reading Binary Files (.bin)  ############################## #

sim = rebound.Simulation()
sim = rebound.Simulation("Num4_Binary_" + str(runnum) + ".bin")
PN = 4  # Number of Planets
orbits = sim.calculate_orbits()
# 1000 is the number of test particles wanted from a one .bin file, and we use "k+PN" to remove the planets,
# if you want to include the number of planets use 1004, and "k".
for k in np.arange(0, 1000):
    a = orbits[k + PN].a
    e = orbits[k + PN].e
    inc = orbits[k + PN].inc
    Omega = orbits[k + PN].Omega
    omega = orbits[k + PN].omega
    M = orbits[k + PN].M
    MeanLong = orbits[k + PN].l

# ########################## Read in the Resonance Check files ######################################## #

Index, SMA, Ecc, Inc, Node, ArgPeri, MeanAnom, Name, AverageSMA, AverageEcc, AverageInc, LibrationCenter, LibrationAmp, KozaiCenter, KozaiAmp = np.genfromtxt(
    "Num4_TPCheck_" + str(runnum) + ".out", unpack=True)

# ########################## Write out the test particles that are in resonance with Neptune ######################################## #

file = open('Num4_Resonance_' + str(runnum) + '.out', 'w')
file.write("# Note: All angles` numerical data are in Degrees.")
file.write("\n")
file.write("# Index, a, e, inc, Omega, omega, M, l: ")
file.write("\n")

# Hint: from the following loop we want to remove any test particle from the .bin files
#	that is not in resonance by comparing the indices of each test particle form the two files,
#	then if a test particle from the check files has one of the libration center, LibrationAmp,
#	KozaiCenter, KozaiAmp to be equal to the value of '-999'we will remove it and don`t include
#	it in the .out files.

for i in np.arange(0, 1000):
    if LibrationCenter[i] != -999 or LibrationAmp[i] != -999 or KozaiCenter[i] != -999 or KozaiAmp[i] != -999:
        a = orbits[i + PN].a
        e = orbits[i + PN].e
        inc = orbits[i + PN].inc
        Omega = orbits[i + PN].Omega
        omega = orbits[i + PN].omega
        M = orbits[i + PN].M
        MeanLong = orbits[i + PN].l
        file.write('%4.0f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \n' % (
        i, a, e, inc * rad2deg, Omega * rad2deg % 360, omega * rad2deg % 360, M * rad2deg % 360,
        MeanLong * rad2deg % 360))
file.close()





