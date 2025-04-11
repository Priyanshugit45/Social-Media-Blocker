import tkinter as tk
from tkinter import messagebox

class TaskLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Goal Lock")
        self.root.geometry("300x200")

        # Goal Input
        tk.Label(root, text="Enter goal (e.g., Study , workout):").pack(pady=5)
        self.Goal_entry = tk.Entry(root)
        self.Goal_entry.pack()

        # Time Input
        tk.Label(root, text="Time (minutes):").pack(pady=5)
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        # Start Button
        tk.Button(root, text="Start Goal", command=self.start_goal).pack(pady=10)

        # Status Label
        self.status_label = tk.Label(root, text="Set a Goal to begin!")
        self.status_label.pack(pady=5)

    def start_goal(self):
        goal= self.goal_entry.get()
        try:
            minutes = int(self.time_entry.get())
            if minutes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid time (in minutes)!")
            return

        if not goal:
            messagebox.showerror("Error", "Please enter a goal!")
            return

        # Simulate social media lock
        self.status_label.config(text=f"Social Media Locked for {goal}!")
        messagebox.showinfo("Goal Started", f"Working on '{goal}' for {minutes} min. Social media locked!")

        # Timer (in milliseconds)
        self.root.after(minutes * 60 * 1000, self.goal_complete)

    def goal_complete(self):
        self.status_label.config(text="Goal Complete! Social Media Unlocked!")
        messagebox.showinfo("Success", "Goal completed! You can now access social media.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GoalLockApp(root)
    root.mainloop()
