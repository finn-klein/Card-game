from Game import Game
from Field import Field
from Card import Card
from MonsterCard import MonsterCard
from SpecialyCard import SpecialyCard

def player_select_card(g:Game, p:Player, name=None):
    if name is None:
        condition = lambda c:True
    else:
        condition = lambda c:(c.name == name)
    
    print("Select one of the following cards:")
    i = 0
    for c in g.field[p]:
        if c is not None and condition(c):
            printf("Position %d: %s"%(i, c.name))
        i += 1
    x = input()
    try:
        x = int(x)
        assert (0 <= x and x <= 2)
    except:
        raise ValueError("brooo you just got chupped up by invalid inputs")
    c = g.field.get_card(p, x)
    assert condition(c)
    return c
