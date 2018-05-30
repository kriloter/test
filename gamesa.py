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

    #      self.__message = message

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
            self.__health = self.__health - wound
            if self.__health < 0:
                self.__health = 0

    def strike(self, enemy):
        """

        :param enemy:
        :return:
        """
        strike = self.__attack + self.__cube.throw()
        enemy.defend(strike)

    def setMessage(self):
        pass

    def getMessage(self):
        pass


class Arena:
    """

    """

    def __init__(self, character1, character2):
        """

        :param character1:
        :param character2:
        """
        self.__character1 = character1
        self.__character2 = character2

    def match(self):
        """

        :return:
        """
        while self.__character2.alive:
            self.__character1.strike(self.__character2)
