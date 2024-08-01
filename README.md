# Mouse Jiggler

Mouse Jiggler is a Python script that simulates mouse activity on macOS by performing periodic mouse clicks at a specified location on the screen. This is useful for preventing the computer from entering sleep mode or locking due to inactivity. The script provides real-time updates on the number of clicks performed, the remaining time, and the expected end time.

## Features

- **Automatic Mouse Clicks**: Simulates mouse clicks at a specified location to keep the system active.
- **Customizable Duration**: Supports jiggling durations of 10, 15, 30, or 60 minutes.
- **Real-time Updates**: Displays the number of clicks performed and the remaining time in both minutes and seconds.
- **Manual Stop**: Allows for easy interruption by pressing the `ESC` key.
- **Expected End Time**: Shows the calculated end time of the script.
### Example: Running the Mouse Jiggler for 30 Minutes

To run the Mouse Jiggler script for 30 minutes, use the following command:

```bash
python3 mouse_jiggler.py 30
```

## Prerequisites

- **macOS**: The script is specifically designed for macOS environments.
- **Python 3**: Make sure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **cliclick**: A command-line utility to simulate mouse and keyboard input on macOS.

### Installing cliclick

To use this script, you need to install `cliclick`. You can do this with Homebrew:

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

## Installation

1. **Clone the Repository**:

    Open a terminal and clone the repository using Git:

    ```bash
    git clone https://github.com/yourusername/mouse-jiggler.git
    cd mouse-jiggler
    ```

2. **Check Python Version**:

    Make sure Python 3 is installed:

    ```bash
    python3 --version
    ```

    If Python 3 is not installed, follow the instructions on [python.org](https://www.python.org/downloads/) to install it.

## Usage

Run the script with Python 3, specifying the duration in minutes:

```bash
python3 mouse_jiggler.py <duration>
