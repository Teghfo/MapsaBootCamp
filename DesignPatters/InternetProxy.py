from abc import ABCMeta, abstractmethod


class Internet(metaclass=ABCMeta):

    @abstractmethod
    def connetcting(self, URL):
        pass


class RealInternet(Internet):
    def connetcting(self, URL):
        print("{} is OK:)) .connected!".format(URL))


class Proxy(Internet):
    def __init__(self):
        self.__internet = RealInternet()
        self.__bannedList = []

    def appendBanned(self, bannedSite):
        self.__bannedList.append(bannedSite)

    def connetcting(self, URL):
        if URL in self.__bannedList:
            print("banned!")

        else:
            self.__internet.connetcting(URL)


class Client:
    def __init__(self):
        self.internet = Proxy()
        self.internet.appendBanned("google.com")

    def connect(self, URL):
        self.internet.connetcting(URL)


if __name__ == "__main__":
    internet = Client()
    internet.connect('parsijoo.ir')
