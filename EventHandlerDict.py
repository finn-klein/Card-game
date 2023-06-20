def blank_dict():
    event_list = ["targeted_by_effect",
                  "start_of_turn",
                  "end_of_turn",
                  "activate",
                  "summon",
                  "die",
                  "attack",
                  "attacked",
                  "hp_set",
                  "strength_set",
                  "damage",
                  "tribute"]
    out_dict = dict()
    for event in event_list:
        out_dict[event] = False
    return out_dict