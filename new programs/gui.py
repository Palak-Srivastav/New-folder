import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json  # To save/load tasks to file

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager - Palak's Edition")
        self.root.geometry("600x500")
        
        # Storage (same as your code)
        self.tasks = []
        self.descriptions = {}
        self.load_tasks()  # Load from file on start
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="📝 My Task Manager", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="➕ Add Task", command=self.add_task, 
                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="✏️ Edit Task", command=self.edit_task, 
                 bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🗑️ Remove Task", command=self.remove_task, 
                 bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="💾 Save", command=self.save_tasks, 
                 bg="#FF9800", fg="white", font=("Arial", 10, "bold"), width=12).pack(side=tk.LEFT, padx=5)
        
        # Task List (Treeview = fancy table)
        columns = ("No", "Task", "Description")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)
        
        self.tree.heading("No", text="No")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Description", text="Description")
        self.tree.column("No", width=50)
        self.tree.column("Task", width=200)
        self.tree.column("Description", width=300)
        
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.refresh_list()
    
    def refresh_list(self):
        # Clear old items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add current tasks
        for i, task in enumerate(self.tasks):
            desc = self.descriptions.get(task, "No description")
            self.tree.insert("", "end", values=(i+1, task, desc))
    
    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name and task_name.strip():
            task_name = task_name.strip()
            desc = simpledialog.askstring("Description", "Enter description:")
            if desc:
                desc = desc.strip()
            else:
                desc = "No description"
            
            self.tasks.append(task_name)
            self.descriptions[task_name] = desc
            self.refresh_list()
            messagebox.showinfo("Success", f"Added: {task_name}")
    
    def edit_task(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to edit!")
            return
        
        item = self.tree.item(selection[0])
        old_task = item['values'][1]
        task_num = int(item['values'][0]) - 1
        
        new_task = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=old_task)
        if new_task and new_task.strip():
            new_task = new_task.strip()
            # Update lists
            del self.descriptions[old_task]  # Remove old description
            self.tasks[task_num] = new_task
            new_desc = simpledialog.askstring("Edit Description", "Enter new description:")
            self.descriptions[new_task] = new_desc.strip() if new_desc else "No description"
            
            self.refresh_list()
            messagebox.showinfo("Success", f"Edited task #{task_num+1}")
    
    def remove_task(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to remove!")
            return
        
        item = self.tree.item(selection[0])
        task_name = item['values'][1]
        task_num = int(item['values'][0]) - 1
        
        confirm = messagebox.askyesno("Confirm Delete", f"Remove '{task_name}'?")
        if confirm:
            del self.descriptions[task_name]
            self.tasks.pop(task_num)
            self.refresh_list()
            messagebox.showinfo("Deleted", f"Removed task #{task_num+1}")
    
    def save_tasks(self):
        data = {
            "tasks": self.tasks,
            "descriptions": self.descriptions
        }
        try:
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Saved", "Tasks saved to tasks.json!")
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {e}")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                self.tasks = data.get("tasks", [])
                self.descriptions = data.get("descriptions", {})
        except FileNotFoundError:
            pass  # First run, no file yet
        except Exception:
            pass  # Corrupted file, start fresh

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
