print("Welcome to my extended adventure game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10
gold = 0

if age >= 18:
    print(f"Hello, {name}! You are old enough to play!")

    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health and", gold, "gold.")
        print("Let’s begin the adventure!")

        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around? (across/around) ").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake.")
                print("You find a small cabin nearby. Do you approach the cabin or keep walking? (cabin/walk) ")
                cabin_or_walk = input().lower()

                if cabin_or_walk == "cabin":
                    print("You knock on the door, and an old man invites you inside.")
                    print("He offers you some tea. Do you accept or decline? (accept/decline) ")
                    tea = input().lower()

                    if tea == "accept":
                        print("You drink the tea and feel stronger. Your health increases by 5!")
                        health += 5
                    else:
                        print("The old man looks disappointed, but you decide to leave.")
                        print("Your health remains the same.")

                    print("You leave the cabin and head back to the main path.")
                    print("Soon, you encounter a fork in the road again. Do you go left or right? (left/right) ")
                    new_choice = input().lower()

                    if new_choice == "left":
                        print("You go left and find a beautiful meadow. You decide to rest.")
                        print("While resting, you hear something approaching. Do you investigate or hide? (investigate/hide) ")
                        investigate_or_hide = input().lower()

                        if investigate_or_hide == "investigate":
                            print("You find a friendly traveler who shares some food with you. Your health increases by 3!")
                            health += 3
                        else:
                            print("You hide, and the noise passes. You avoid danger, but your health doesn't improve.")
                    else:
                        print("You go right and find yourself in a dark forest. It's difficult to navigate.")
                        print("Suddenly, you hear growling. Do you run or fight? (run/fight) ")
                        fight_or_run = input().lower()

                        if fight_or_run == "fight":
                            print("You bravely fight a wild animal and win, but you lose 3 health in the process.")
                            health -= 3
                        else:
                            print("You run and escape safely, but you lose some stamina. Your health is slightly affected.")
                            health -= 1

                else:
                    print("You continue walking and find a mysterious cave. Do you enter or keep walking? (enter/walk) ")
                    cave_or_walk = input().lower()

                    if cave_or_walk == "enter":
                        print("You enter the cave and find some treasure. You gain 10 gold!")
                        gold += 10
                        print("But as you take the gold, the cave begins to collapse! You barely escape but lose 2 health.")
                        health -= 2
                    else:
                        print("You keep walking and find yourself at a dead end. You turn back.")
                        print("You decide to rest and regain some strength. Your health increases by 2.")
                        health += 2

            elif ans == "across":
                print("You managed to get across, but were bitten by a fish and lost 5 health.")
                health -= 5

                ans = input("You notice a house and a river. Which do you go to? (river/house) ").lower()
                if ans == "house":
                    print("You go to the house and are greeted by the owner. He doesn't like you and you lose 5 health.")
                    health -= 5

                    if health <= 0:
                        print("You now have 0 health and lost the game...")
                    else:
                        print("You survived the encounter... but now, what next?")
                        print("The house has a garden with two paths. One leads to a dark forest, and the other to a village. Which do you choose? (forest/village) ")
                        choice = input().lower()

                        if choice == "forest":
                            print("You enter the forest and find some magical mushrooms. You eat them and feel revitalized. Your health increases by 7!")
                            health += 7
                        else:
                            print("You go to the village and meet a healer. She gives you a potion that heals you by 5 health.")
                            health += 5

                else:
                    print("You fall into the river and lose the game. Better luck next time!")

        else:
            print("You fall into the river and lose the game. Better luck next time!")

        # New Path
        print("You decide to explore further...")
        print("You come across an old marketplace. A merchant offers you a magical amulet for 5 gold.")
        buy_amulet = input("Do you want to buy the amulet? (yes/no) ").lower()
        if buy_amulet == "yes":
            if gold >= 5:
                print("You buy the amulet! It grants you protection from one dangerous encounter. You now have", gold - 5, "gold left.")
                gold -= 5
            else:
                print("You don't have enough gold to buy the amulet. The merchant seems disappointed.")
        else:
            print("You decline the offer and continue your journey.")

        # Additional Encounter
        print("While walking, you encounter a strange figure in a cloak. They offer to tell your fortune for 3 gold.")
        tell_fortune = input("Do you want to hear your fortune? (yes/no) ").lower()
        if tell_fortune == "yes":
            if gold >= 3:
                print("The figure gazes into a crystal ball and says: 'Beware of the forest ahead, danger lurks there.' You feel a chill run down your spine.")
                gold -= 3
            else:
                print("You don't have enough gold, and the figure disappears into the mist.")
        else:
            print("You continue on your journey, keeping your gold for something else.")

        # Final Encounter
        print("You approach a huge castle. It seems abandoned, but there’s a light flickering in the tower. Do you enter or walk away? (enter/walk) ")
        castle_choice = input().lower()

        if castle_choice == "enter":
            print("Inside the castle, you find a sleeping dragon guarding a chest. You can either sneak past it or try to fight it. (sneak/fight) ")
            dragon_choice = input().lower()

            if dragon_choice == "sneak":
                print("You carefully sneak past the dragon and open the chest. Inside, you find a legendary sword that increases your health by 10!")
                health += 10
                print("Congratulations, you now have the power to defeat any enemy!")
            else:
                print("You try to fight the dragon, but it awakens and breathes fire at you. You lose 5 health.")
                health -= 5
                if health <= 0:
                    print("You succumb to the dragon's flames and lose the game.")
                else:
                    print("You narrowly escape, but you're badly burned.")

        else:
            print("You walk away from the castle and return home. It was a long journey, but at least you’re alive!")

    else:
        print("BYE BYE!")

else:
    print("You are not old enough to play.....")
