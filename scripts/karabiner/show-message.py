import tkinter as tk

import argparse

def show_notification(text, duration=2000, alpha=0.8, radius=20):
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Create a top-level window
    win = tk.Toplevel(root)
    win.geometry("300x100+%d+%d" % (root.winfo_screenwidth()/2 - 150, root.winfo_screenheight()/2 - 50))
    win.overrideredirect(True)  # Remove the window borders
    win.attributes("-topmost", True)  # Keep the window on top
    win.attributes("-alpha", alpha)  # Set the window transparency

    # Create a Canvas to draw the rounded rectangle
    canvas = tk.Canvas(win, width=300, height=100, bg='lightgray', highlightthickness=0)
    canvas.pack()

    # Draw rounded rectangle
    canvas.create_oval((0, 0, radius*2, radius*2), fill='lightgray', outline='lightgray')
    canvas.create_oval((300-radius*2, 0, 300, radius*2), fill='lightgray', outline='lightgray')
    canvas.create_oval((0, 100-radius*2, radius*2, 100), fill='lightgray', outline='lightgray')
    canvas.create_oval((300-radius*2, 100-radius*2, 300, 100), fill='lightgray', outline='lightgray')
    canvas.create_rectangle((radius, 0, 300-radius, 100), fill='lightgray', outline='lightgray')
    canvas.create_rectangle((0, radius, 300, 100-radius), fill='lightgray', outline='lightgray')

    # Create a label with the notification text
    label = tk.Label(win, text=text, font=("Helvetica", 16), bg='lightgray', fg='black')
    label.place(relx=0.5, rely=0.5, anchor='center')

    # Schedule the window to close after the specified duration
    root.after(duration, win.destroy)
    root.after(duration, root.destroy)

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display a notification on the screen")
    parser.add_argument("text", type=str, help="The text to display in the notification")
    parser.add_argument("--duration", type=int, default=2000, help="Duration in milliseconds for the notification to stay on screen")
    parser.add_argument("--alpha", type=float, default=0.8, help="Transparency level of the notification window (0.0 to 1.0)")
    parser.add_argument("--radius", type=int, default=20, help="Radius of the rounded corners")

    args = parser.parse_args()

    show_notification(args.text, args.duration, args.alpha, args.radius)
