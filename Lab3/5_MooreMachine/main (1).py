class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol)

class MooreMachine:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.initial_state

    def process_input(self, input_sequence):
        outputs = []
        for input_symbol in input_sequence:
            outputs.append(self.current_state.name)
            self.current_state = self.current_state.get_next_state(input_symbol)
        # Dodanie wyjścia dla ostatniego stanu
        outputs.append(self.current_state.name)
        return outputs

state_A = MooreState("A", "0")
state_B = MooreState("B", "1")
state_C = MooreState("C", "1")
state_D = MooreState("D", "0")
state_E = MooreState("E", "1")

#State A
state_A.add_transition('0', state_A)
state_A.add_transition('1', state_B)

#State B
state_B.add_transition('0', state_C)
state_B.add_transition('1', state_E)

#State C
state_C.add_transition('0', state_D)
state_C.add_transition('1', state_B)

#State D
state_D.add_transition('0', state_D)
state_D.add_transition('1', state_E)

#State E
state_E.add_transition('0', state_D)
state_E.add_transition('1', state_A)

moore_machine = MooreMachine(state_A)


input_sequence = "11011100"
output_sequence = moore_machine.process_input(input_sequence)

print(f"Sekwencja wejściowa:  {input_sequence}")
print(f"Sekwencja wyjściowa: {''.join(output_sequence)}")