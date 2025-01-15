# Turtle Racing Game

This is a Python project that implements a fun and interactive turtle racing game. The game allows users to select the number of turtles to race, and each turtle is randomly assigned a color. The goal is to see which turtle reaches the finish line first!

## Features

- Interactive input for the number of racing turtles (2 to 10).
- Dynamic creation of turtles with random colors.
- Real-time racing simulation with a graphical display using the `turtle` module.
- Randomized turtle movements for an unpredictable and exciting race.

## Requirements

- Python 3.x
- Standard Python libraries: `turtle`, `time`, and `random`.

## How to Run

1. Clone this repository or download the code files.

```bash
git clone <repository_url>
```

2. Navigate to the project directory.

```bash
cd turtle-racing-game
```

3. Run the Python script.

```bash
python turtle_racing_game.py
```

## Game Instructions

1. When prompted, enter the number of turtles that will participate in the race (between 2 and 10).
2. Watch the race on the graphical interface.
3. The winner will be announced in the console after the race is completed.

## Code Overview

### `get_number_of_turtles()`
This function prompts the user to input the number of turtles for the race. It ensures the input is valid and within the range of 2 to 10.

### `setting_screen()`
Sets up the game screen with a fixed width and height and a title.

### `creating_racers(colors)`
Creates turtle racers with random colors and positions them at the starting line.

### `race(colors)`
Handles the race logic. Each turtle moves forward by a random distance until one crosses the finish line. The function returns the winning turtle's color.

### `main()`
The entry point of the game. It integrates all the functions to set up and execute the turtle race.

## Customization

- Modify the `COLORS` list to add or change the available turtle colors.
- Adjust the `WIDTH` and `HEIGHT` variables to change the screen size.
- Change the random distance range in the `race()` function to alter the pace of the race.

## Example Output

```text
Enter the number of turtles that will be racing(2-10): 5
The winner is: red
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

## Acknowledgements

- The Python `turtle` module documentation for providing great resources to create graphical programs.
- Inspiration from classic turtle race games.
