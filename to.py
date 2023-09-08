import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.pack()
        
        self.update_task_listbox()
    
    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            task = Task(task_text, "", "")
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty!")
    
    def mark_as_complete(self):
        selected_idx = self.task_listbox.curselection()
        if selected_idx:
            idx = selected_idx[0]
            self.tasks[idx].completed = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to mark as complete.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            self.task_listbox.insert(tk.END, f"{status} {idx}. {task.title}")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
