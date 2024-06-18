import time
import pyautogui
import os
import tkinter as tk
from tkinter import messagebox, filedialog


def create_directory_if_not_exists(directory):
    """Create the directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def capture_screenshot():
    """Capture a screenshot and save it to a file."""
    try:
        # Generate a unique filename based on the current time in milliseconds
        timestamp = int(round(time.time() * 1000))
        # Define the directory path
        directory = filedialog.askdirectory(title="Select Directory to Save Screenshot")
        if not directory:
            return  # User cancelled the directory selection
        # Ensure the directory exists
        create_directory_if_not_exists(directory)
        # Define the full path for the screenshot file
        path = os.path.join(directory, f'{timestamp}.png')
        # Wait for 5 seconds before taking the screenshot
        time.sleep(5)
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        # Save the screenshot to the specified path
        screenshot.save(path)
        # Display success message
        messagebox.showinfo("Screenshot Taken", f"Screenshot saved to {path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def start_screenshot():
    """Start the screenshot capture process."""
    messagebox.showinfo("Get Ready", "You have 5 seconds to prepare for the screenshot.")
    capture_screenshot()


# Set up the GUI
root = tk.Tk()
root.title("Screenshot App")
root.geometry("400x200")
root.resizable(False, False)

# Create and place the label
lbl_instructions = tk.Label(root,
                            text="Click the button below to take a screenshot.\nYou will have 5 seconds to prepare.",
                            font=("Arial", 12))
lbl_instructions.pack(pady=20)

# Create and place the button
btn_screenshot = tk.Button(root, text="Take Screenshot", font=("Arial", 14), command=start_screenshot, bg="blue",
                           fg="white", padx=20, pady=10)
btn_screenshot.pack(pady=20)

# Start the GUI event loop
root.mainloop()
