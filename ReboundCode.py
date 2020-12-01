# ---- Author/Instructor: Samantha Lawler ---- #
# ---- CoAuthor/Student: Mriana Yadkoo ---- #
# ---- Student Email: mriana.saeed1997@gmail.com / May99@uregina.ca ---- #
# ---- Copyrights: Fall 2020 ---- #

# Used Modulars
import numpy as np
import rebound
import sys

# Conversion tools
deg2rad = np.pi/180.0
rad2deg = 180.0/np.pi

# User to call the test particals files by using terminal, each file takes a one argument
runnum = int(sys.argv[1])

# ############################## Run Simulation ############################## #
sim = rebound.Simulation()

sim.move_to_com()

# Number of years to simulate
sim_length = 1e7 # you can also multiply by 2.*np.pi

# Set integrator type
sim.integrator = "whfast"
sim.integrator_whfast_safe_mode = 0
sim.whfast_corrector = 11

# Set simulation time variables
sim.dt = 0.5*2.*np.pi
sim.t = 0
Noutputs = 1000 # 1000 or 10000 or 100000.... which is the number of outputs (time steps) for different timing (number of divisions)
times = np.linspace(0, sim_length, Noutputs)  # Length of simulation (start, end, number of divisions)
# ############################# Adding Planets and Test Particles ############################## #
# Sun
sim.add(m=1, x=0., y=0., z=0.)
# Jupiter Barycenter 2021-01-01
sim.add(
    m=1/1047.3486,
    a=5.186248776397993E+00,
    e=4.823236893843078E-02,
    omega=2.752984816928482E+02*deg2rad,
    inc=1.303422338076160E+00*deg2rad,
    Omega=1.005033409512034E+02*deg2rad,
    M=2.959307755201842E+02*deg2rad
    )
# Saturn Barycenter 2021-01-01
sim.add(
    m=1/3497.898,
    a=9.534117213133813E+00,
    e=5.521891270197320E-02,
    omega=3.389549467947007E+02*deg2rad,
    inc=2.488013281059568E+00*deg2rad,
    Omega=1.135948607848353E+02*deg2rad,
    M=2.141554644391900E+02*deg2rad
    )
# Uranus Barycenter 2021-01-01
sim.add(
    m=1/22902.98,
    a=1.918807165506669E+01,
    e=4.730464485303179E-02,
    omega=9.707780440344314E+01*deg2rad,
    inc=7.721279748238701E-01*deg2rad,
    Omega=7.400324737552683E+01*deg2rad,
    M=2.321388820122650E+02*deg2rad
    )
# Neptune Barycenter 2021-01-01
sim.add(
    m=1/19412.24,
    a=3.007444132979245E+01,
    e=8.747220233002007E-03,
    omega=2.724435538782596E+02*deg2rad,
    inc=1.770224289360134E+00*deg2rad,
    Omega=1.317826858858846E+02*deg2rad,
    M=3.065367266197209E+02*deg2rad
    )
# Reading the TestParticles files
Index, time, a, e, inc, Omega, omega, M = np.genfromtxt('TestParticle' + str(runnum) + '.in', unpack=True)
PN = 4      # Number of Test Particles
TPN = 1000  # Number of Test Particles + Planets (for index checking)
for i in np.arange(0, len(a)):
    sim.add(m=0, a=a[i], e=e[i], inc=inc[i]*deg2rad, Omega=Omega[i]*deg2rad, omega=omega[i]*deg2rad, M=M[i]*deg2rad)

# ############################# Write to file + compute the orbital elements ############################ #
file1 = open('pl' + str(runnum) + '.out', 'w')
file1.write("# Note: All angles` numerical data are in Degrees.")
file1.write("\n")
file1.write("# time, index, a, e, inc, Omega, omega, M, l: ")
file1.write("\n")
file2 = open('tp' + str(runnum) + '.out', 'w')
file2.write("# Note: All angles` numerical data are in Degrees.")
file2.write("\n")
file2.write("# time, index, a, e, inc, Omega, omega, M, l: ")
file2.write("\n")
file3 = open('LN.out', 'w')
file3.write("# Note: All angles` numerical data are in Degrees.")
file3.write("\n")
file3.write("# time, index, a, e,  inc, Omega, omega, M, lN: ")
file3.write("\n")
for j, time in enumerate(times):
    sim.integrate(time, exact_finish_time=0)
    orbits = sim.calculate_orbits()
    for k in np.arange(0, PN):
        a = orbits[k].a
        e = orbits[k].e
        inc = orbits[k].inc
        Omega = orbits[k].Omega
        omega = orbits[k].omega
        M = orbits[k].M
        MeanLong = orbits[k].l
        file1.write('%1.1f \t %4.0f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \n' % (time, k, a, e, inc*rad2deg, Omega*rad2deg%360, omega*rad2deg%360, M*rad2deg%360, MeanLong*rad2deg%360))
    for k in np.arange(0, TPN):
        a = orbits[k + PN].a
        e = orbits[k + PN].e
        inc = orbits[k + PN].inc
        Omega = orbits[k + PN].Omega
        omega = orbits[k +PN].omega
        M = orbits[k + PN].M
        MeanLong = orbits[k + PN].l
        file2.write('%1.1f \t %4.0f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \n' % (time, k, a, e, inc*rad2deg, Omega*rad2deg%360, omega*rad2deg%360, M*rad2deg%360, MeanLong*rad2deg%360))
    for k in np.arange(0, 1):
        a = orbits[k + 3].a
        e = orbits[k + 3].e
        inc = orbits[k + 3].inc
        Omega = orbits[k + 3].Omega
        omega = orbits[k + 3].omega
        M = orbits[k + 3].M
        MeanLong = orbits[k + 3].l
        file3.write('%1.1f \t %4.0f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \t %1.15f \n' % (time, k, a, e, inc*rad2deg, Omega*rad2deg%360, omega*rad2deg%360, M*rad2deg%360, MeanLong*rad2deg%360))
file1.close()
file2.close()
file3.close()
# ############################### Save the orbital elements data to .bin files ############################## #
sim.save('Simulation' + str(runnum) + '.bin')
