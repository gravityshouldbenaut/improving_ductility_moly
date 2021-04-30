# improving_ductility_moly
Combined ANSYS, LAMMPS, ThermoCalc workflow for the improvement of molybdenum, powered by CSV files

Installing LAMMPS on Linux
Go here: https://lammps.sandia.gov/download.html, click on the bubble next to the stable version, and click install
Move your downloaded lammps folder to your user folder. If on windows, move to the folder of your WSL username. If on mac, move to user/yournamehere. 
Untar the downloaded folder by opening the terminal and typing tar -xzvf lammps-stable.tar.gz 
Make sure you are in your user folder where you put your lammps folder! Otherwise, it will not work.
Navigate into your folder by doing cd lammps/src when you open your terminal 
Type make mpi and hit enter
Make sure make is installed on your system! 
Type make serial and hit enter 
Make sure you have jupyter notebook installed
From your User/yournamehere/lammps/src folder, do cd .. and then cd python/examples/pylammps/montecarlo 
Now type jupyter notebook and hit enter. 
Follow this link : Install Jupyter notebook 
https://www.digitalocean.com/community/tutorials/how-to-set-up-jupyter-notebook-with-python-3-on-ubuntu-20-04-and-connect-via-ssh-tunneling

Open the link given for your jupyter notebook in the browser. 

Mac
Install lammps via homebrew https://lammps.sandia.gov/doc/Install_mac.html 
Run commands straight in terminal, the python interpreter did not work here 

