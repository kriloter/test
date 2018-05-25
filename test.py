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

    def defend(self, strike):
        """
        pokec
        :param strike:
        :return:
        """
        wound = strike - (self.__defense + self.__cube.throw())

    def strike(self):
        """

        :return:
        """
        pass


kocka = Cube()
kocka2 = Cube(10)

print(kocka)
for _ in range(10):
    print(kocka.throw(), end=" ")
print("\n", kocka2)
for _ in range(10):
    print(kocka2.throw(), end=" ")

banan = Character("BaNaN", 100, 8, 4, kocka)
onan = Character("OnaN", 100, 6, 10, kocka)
print("\n")
print(banan, banan.alive, kocka, kocka.throw())
print(banan.healthGraph())
print(onan, banan.alive, kocka2, kocka2.throw())
print("zivot: ", onan.healthGraph())
