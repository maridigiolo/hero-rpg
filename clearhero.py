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
    def attack(self, goblin):
        super().attack(goblin)
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")

    def attackz(self, zombie):
        super().attack(zombie)
        print("You do {} damage to the zombie.".format(self.power))
        print("He is still alive, better flee")


class Goblin(Character):
    def attack(self, hero):
        super().attack(hero)
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")

class Zombie(Character):
    def attack(self, hero):
        super().attack(hero)
        print("The zombie does {} damage to you.".format(zombie.power))
        if hero.health <= 0:
            print("You are dead.")

hero = Hero('You', 10, 2)
goblin = Goblin('Goblin', 6, 2)
zombie = Zombie('Zombie', 1, 1)

def main():
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        # zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight zombie")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            hero.attack(goblin)

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


if __name__ == "__main__":
  main()
