from abc import ABC, abstractmethod


class Context:
    def __init__(self, **kwargs):
        self.nameList = []
        self.methods = []
        for name, impl in kwargs.items():
            setattr(self, name, impl)
            self.nameList.append(name)

    def context_interface(self):
        for name in self.nameList:
            self.methods.append(getattr(self, name).strategy_interface())


class Strategy(ABC):

    @abstractmethod
    def strategy_interface(self):
        pass


class Bomb(Strategy):
    def strategy_interface(self):
        print("bomb andazam!")


class Chagho(Strategy):
    def strategy_interface(self):
        print("chagho kesham!")


class Tank(Strategy):
    def strategy_interface(self):
        print("Khompare andazam!")


def client():
    bomb = Bomb()
    chagho = Chagho()

    # Just pass Method to the Context
    # ashkan = Context(bomb=bomb.strategy_interface,
    #                  chagho=chagho.strategy_interface)
    ashkan = Context(bomb=bomb, chagho=chagho)
    # ashkan.chagho()


if __name__ == "__main__":
    client()
