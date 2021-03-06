from pandas import DataFrame

class Pandas_KineticTransitionNetwork():

    def __init__(self, temperature=None, time_step=None):

        from openktn.native.network import attributes as network_attributes

        self.microstates = Pandas_MicrostatesDataFrame()
        self.transitions = Pandas_TransitionsDataFrame()

        for attribute, value in network_attributes.items():
            setattr(self, attribute, value)

        self.temperature=temperature
        self.time_step=time_step

class Pandas_MicrostatesDataFrame(DataFrame):

    def __init__(self):

        from openktn.native.microstate import attributes as microstate_attributes

        super().__init__(columns=microstate_attributes.keys())

class Pandas_TransitionsDataFrame(DataFrame):

    def __init__(self):

        from openktn.native.transition import attributes as transition_attributes

        super().__init__(columns=transition_attributes.keys())

