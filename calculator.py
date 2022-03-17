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

    ##removes the operator from the list so only nums are left
    operator = token[0]
    token.pop(0)

    ## need to turn all indexes after 0 into ints
    for num in range(len(token)):
        token[num] = int(token[num])

    ## stop if the user inputs q
    if operator == "q":
        print("Bye")
        break

    ## elif use arithmetic functions for other index 0s
    ## add
    elif operator == "+":
        print(add(token))
    ## subtract
    elif operator == "-":
        print(subtract(token))
    ## multiply
    elif operator == "*":
        print(multiply(token))
    ## divide
    elif operator == "/":
        print(divide(token))
    ## square
    elif operator == "square":
        print(square(token[1]))
    ## cube
    elif operator == "cube":
        print(cube(token[1]))
    ## power
    elif operator == "power":
        print(power(token[1], token[2]))
    ## mod
    elif operator == "mod":
        print(mod(token[1], token[2]))
        
    print()