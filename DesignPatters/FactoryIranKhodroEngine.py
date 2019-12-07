from abc import ABC, abstractmethod


class IranKhodro(ABC):

    @abstractmethod
    def engine(self):
        pass


class Samand(IranKhodro):
    def engine(self):
        print("man Samandam!")


class Pejo207(IranKhodro):
    def engine(self):
        print("man Pejo207am")


class Rona(IranKhodro):
    def engine(self):
        print("Samand ba peride tarkib shod")


class IranKhodroEngineFactory:
    def __init__(self):
        self.typeEngine = input("che motori mikhay(Samand or Pejo27 or Rona)?")
        eval(self.typeEngine)().engine()


if __name__ == "__main__":
    f = IranKhodroEngineFactory()
