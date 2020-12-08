Files: 
TestParticleGen.py "Python"
ResonanceCheck.py  "Python"
Visualize.py       "Python"

----------------------------------------------------------------------------------------------------
#|TestParticleGen.py|

Description:
Generate number of test particles with the Kozai plutino orbital elements randomly.
-Any code to be ran before: No

Variables inside:
"NumberOfFiles" : Number of files 

#Run argument expects:
A number, entered after the python TestParticleGen.py, to specify how many Testparticles wanted per file

#Example run:
python TestParticleGen.py 1000

----------------------------------------------------------------------------------------------------
#|ResonanceCheck.py|

#Description:
Given the Rebound code output, or output from any particles with the six orbital elements integrated over time followed by the lambda of neptune with the following order:
time, index, SMA, ECC,  inc, Omega, omega, M, l
-Any code to be ran before: ReboundCode.py

#Run argument expects:
A number, entered after the python ResonanceCheck.py, to specify which file number is it going to read "name"

#Example run:
python ResonanceCheck.py 1

----------------------------------------------------------------------------------------------------
#|Visualize.py|

#Description:
Graphs the Semimajor axis against Eccentricity of, or the output of the ResonanceCheck.py files. With 3 states, "0": Not Resonance, "1": Resonance but not Kozai, "2": Resonance and Kozai
-Any code to be ran before: ResonanceCheck.py

Variables inside:
"NumberOfFiles" : Number of files 

#Example run:
python Visualize.py


