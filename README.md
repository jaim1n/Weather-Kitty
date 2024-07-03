My final project in CS50P, and first ever program written from scratch in Python.

![alt text](https://github.com/jaim1n/Weather-Kitty/blob/main/CS50P.png?raw=true)

# DESCRIPTION:
Enter your name when prompted so that Weather Kitty knows how to properly address you!
She's been having a bit of trouble with her thermometer lately, so she might need your help.

The 'colorama' module was used to make Weather Kitty red, and the hearts (<3) magenta.

The 'os' module was used to clear all text upon the program starting and ending.

The 'main' function is, appropriately, the main function used throughout the project. It consists of two parts, both of which use the 'time' module.

The 'message' is the text output on the screen by Weather Kitty. The 'seconds' is the amount of seconds that it takes for the next line of code to be run.
This is done to give the illusion that Weather Kitty is taking time to process requests as she's receiving them.

The 'loading' function creates the fake loading message at the start of the program.

'btc_price' is essentially just a rip from a previous problem set that I decided to implement for no real reason. This uses the 'requests' module.

'bubble_text', 'clear_bubble_text', and 'move_cursor_up' work together to create the beautiful speech bubbles around all of Weather Kitty's outputs.

For the best results, run the program while your terminal is in full screen.

# TODO:
where do i even start lol

You have to include -s as an argument when testing (pytest test_project.py -s) for some reason.
I tried finding the answer in online forums and none of the solutions given seemed to work.

I wanted to allow inputs to be shown within the speech bubble but couldn't figure out how to do that.
So I decided to instead move them below the static ASCII art of Weather Kitty, which I couldn't figure out how to do without completely breaking my code.

I also wanted to make her wink quickly at the end before the script ended but am not skilled enough at ASCII art to do that without it looking weird.

This project (obviously) isn't perfect, and I went into it way more ambitiously than I should have. It turned out a lot better than I thought it would, though.
I think I'll leave it as is, maybe come back to it in a few years when I'm more skilled to see how far I've come.

v2 in 2034 perhaps? :D
