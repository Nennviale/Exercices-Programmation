
print('Debut du jeu')

def print_state(repr3):
    state_str = ''

    for element in repr3:
        if element == True:
            state_str = state_str + '1'
        else:
            state_str = state_str + '-'

    print(state_str)
    return

state = [False, False, False, True, False, False, False, False, False, False, ]
print_state(repr3=state)

other_state = [True, False, False, False, False, False, False, False, False, False, ]
print_state(repr3=other_state)


