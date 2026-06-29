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


def create_hall_of_fame(hunts):
    hall_of_fame = [get_character_name(hunt[1]) for hunt in hunts if hunt[3]]

    return hall_of_fame


def get_character_name(player_id):
    for player, name in players:
        if player == player_id:
            return name
