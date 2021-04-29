from __future__ import print_function
import matplotlib.pyplot as plt
import random, math
from lammps import lammps, PyLammps
from ansystrial import getPerturbationsFromANSYSStrain

L = PyLammps()

#set the unit type 
L.units("si")
L.atom_style("atomic")
L.atom_modify("map array sort", 0, 0.0)
L.dimension(3)
# L.angle_style("hybrid harmonic cosine")

#specify the material type and lattice constant (in Meters as per the units page https://lammps.sandia.gov/doc/units.html) 
L.lattice("bcc", 3.15)
#set up simulation box for the atoms, following these dimensions (https://lammps.sandia.gov/doc/region.html) (xlo, xhi, ylo, yhi, zlo, zhi)
# L.region("box block", 0, 12, 0, 12, 0,  12)
L.region("box block", 0, 10,0,10,0,10)

#create the box and atoms designed, with type 1
L.create_box(2, "box")
# L.create_atoms(3, "region", "regsphere", "basis", 2, 3, "ratio", 0.5, 74637)
L.create_atoms(1, "box")
# L.create_atoms(2, "box")
L.create_atoms(2, "single", 0,0,1)
L.create_atoms(2, "single", 1,2,4)
L.create_atoms(2, "single", 3,6,6)
L.create_atoms(2, "single", 2,1,1)
L.create_atoms(2, "single", 5,5,4)
L.create_atoms(2, "single", 1,1,6)
# #Mass of each Mo atom (in Kg as per SI units)
L.mass(1, 1.59*10**-25) 

# #trying to add oxygen
L.mass(2, 2.65*10**-26) 


#lenneard jones potential calcs
L.pair_style("lj/cut",2.5) 
L.pair_coeff("*", "*", 1.0, 1.0, 2.5)
L.pair_modify("shift", "yes")

L.neighbor(0.3, "bin")
L.neigh_modify("delay", 0, "every", 1, "check", "yes")
# L.image(zoom=1.6)
L.run(0)
emin = L.eval("ke")
random.seed(27848)
deltaperturb = 0.2

strains = getPerturbationsFromANSYSStrain()
for i in range(L.system.natoms):
    print(L.atoms[i].position)
    x, y,z = L.atoms[i].position
    if(i < len(strains)):
        dx = deltaperturb * random.uniform(-1, 1) * strains[i]
        dy = deltaperturb * random.uniform(-1, 1) * strains[i]
        dz = deltaperturb * random.uniform(-1, 1) * strains[i]
    L.atoms[i].position = (x+dx, y+dy, z+dz)

L.run(0)
# L.image(zoom=1.6)

estart = L.eval("ke")
elast = estart

naccept = 0
energies = [estart]
niterations = 3000
deltamove = 0.1
#boltzmann constant times temperature 
# kT = 0.05
kT = 4.11 * 10 ** (-21)

natoms = L.system.natoms
strains = getPerturbationsFromANSYSStrain()
for i in range(niterations):
    iatom = random.randrange(0, natoms)
    current_atom = L.atoms[iatom]
    
    x0, y0,z0 = current_atom.position
    
    dx = deltamove * random.uniform(-1, 1) 
    dy = deltamove * random.uniform(-1, 1) 
    dz = deltamove * random.uniform(-1, 1) 
    
    current_atom.position = (x0+dx, y0+dy, z0+dz)
    
    L.run(1, "pre no post no")
    
    e = L.eval("ke")
    energies.append(e)
    
    if e <= elast:
        naccept += 1
        elast = e
    elif random.random() <= math.exp(natoms*(elast-e)/kT):
        naccept += 1
        elast = e
    else:
        current_atom.position = (x0, y0, z0)

plt.xlabel('iteration')
plt.ylabel('kinetic energy')
plt.plot(energies)
plt.savefig('ke_moly_6atomsoxygen_withansysstrain.png')

L.eval("ke")
print(emin)
print(estart)
print(naccept)
# L.image(zoom=1.6) 