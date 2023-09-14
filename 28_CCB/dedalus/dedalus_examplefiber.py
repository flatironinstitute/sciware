# NO ACTIVITY: AN IMPOSED POLAR FORCE + ELASTICITY OF THE DIRECTOR IN THE EVOLUTION + ELASTIC STRESSES IN THE MOMENTUM BALANCE
import numpy as np 
import dedalus.public as d3
import logging
logger = logging.getLogger(__name__)
#--------------------------------------------------------------------------------------------------------
# DIMENSIONS, FIELDS, AND OPERATORS 

# Geometry and data type
L = 4*np.pi;  # Length of my box 
N = 512;      # Number of poits 
dtype = np.float64 # Data type
timestepper = d3.RK443

# Bases
coords = d3.CartesianCoordinates('x','y'); 
dist   = d3.Distributor(coords, dtype=dtype);
xbasis = d3.RealFourier(coords['x'], size=N, bounds=(-L/2,L/2), dealias=2);
ybasis = d3.RealFourier(coords['y'], size=N, bounds=(-L/2,L/2), dealias=2); 
(x,y)  = dist.local_grids(xbasis,ybasis) 

# Fields
rho = dist.Field(name='rho', bases=(xbasis,ybasis)) # density
S   = dist.Field(name='S',   bases=(xbasis,ybasis)) # Stretch field
phi = dist.Field(name='phi', bases=(xbasis,ybasis)) # angular field
p   = dist.Field(name='p',   bases=(xbasis,ybasis)) # pressure

u   = dist.VectorField(coords, name='u', bases=(xbasis,ybasis)) # Solvent velocity field
v    = dist.VectorField(coords, name='v',     bases=(xbasis,ybasis))   # Fiber velocity field

n    = dist.VectorField(coords, name='n',     bases=(xbasis,ybasis))   # Tangent vector field
nperp= dist.VectorField(coords, name='nperp', bases=(xbasis,ybasis))   # Perpendicular to tangent

# Field with which you want to anti-align
q    = dist.VectorField(coords, name='q',     bases=(xbasis,ybasis));
q['g'] = 0; q['g'][0] = np.cos(np.pi/4); q['g'][1] = np.sin(np.pi/4);


# Unit vectors in the x and y directions and the identity tensor
ex  = dist.VectorField(coords, name='ex', bases=(xbasis,ybasis))   # Fiber velocity field
ey  = dist.VectorField(coords, name='ey', bases=(xbasis,ybasis))   # Tangent vector field
ex['g'] = 0; ex['g'][0] = 1;
ey['g'] = 0; ey['g'][1] = 1;


I = dist.TensorField((coords,coords), name='I', bases=(xbasis,ybasis)); # Identity matrix 
I['g'][0,0] = 1; I['g'][0,1] = 0; I['g'][1,0] = 0; I['g'][1,1] = 1;

tau_p = dist.Field(name='tau_p'); tau_v   = dist.VectorField(coords, name='tau_v'); tau_u   = dist.VectorField(coords, name='tau_u'); # tau fields for pressure and velocity
#-------------------------------------------------------------------------------------------------------- 
# Function for initial conditions 
def init(x,y,Lx):
    np.random.seed(seed=3)
    nk = 12;  epsi = (x+y)*0; 
    for k in range(nk):
        pert1 = 0.01*(np.random.rand(1)-0.5)
        pert2 = 0.01*(np.random.rand(1)-0.5)

        epsi = epsi + 0.01*(np.cos(2*np.pi*(k-nk/2)*x/Lx)+np.cos(2*np.pi*(k-nk/2)*y/Lx))
    return epsi
#-----------------------------------------------------------------------------------------------------------
# PARAMETERS FOR THE PROBLEM
 
Ma  = 1000;  # Machin number
ks  = 100;   # Spring constant
A   = 20;    # Activity
D   =0.2;    # Diffusion 
damp= 1;     # Damping in the problem 
#-----------------------------------------------------------------------------------------------------------
# PROBLEM AND EQUATIONS OF MOTION 
problem = d3.IVP([nperp,n,u,v,p,tau_p,tau_u,phi,S,rho], namespace=locals())

# Define directors
problem.add_equation(" n     = np.cos(phi)*ex + np.sin(phi)*ey")
problem.add_equation(" nperp =-np.sin(phi)*ex + np.cos(phi)*ey")

# Stokes solve
problem.add_equation("-grad(p) + lap(u) + (v-u) + tau_u = -A*div(rho*(I-n*n))-(rho-1)*(v-u)+ rho*dot(n*n,(v-u))/2") # momentum balance
problem.add_equation(" Ma*(v-u)   = (I+n*n)@(-n@grad(n@grad(S*n@grad(n))) + ks*n@grad((S**2-1)*n))")                  # fiber field evolution
problem.add_equation(" div(u) + tau_p = 0")   # incompressibility
problem.add_equation(" integ(p) = 0")         # Velocity gauge
problem.add_equation(" integ(u) = 0")         # Velocity gauge

# Evolution of director, density, and stretch-field
problem.add_equation(" dt(phi) - D*lap(phi) + damp*lap(lap(phi)) =-v@grad(phi) + nperp@(n@grad(v)) + damp*lap(lap(phi))") # angle evolution for tangent field
problem.add_equation(" dt(S)                + damp*lap(lap(S))   =-v@grad(S)   + S*n@(n@grad(v))   + damp*lap(lap(S))")   # stretch field evolution
problem.add_equation(" dt(rho) - D*lap(rho) + damp*lap(lap(rho)) =-div(v*rho)                      + damp*lap(lap(rho))") # density of fiber

#-----------------------------------------------------------------------------------------------------------
# INITIAL CONDITIONS 

# Angle, density, and stretch field
phi['g'] = np.pi + 0.2*(np.cos(x)+np.sin(y)); 
rho['g'] = 1; S['g'] = 1; 
#-----------------------------------------------------------------------------------------------------------
# INITIATE SOLVER AND TIMESTEP

# Initiate solver
solver = problem.build_solver(timestepper)
solver.stop_sim_time = 100;

# Intial dt
delt = 3e-5; 

# Define velocity for CFL condition
cfl = d3.CFL(solver, initial_dt=delt, cadence=10, safety=0.1, max_change=1.5, 
             min_change=0.5, max_dt=10*delt, threshold=0.05)
cfl.add_velocity(u)

# Analysis
snapshots = solver.evaluator.add_file_handler('snapshots', sim_dt=0.02, max_writes=50)
snapshots.add_task(rho,name='c0');
snapshots.add_task(S,  name='S'); 
snapshots.add_task(u,  name='u');
snapshots.add_task(v,  name='v');
snapshots.add_task(n,  name='n'); 



# Checkpoint 
checkpoints = solver.evaluator.add_file_handler('checkpoints', sim_dt=0.5, max_writes=1, mode='overwrite')
checkpoints.add_tasks(solver.state)



# Main loop
try:
    logger.info('Starting main loop')
    while solver.proceed:
        dt = cfl.compute_timestep()    # Compute dt based on velocity
        solver.step(dt)
        if (solver.iteration-1) % 10 == 0: # Print logger stats after every 10 iterations/time-steps
            logger.info('Iteration=%i, Time=%e, dt=%e' %(solver.iteration, solver.sim_time, dt))
        if (np.max(S['g']) > 100 or np.min(S['g']) < 0):
            print("stopping simulation")
            break
except:
    logger.error('Exception raised, triggering end of main loop.')
    raise
finally:
    solver.log_stats()
