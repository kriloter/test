# my first game
# @kriloter

class Cube:
    """
    playing cube with custom number of sides
    """
    def __init__(self, sides = 6):
        """
        Cube init
        :param sides: number of sides
        """
        self.__sides = sides

    def __str__(self):
        """
        Cube text overlay
        :return:
        """
        return str("Cube with {0} sides.".format(self.__sides))

    def throw(self):
        """
        throw the cube
        :return: random integer number of range (1, self.__sides)
        """
        import random as _random
        return _random.randint(1, self.__sides)

class Character:
    """
    game character
    """
    def __init__(self, name, maxHealth, attack, defense, cube):
        """
        :param name:
        :param maxHealth:
        :param attack:
        :param defense:
        :param cube:
        """
        self.__name = name
        self.__maxHealth = maxHealth
        self.__health = maxHealth
        self.__attack = attack
        self.__defense = defense
        self.__cube = cube
        self.__message = ""

    def __str__(self):
        """
        character name overlay
        :return:
        """
        return str("{0}".format(self.__name))

    @property
    def alive(self):
        """
        character alive
        :return:
        """
        return self.__health >0

    def healthGraph(self):
        """
        character graphic health
        :return:
        """
        maxBar = 20
        countBar = int(self.__health / self.__maxHealth * maxBar)
        if (self.alive and countBar ==0):
            countBar = 1
        return "[{0}{1}]".format("#"*countBar, " "*(maxBar - countBar))

    def defend(self, strike):
        """

        :param strike:
        :return:
        """
        wound = strike - (self.__defense + self.__cube.throw())
        if wound > 0:
            message = "{0} utrzil zranenie {1}hp.".format(self.__name, wound)
            self.__health = self.__health - wound
            if self.__health < 0:
                self.__health = 0
                message = message[:-1] + " a skapal."
        else:
            message = "{0} odrazil utok.".format(self.__name)
        self.__setMessage(message)

    def strike(self, enemy):
        """

        :param enemy:
        :return:
        """
        strike = self.__attack + self.__cube.throw()
        message = "{0} utoci s uderom za {1}hp.".format(self.__name, strike)
        self.__setMessage(message)
        enemy.defend(strike)

    def __setMessage(self, message):
        """

        :return:
        """
        self.__message = message

    def getLastMessage(self):
        return self.__message

class Arena:
    """

    """
    def __init__(self,fighter1, fighter2):
        self.__fighter1 =fighter1
        self.__fighter2 = fighter2

    def print(self):
        """

        :return:
        """
        self.clearScreen()
        print("---------- ARENA ---------- \n")
        print("{0} : {1}".format(self.__fighter1, self.__fighter1.healthGraph()))
        print("{0} : {1}".format(self.__fighter2, self.__fighter2.healthGraph()))

    def printMessage(self, message):
        self.__message = message
        import time as _time
        _time.sleep(1)
        print(self.__message)
        _time.sleep(1)

    def clearScreen(self):
        """

        :return:
        """
        import sys as _sys
        import subprocess as _subprocess
        _subprocess.call(["cmd.exe","/C","cls"])

    def match(self):
        """

        :return:
        """
        self.clearScreen()
        print("---------- ARENA ----------")
        print("Vitajte v nasej arene!")
        print("Dnes sa v suboji stretnu {0} a {1}!".format(self.__fighter1, self.__fighter2), "\n")
        input()
        while (self.__fighter1.alive and self.__fighter2.alive):
            self.__fighter1.strike(self.__fighter2)
            self.print()
            self.printMessage(self.__fighter1.getLastMessage())
            self.printMessage(self.__fighter2.getLastMessage())
            self.__fighter2.strike(self.__fighter1)
            self.print()
            self.printMessage(self.__fighter2.getLastMessage())
            self.printMessage(self.__fighter1.getLastMessage())

kocka = Cube(10)
fighter1 = Character("banan",100,10,8,kocka)
fighter2 = Character("alojz",100,10,8,kocka)
arena1 =Arena(fighter1, fighter2)
arena1.match()
input()
