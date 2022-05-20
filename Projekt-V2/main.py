from NPC.OpponentBasic import OpponentBasic
from NPC.Player import Player
from SPRZEDAWCA.Sprzedawca import Sprzedawca
from CZARODZIEJKA.Czarodziajka import Czarodziejka
from EVENTS.Events import Events
from KOWAL.Kowal import kowal

def main():
    print("=<>="*20)
    player = Player()
    sprzedawca = Sprzedawca()
    czarodziejka = Czarodziejka()
    Kowal = kowal()
    events = Events()
    game = True
    while game:

        events.envents(player)

        if player.is_the_hero_alive() != True:
            print("=<>="*20)
            print("\t \t \t \t GAME OVER !!!")
            print("=<>="*20)
            break
        # -----------------------------------------------------------------------------------
        print("Eksploruje - e | Statystyki - s ")
        print("Czarodziejka - cz | Sprzedawca - z | Kowal - p |")
        what_are_you_doing = input("Co robisz ")
        if what_are_you_doing.lower() == "e":
            opponent = OpponentBasic()
            player.fight(opponent)
        elif what_are_you_doing.lower() == "s":
            player.statystic()
        # --------------------------------------------------------------
        elif what_are_you_doing.lower() == "z":
            sprzedawca.services()
            what_are_you_doing = input("Co robisz ")
            if what_are_you_doing.lower() == "h":
                sprzedawca.healing(player)
            elif what_are_you_doing.lower() == "m":
                sprzedawca.mana_regeneration(player)
            elif what_are_you_doing.lower() == "n":
                sprzedawca.nie_stac_mnie(player)
            elif what_are_you_doing.lower() == "c":
                sprzedawca.towarzystwo()
            else:
                print("Wybacz przyjacielu, ale nie prowadzę takich usług !")
        # -------------------------------------------------------------- 
        elif what_are_you_doing.lower() == "cz":
            czarodziejka.inf()
            czarodziejka.wizyta(player)
        # -------------------------------------------------------------- 
        elif what_are_you_doing.lower() == "p":
            Kowal.services()
            what_are_you_doing = input("Co robisz ")
            if what_are_you_doing.lower() == "a":
                Kowal.Broń(player)
            elif what_are_you_doing.lower() == "c":
                Kowal.towarzystwo()
        else:
            print("Wybacz przyjacielu, ale nie prowadzę takich usług !")
        # ------------------------------------------------------------
        
            
            

        

        player.level_up()


if __name__ == '__main__':
    main()
else:
    print(f"Error")