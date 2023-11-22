import pandas as pd

class PetriNet():

    def __init__(self, initial_state_txt_file: str):
        """
        Function that builds the corresponding Petri Net based on the initial state settings from the substation
        operation state machine

        :param initial_state_txt_file: windows file location of a txt file containing the initial state of the substation
            it is assumed that the substation consists of two buses (BB1 and BB2) and the file should have two lists,
            for example:

                BB1=["B1","B3","B4","bus_tie"]
                BB2=["B2","B5","B6","bus_tie"]

            Note that the bays "B1","B3","B4" are connected to the bus BB1, meanwhile the bays "B2","B5","B6" are
            connected to the bus BB2.

            Also note that in case the bus tie is closed, the user must add the variable "bus_tie" between the
            corresponding buses
        """

        # Read the lists containing the substation initial state
        BB1, BB2 = self.read_case(initial_state_txt_file=initial_state_txt_file)

        # Get all the bays connected to the substation
        bays = set(sorted(BB1 + BB2))
        # Ignore Bus Tie since this does not correspond to a bay of interest.
        bays.discard("bus_tie")

        # Define the initial Petri net
        self.petri_net = {
            'places': {
                'Initial_state': {
                    "mark": 1,  # Place with 1 token initially
                    "message": "System without fault"
                },
            },
            'transitions': {}
        }

        # Build petri net branches for line faults
        for bay in bays:
            self.petri_net["places"][f"Fault at: {bay}"] = {
                "mark": 0,
                "message": f"Fault found at bay {bay}, without trip"
            }
            self.petri_net["transitions"][f"PL{bay.replace('B', '')}"] = {
                'input': ['Initial_state'],
                'output': [f"Fault at: {bay}"]
            }

            self.petri_net["places"][f"CB{bay.replace('B', '')}_tripped"] = {
                "mark": 0,
                "message": f"Fault found at bay {bay}, with trip CB{bay.replace('B', '')}"
            }
            self.petri_net["transitions"][f"CB{bay.replace('B', '')}"] = {
                'input': [f"Fault at: {bay}"],
                'output': [f"CB{bay.replace('B', '')}_tripped"]
            }

            breaker_failure_bays = BB1.copy() if bay in BB1 else BB2.copy()
            breaker_failure_bays.remove(bay)

            breaker_failure_bays = [x.replace("B", "CB") for x in breaker_failure_bays]

            self.petri_net["places"][f"CB{bay.replace('B', '')}_not_tripped__BF"] = {
                "mark": 0,
                "message": f"Fault found at bay {bay},"
                           f" with refused trip at CB{bay.replace('B', '')} and operation of: {breaker_failure_bays}"
            }
            self.petri_net["transitions"][f"{'-'.join(breaker_failure_bays)}"] = {
                'input': [f"Fault at: {bay}"],
                'output': [f"CB{bay.replace('B', '')}_not_tripped__BF"]
            }

        bus_bays = {"BB1": BB1, "BB2": BB2}

        # Build Petri Net for Bus faults
        for bus in ["BB1", "BB2"]:
            self.petri_net["places"][f"Fault at: {bus}"] = {
                "mark": 0,
                "message": f"Fault at: {bus}, without trip"
            }
            self.petri_net["transitions"][f"DIFF_{bus}"] = {
                'input': ['Initial_state'],
                'output': [f"Fault at: {bus}"]
            }

            bus_bay = bus_bays[bus]
            bus_bay = [x.replace("B", "CB") for x in bus_bay]
            self.petri_net["places"][f"{bus}_Diff_Operation"] = {
                "mark": 0,
                "message": f"Fault at: {bus}, with trip of: {bus_bay}"
            }
            self.petri_net["transitions"][f"{'-'.join(bus_bay)}"] = {
                'input': [f"Fault at: {bus}"],
                'output': [f"{bus}_Diff_Operation"]
            }

    def read_case(self, initial_state_txt_file: str) -> tuple:
        """
        Function used to read the substation initial state
        
        :param initial_state_txt_file: 
        :return: tuple of lists for the Buses of interest
        """
        with open(initial_state_txt_file, "r") as init_state_txt:
            buses = init_state_txt.readlines()
            BB1 = eval(buses[0].split()[0].replace("BB1=", ""))
            BB2 = eval(buses[1].split()[0].replace("BB2=", ""))
        return BB1, BB2

    def fire_transition(self, transition: str, verbose: bool = False):
        """
        Function that allows the user to fire a transition
        :param transition:
        :param verbose:
        :return:
        """
        # Check if the transition is enabled
        enabled = all(
            self.petri_net['places'][place]["mark"] > 0
            for place in self.petri_net['transitions'][transition]['input']
        )

        if enabled:
            # Perform the transition
            for place in self.petri_net['transitions'][transition]['input']:
                self.petri_net['places'][place]["mark"] -= 1
            for place in self.petri_net['transitions'][transition]['output']:
                self.petri_net['places'][place]["mark"] += 1
            if verbose:
                print(f"Transition '{transition}' fired successfully.\n")
            # print_state()
        else:
            if verbose:
                print(f"Transition '{transition}' is not enabled.\n")

    def print_state(self, verbose: bool = False):

        if verbose:
            print("Current Petri net state:")
            print("Places:")
            for place, tokens in self.petri_net['places'].items():
                print(f"{place}: {tokens} marks")
            print("\n")

        print("Final States: ")

        for place, tokens in self.petri_net['places'].items():
            if tokens["mark"] == 1:
                print(f"{place}: {tokens['mark']} marks")
                print(f"{tokens['message']}")
        print("\n")

    def get_state(self) -> list:
        messages = []
        for place, tokens in self.petri_net['places'].items():
            if tokens["mark"] == 1:
                messages.append(tokens['message'])
        return messages



def fault_diagnosis(fault_case_folder):
    petri_net = PetriNet(fr"{fault_case_folder}\Initial_State.txt")

    df_PL_CB_operation = pd.read_csv(fr"{fault_case_folder}\PL_CB_operation.csv")

    for index, data_row in df_PL_CB_operation.iterrows():
        transitions = petri_net.petri_net["transitions"].keys()
        for transition in transitions:

            events = transition.split("-")
            data_events = [data_row[event] for event in events]
            if all(data_events):
                petri_net.fire_transition(transition=transition, verbose=False)

    return petri_net.get_state()


if __name__ == "__main__":
    petri_net = PetriNet("data\case1")
    # Initial state
    petri_net.print_state()

    # # Fire transitions
    petri_net.fire_transition('PL2')
    petri_net.fire_transition('B1_B2_B3_bus_tie')
    #
    # # Final State
    petri_net.print_state()
