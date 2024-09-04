class library():
    gameslist = ["G1", "G2", "G3", "G4"]
    lenders = {}
    donors = {}

    def games(self):
        print(f"{self.gameslist}\n")
    
    def lend(self):
        name = input("Enter your name: ")
        game = input(f"{library.gameslist}\nEnter the name of game you want to lend: ")
        self.gameslist.remove(game)
        self.lenders[name] = game
        print(f"{self.gameslist}\n{self.lenders}\nlend successful\n")

    def returnb(self):
        name = input("Enter your name: ")
        rgame = input("Enter the name of game you want to return: ")
        self.gameslist.append(rgame)
        del self.lenders[name]
        print(f"{self.gameslist}\nreturn successful\n")

    def donate(self):
        name = input("Enter your name: ")
        dgame = input("Enter the name of game you want to donate: ")
        self.gameslist.append(dgame)
        self.donors[name] = dgame
        print(f"{self.gameslist}\n{self.donors}\ndonation successful\n")