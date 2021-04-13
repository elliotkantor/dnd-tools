import random
import pyinputplus as pyip
import re
import pandas as pd


def menu_screen():
    feature_choices = ["dice roller", "fast initiative", "quit"]
    while True:
        print()
        if len(feature_choices) > 1:
            choice = pyip.inputMenu(feature_choices, prompt="Choose a feature:\n", numbered=True)
        else:
            assert feature_choices, "Must exist"
            choice = feature_choices[0]
        
        # navigate to feature
        if choice == feature_choices[0]:
            dice_roller()
        if choice == feature_choices[1]:
            fast_initiative()
        if choice == feature_choices[-1]:
            return


def dice_roller():
    """
    Rolls dice quickly and with DnD format
    """
    print("Dice roller")
    dice_regex = re.compile(r"""
        (\d*)  # 1 in 1d20 (optional)
        (d\d+)  # d10
        (\s*)  # space
        (
            (\+|-)  # plus or minus
            (\s*)  # space
            (\d+)  # bonus
        )?  # optional bonus
        (\s*)  # space
        (a|d)?  # adv or disadv
    """, re.VERBOSE|re.I)
    while True:
        print()
        dice_input_str = input("Roll: ")
        if not dice_input_str:
            return
        mo = dice_regex.search(dice_input_str)
        if mo is None:
            print("Could not understand")
            return

        multiplier, bonus = 1, 0
        if mo.group(1):
            multiplier = int(mo.group(1))
        if mo.group(4):
            # bonus
            if mo.group(5) == "-":
                bonus = -1 * int(mo.group(7))
            else:
                bonus = int(mo.group(7))

        sides = int(mo.group(2)[1:])

        # roll and calculate
        total = 0
        for _ in range(multiplier):
            if not mo.group(8):
                roll = random.randint(1, sides)
                print(f"d{sides} = {roll}")
            else:
                # roll two and take either highest or lowest
                rolls = sorted([random.randint(1, sides) for _ in range(2)])
                if mo.group(8) == "a":
                    roll = rolls[-1]
                else:
                    roll = rolls[0]
                print(f"d{sides} = {', '.join([str(r) for r in rolls])} -> {roll}")
            total += roll
        if multiplier > 1 or bonus != 0:
            if bonus != 0:
                print(f"Total: {total} + {bonus} = {total + bonus}")
            else:
                print(f"Total: {total}")


def fast_initiative():
    """
    Rolls initiative for n players instantly (no modifiers)
    """
    print("Fast initiative")
    print()
    num_players = pyip.inputInt("Number of players: ", blank=True)
    if num_players == "":
        return
    for num in range(num_players):
        print(f"Player {num + 1}: {random.randint(1, 20)}")


def custom_initiative():
    """
    Rolls initiative for all players in characters.csv based on their stats
    """
    char_df = pd.read_csv("characters.csv")
    char_dict = {}
    for i, char in enumerate(char_df["name"]):
        roll = random.randint(1, 20)
        mod = char_df.iloc[i]["initiative_mod"]
        char_dict[char] = roll + mod
        print(f"{char}: {roll} + {mod} = {roll + mod}")

    # show order
    i = 0
    for name, _ in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"Turn {i + 1}: {name}")
        i += 1


if __name__ == "__main__":
    menu_screen()
    print("Thanks for playing")
