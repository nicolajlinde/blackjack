import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == "y":
        print(art.logo)

        ai_c1 = random.choice(cards)
        ai_c2 = random.choice(cards)
        ai_collector = [ai_c1 + ai_c2]
        ai_res = ai_c1 + ai_c2

        while ai_res < 15:
            ai_c3 = random.choice(cards)
            ai_collector.append(ai_c3)
            ai_res += ai_c3

        if ai_res > 21:
            ai_collector[0] = 1

        p_c1 = random.choice(cards)
        p_c2 = random.choice(cards)
        p_collector = [p_c1, p_c2]
        p_res = p_c1 + p_c2

        print(f"Your cards {p_collector}, the current score is {p_res}")
        print(f"Dealers first card: {ai_c1}")

        try_your_luck = False
        while not try_your_luck:
            cont_play = input("Type 'y' to get another card or type 'n' to pass: ").lower()

            if cont_play == "y":
                p_c3 = random.choice(cards)
                p_collector.append(p_c3)
                p_res += p_c3

                # if p_res > 21:
                #     p_collector[0] = 1
                # else:
                print(f"Your cards {p_collector}, the current score is {p_res}")
                if p_res > 21:
                    try_your_luck = True
                    print(f"Your score is {p_res}, that means it's over 21 and you've lost!")
            else:
                try_your_luck = True
                print(f"Your final hand is: {p_collector}")
                print(f"The dealer final hand is {ai_collector}")

                if p_res == ai_res:
                    print(f"It's a tie.\nYour hand is {p_res}\nDealers hand is {ai_res}")
                elif p_res > ai_res:
                    print(f"You win!\nYour hand is {p_res}\nDealers hand is {ai_res}")
                else:
                    print(f"You lost!\nYour hand is {p_res}\nDealers hand is {ai_res}")


blackjack()
