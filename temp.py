import time

print(r"""⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠴⠒⠒⠒⠒⠒⠒⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⡀⠀⠀
⠀⣰⠃⠀  ⠀⠀Hello, world!⠀⠀  ⠀⠙⣆⠀
⢰⠃⠀  ⠀                   ⠀⠀⠸⡆
⡟⠀ ⠀  I'm Weather Kitty,⠀  ⠀⣷
⣧⠀  your personal weather⠀ ⠀⡿
⢸⡄⠀⠀⠀⠀   ⠀assistant!⠀  ⠀⠀⠀⠀⢠⠇
⠀⢳⡄ ⠀ ⠀                 ⠀⠀⢠⡯⠁
⠀⠀⠙⢦   It looks like...⠀⢀⡴⠋⠁⠀
⠀⠀⠀⠀⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⠤⢤⣀⠀⠀⠀⠀⠀⢶⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⢦⣝⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣓⠀⠀⠀⠀⠀⠀
                       ⠀ ⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀⠀⠀⠀⠀
                        ⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿⠀⠀⠀⠀
                        ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆⠀⠀⠀
                        ⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽⠀⠀⠀
                        ⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇⠀⠀⠀
                        ⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀⠀⠀
                        ⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒
                        ⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤⠀
                        ⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
                        ⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀
      """)

def print_loading_animation(duration_seconds):
    while True:
        time.sleep(5)
        print("                            Bare with me here <3.", end="\r")
        time.sleep(1)
        print("                            Bare with me here <3..", end="\r")
        time.sleep(1)
        print("                            Bare with me here <3...", end="\r")
        time.sleep(1)

        # Check if the specified duration has elapsed
        if time.time() >= start_time + duration_seconds:
            break

# Specify the duration (in seconds) for the animation
duration_seconds = 1

# Record the start time
start_time = time.time()

# Start the loading animation
print_loading_animation(duration_seconds)

# Print a newline to clear the animation
print()

print("OK! I'm all set up. Just need one more thing...")
time.sleep(1.5)

while True:
    name = input("What's your name? ")
    if name.isalpha():
        break
    else:
        time.sleep(0.5)
        print("I don't think that's right. ", end="")

time.sleep(0.5)
print("Nice to meet you, " + name, end="")
print(". What a beautiful name!")
time.sleep(2)

print("Now let's see...")
time.sleep(2)

print("Okay, no storms...")
time.sleep(1.5)

print("No heavy winds...")
time.sleep(1.5)

print("Weather conditions seem to be normal!")
time.sleep(2)

print("Wait...")
time.sleep(2)

print("Oh no! My thermometer seems to be broken!")
time.sleep(2)

print("I'm going to need your help... ", end="")

while True:
    try:
        temp = float(input("What's the temperature outside? "))
        if temp <= 32:
            if temp <= -10:
                time.sleep(1.5)
                print("That's extremely cold!")
                time.sleep(2)
                print("You might want to stay inside.\n")
            else:
                time.sleep(1.5)
                print("OMG! Snow weather!")
                time.sleep(2)
                print("Have fun out there, but be careful. <3\n")
        elif temp < 60:
            time.sleep(1.5)
            print("It's cold outside.")
            time.sleep(2)
            print("Wear warm clothes and try not to get sick!")
        elif temp > 80:
            if temp >= 103:
                time.sleep(1.5)
                print("It's extremely hot outside!")
                time.sleep(2)
                print("Please be extra careful.")
            else:
                time.sleep(1.5)
                print("Whew, it's hot outside!")
                time.sleep(2)
                print("Be sure to stay hydrated!")
        else:
            time.sleep(1.5)
            print("Oh, it's nice outside.")
            time.sleep(2)
            print("Go for a walk or swim!")
        break
    except ValueError:
        print("Hmm, that's not quite right.\nLet's try again! ", end="")
time.sleep(3)
print("Thank you so much for helping me, by the way!")
time.sleep(2)
print("I'm so glad that I get to be your friend.")
time.sleep(2)
print("It gets lonely here inside of this computer sometimes...")
time.sleep(2)
print("Don't be a stranger! I'm always here for you when you need me. Until next time, " + name, end="")
print(" <3")
time.sleep(5)
