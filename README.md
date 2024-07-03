My final project in CS50P, and first ever program written from scratch in Python.

![certificate](https://github.com/jaim1n/Weather-Kitty/blob/main/CS50P.png?raw=true)

# DESCRIPTION:
Enter your name when prompted so that Weather Kitty knows how to properly address you!
She's been having a bit of trouble with her thermometer lately, so she might need your help.

The *os* module makes clearing all text upon the program starting and ending possible.

The *colorama* module is used to make Weather Kitty red, and the hearts (<3) magenta.

The **main** function is, appropriately, the main function used throughout the project. It consists of two parameters, both of which call for the *time* module.
The (message) parameter is the text output on the screen by Weather Kitty. The (seconds) parameter is the amount of seconds that it takes for the next line of code to be run.
This is done to give the illusion that Weather Kitty is taking time to process requests as she's receiving them.

The **loading** function creates the fake loading message at the start of the program.

**btc_price** is essentially just a rip from a previous problem set that I decided to implement for no real reason. This uses the *requests* module.

**bubble_text**, **clear_bubble_text**, and **move_cursor_up** work together to create the beautiful speech bubbles around all of Weather Kitty's outputs.

![screenshot](https://github.com/jaim1n/Weather-Kitty/blob/main/screenshot.PNG?raw=true)

For the best results, run the program while your terminal is in full screen.

# TODO:
where do i even start lol

You have to include -s as an argument when testing for some reason.

Example: `pytest test_project.py -s`

I tried finding a solution in online forums but nothing seemed to work.
Ideally, this shouldn't happen.

I wanted to allow inputs to be shown within the speech bubble but couldn't figure out how to do that.
So I decided to instead move them below the static ASCII art of Weather Kitty, which I couldn't figure out how to do without completely breaking my code.

I also wanted to make her wink quickly at the end before the script ended but am not skilled enough at ASCII art to do that without it looking weird.

## Conclusion

This project (obviously) isn't perfect, and I went into it way more ambitiously than I should have. It turned out a lot better than I thought it would, though.
I think I'll leave it as is, maybe come back to it in a few years when I'm more skilled to see how far I've come.

v2 in 2034 perhaps? :D
