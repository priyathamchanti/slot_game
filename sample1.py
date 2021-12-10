from random import *
import time
import sys

Symbol_1 = ''
Symbol_2 = ''
Symbol_3 = ''
bank = 0
current_bet = 0
spin_count = 0
total_won = 0
total_lost = 0


def game_symbols(Symbol1, Symbol2, Symbol3):
    for symbol in (Symbol_1, Symbol_2, Symbol_3):
        sys.stdout.write(symbol)
        sys.stdout.flush()
        time.sleep(0.1)


game_symbols(Symbol_1, Symbol_2, Symbol_3)


def game_loop():
    global Symbol_1, Symbol_2, Symbol_3, bank, current_bet, spin_count, total_lost, total_won
    if bank <= 0:
        print("GAME OVER LOSER!")
    while bank > 0:
        if 0 < current_bet <= bank:
            bet_r = input("\n[ENTER] TO REPEAT BET, 'NO' TO PLACE NEW ONE: ")
            if bet_r == "" or bet_r == "Y":
                bet = current_bet
            else:
                current_bet = 0
                bet = 0
                game_loop()
        else:
            try:
                bet = int(input("PLACE YOUR BET!: "))
            except ValueError:
                return game_loop()

        if 0 <= bet <= bank:
            bank -= bet
            total_lost += bet
            current_bet = bet
            try:
                Symbol1 = ['!', '@', '@', '#', '#', '#', '&', '&', '&', '&', '%', '%', '%', '%', '%']
                Symbol2 = ['!', '@', '@', '#', '#', '#', '&', '&', '&', '&', '%', '%', '%', '%', '%']
                Symbol3 = ['!', '@', '@', '#', '#', '#', '&', '&', '&', '&', '%', '%', '%', '%', '%']
                Symbol_1 = choice(Symbol1)
                Symbol_2 = choice(Symbol2)
                Symbol_3 = choice(Symbol3)
                print("\n-----SPINNING FOR: ${}-----\n".format(current_bet))
                for i in Symbol_1:
                    time.sleep(0.4)
                    print(" (", "<", i, ">", end=' | ', flush=True)
                for i in Symbol_2:
                    time.sleep(0.8)
                    print("<", i, ">", end=' | ', flush=True)
                for i in Symbol_3:
                    time.sleep(1.0)
                    print("<", i, ">", end=' )', flush=True)
                    time.sleep(1.5)
                print("\n")
                print("----------------------------")
                spin_count += 1

                if Symbol_1 == '!' and Symbol_2 == '!' and Symbol_3 == '!':
                    bank += 100 * current_bet
                    total_won += 100 * current_bet
                    print("YOU WON THE JACKPOT!!!: $", 100 * current_bet)
                    print("spin_count", spin_count)
                    exit(0)
                elif Symbol_1 == '@' and Symbol_2 == '@' and Symbol_3 == '@':
                    bank += 50 * current_bet
                    total_won += 50 * current_bet
                    print("YOU WON!!: $", 50 * current_bet)
                elif Symbol_1 == '#' and Symbol_2 == '#' and Symbol_3 == '#':
                    bank += 20 * current_bet
                    total_won += 20 * current_bet
                    print("YOU WON!!: $", 20 * current_bet)
                elif Symbol_1 == '&' and Symbol_2 == '&' and Symbol_3 == '&':
                    bank += 10 * current_bet
                    total_won += 10 * current_bet
                    print("YOU WON!!: $", 10 * current_bet)
                elif Symbol_1 == '%' and Symbol_2 == '%' and Symbol_3 == '%':
                    bank += 5 * current_bet
                    total_won += 5 * current_bet
                    print("YOU WON!!: $", 5 * current_bet)
                elif Symbol_1 == '%' and Symbol_2 == '%':
                    bank += current_bet
                    total_won += current_bet
                    print("YOU WON!!: $", current_bet)
                elif Symbol_1 == '%' and Symbol_3 == "%":
                    bank += current_bet
                    total_won += current_bet
                    print("YOU WON!!: $", current_bet)
                else:
                    pass
                print("\nYour Statistics")
                print("Won: $", total_won, "Spent: $", total_lost, "\nCurrent Balance: $", bank)

            except (Exception):
                pass


def start():
    global bank
    command = input("Balance $1000! \n\nPRESS [ENTER] TO START ")
    if command == "":
        bank = 1000
        game_loop()
    else:
        start()


start()
