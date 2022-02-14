from athlete.Boxer import Boxer
from athlete.Swimmer import Swimmer

def main():
    boxer1= Boxer("Floyd Mayweather", "02/24/1977", "USA", ["Gold", "Silver"], "Heavy weight", [50,0])
    print(boxer1)
    swimmer1=Swimmer("Michael Phelps", "08/12/1980", "UK", ["Gold", "Bronze", "Gold", "Gold"],["Freestyle"])
    print(swimmer1)
    swimmer1.add_strokes("Breaststroke")
    boxer1.win_fight()
    print(boxer1.lose_fight())
    boxer1.win_fight()
    print(boxer1)
    print(swimmer1)

if __name__ == "__main__":
    main()