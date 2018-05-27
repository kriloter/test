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
        self.__setMessage(message)

    def strike(self, enemy):
        """

        :return:
        """
        punch = self.__attack + self.__cube.throw()
        enemy.defend(punch)

    def __setMessage(self, message):
        """

        :param message:
        :return:
        """
        self.__message = message

    def getLastMessage(self):
        return self.__message


cube = Cube(10)
fighter = Character("bazmeg", 100, 10, 8, cube)
print("Bojovnik: {0}".format(fighter))
print("Nazive: {0}".format(fighter.alive))
print("Zivot: {0}".format(fighter.healthGraph()))
fighter.strike(fighter)
print("Zivot: {0}".format(fighter.healthGraph()))
