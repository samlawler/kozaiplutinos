#!/bin/bash
export HOME=`cd ~ ; pwd`
set -m

# Copying from VOSpace
#1) copy the generated test particles from rabaa VOSpace
for i in {1..100}
do
	vcp vos:rabaa/TestparticlesOutput/TestParticle${1}.in . && break
done
#2) copyRebound code from mriana19 VOSpace
for i in {1..100}
do
	vcp vos:mriana19/ReboundCode.py . && break
done
#3) coby ResonanceCheck code from rabaa VOSpace
for i in {1..100}
do
	vcp vos:rabaa/ResonanceCheck.py . && break
done

# Running the codes
# Run ReboundCode.py (run the simulation)
python ReboundCode.py $1

# Run ResonanceCheck.py code
python ResonanceCheck.py $1

#copy over the test particles` orbital elements files from the ReboundCode.py to mriana19 VOSpace
#The Planets files
for i in {1..100}
do
	vcp pl${1}.out vos:mriana19/TheFourthRun/PlanetsRunFinal/pl${1}.out && break
done
#The test particles files
for i in {1..100}
do
	vcp tp${1}.out vos:mriana19/TheFourthRun/TParticlesRunFinal/tp${1}.out && break
done
#The .bin files
for i in {1..100]
do
	vcp Simulation${1}.bin vos:mriana19/TheFourthRun/BinRunFinal/Simulation${1}.bin && break
done

# copy over Rabaa`s Resonance Check files to mriana19 VOSpace
# The Resonance Check files
for i in {1..100}
do
        vcp TestParticleResonance${1}.out vos:mriana19/TheFourthRun/CheckRunFinal/TPCheck${1}.out && break
done
