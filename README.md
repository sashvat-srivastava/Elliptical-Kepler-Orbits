# Orbital Dynamics Simulation: Verification of Elliptical Keplerian Motion

This repository contains a numerical simulation of the Earth-Sun system designed to verify the geometric and conservation laws of classical mechanics. The project utilizes an *ab initio* approach, where elliptical trajectories emerge from first principles rather than pre-defined geometric constraints.

## Numerical Methodology
The simulation employs a **Velocity Verlet integrator**, a symplectic algorithm selected for its stability in conserving the Hamiltonian of the system over long timescales. This approach prevents numerical dissipation and energy drift, which are characteristic of non-symplectic methods such as Euler integration.



## Theoretical Foundation
The system is modeled using the Lagrangian for a central force field:

$$\mathcal{L}=\frac{1}{2}m(\dot{r}^{2}+r^{2}\dot{\theta}^{2})-V(r)$$

Where the gravitational potential is defined as $V(r) = -GMm/r$. The simulation demonstrates that for a total mechanical energy $E < 0$, the resulting trajectory is a stable ellipse with the primary mass at one focus.

## Results and Validation
The implementation achieves high-fidelity conservation of physical invariants:
* **Total Energy (TE) Stability:** Relative error $\Delta/E_0 \approx 3.28 \times 10^{-9}$.
* **Angular Momentum (L) Conservation:** Maintained to machine precision, $\Delta/L_0 \approx 1.13 \times 10^{-16}$.
* **Kepler’s Second Law:** Quantitatively verified through the constant rate of area swept by the radius vector ($L/2m$).



## Repository Structure
* `main.py`: VPython implementation of the Velocity Verlet integrator and 3D visualization.
* `Latex-Report.pdf`: Technical report including Lagrangian derivations and error analysis.

## Dependencies
* Python 3.x
* VPython library

---
**Author:** Sashvat Srivastava  
**Institution:** Shiv Nadar Institute of Eminence  
**Course:** PHY1005: Introduction to Computational Physics
