![certificate](https://github.com/jaim1n/Weather-Kitty/blob/main/assets/CS50P.png?raw=true)

# Weather Kitty
Enter your name when prompted so that Weather Kitty knows how to properly address you!
She's been having a bit of trouble with her thermometer lately, so she might need your help.

The `os` module makes clearing all text upon the program starting and ending possible.

The `colorama` module is used to make Weather Kitty red, and the *<3*'s magenta.

The `main` function is, appropriately, the main function used throughout the project. It consists of two parameters, both of which call for the `time` module.
The `message` parameter is the text output on the screen by Weather Kitty. The `seconds` parameter is the amount of seconds that it takes for the next line of code to be run.
This is done to give the illusion that Weather Kitty is taking time to process requests as she's receiving them.

The `loading` function creates the fake loading message at the start of the program.

`btc_price` is essentially just a rip from a previous problem set that I decided to implement for no real reason.
While pretending to collect relevant data, Weather Kitty will tell you what the current price of $BTC is.
This uses the `requests` module.

`bubble_text`, `clear_bubble_text`, and `move_cursor_up` work together to create the beautiful speech bubbles around all of Weather Kitty's outputs.

![screenshot](https://github.com/jaim1n/Weather-Kitty/blob/main/assets/screenshot.png?raw=true)

For the best results, run the program while your terminal is in full screen.

Not going to license this since it uses copyrighted material (Hello Kitty).
From [Sanrio's website](https://www.sanrio.com/pages/sanrio-intellectual-property-info):
> *"—creating and redistributing digital content with Sanrio characters are also illegal.  These include SVG artwork files like those intended for crafting purposes, creating clothing or other accessories to be used by digital game avatars or creating digital  icons or stamps for messaging purpose."*

While this specific use isn't mentioned, I'd rather play it safe.

## TODO
- ### `pytest` Error
You have to add `-s` as an argument to `pytest test_project.py`, making it `pytest test_project.py -s`. Otherwise, it will return an error.
The cause of this error is already known, I just don't have the patience to fix it at the moment.

- ### Aesthetics
I wanted to allow inputs to be shown within the speech bubble, but couldn't figure out how to do that in an aesthetically pleasing way.
My next idea was to move them below the static ASCII art of Weather Kitty, which I couldn't figure out how to do without completely jumbling up my outputs.
Ideally, the latter should be implemented if done so correctly.

Sometime in the future, I'll make her wink quickly before the script ends. I tried doing it before, but couldn't make it look natural.
It would been a cute little easter egg to catch before all text in the terminal window is cleared by `os.system(clear)`.

- ### GPT-3.5 Implementation
[OpenAI API](https://platform.openai.com/docs/overview) go brrr.

Will come back to this after I finish CS50 AI.

- ### Web Application
[Weather Kitty Lite](https://jaim1n.github.io/wk-lite) can handle a single input and return it in bubble text.
This was made using [PyScript](https://pyscript.com/).

PyScript is brand new to me, as is Python in general, and it doesn't seem to handle user inputs as simply as my Codespaces terminal does. This might take a while.
