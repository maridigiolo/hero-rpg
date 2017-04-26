#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
#Step 6
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
#Step 7
    def alive(self):
        if self.health > 0:
            return True

#Step 1
class Hero(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

#Step 2  -  Hero attacks goblin
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))


#Step 3  -  Hero attacks goblin
class Goblin(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

hero = Hero(10,5)
goblin = Goblin(6,2)
#----
#Original
def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

# Step 4
    # while goblin.health > 0 and hero.health > 0:
    while goblin.alive() and hero.alive():

# Step 5
        hero.print_status()
        goblin.print_status()
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
        # Hero attacks goblin
            hero.attack(goblin)
            # goblin_health -= hero_power
    #         print("You do {} damage to the goblin.".format(hero_power))
    #         if goblin_health <= 0:
    #             print("The goblin is dead.")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.health > 0:
        #     # Goblin attacks hero
            goblin.attack(hero)
        #     hero.health -= goblin.power
        #     print("The goblin does {} damage to you.".format(goblin_power))
        #     if hero_health <= 0:
        #         print("You are dead.")

if __name__ == "__main__":
  main()

  Comment to be different
  
