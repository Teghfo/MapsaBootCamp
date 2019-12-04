class A:

    def __init__(self):
        pass

    __instance = None

    def __new__(cls):
        if not A.__instance:
            A.__instance = super().__new__(cls)
        return A.__instance
