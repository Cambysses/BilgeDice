from player import *
from die import *
from ascii import ascii_list


def draw_die(dice):

    # Draws each die line-by-line.
    line_index = 0
    for i in range(4):
        for die in dice:
            print(f"{ascii_list[die.value][line_index]} ", end="")
        print("")
        line_index += 1
    for die in dice:
        print(f"   {die.value}    ", end="")


def draw_board(rolled_dice, player):

    print("\n" * 50)
    print("\n               BILGE DICE!")
    print("Your rolls:")
    draw_die(rolled_dice)
    print("")
    print("Your dice:")
    draw_die(player.dice)
    print("")
    print("Qualifiers:")
    draw_die(player.qualifiers)
    print("")
    print(f"Total: {score(player.dice)}\n")


def score(dice):

    total_value = 0
    for die in dice:
        total_value += die.value
    return total_value


def pick_keepers(rolled_dice, player):

    dice_to_keep = input("Which dice would you like to keep?: ")
    dice_to_keep = dice_to_keep.split(",")
    dice_to_keep = [int(keeper) for keeper in dice_to_keep]
    for keeper in sorted(dice_to_keep, reverse=True):
        player.add_die(rolled_dice[keeper-1])
        rolled_dice.pop(keeper-1)


def main():

    # Initialize player and roll first dice.
    player = Player()
    rolled_dice = [Die(), Die(), Die(), Die(), Die(), Die()]

    while 1:
        draw_board(rolled_dice, player)
        pick_keepers(rolled_dice, player)


if __name__ == '__main__':
    main()
