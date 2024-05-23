# Space Invader Game

This is a simple Space Invader game developed using Python and Pygame. The game involves shooting down enemies that descend from the top of the screen while avoiding collisions with them.

## Features

- Background music and sound effects.
- Player controls to move left, right, and shoot bullets.
- Multiple enemies that move and respawn after being shot.
- Score display and game over screen.


## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
2. Install the Pygame library using pip:

    ```sh
    pip install pygame
    ```

3. Clone or download the repository to your local machine.

## Usage

1. Navigate to the directory where the `space_invader.py` file is located.
2. Run the script using the following command:

    ```sh
    python space_invader.py
    ```

## File Structure

The project contains the following files:

- `space_invader.py`: The main file containing the game logic.
- `ss.jpg`: The background image.
- `background.wav`: The background music file.
- `ufo.png`: The icon image for the game window.
- `game.png`: The image of the player.
- `skull.png`: The image of the enemy.
- `bul.png`: The image of the bullet.
- `laser.wav`: The sound effect for shooting a bullet.
- `explosion.wav`: The sound effect for an enemy explosion.

## Code Explanation

The game initializes the Pygame library, sets up the display, and loads the required assets such as images and sounds. The main game loop handles events, updates the game state, and renders the screen.

### Game Components

- **Screen Setup**: Creates the game window with a specified size.
- **Background**: Loads and displays the background image.
- **Sound**: Loads and plays background music and sound effects.
- **Player**: Displays the player image and handles player movement.
- **Enemies**: Creates multiple enemies, handles their movement, and detects collisions with bullets.
- **Bullet**: Handles the firing and movement of bullets.
- **Score**: Displays the current score on the screen.
- **Game Over**: Displays the game over text when the player loses.

### Event Handling

The game responds to the following events:

- **QUIT**: Exits the game.
- **KEYDOWN**: Moves the player left or right and fires bullets.
- **KEYUP**: Stops the player movement when the key is released.

### Collision Detection

The `isCollision` function calculates the distance between the bullet and an enemy to determine if a collision has occurred.

### Game Loop

The main game loop updates the game state, including player and enemy positions, bullet movement, and collision detection. It also renders the updated game state to the screen.

## Contributing

If you wish to contribute to the project, feel free to fork the repository and submit a pull request.

