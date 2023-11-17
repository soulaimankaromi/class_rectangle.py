class Rectangle() :
    def __init__(self) :
        self.largeur=4.2
        self.longueur=6.2
    def perimetre(self) :
        return 2*(self.largeur+self.longueur)
    def Aire(self) :
        return self.longueur*self.largeur
    def IsCarre(self) :
        if self.longueur==self.largeur :
            return True
        else :
            return False
    def AfficherRectangle(self):
            print("La longueur est: ",self.longueur)
            print("La largeur est: ",self.largeur)
            print("Le perimetre est:",self.perimetre())
            print("L'aire est:",self.Aire())
            if self.IsCarre()==True :
                print("Ce regtangle est un carre.")
            else:
                print("Ce regtangle est un regtangle.")

