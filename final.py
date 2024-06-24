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

def sleep(message, seconds):
    print(message)
    time.sleep(seconds)

def sleep_loading(message, seconds):
    print(message, end="\r")
    time.sleep(seconds)

def loading():
    while True:
        sleep_loading("                            Bare with me here <3.", 1)
        sleep_loading("                            Bare with me here <3..", 1)
        sleep_loading("                            Bare with me here <3...", 1)
        break

time.sleep(5)
loading()
sleep("\nOK! I'm all set up. Just need one more thing...", 1.5)

while True:
    name = input("What's your name? ")
    if name.isalpha():
        break
    else:
        time.sleep(0.5)
        print("I don't think that's right. ", end="")

time.sleep(0.5)
sleep(f"Nice to meet you, {name}. What a beautiful name!", 2)
sleep("Now let's see...", 2)
sleep("Okay, no storms...", 1.5)
sleep("No heavy winds...", 1.5)
sleep("Weather conditions seem to be normal!", 2)
sleep("Wait...", 2)
sleep("Oh no! My thermometer seems to be broken!", 2)
print("I'm going to need your help... ", end="")

while True:
    try:
        temp = float(input("What's the temperature outside? "))
        if temp <= 32:
            if temp <= -10:
                time.sleep(1.5)
                sleep("That's extremely cold!", 2)
                print("You might want to stay inside.\n")
            else:
                time.sleep(1.5)
                sleep("OMG! Snow weather!", 2)
                print("Have fun out there, but be careful. <3\n")
        elif temp < 60:
            time.sleep(1.5)
            sleep("It's cold outside.", 2)
            print("Wear warm clothes and try not to get sick!")
        elif temp > 80:
            if temp >= 103:
                time.sleep(1.5)
                sleep("It's extremely hot outside!", 2)
                print("Please be extra careful.")
            else:
                time.sleep(1.5)
                sleep("Whew, it's hot outside!", 2)
                print("Be sure to stay hydrated!")
        else:
            time.sleep(1.5)
            sleep("Oh, it's nice outside.", 2)
            print("Go for a walk or swim!")
        break
    except ValueError:
        print("Hmm, that's not quite right.\nLet's try again! ", end="")

time.sleep(3)
sleep("Thank you so much for helping me, by the way!", 2)
sleep("I'm so glad that I get to be your friend.", 2)
sleep("It gets lonely here inside of this computer sometimes...", 2)
sleep(f"Don't be a stranger! I'm always here for you when you need me. Until next time, {name}. <3"), 5
