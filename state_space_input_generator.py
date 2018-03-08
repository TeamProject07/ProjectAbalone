'''
Copyright (C) BCIT AI/ML Option 2018 Team with Members Following - All Rights Reserved.
- Jake Jonghun Choi     jchoi179@my.bcit.ca
- Justin Carey          justinthomascarey@gmail.com
- Pashan Irani          pashanirani@gmail.com
- Tony Huang	        tonyhuang1996@hotmail.ca
- Chil Yuqing Qiu       yuqingqiu93@gmail.com
Unauthorized copying of this file, via any medium is strictly prohibited.
Written by Pashan Irani <pashanirani@gmail.com>
'''


import random, os

LETTERS = "ABCDEFGHI"
COLORS = "bw"
PIECES_PER_PLAYER = 14
BLACK_COUNT = random.randint(1, PIECES_PER_PLAYER)
WHITE_COUNT = random.randint(1, PIECES_PER_PLAYER)

# The entry point of this file.
if __name__ == '__main__':

    # Join the path with the complete file name.
    complete_path = os.path.join('ssg_tester_generated_inputs', "input.gen")

    # Open the file for writing.
    file = open(complete_path, "w")
    output = ""

    used_spots = set()

    #decide turn
    if random.randint(0, 1) == 0:
        output += "w\n"
    else:
        output += "b\n"

    # get random locations
    while WHITE_COUNT != 0 and BLACK_COUNT != 0:
        row = random.choice(LETTERS)
        col = str(random.randint(1, 9))
        color = random.choice(COLORS)
        spot = row + col + color

        if spot not in used_spots:
            output += spot

            if color == "b":
                BLACK_COUNT -= 1
            elif color == "w":
                WHITE_COUNT -= 1

            if BLACK_COUNT == 0 or WHITE_COUNT == 0:
                continue

            output += ", "

        used_spots.add(spot)

    # Write to the file and close it.
    file.write(output)
    file.close()











