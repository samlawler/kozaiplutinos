# ---- Author/Instructor: Samantha Lawler ---- #
# ---- CoAuthor/Student: Mriana Yadkoo ---- #
# ---- Student Email: mriana.saeed1997@gmail.com / May699@uregina.ca ---- #
# ---- Copyrights: Fall 2020 ---- #

# Used Modules
import numpy as np
import rebound

# Conversion tools
deg2rad = np.pi/180.0  # (degrees to radians)
rad2deg = 180.0/np.pi  # (radians to degrees)

# ############################# Adding Planets and Test Particles By Reading Binary Files (.bin) ############################## #

sim = rebound.Simulation()
sim = rebound.Simulation("Simulationb.bin")

# ############################# Write to files + Compute the orbital elements ############################ #

file = open('BinsTest.out', 'w')
file.write("# Note: All angles` numerical data are in Degrees.")
file.write("\n")
file.write("#index, a, e,  inc, Omega, omega, M, l: ")
file.write("\n")
orbits = sim.calculate_orbits()
# 1000 is the number of test particles in a one .bin file,
# if the files contain test particles and the four giant planets use 1004.
for k in np.arange(0, 1004):
    a = orbits[k].a
    e = orbits[k].e
    inc = orbits[k].inc
    Omega = orbits[k].Omega
    omega = orbits[k].omega
    M = orbits[k].M
    MeanLong = orbits[k].l
    file.write('%4.0f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \n'%(k, a, e, inc*rad2deg, Omega*rad2deg%360, omega*rad2deg%360, M*rad2deg%360, MeanLong*rad2deg%360))
file.close()
