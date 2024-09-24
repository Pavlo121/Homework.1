default_time = 60

def training_session(num_rounds):
    for round_num in range(1, num_rounds + 1):
        user_input = input(f"Раунд {round_num}: Введіть тривалість хвилини: ")
        time_per_round = int(user_input) if user_input.strip() else default_time
        print(f"Раунд {round_num}: {time_per_round} хвилин")

training_session(3)


