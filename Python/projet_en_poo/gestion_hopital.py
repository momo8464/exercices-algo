class hopital:
    def __init__(self,lit,malade,gueri):
        self.lit=lit
        self.malade=malade
        self.gueri=gueri
    def presenter(self,nombre):
        self.malade+=nombre
        print(f"Le nombre de malade est : {self.malade}")

hopital_1= hopital(lit=100, malade=20, gueri=100)
hopital_1.presenter(500)