# fys4620
Some code for the course 4620 at UiO

The main purpose is to simulate trajectories of charged particles in 3 spacial dimensions in time, subject to a static or varying electric and magnetic fields. This is achieved with a class BDriftSolver, initially created to simulate grad B drift, but that can be expanded to do more. The main equation of motion is the Lorentz force, solved with the simple Euler Cromer method in Python. 