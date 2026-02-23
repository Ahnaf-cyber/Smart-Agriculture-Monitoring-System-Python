import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pickle
import os


DATA_FILE = "sams_data.pkl"

BG_PATH = r"F:\Assignment 04 (Python)\background.jpg"


class Farmer:
    def __init__(self, fid, name, ftype):
        self.id = str(fid)
        self.name = name
        self.ftype = ftype
        self.observations = []

class Technician:
    def __init__(self, tid, name, spec):
        self.id = str(tid)
        self.name = name
        self.spec = spec

class Task:
    def __init__(self, tid, desc, tech, date):
        self.id = str(tid)
        self.desc = desc
        self.tech = tech
        self.date = date
        self.status = "Pending"

class Transaction:
    def __init__(self, tid, farmer, amount):
        self.id = str(tid)
        self.farmer = farmer
        try:
            self.amount = float(amount)
        except:
            self.amount = 0.0

class SAMS:
    def __init__(self):
        self.farmers = []
        self.technicians = []
        self.tasks = []
        self.transactions = []


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "rb") as f:
                return pickle.load(f)
        except:
            return SAMS()
    return SAMS()

def save_data(system_obj):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(system_obj, f)

system = load_data()


class MainGUI:
    def __init__(self, root):
        self.root = root
        root.title("Smart Agriculture Monitoring System")
        root.geometry("1000x650")
        root.resizable(False, False)

        root.protocol("WM_DELETE_WINDOW", self.on_close)

     
        if os.path.exists(BG_PATH):
            try:
                img = Image.open(BG_PATH)
                img = img.resize((1000, 650), Image.Resampling.LANCZOS)
                self.bg = ImageTk.PhotoImage(img)
                self.bg_label = tk.Label(root, image=self.bg)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            except:
                root.configure(bg="#e8f5e9")
        else:
            root.configure(bg="#e8f5e9")

        tk.Label(root, text="SMART AGRICULTURE MONITORING SYSTEM",
                 font=("Segoe UI", 18, "bold"),
                 bg="#2c3e50", fg="white").pack(fill="x")

        frame = tk.Frame(root, bg="white", bd=2, relief="groove")
        frame.place(relx=0.5, rely=0.55, anchor="center")

        self.btn(frame, "Farmer Management", self.farmer_menu).pack(pady=8, padx=20)
        self.btn(frame, "Technician Management", self.tech_menu).pack(pady=8)
        self.btn(frame, "Task Management", self.task_menu).pack(pady=8)
        self.btn(frame, "Observations", self.obs_menu).pack(pady=8)
        self.btn(frame, "Financials", self.fin_menu).pack(pady=8)
        self.btn(frame, "Exit", self.on_close).pack(pady=8)

    def btn(self, parent, text, cmd):
        b = tk.Button(parent, text=text, command=cmd,
                      font=("Segoe UI", 12, "bold"),
                      bg="#4a90e2", fg="white",
                      relief="raised", bd=5,
                      width=25, height=1, cursor="hand2")
        b.bind("<Enter>", lambda e: b.config(bg="#357ABD"))
        b.bind("<Leave>", lambda e: b.config(bg="#4a90e2"))
        return b

    def popup(self, title, w=400, h=400):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.transient(self.root)
        win.grab_set()
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry(f"{w}x{h}+{x}+{y}")
        win.configure(bg="#f4f6f7")
        return win

    def on_close(self):
        save_data(system)
        self.root.destroy()


    def farmer_menu(self):
        win = self.popup("Farmer Management", 300, 300)
        self.btn(win, "Add Farmer", self.add_farmer).pack(pady=10)
        self.btn(win, "View Farmers", self.view_farmers).pack(pady=5)
        self.btn(win, "Remove Farmer", self.remove_farmer).pack(pady=5)

    def add_farmer(self):
        win = self.popup("Add Farmer", 300, 300)
        tk.Label(win, text="ID", bg="#f4f6f7").pack()
        fid_ent = tk.Entry(win); fid_ent.pack()
        tk.Label(win, text="Name", bg="#f4f6f7").pack()
        name_ent = tk.Entry(win); name_ent.pack()
        tk.Label(win, text="Type", bg="#f4f6f7").pack()
        ftype_ent = tk.Entry(win); ftype_ent.pack()

        def save():
            new_id = fid_ent.get()
            if not new_id: return
            if any(f.id == new_id for f in system.farmers):
                messagebox.showerror("Error", "ID already exists!")
                return
            system.farmers.append(Farmer(new_id, name_ent.get(), ftype_ent.get()))
            messagebox.showinfo("Success", "Farmer Added")
            win.destroy()
        self.btn(win, "Save", save).pack(pady=10)

    def view_farmers(self):
      
        data = "\n".join([f"ID: {f.id} | Name: {f.name} | Type: {f.ftype}" for f in system.farmers])
        messagebox.showinfo("Farmers List", data if data else "No farmers")

    def remove_farmer(self):
        win = self.popup("Remove Farmer", 300, 200)
        tk.Label(win, text="Farmer ID", bg="#f4f6f7").pack()
        fid_ent = tk.Entry(win); fid_ent.pack()
        def delete():
            system.farmers[:] = [f for f in system.farmers if f.id != fid_ent.get()]
            win.destroy()
        self.btn(win, "Delete", delete).pack(pady=10)


    def tech_menu(self):
        win = self.popup("Technician Management", 300, 300)
        self.btn(win, "Add Technician", self.add_tech).pack(pady=10)
        self.btn(win, "View Technicians", self.view_tech).pack(pady=5)
        self.btn(win, "Remove Technician", self.remove_tech).pack(pady=5)

    def add_tech(self):
        win = self.popup("Add Technician", 300, 300)
        tk.Label(win, text="ID", bg="#f4f6f7").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        tk.Label(win, text="Name", bg="#f4f6f7").pack()
        name_ent = tk.Entry(win); name_ent.pack()
        tk.Label(win, text="Specialization", bg="#f4f6f7").pack()
        spec_ent = tk.Entry(win); spec_ent.pack()

        def save():
            new_id = tid_ent.get()
            if not new_id: return
            if any(t.id == new_id for t in system.technicians):
                messagebox.showerror("Error", "ID already exists!")
                return
            system.technicians.append(Technician(new_id, name_ent.get(), spec_ent.get()))
            messagebox.showinfo("Success", "Technician Added")
            win.destroy()
        self.btn(win, "Save", save).pack(pady=10)

    def view_tech(self):
      
        data = "\n".join([f"ID: {t.id} | Name: {t.name} | Spec: {t.spec}" for t in system.technicians])
        messagebox.showinfo("Technicians", data if data else "No technicians")

    def remove_tech(self):
        win = self.popup("Remove Tech", 300, 200)
        tk.Label(win, text="ID").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        def delete():
            system.technicians[:] = [t for t in system.technicians if t.id != tid_ent.get()]
            win.destroy()
        self.btn(win, "Delete", delete).pack(pady=10)


    def task_menu(self):
        win = self.popup("Task Management", 300, 350)
        self.btn(win, "Add Task", self.add_task).pack(pady=10)
        self.btn(win, "View Tasks", self.view_tasks).pack(pady=5)
        self.btn(win, "Remove Task", self.remove_task).pack(pady=5)
        self.btn(win, "Mark Completed", self.complete_task).pack(pady=5)

    def add_task(self):
        win = self.popup("Add Task")
        tk.Label(win, text="Task ID").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        tk.Label(win, text="Description").pack()
        desc_ent = tk.Entry(win); desc_ent.pack()
        tk.Label(win, text="Technician").pack()
        tech_ent = tk.Entry(win); tech_ent.pack()
        tk.Label(win, text="Date").pack()
        date_ent = tk.Entry(win); date_ent.pack()

        def save():
            new_id = tid_ent.get()
            if not new_id: return
            if any(tk_item.id == new_id for tk_item in system.tasks):
                messagebox.showerror("Error", "ID already exists!")
                return
            system.tasks.append(Task(new_id, desc_ent.get(), tech_ent.get(), date_ent.get()))
            messagebox.showinfo("Success", "Task Added")
            win.destroy()
        self.btn(win, "Save", save).pack(pady=10)

    def view_tasks(self):
        data = "\n".join([f"ID: {t.id} | Desc: {t.desc} | Tech: {t.tech} | Date: {t.date} | Status: {t.status}" for t in system.tasks])
        messagebox.showinfo("Tasks", data if data else "No tasks")

    def complete_task(self):
        win = self.popup("Complete Task", 300, 200)
        tk.Label(win, text="Task ID").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        def update():
            for t in system.tasks:
                if t.id == tid_ent.get():
                    t.status = "Completed"
            win.destroy()
        self.btn(win, "Update", update).pack(pady=10)

    def remove_task(self):
        win = self.popup("Remove Task")
        tk.Label(win, text="ID").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        def delete():
            system.tasks[:] = [t for t in system.tasks if t.id != tid_ent.get()]
            win.destroy()
        self.btn(win, "Delete", delete).pack(pady=10)


    def obs_menu(self):
        win = self.popup("Observations", 300, 300)
        self.btn(win, "Add Observation", self.add_obs).pack(pady=10)
        self.btn(win, "View Observations", self.view_obs).pack(pady=5)
        self.btn(win, "Remove Observation", self.remove_obs).pack(pady=5)

    def add_obs(self):
        win = self.popup("Add Observation")
        tk.Label(win, text="Farmer ID").pack()
        fid_ent = tk.Entry(win); fid_ent.pack()
        tk.Label(win, text="Observation").pack()
        obs_ent = tk.Entry(win); obs_ent.pack()

        def save():
            for f in system.farmers:
                if f.id == fid_ent.get():
                    f.observations.append(obs_ent.get())
                    messagebox.showinfo("Success", "Added")
                    win.destroy()
                    return
            messagebox.showerror("Error", "Farmer ID not found")
        self.btn(win, "Save", save).pack(pady=10)

    def view_obs(self):
        data = ""
        for f in system.farmers:
            if f.observations:
                data += f"Farmer {f.name} ({f.id}): {', '.join(f.observations)}\n"
        messagebox.showinfo("Observations", data if data else "No observations")

    def remove_obs(self):
        win = self.popup("Clear Obs")
        tk.Label(win, text="Farmer ID").pack()
        fid_ent = tk.Entry(win); fid_ent.pack()
        def clear():
            for f in system.farmers:
                if f.id == fid_ent.get(): f.observations.clear()
            win.destroy()
        self.btn(win, "Clear", clear).pack(pady=10)


    def fin_menu(self):
        win = self.popup("Financials", 300, 350)
        self.btn(win, "Add Transaction", self.add_transaction).pack(pady=10)
        self.btn(win, "View Transactions", self.view_transactions).pack(pady=5)
        self.btn(win, "Remove Transaction", self.remove_transaction).pack(pady=5)
        self.btn(win, "Total Revenue", self.total_revenue).pack(pady=5)

    def add_transaction(self):
        win = self.popup("Add Transaction")
        tk.Label(win, text="ID").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        tk.Label(win, text="Farmer Name").pack()
        farm_ent = tk.Entry(win); farm_ent.pack()
        tk.Label(win, text="Amount").pack()
        amt_ent = tk.Entry(win); amt_ent.pack()

        def save():
            new_id = tid_ent.get()
            if not new_id: return
            if any(tr.id == new_id for tr in system.transactions):
                messagebox.showerror("Error", "ID already exists!")
                return
            system.transactions.append(Transaction(new_id, farm_ent.get(), amt_ent.get()))
            win.destroy()
        self.btn(win, "Save", save).pack(pady=10)

    def view_transactions(self):
        data = "\n".join([f"ID: {t.id} | Farmer: {t.farmer} | Amt: ${t.amount:.2f}" for t in system.transactions])
        messagebox.showinfo("Transactions", data if data else "No records")

    def total_revenue(self):
        total = sum(t.amount for t in system.transactions)
        messagebox.showinfo("Revenue", f"Total: ${total:.2f}")

    def remove_transaction(self):
        win = self.popup("Remove Trans")
        tk.Label(win, text="ID").pack()
        tid_ent = tk.Entry(win); tid_ent.pack()
        def delete():
            system.transactions[:] = [t for t in system.transactions if t.id != tid_ent.get()]
            win.destroy()
        self.btn(win, "Delete", delete).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()