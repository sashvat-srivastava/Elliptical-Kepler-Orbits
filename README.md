# Orbital Dynamics Simulation: Verification of Elliptical Keplerian Motion

This project implements a numerical simulation of the Earth-Sun system to verify the geometric and conservation laws of classical mechanics. [cite_start]It utilizes an *ab initio* approach, where elliptical trajectories emerge from first principles rather than pre-defined geometric constraints[cite: 4, 338, 339].

## Numerical Methodology
[cite_start]The simulation employs a **Velocity Verlet integrator**, a symplectic algorithm selected for its stability in conserving the Hamiltonian of the system over long timescales[cite: 32, 41]. [cite_start]This approach prevents the numerical dissipation and energy drift common in non-symplectic methods like Euler integration[cite: 39, 40].


## Theoretical Foundation
[cite_start]The system is modeled using the Lagrangian for a central force field[cite: 50, 54]:

$$\mathcal{L}=\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})-V(r)$$

[cite_start]Where the gravitational potential is defined as $V(r) = -GMm/r$[cite: 80]. [cite_start]The simulation demonstrates that for a total mechanical energy $E < 0$, the resulting trajectory is a stable ellipse with the primary mass at one focus[cite: 89, 94].

## Results and Validation
[cite_start]The implementation achieves high-fidelity conservation of physical invariants[cite: 333, 334]:
* [cite_start]**Total Energy (TE) Stability:** Relative error $\Delta/E_0 \approx 3.28 \times 10^{-9}$[cite: 293].
* [cite_start]**Angular Momentum (L) Conservation:** Maintained to machine precision, $\Delta/L_0 \approx 1.13 \times 10^{-16}$[cite: 295].
* [cite_start]**Kepler’s Second Law:** Quantitatively verified through the constant rate of area swept by the radius vector, tied to $L/2m$[cite: 96, 46].


## Repository Structure
* [cite_start]`main.py`: VPython implementation of the Velocity Verlet integrator and 3D visualization[cite: 102].
* [cite_start]`Latex-Report.pdf`: Comprehensive technical report including Lagrangian derivations and error analysis[cite: 2, 7].

## Dependencies
* Python 3.x
* VPython library

---
[cite_start]**Author:** Sashvat Srivastava [cite: 3]
[cite_start]**Course:** PHY1005: Introduction to Computational Physics, Shiv Nadar University [cite: 1, 6]
