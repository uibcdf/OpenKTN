attributes = {'temperature':None, 'time_step':None, 'weight':0.0, 'symmetrized':False,
              'with_components':False, 'with_basins':False}

class KineticTransitionNetwork():


    def __init__(self):

        self.microstates_dataframe=None
        self.transitions_dataframe=None

        for attr, value in attributes.items():
            setattr(self, attr, value)

