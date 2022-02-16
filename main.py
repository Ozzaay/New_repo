import resources
from resources import Character, Goblin
from random import randint, shuffle




def fight(players: list, enemies: list):
    participants = players+enemies
    shuffle(participants)
    for char in participants:
        target = ""
        # Is the character a player or an enemy
        if char in players:
            target = choice(enemies)
        else:
            target = choice(players)
        target.take_damage(char.get_attack())
        if target.get_hp == 0:
            print(f"{target.get_name()} has died.")
            if type(target) == Goblin:
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} has {target.get_health} hp left.")
        if len(players) == 0 or len(enemies) == 0:
            break


if __name__ == "__main__":
    nemy = Character("Nemy", 20, 5, 2)
    goblin_one = Goblin(10, 3, 1)
    players.append(nemy)
    print(nemy)
    print()
    print(goblin_one)
    
    fight_round = 1
    print("=========FIGHT=========")
    while nemy.get_health() != 0 and goblin_one.get_health != 0:
        print(f"Round {fight_round}")
        nemy_attack = nemy.get_attack()*randint(1,3)
        goblin_one.take_damage(nemy_attack)
        if(goblin_one.get_health() == 0):
            print("Goblin has died.")
            break
        else:
            print(f"Goblin has {goblin_one.get_health()} hp left.")
            goblin_attack = goblin_one.damage()*randint(1,4)
            nemy.take_damage(goblin_attack)
            print(f"Nemy has {nemy.get_health()} hp left.")
            if(nemy.get_health() == 0): print("Nemy has died.")
        fight_round += 1
    
    if(nemy.get_health() == 0): print("The Goblin won!")
    else: print("Nemy has won!")
        
