def create_hall_of_fame(hunts):
    pass


# don't touch below this line


def get_character_name(player_id):
    players = [
        (1, "Vin"),
        (2, "Kelsier"),
        (3, "Elend"),
        (4, "Sazed"),
        (5, "Ham"),
        (6, "Dockson"),
        (7, "Breeze"),
        (8, "Lestibournes"),
    ]

    for player, name in players:
        if player == player_id:
            return name
