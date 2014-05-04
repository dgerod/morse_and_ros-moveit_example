# =======================================================================================
# Local configuration of the experiment.
# =======================================================================================

# Exported module information
# ---------------------------------------------

objects_dir = "";
environment_dir = "";
mw_dir = "";
mw_loc = "";

# Function that mount the structure of directories used by the simulation,
# and the middleware (ROS) location.
# ---------------------------------------------

def load_experiment_config( ExperimentName ):
    
    global objects_dir, environment_dir
    global mw_dir, mw_loc
    
    # Mount structure of directories used by the simulation.
    objects_dir = ExperimentName + '/props/'
    environment_dir = ExperimentName + '/environments/'
    mw_dir = ExperimentName + '/middleware_ros/'
    
    # Middleware location based on directory.
    # Remember that middleware objects must be added to "__init__.py" of the directory.
    mw_loc = mw_dir
    mw_loc = mw_loc.replace("/", ".")

# ---------------------------------------------------------------------------------------

# Configure with the name of the experiment.
experiment_name = 'my_simulation'
load_experiment_config( experiment_name )

# =======================================================================================
