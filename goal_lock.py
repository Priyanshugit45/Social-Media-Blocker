import tkinter as tk
from tkinter import messagebox

class TaskLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Lock")
        self.root.geometry("300*200")

        # Goal Input
        tk.Label(root, text="Enter Task (e.g., Study , workout):").pack(pady=5)
        self.Task_entry = tk.Entry(root)
        self.Task_entry.pack()

        # Time Input
        tk.Label(root, text="Time (minutes):").pack(pady=5)
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        # Start Button
        tk.Button(root, text="Task start", command=self.task_start.pack(pady=10))

        # Status Label
        self.status_label = tk.Label(root, text="Set a Task to begin!")
        self.status_label.pack(pady=5)

    def task_start(self):
        task= self.task_entry.get()
        try:
            minutes = int(self.time_entry.get())
            if minutes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid time (in minutes)!")
            return

        if not task:
            messagebox.showerror("Error", "Please enter a task!")
            return

        # Simulate social media lock
        self.status_label.config(text=f"Social Media Locked for {task}!")
        messagebox.showinfo("task Started", f"Working on '{task}' for {minutes} min. Social media locked!")

        # Timer (in milliseconds)
        self.root.after(minutes * 60 * 1000, self.task_complete)

    def task_complete(self):
        self.status_label.config(text="task Complete! Social Media Unlocked!")
        messagebox.showinfo("Success", "task completed! You can now access social media.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskLockApp(root)
    root.mainloop()