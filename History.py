class History:
    new_round = {}

    def __init__(self, round_number, event):
        self.new_round_number = round_number
        self.new_round_event = event
        History.new_round[self.new_round_number] = self.new_round_event
