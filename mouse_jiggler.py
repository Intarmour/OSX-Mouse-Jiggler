import os
import time
import sys
import threading
from datetime import datetime, timedelta

def mouse_click(x, y):
    """
    Simulates a mouse click at the specified position.
    """
    os.system(f"""
    osascript -e 'tell application "System Events" to do shell script "cliclick c:{x},{y}"'
    """)

def esc_listener(stop_event):
    """
    Listens for the ESC key and stops the script when pressed.
    """
    try:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)

        while not stop_event.is_set():
            if sys.stdin.read(1) == '\x1b':  # ESC key pressed
                print("ESC key pressed. Exiting the script.")
                stop_event.set()

    except Exception as e:
        print(f"Error in ESC key listener: {e}")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def mouse_jiggler(duration_minutes):
    """
    Starts the mouse jiggler for the specified duration, showing the number of clicks performed, 
    the remaining time, and the expected stop time.
    """
    duration_seconds = duration_minutes * 60
    start_time = time.time()
    end_time = start_time + duration_seconds  # Calculate end time
    end_datetime = datetime.now() + timedelta(seconds=duration_seconds)  # Calculate end date and time

    # Click position coordinates (example)
    click_x, click_y = 500, 500

    stop_event = threading.Event()
    listener_thread = threading.Thread(target=esc_listener, args=(stop_event,))
    listener_thread.start()

    click_count = 0

    print(f"Mouse jiggler started for {duration_minutes} minutes. Press ESC to stop.")
    print(f"Expected stop time is: {end_datetime.strftime('%H:%M:%S')}")

    try:
        while not stop_event.is_set():
            elapsed_time = time.time() - start_time
            remaining_time = duration_seconds - elapsed_time

            if remaining_time <= 0:
                print("Duration completed. Exiting the script.")
                stop_event.set()
                break

            # Simulate a mouse click
            mouse_click(click_x, click_y)
            click_count += 1

            # Calculate remaining minutes and seconds
            remaining_minutes = int(remaining_time // 60)
            remaining_seconds = int(remaining_time % 60)

            # Print current status
            print(f"Clicks performed: {click_count}, Time remaining: {remaining_minutes} minutes and {remaining_seconds} seconds")

            # Wait 5 seconds before the next click
            time.sleep(5)

    except KeyboardInterrupt:
        print("Script interrupted manually.")
    except Exception as e:
        print(f"Error during script execution: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mouse_jiggler.py <duration in minutes>")
        print("Valid durations: 10, 15, 30, 60")
        sys.exit(1)

    try:
        duration = int(sys.argv[1])
        if duration not in [10, 15, 30, 60]:
            raise ValueError
    except ValueError:
        print("Invalid duration. Use 10, 15, 30, or 60.")
        sys.exit(1)

    mouse_jiggler(duration)
