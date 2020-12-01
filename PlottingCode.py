# ---- Instructor: Samantha Lawler ----#
# ---- Auther: Lowell Peltier ---------#
# ---- CoAuther: Mriana Yadkoo --------#


import matplotlib.pyplot as plt
import numpy as np
import rebound
import sys

# conversion tools
deg2rad = np.pi / 180
rad2deg = 180 / np.pi

# Control structure
year_choice = 2020  # 2010 or 2020 or 2021 or 2030
test_choice = 'TestParticles'  # Pluto or TestParticles
mass_choice = 'MrianaProject'  # Giants or Neptune or MrianaProject or Test

# Number of years to simulate
sim_length = 1e7

###################### Launch Simulation #####################
sim = rebound.Simulation()

# Planets indexes
Sun = 0
Jupiter = 1
Saturn = 2
Uranus = 3
Neptune = 4
Test = 5

# Planet Mass
# Mass numbers as fraction of the sun: https://ssd.jpl.nasa.gov/?constants

if mass_choice == 'Giants':  # Sets accurate masses for all planets
    MSu = 1  # Mass of the Sun (Defined as 1 in units where G = 1)
    MMe = 1 / 6023600  # Mercury
    MV = 1 / 408523.71  # Venus
    ME = 1 / 328900.56  # Earth
    MMa = 1 / 3098708  # Mars
    MJ = 1 / 1047.3486  # Jupiter
    MS = 1 / 3497.898  # Saturn
    MU = 1 / 22902.98  # Uranus
    MN = 1 / 19412.24  # Neptune
    MP = 1 / 1.35e8  # Pluto
    MI = 0  # Ixion
elif mass_choice == 'Neptune':  # Sets only the masses for the Sun, Neptune, and Pluto
    MSu = 1  # Mass of the Sun (Defined as 1 in units where G = 1)
    MMe = 0  # Mercury
    MV = 0  # Venus
    ME = 0  # Earth
    MMa = 0  # Mars
    MJ = 0  # Jupiter
    MS = 0  # Saturn
    MU = 0  # Uranus
    MN = 1 / 19412.24  # Neptune
    MP = 1 / 1.35e8  # Pluto
    MI = 0  # Ixion
elif mass_choice == 'MrianaProject':  # Sets only the masses for the Sun, Jupiter, Saturn, Uranus, Neptune, and Pluto
    MSu = 1  # Mass of the Sun (Defined as 1 in units where G = 1)
    MMe = 0  # 1/6023600           #Mercury
    MV = 0  # 1/408523.71          #Venus
    ME = 0  # 1/328900.56          #Earth
    MMa = 0  # 1/3098708           #Mars
    MJ = 1 / 1047.3486  # Jupiter
    MS = 1 / 3497.898  # Saturn
    MU = 1 / 22902.98  # Uranus
    MN = 1 / 19412.24  # Neptune
    MP = 1 / 1.35e8  # Pluto
    MI = 0  # Ixion
elif mass_choice == 'Test':  # Sets test masses
    MSu = 1  # Mass of the Sun (Defined as 1 in units where G = 1)
    MMe = 1 / 6023600  # Mercury
    MV = 1 / 408523.71  # Venus
    ME = 1 / 328900.56  # Earth
    MMa = 1 / 3098708  # Mars
    MJ = 1 / 1047.3486  # Jupiter
    MS = 0  # 1/3497.898            #Saturn
    MU = 1 / 22902.98  # Uranus
    MN = 0  # 1/19412.24            #Neptune
    MP = 0  # 1/1.35e8              #Pluto
    MI = 0  # Ixion
else:
    print('Error: incorrect mass option chosen.')
    sys.exit('Mass Error')

# Set integrator type
sim.integrator = "whfast"
sim.integrator_whfast_safe_mode = 0
sim.whfast_corrector = 11

# Set simulation time variables
sim.dt = 0.6 * 2 * np.pi  # for 0.6*2*np.pi Jupiter
# 7*2*np.pi sim.dt for neptune
sim.t = 0

Noutputs = 10000  # 1000 or 10000 or 10000... Number of outputs
year = 2. * np.pi  # One year in units where G=1
times = np.linspace(0, sim_length * year, Noutputs)  # Length of simulation (start, end, # of divisions)

Su = np.zeros((2, Noutputs))
J = np.zeros((2, Noutputs))
S = np.zeros((2, Noutputs))
U = np.zeros((2, Noutputs))
N = np.zeros((2, Noutputs))
T = np.zeros((2, Noutputs))

NR = np.zeros((9, Noutputs))
TR = np.zeros((9, Noutputs))

####################### Add Planets #####################

# Sun
sim.add(
    m=MSu  # +MMe+MV+ME+MMa #Mass of the Sun plus each of the inner planets
)

if year_choice == 2010:

    # Jupiter Barycenter 2010-01-01
    sim.add(
        m=MJ,
        a=5.197681374151021E+00,
        e=4.878131026219109E-02,
        omega=2.739361835615551E+02 * deg2rad,
        inc=1.304557417695576E+00 * deg2rad,
        Omega=1.004972288251569E+02 * deg2rad,
        M=3.234223438835631E+02 * deg2rad
    )

    # Saturn Barycenter 2010-01-01
    sim.add(
        m=MS,
        a=9.546222266792196E+00,
        e=5.432345763666385E-02,
        omega=3.391814134742261E+02 * deg2rad,
        inc=2.486802463513464E+00 * deg2rad,
        Omega=1.136137937424876E+02 * deg2rad,
        M=7.945800301445027E+01 * deg2rad
    )

    # Uranus Barycenter 2010-01-01
    sim.add(
        m=MU,
        a=1.918643530824538E+01,
        e=4.741140499740572E-02,
        omega=9.709716928022614E+01 * deg2rad,
        inc=7.721991805267915E-01 * deg2rad,
        Omega=7.399363442135255E+01 * deg2rad,
        M=1.849871858393594E+02 * deg2rad
    )

    # Neptune Barycenter 2010-01-01
    sim.add(
        m=MN,
        a=3.007285525641584E+01,
        e=8.733961280257319E-03,
        omega=2.727958343243391E+02 * deg2rad,
        inc=1.770240895167752E+00 * deg2rad,
        Omega=1.317829440715040E+02 * deg2rad,
        M=2.821585299354812E+02 * deg2rad
    )

    if test_choice == 'Pluto':
        # Pluto Barycenter 2010-01-01
        sim.add(
            m=MP,
            a=3.948901610407399E+01,
            e=2.490110972054139E-01,
            omega=1.137773009650397E+02 * deg2rad,
            inc=1.714063118759761E+01 * deg2rad,
            Omega=1.103010643420244E+02 * deg2rad,
            M=2.936441984084609E+01 * deg2rad
        )

    elif test_choice == 'Ixion':
        # Ixion 2010-01-01
        sim.add(
            m=MI,
            a=3.949779478900530E+01,
            e=2.440565540968652E-01,
            omega=2.998571590209485E+02 * deg2rad,
            inc=1.963028209627355E+01 * deg2rad,
            Omega=7.103056886881051E+01 * deg2rad,
            M=2.719260328018023E+02 * deg2rad
        )
    else:
        print('Error: incorrect test planet chosen.')
        sys.exit('Test Error')

elif year_choice == 2020:

    # Jupiter Barycenter 2020-01-01
    sim.add(
        m=MJ,
        a=5.189034363651531E+00,
        e=4.933876696672575E-02,
        omega=2.749391300454769E+02 * deg2rad,
        inc=1.303345861187322E+00 * deg2rad,
        Omega=1.005027210046552E+02 * deg2rad,
        M=2.659058770288409E+02 * deg2rad
    )

    # Saturn Barycenter 2020-01-01
    sim.add(
        m=MS,
        a=9.536015982439171E+00,
        e=5.487766088871625E-02,
        omega=3.391578015655538E+02 * deg2rad,
        inc=2.487713663542724E+00 * deg2rad,
        Omega=1.135945066551931E+02 * deg2rad,
        M=2.016596834865320E+02 * deg2rad
    )

    # Uranus Barycenter 2020-01-01
    sim.add(
        m=MU,
        a=1.918774806275869E+01,
        e=4.733056598595431E-02,
        omega=9.707910701648791E+01 * deg2rad,
        inc=7.721296647613640E-01 * deg2rad,
        Omega=7.400315065053120E+01 * deg2rad,
        M=2.278454014078340E+02 * deg2rad
    )

    # Neptune Barycenter 2020-01-01
    sim.add(
        m=MN,
        a=3.007458801874063E+01,
        e=8.751571671933800E-03,
        omega=2.724247744218142E+02 * deg2rad,
        inc=1.770223382188710E+00 * deg2rad,
        Omega=1.317826633664084E+02 * deg2rad,
        M=3.043672561700226E+02 * deg2rad
    )

    if test_choice == 'Pluto':
        # Pluto Barycenter 2020-01-01
        sim.add(
            m=MP,
            a=3.948854534561571E+01,
            e=2.490176367407518E-01,
            omega=1.137711050921430E+02 * deg2rad,
            inc=1.714078278098203E+01 * deg2rad,
            Omega=1.103010205364683E+02 * deg2rad,
            M=4.388330583550427E+01 * deg2rad
        )

    elif test_choice == 'Ixion':
        # Ixion 2020-01-01
        sim.add(
            m=MI,
            a=3.949719680262456E+01,
            e=2.440624775047037E-01,
            omega=2.998610215086155E+02 * deg2rad,
            inc=1.963032695835533E+01 * deg2rad,
            Omega=7.103057314504557E+01 * deg2rad,
            M=2.864327268719799E+02 * deg2rad
        )
    else:
        print('Error: incorrect test planet chosen.')
        sys.exit('Test Error')

elif year_choice == 2021:

    # Jupiter Barycenter 2021-01-01
    sim.add(
        m=MJ,
        a=5.186248776397993E+00,
        e=4.823236893843078E-02,
        omega=2.752984816928482E+02 * deg2rad,
        inc=1.303422338076160E+00 * deg2rad,
        Omega=1.005033409512034E+02 * deg2rad,
        M=2.959307755201842E+02 * deg2rad
    )

    # Saturn Barycenter 2021-01-01
    sim.add(
        m=MS,
        a=9.534117213133813E+00,
        e=5.521891270197320E-02,
        omega=3.389549467947007E+02 * deg2rad,
        inc=2.488013281059568E+00 * deg2rad,
        Omega=1.135948607848353E+02 * deg2rad,
        M=2.141554644391900E+02 * deg2rad
    )

    # Uranus Barycenter 2021-01-01
    sim.add(
        m=MU,
        a=1.918807165506669E+01,
        e=4.730464485303179E-02,
        omega=9.707780440344314E+01 * deg2rad,
        inc=7.721279748238701E-01 * deg2rad,
        Omega=7.400324737552683E+01 * deg2rad,
        M=2.321388820122650E+02 * deg2rad
    )

    # Neptune Barycenter 2021-01-01
    sim.add(
        m=MN,
        a=3.007444132979245E+01,
        e=8.747220233002007E-03,
        omega=2.724435538782596E+02 * deg2rad,
        inc=1.770224289360134E+00 * deg2rad,
        Omega=1.317826858858846E+02 * deg2rad,
        M=3.065367266197209E+02 * deg2rad
    )

    if test_choice == 'Pluto':
        # Pluto Barycenter 2021-01-01
        sim.add(
            m=MP,
            a=3.948849881363497E+01,
            e=2.490141572030435E-01,
            omega=1.137715863296692E+02 * deg2rad,
            inc=1.714077126500989E+01 * deg2rad,
            Omega=1.103010180141096E+02 * deg2rad,
            M=4.533794544248052E+01 * deg2rad
        )

    elif test_choice == 'TestParticles':
        # Ixion 2021-01-01
        sim.add(
            m=MI,
            a=47.47789011300,
            e=0.27609503000,
            omega=0.27609503000 * deg2rad,
            inc=25.70718030000 * deg2rad,
            Omega=42.81693363800 * deg2rad,
            M=207.17291419500 * deg2rad
        )
    else:
        print('Error: incorrect test planet chosen.')
        sys.exit('Test Error')

elif year_choice == 2030:

    # Jupiter Barycenter 2030-01-01
    sim.add(
        m=MJ,
        a=5.207323880186078E+00,
        e=4.735744936651342E-02,
        omega=2.730926269533012E+02 * deg2rad,
        inc=1.304126873411264E+00 * deg2rad,
        Omega=1.005349707306574E+02 * deg2rad,
        M=2.112078224273227E+02 * deg2rad
    )

    # Saturn Barycenter 2030-01-01
    sim.add(
        m=MS,
        a=9.532355341006225E+00,
        e=5.427285060528492E-02,
        omega=3.390829196841603E+02 * deg2rad,
        inc=2.487866215035114E+00 * deg2rad,
        Omega=1.135944373948022E+02 * deg2rad,
        M=3.240223146732514E+02 * deg2rad
    )

    # Uranus Barycenter 2030-01-01
    sim.add(
        m=MU,
        a=1.918676556453253E+01,
        e=4.723291061047560E-02,
        omega=9.720080586447786E+01 * deg2rad,
        inc=7.719408277599551E-01 * deg2rad,
        Omega=7.400508866199539E+01 * deg2rad,
        M=2.705715365470622E+02 * deg2rad
    )

    # Neptune Barycenter 2030-01-01
    sim.add(
        m=MN,
        a=3.007451352361228E+01,
        e=8.774333985534795E-03,
        omega=2.726073894039024E+02 * deg2rad,
        inc=1.770248672441602E+00 * deg2rad,
        Omega=1.317835614810209E+02 * deg2rad,
        M=3.260307658240481E+02 * deg2rad
    )

    if test_choice == 'Pluto':
        # Pluto Barycenter 2030-01-01
        sim.add(
            m=MP,
            a=3.948946925097717E+01,
            e=2.490294465307500E-01,
            omega=1.137752256313718E+02 * deg2rad,
            inc=1.714059434066449E+01 * deg2rad,
            Omega=1.103009126578768E+02 * deg2rad,
            M=5.839764244325179E+01 * deg2rad
        )

    elif test_choice == 'Ixion':
        # Ixion 2030-01-01
        sim.add(
            m=MI,
            a=3.949674990911837E+01,
            e=2.440552256920120E-01,
            omega=2.998628705735873E+02 * deg2rad,
            inc=1.963027594097307E+01 * deg2rad,
            Omega=7.103053409991722E+01 * deg2rad,
            M=3.009446159592601E+02 * deg2rad
        )
    else:
        print('Error: incorrect test planet chosen.')
        sys.exit('Test Error')

else:
    print('Error: incorrect year chosen.')
    sys.exit('Year Error')

############################ Run Simulation #########################

sim.move_to_com()

fig = rebound.OrbitPlot(sim, unitlabel="[AU]", color=True, periastron=True)

SM = sim.particles

for j, time in enumerate(times):
    sim.integrate(time, exact_finish_time=0)
    # Assign components for resonance test
    NR[0][j] = SM[4].a  # 0 (a) -> semi-major axis
    TR[0][j] = SM[5].a
    NR[1][j] = SM[4].e  # 1 (e) -> eccentricity
    TR[1][j] = SM[5].e
    NR[2][j] = SM[4].inc  # 2 (inc) -> inclination
    TR[2][j] = SM[5].inc
    NR[3][j] = SM[4].Omega  # 3 (Omega, O upper case) -> Longitude of the ascending node
    TR[3][j] = SM[5].Omega
    NR[4][j] = SM[4].omega  # 4 (omega, o lower case) -> argument of periapsis
    TR[4][j] = SM[5].omega
    NR[5][j] = SM[4].f  # 5 (f) -> true anomaly
    TR[5][j] = SM[5].f
    NR[6][j] = SM[4].M  # 6 (M) -> mean anomaly
    TR[6][j] = SM[5].M
    NR[7][j] = SM[4].pomega  # 7 (pomega) -> longitude of periapsis
    TR[7][j] = SM[5].pomega
    NR[8][j] = SM[4].l  # 8 (l) -> mean longitude
    TR[8][j] = SM[5].l
    # Assign components for orbital plotting
    Su[0][j] = SM[0].x
    Su[1][j] = SM[0].y
    J[0][j] = SM[1].x
    J[1][j] = SM[1].y
    S[0][j] = SM[2].x
    S[1][j] = SM[2].y
    U[0][j] = SM[3].x
    U[1][j] = SM[3].y
    N[0][j] = SM[4].x
    N[1][j] = SM[4].y
    T[0][j] = SM[5].x
    T[1][j] = SM[5].y

###############################  Write to files ##########################

# Neptune Data

outfile1 = open('Neptune.out', 'w')

outfile1.write("#Note: All angles` numerical data are in Radians")
outfile1.write("\n")
outfile1.write("#a, e, inc, Omega, omega, f, M, pomega, l:")
outfile1.write("\n")
outfile1.write(str(time))
outfile1.write(" ")
outfile1.write(str(SM[4].a))
outfile1.write(" ")
outfile1.write(str(SM[4].e))
outfile1.write(" ")
outfile1.write(str(SM[4].inc))
outfile1.write(" ")
outfile1.write(str(SM[4].Omega))
outfile1.write(" ")
outfile1.write(str(SM[4].omega))
outfile1.write(" ")
outfile1.write(str(SM[4].f))
outfile1.write(" ")
outfile1.write(str(SM[4].M))
outfile1.write(" ")
outfile1.write(str(SM[4].pomega))
outfile1.write(" ")
outfile1.write(str(SM[4].l))
outfile1.write("\n")

outfile1.close()

# Pluto Data

outfile2 = open('Pluto.out', 'w')

outfile2.write("#Note: All angles` numerical data are in Radians")
outfile2.write("\n")
outfile2.write("#Time, a, e, inc, Omega, omega, f, M, pomega, l:")
outfile2.write("\n")
outfile2.write(str(time))
outfile2.write(" ")
outfile2.write(str(SM[5].a))
outfile2.write(" ")
outfile2.write(str(SM[5].e))
outfile2.write(" ")
outfile2.write(str(SM[5].inc))
outfile2.write(" ")
outfile2.write(str(SM[5].Omega))
outfile2.write(" ")
outfile2.write(str(SM[5].omega))
outfile2.write(" ")
outfile2.write(str(SM[5].f))
outfile2.write(" ")
outfile2.write(str(SM[5].M))
outfile2.write(" ")
outfile2.write(str(SM[5].pomega))
outfile2.write(" ")
outfile2.write(str(SM[5].l))
outfile2.write("\n")

outfile2.close()

########################## Read from a file ############################

Time, a, e, inc, Omega, omega, f, M, pomega, l = np.genfromtxt('Neptune.out', unpack=True)
Time, a, e, inc, Omega, omega, f, M, pomega, l = np.genfromtxt('Pluto.out', unpack=True)

########################## Plot ######################################

fig, axs = plt.subplots(5, sharex='col', sharey='row', gridspec_kw={'hspace': 0}, figsize=(8, 14))
axs[0].set_ylabel("a [AU]")
axs[0].plot(times / (year * 1e6), TR[0], color='black', marker='o', linestyle='none', linewidth=2, markersize=1);

axs[1].set_ylabel("e")
axs[1].plot(times / (year * 1e6), TR[1], color='black', marker='o', linestyle='none', linewidth=2, markersize=1);

axs[2].set_ylabel("i [Â°]")
axs[2].plot(times / (year * 1e6), TR[2] * rad2deg, color='black', marker='o', linestyle='none', linewidth=2,
            markersize=1);

axs[3].set_ylabel("omega [\u00B0]")
axs[3].plot(times / (year * 1e6), (TR[4] * rad2deg) % 360, color='black', marker='o', linestyle='none', linewidth=2,
            markersize=1);

axs[4].set(xlabel="time [Myr]", ylabel=r"resonant argument [$\degree$]")
ResAng = ((3 * TR[8] - 2 * NR[8] - TR[7]) * rad2deg) % 360
axs[4].plot(times / (year * 1e6), ResAng, color='black', marker='o', linestyle='none', linewidth=2, markersize=1);

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)
ax.set_xlim([-70, 70])
ax.set_ylim([-70, 70])
ax.set_facecolor('#333333')
plt.plot(Su[0], Su[1], color='yellow', marker='*', linestyle='none', linewidth=2, markersize=8);
plt.plot(J[0], J[1], color='#E36E4B', marker='o', linestyle='none', linewidth=2, markersize=1);
plt.plot(S[0], S[1], color='#CDA056', marker='o', linestyle='none', linewidth=2, markersize=1);
plt.plot(U[0], U[1], color='#93B8BE', marker='o', linestyle='none', linewidth=2, markersize=1);
plt.plot(N[0], N[1], color='#3E54E8', marker='o', linestyle='none', linewidth=2, markersize=1);
plt.plot(T[0], T[1], color='white', marker='o', linestyle='none', linewidth=2, markersize=1);

plt.show()
