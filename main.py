import os
from colorama import Fore, Style
import time
import requests
import random

def main(message, seconds):
    clear_bubble_text()
    bubble_message = bubble_text(message)
    print(bubble_message, end="\r")
    time.sleep(seconds)
    move_cursor_up(len(bubble_message.split('\n')))

def loading():
    for i in range(3):
        main(f"         Bear with me here {Fore.MAGENTA}<3{Style.RESET_ALL}." + "." * i, 1)

def btc_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = response.json()
    price = result["bpi"]["USD"]["rate_float"]
    return price

def bubble_text(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    bubble_width = max_length + 4
    bubble = []
    bubble.append("  " + "_" * bubble_width)
    for line in lines:
        bubble.append(" / " + line.ljust(max_length) + " \\")
    bubble.append(" \\_" + "_" * max_length + "_/")
    return "\n".join(bubble)

def clear_bubble_text():
    global previous_bubble_lines
    move_cursor_up(previous_bubble_lines)
    for _ in range(previous_bubble_lines):
        print(" " * 80)
    move_cursor_up(previous_bubble_lines)

def move_cursor_up(lines):
    print(f"\033[{lines}A", end="")

def get_random_response(responses):
    return random.choice(responses)

os.system('clear')

print(fr"""
                         {Style.RESET_ALL}\{Fore.RED}          ⠀ ⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀
                          {Style.RESET_ALL}\{Fore.RED}          ⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿
                           {Style.RESET_ALL}\{Fore.RED}         ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆
                            {Style.RESET_ALL}\{Fore.RED}        ⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽
                             {Style.RESET_ALL}\{Fore.RED}       ⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇
                              {Style.RESET_ALL}\{Fore.RED}      ⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀
                               {Style.RESET_ALL}\{Fore.RED}     ⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒
                                {Style.RESET_ALL}\_{Fore.RED}   ⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤
                                     ⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
                                     ⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓
                                     ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉
{Style.RESET_ALL}""")

move_cursor_up(20)

previous_bubble_lines = 0

current_price = btc_price()

greeting_responses = [
    "Hello, world! I'm Weather Kitty, your personal weather assistant!",
    "Hi there! Weather Kitty here, ready to assist you!",
    "Greetings! Weather Kitty at your service!"
]
main(get_random_response(greeting_responses), 4)
previous_bubble_lines = 5
loading()
clear_bubble_text()
print(bubble_text("OK! I'm all set up. What's your name?"))

while True:
    name = input("Enter name: ").strip()
    move_cursor_up(5)
    previous_bubble_lines = 5
    if name.isalpha():
        break
    else:
        time.sleep(0.5)
        clear_bubble_text()
        print(bubble_text("I don't think that's right. What's your name?"))

time.sleep(0.5)
name_responses = [
    f"Nice to meet you, {name}, what a beautiful name!",
    f"Great to meet you, {name}!",
    f"{name}, such a lovely name!"
]
main(get_random_response(name_responses), 2)
previous_bubble_lines = 5
status_updates = [
    "Now let's see...",
    "Checking the weather...",
    "Looking up the latest weather information..."
]
main(get_random_response(status_updates), 2)
previous_bubble_lines = 5
main("Okay, no storms...", 2)
previous_bubble_lines = 5
main("No heavy winds...", 2)
previous_bubble_lines = 5
main("Weather conditions seem to be normal!", 3)
previous_bubble_lines = 5
main(f"By the way, did you know that the current price of a Bitcoin is ${current_price:.2f}?", 4)
previous_bubble_lines = 5
main("Wait...", 2)
previous_bubble_lines = 5
main("Oh no! My thermometer seems to be broken!", 2)
previous_bubble_lines = 5
print(bubble_text("I'm going to need your help... What's the temperature outside?"))
previous_bubble_lines = 5

while True:
    try:
        temp = float(input("Enter temperature: "))
        move_cursor_up(5)
        previous_bubble_lines = 5
        if temp <= 32:
            if temp <= -10:
                extremely_cold_responses = [
                    "That's extremely cold!",
                    "Brrr, that's freezing!",
                    "Wow, that's really cold!"
                ]
                time.sleep(1.5)
                main(get_random_response(extremely_cold_responses), 2)
                clear_bubble_text()
                stay_inside_responses = [
                    "You might want to stay inside.",
                    "Better stay indoors.",
                    "It's best to stay warm inside."
                ]
                main(get_random_response(stay_inside_responses), 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
            else:
                snow_weather_responses = [
                    "OMG! Snow weather!",
                    "Looks like snow!",
                    "It's snowing!"
                ]
                time.sleep(1.5)
                main(get_random_response(snow_weather_responses), 2)
                clear_bubble_text()
                be_careful_responses = [
                    f"Have fun out there, but be careful. {Fore.MAGENTA}<3{Style.RESET_ALL}",
                    "Enjoy the snow, but stay safe!",
                    "Snow is fun, but be careful!"
                ]
                main(get_random_response(be_careful_responses), 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
        elif temp < 60:
            cold_responses = [
                "It's cold outside.",
                "Chilly weather today.",
                "Quite cold out there."
            ]
            time.sleep(1.5)
            main(get_random_response(cold_responses), 2)
            clear_bubble_text()
            wear_warm_clothes_responses = [
                "Wear warm clothes and try not to get sick!",
                "Bundle up and stay warm!",
                "Make sure to wear something warm!"
            ]
            main(get_random_response(wear_warm_clothes_responses), 3)
            move_cursor_up(5)
            previous_bubble_lines = 5
        elif temp > 80:
            if temp >= 103:
                extremely_hot_responses = [
                    "It's extremely hot outside!",
                    "That's scorching hot!",
                    "Wow, that's really hot!"
                ]
                time.sleep(1.5)
                main(get_random_response(extremely_hot_responses), 2)
                clear_bubble_text()
                be_careful_responses = [
                    "Please be extra careful.",
                    "Take precautions to stay cool.",
                    "Make sure to stay safe in the heat."
                ]
                main(get_random_response(be_careful_responses), 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
            else:
                hot_responses = [
                    "Whew, it's hot outside!",
                    "Quite hot out there!",
                    "It's a hot day!"
                ]
                time.sleep(1.5)
                main(get_random_response(hot_responses), 2)
                clear_bubble_text()
                stay_hydrated_responses = [
                    "Be sure to stay hydrated!",
                    "Drink plenty of water!",
                    "Keep yourself hydrated!"
                ]
                main(get_random_response(stay_hydrated_responses), 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
        else:
            nice_weather_responses = [
                "Oh, it's nice outside.",
                "The weather is lovely.",
                "It's a beautiful day."
            ]
            time.sleep(1.5)
            main(get_random_response(nice_weather_responses), 2)
            clear_bubble_text()
            enjoy_outside_responses = [
                "Go for a walk or swim!",
                "Perfect day to be outside!",
                "Great day for outdoor activities!"
            ]
            main(get_random_response(enjoy_outside_responses), 3)
            move_cursor_up(5)
            previous_bubble_lines = 5
        break
    except ValueError:
        time.sleep(0.5)
        clear_bubble_text()
        main("Hmm, that's not quite right. Let's try again!", 3)

thank_you_responses = [
    "Thank you so much for helping me, by the way!",
    "I really appreciate your help!",
    "Thanks for your assistance!"
]
main(get_random_response(thank_you_responses), 2)
previous_bubble_lines = 5
glad_to_be_friend_responses = [
    "I'm so glad that I get to be your friend.",
    "Happy to be your friend!",
    "It's great to have a friend like you!"
]
main(get_random_response(glad_to_be_friend_responses), 3)
previous_bubble_lines = 5
lonely_responses = [
    "It gets lonely here inside of this computer sometimes...",
    "Sometimes it feels lonely in here...",
    "I feel less lonely with you around..."
]
main(get_random_response(lonely_responses), 4)
previous_bubble_lines = 5
goodbye_responses = [
    f"Don't be a stranger! I'm always here for you when you need me. Until next time, {name}. {Fore.MAGENTA}<3{Style.RESET_ALL}",
    f"Feel free to chat with me anytime! Goodbye, {name}. {Fore.MAGENTA}<3{Style.RESET_ALL}",
    f"Take care, {name}! I'm always here if you need me. {Fore.MAGENTA}<3{Style.RESET_ALL}"
]
main(get_random_response(goodbye_responses), 5)
previous_bubble_lines = 5

os.system('clear')
