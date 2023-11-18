from PetriNet import PetriNet
import pandas as pd


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
    message = fault_diagnosis(fault_case_folder=r"..\case1")
    print(message[0])
