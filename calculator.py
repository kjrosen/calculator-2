"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


## repeat forever
while True:
    ## read user input (string of operator, num1, num2)
    ## tokenize (split) input into list, so each entry has an index
    nums = input("""Input some math \nAdd (+), Subtract (-), Multiply (*), Divide (/),
    Square, Cube, Power, or Mod\n > """)
    token = nums.split()

    ## need to turn all indexes after 0 into ints
    if len(token) > 1:
        token[1] = int(token[1])
        if len(token) == 3:
            token[2] = int(token[2])

    ## stop if the user inputs q
    if token[0] == "q":
        print("Bye")
        break

    ## elif use arithmetic functions for other index 0s
    ## add
    elif token[0] == "+":
        print(add(token[1], token[2]))
    ## subtract
    elif token[0] == "-":
        print(subtract(token[1], token[2]))
    ## multiply
    elif token[0] == "*":
        print(multiply(token[1], token[2]))
    ## divide
    elif token[0] == "/":
        print(divide(token[1], token[2]))
    ## square
    elif token[0] == "square":
        print(square(token[1]))
    ## cube
    elif token[0] == "cube":
        print(cube(token[1]))
    ## power
    elif token[0] == "power":
        print(power(token[1], token[2]))
    ## mod
    elif token[0] == "mod":
        print(mod(token[1], token[2]))
        
    print()