class Father:
    def property(self):
        print("Father Property")

    def business(self):
        print("Father Business")


class Son(Father):
    def study(self):
        print("Son Studies")


class Daughter(Father):
    def dance(self):
        print("Daughter Dances")


class GrandChild(Son, Daughter):
    def gaming(self):
        print("Gaming")


g = GrandChild()
g.property()  # From Father
g.business()  # From Father
g.study()  # From Son
g.dance()  # From Daughter
g.gaming()  # From GrandChild
