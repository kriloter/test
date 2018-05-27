class Cube:
    """
    pokec
    """

    def __init__(self, sidesCount=6):
        self.__sidesCount = sidesCount

    def returnSidesCount(self):
        """
        pokec
        """
        return self.__sidesCount

    def throw(self):
        """
        pokec
        :return:
        """
        import random as _random
        return _random.randint(1, self.__sidesCount)

    def __str__(self):
        """

        :return:
        """
        return str("Cube with {0} sides".format(self.__sidesCount))


class Character:
    """
    pokec
    """

    def __init__(self, name, health, attack, defense, cube):
        """
        pokec
        :param name:
        :param health:
        :param attack:
        :param defense:
        :param cube:
        """
        self.__name = name
        self.__maxHealth = health
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        self.__cube = cube
        self.__message = ""

    def __str__(self):
        """
        pokec
        :return:
        """
        return str(self.__name)

    @property
    def alive(self):
        """
        pokec
        :return:
        """
        return self.__health > 0

    def healthGraph(self):
        """
        pokec
        :return:
        """
        barsMax = 20
        bars = int(self.__health / self.__maxHealth * barsMax)
        if bars == 0 and self.alive():
            bars = 1
        return "[{0}{1}]".format("#" * bars, " " * (barsMax - bars))

    def defend(self, punch):
        """
        pokec
        :param punch:
        :return:
        """
        wound = punch - (self.__defense + self.__cube.throw())
        if wound > 0:
            message = "{0} utrzil zranenie {1}hp".format(self.__name, wound)
            self.__health = self.__health - wound
            if self.__health < 0:
                self.__health = 0
                message = message[:-1] + "a skapal"
        else:
            message = "{0} odrazil utok".format(self.__name)
        self.__setMessage(message)

    def strike(self, enemy):
        """

        :return:
        """
        punch = self.__attack + self.__cube.throw()
        message = "{0} utoci s uderom za {1}hp".format(self.__name, punch)
        self.__setMessage(message)
        enemy.defend(punch)

    def __setMessage(self, message):
        """

        :param message:
        :return:
        """
        self.__message = message

    def getLastMessage(self):
        return self.__message

class arena:
    '''

    '''
    def __init__(self, fighter1, fighter2, cube):
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2
        self.__cube = cube

    def clearScreen(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    def printScreen(self):
        self.clearScreen()
        print("---------- ARENA ---------- \n")
        print("Zdravie bojovnikov: \n")

'''
cube = Cube(10)
fighter = Character("bazmeg", 100, 10, 8, cube)
fighter2 = Character("onan", 100, 8, 10, cube)
print("Bojovnik: {0}".format(fighter))
print("Nazive: {0}".format(fighter.alive))
print("Zivot: {0}".format(fighter.healthGraph()))
print("\n")
print("Bojovnik: {0}".format(fighter2))
print("Nazive: {0}".format(fighter2.alive))
print("Zivot: {0}".format(fighter2.healthGraph()))
print("\n")
fighter.strike(fighter2)
print(fighter.getLastMessage())
print(fighter2.getLastMessage())
print("Zivot: {0}".format(fighter2.healthGraph()))
'''
