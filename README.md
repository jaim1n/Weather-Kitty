![certificate](https://github.com/jaim1n/Weather-Kitty/blob/main/CS50P.png?raw=true)

# DESCRIPTION:
Enter your name when prompted so that Weather Kitty knows how to properly address you!
She's been having a bit of trouble with her thermometer lately, so she might need your help.

The `os` module makes clearing all text upon the program starting and ending possible.

The `colorama` module is used to make Weather Kitty red, and the <3's magenta.

The `main` function is, appropriately, the main function used throughout the project. It consists of two parameters, both of which call for the `time` module.
The `message` parameter is the text output on the screen by Weather Kitty. The `seconds` parameter is the amount of seconds that it takes for the next line of code to be run.
This is done to give the illusion that Weather Kitty is taking time to process requests as she's receiving them.

The `loading` function creates the fake loading message at the start of the program.

`btc_price` is essentially just a rip from a previous problem set that I decided to implement for no real reason.
While pretending to collect relevant data, Weather Kitty will tell you what the current price of $BTC is.
This uses the `requests` module.

`bubble_text`, `clear_bubble_text`, and `move_cursor_up` work together to create the beautiful speech bubbles around all of Weather Kitty's outputs.

![screenshot](https://github.com/jaim1n/Weather-Kitty/blob/main/screenshot.png?raw=true)

For the best results, run the program while your terminal is in full screen.

## TODO:
where do i even start lol

### Unit Test
If you try running `pytest test_project.py`, it returns an error. You have to add `-s` as an argument, making it `pytest test_project.py -s` for it to work.
I drove myself crazy trying to fix it and eventually gave up.

### Aesthetics
I wanted to allow inputs to be shown within the speech bubble, but couldn't figure out how to do that in an aesthetically pleasing way.
My next idea was to move them below the static ASCII art of Weather Kitty, which I couldn't figure out how to do without completely jumbling up my outputs.
Ideally, the latter should be implemented if done so correctly.

I also wanted to make her wink quickly before the script ended but am not skilled enough at ASCII art to do that without it looking weird.
Would've been a neat little easter egg to catch before all text in the terminal window is cleared by `os.system(clear)`.
I suppose I could have made two different pictures myself in Photoshop, and then converted them to ASCII art, but I had that idea a bit too late.
