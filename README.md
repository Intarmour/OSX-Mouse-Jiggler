# Mouse Jiggler

Mouse Jiggler is a simple Python script that simulates mouse clicks on macOS to keep the system active. This can be useful for preventing the computer from going to sleep or locking while you're away from your desk. The script also provides real-time updates on the number of clicks performed and the remaining time until it stops running.

## Features

- Simulates mouse clicks at a specific screen location.
- Supports click durations of 10, 15, 30, or 60 minutes.
- Displays the number of clicks performed and the remaining time.
- Shows the expected end time of the operation.
- Allows for manual stopping by pressing the `ESC` key.

## Prerequisites

- **macOS**: This script is designed to work on macOS systems.
- **Python 3**: Make sure Python 3 is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **cliclick**: A command-line utility to simulate mouse and keyboard input on macOS.

### Installing cliclick

You need to install `cliclick` using Homebrew:

1. **Install Homebrew** (if not already installed):

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Install cliclick**:

    ```bash
    brew install cliclick
    ```

3. **Grant Accessibility Permissions**:

    Ensure that your terminal and `cliclick` have accessibility permissions:
    
    - Go to `System Preferences` -> `Security & Privacy` -> `Privacy` -> `Accessibility`.
    - Add your terminal application and `cliclick` to the list.

## Usage

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/mouse-jiggler.git
cd mouse-jiggler
