class RPS:

    def __init__(self, file_name:str):

        self.values = dict()
        self.states = list()
        
        for l1, l2, val in ('A', 'X', 1), ('B', 'Y', 2), ('C', 'Z', 3):
            self.values[l1] = self.values[l2] = val

        with open(file_name,'r') as f:
            for line in f:
                opponent, my_player = line.strip().split()
                self.states.append((opponent, my_player))

    def eval_choice(self, player:str) -> int:
        return self.values[player]

    def eval_state(self, opponent:str, my_player:str) -> int:

        o, p = self.eval_choice(opponent), self.eval_choice(my_player)

        winning_states = {(1,2), (3,1), (2, 3)}

        res = p

        if o == p:
            res += 3
        elif (o,p) in winning_states:
            res += 6

        return res

    def simulate_game(self) -> int:
        out = 0

        for opponent, my_player in self.states:
            out += self.eval_state(opponent, my_player)

        return out
    
    def simulate_plan(self) -> int:
        res = 0
        winning_choices = {1:2, 3:1, 2:3}
        

        for opponent, my_player in self.states:
            if my_player == "Y":
                res += self.eval_choice(opponent) + 3

            elif my_player == "Z":
                choice = winning_choices[self.eval_choice(opponent)]
                res += choice + 6
            else:
                all_choices = {1, 2, 3}
                o = self.eval_choice(opponent)
                all_choices.discard(o)
                all_choices.discard(winning_choices[o])

                p, *_ = all_choices
                res += p
        return res
                
                
                
            

        
        

if __name__ == "__main__":
    game = RPS("input.txt")
    #res = game.simulate_game()
    res = game.simulate_plan()
    print(res)
            
                
