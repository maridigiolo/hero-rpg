#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
#Step 6
class Character:
    def __init__(self,name, health, power):
        self.name = name
        self.health = health
        self.power = power
#Step 7
    def alive(self):
        if self.health > 0:
            return True

#Step 7 - Challenge
    def attack(self, enemy):
        enemy.health -= self.power


    def print_status(self):
        print("{} have {} health and {} power.".format(self.name, self.health, self.power))

#Step 1
class Hero(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

#Step 2  -  Hero attacks goblin
    def attack(self, goblin):
        # goblin.health -= self.power
        super().attack(goblin)
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")


    def attackz(self, zombie):
        # zombie.health -= self.power
        super().attack(zombie)
        print("You do {} damage to the zombie.".format(self.power))
        print("He is still alive, better flee")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    # def print_status(self):
    #     print("You have {} health and {} power.".format(self.health, self.power))


#Step 3  -  Hero attacks goblin
class Goblin(Character):
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    def attack(self, hero):
        # hero.health -= goblin.power
        super().attack(hero)
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    # def print_status(self):
    #     print("You have {} health and {} power.".format(self.health, self.power))

class Zombie(Character):
    def attack(self, hero):
        super().attack(hero)
        print("The zombie does {} damage to you.".format(zombie.power))
        if hero.health <= 0:
            print("You are dead.")

hero = Hero('You', 10, 2)
goblin = Goblin('Goblin', 6, 2)
zombie = Zombie('Zombie', 1, 1)
#----
#Original
def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

# Step 4
    # while goblin.health > 0 and hero.health > 0:
    while goblin.alive() and hero.alive:

# Step 5
        hero.print_status()
        goblin.print_status()
        #zombie.print_status()
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight zombie")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
        # Hero attacks goblin
            hero.attack(goblin)
            # goblin_health -= hero_power
    #         print("You do {} damage to the goblin.".format(hero_power))
    #         if goblin_health <= 0:
    #             print("The goblin is dead.")
            if goblin.health > 0:
                goblin.attack(hero)

        elif inpt == "2":
            if goblin.health > 0:
                goblin.attack(hero)
        elif inpt == "3":
            print("Goodbye.")
            break
        elif inpt == "4":
            hero.attackz(zombie)
            if zombie.health > 0:
                zombie.attack(hero)
        else:
            print("Invalid inpt {}".format(inpt))

        # if goblin.health > 0:
        # #     # Goblin attacks hero
        #     goblin.attack(hero)
        #     hero.health -= goblin.power
        #     print("The goblin does {} damage to you.".format(goblin_power))
        #     if hero_health <= 0:
        #         print("You are dead.")
        # if zombie.health > 0:
        #     zombie.attack(hero)
if __name__ == "__main__":
  main()
