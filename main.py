from vpython import *

# Scene setup
scene = canvas(title='Earth Orbit (Velocity Verlet, Textured Earth)',
               width=800, height=600,
               background=color.black)
scene.center = vector(0,0,0)

# Constants & scaling
G = 6.67430e-11
M_sun = 1.989e30
M_earth = 5.972e24
AU = 1.496e11
scale = 1.5e-10
scene.range = 1.6 * AU * scale

# Objects
sun = sphere(pos=vector(0,0,0),
             radius=6.96e8*scale*50,
             color=color.yellow,
             emissive=True)
sun.mass = M_sun

earth = sphere(pos=vector(AU*scale, 0, 0),
               radius=6.37e6*scale*500,
               texture=textures.earth,
               make_trail=True)
earth.mass = M_earth

# Labels
energy_label = label(pos=vector(0, 1.1*scene.range, 0),
                     text="Calculating...", height=14, color=color.white, box=False)
L_label = label(pos=vector(0, -1.1*scene.range, 0),
                text="Calculating...", height=14, color=color.yellow, box=False)

# Initialization
v_circular = sqrt(G * M_sun / AU)
earth.velocity = vector(0, 0.8 * v_circular, 0)
dt = 24 * 3600
t = 0.0
step = 0

# Initial acceleration
r_vector_real = (earth.pos / scale) - (sun.pos / scale)
r_mag = mag(r_vector_real)
force_mag = G * sun.mass * earth.mass / (r_mag**2)
force_vector = -force_mag * norm(r_vector_real)
acceleration = force_vector / earth.mass

# Reference invariants
L0 = mag(cross(r_vector_real, earth.mass * earth.velocity))
TE0 = 0.5 * earth.mass * mag(earth.velocity)**2 - G * sun.mass * earth.mass / r_mag

# Graphs
graph1 = graph(title="Orbital Energies", width=600, height=300,
               xtitle="Time (days)", ytitle="Energy (J)")
KE_curve = gcurve(color=color.red, label="Kinetic Energy")
PE_curve = gcurve(color=color.green, label="Potential Energy")
TE_curve = gcurve(color=color.blue, label="Total Energy")

graph2 = graph(title="Angular Momentum", width=600, height=300,
               xtitle="Time (days)", ytitle="Angular Momentum (kg·m²/s)",
               ymin=L0*0.999, ymax=L0*1.001)
L_curve = gcurve(color=color.orange, label="Angular Momentum")

# Simulation loop
while True:
    rate(120)

    earth.pos = earth.pos + earth.velocity*dt*scale + 0.5*acceleration*(dt**2)*scale

    r_vector_real = (earth.pos / scale) - (sun.pos / scale)
    r_mag = mag(r_vector_real)
    force_mag = G * sun.mass * earth.mass / (r_mag**2)
    force_vector = -force_mag * norm(r_vector_real)
    new_acceleration = force_vector / earth.mass

    earth.velocity = earth.velocity + 0.5*(acceleration + new_acceleration)*dt
    acceleration = new_acceleration

    KE = 0.5 * earth.mass * mag(earth.velocity)**2
    PE = -G * sun.mass * earth.mass / r_mag
    TE = KE + PE
    L = mag(cross(r_vector_real, earth.mass * earth.velocity))

    if step % 10 == 0:
        rel_TE = (TE - TE0) / abs(TE0)
        rel_L  = (L  - L0)  / abs(L0)
        energy_label.text = f"TE: {TE:.3e} J (Δ/|TE0|={rel_TE:.3e})"
        L_label.text = f"L: {L:.3e} (Δ/|L0|={rel_L:.3e})"

    days = t / (3600*24)
    KE_curve.plot(days, KE)
    PE_curve.plot(days, PE)
    TE_curve.plot(days, TE)
    L_curve.plot(days, L)

    t += dt
    step += 1