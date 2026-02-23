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


def main():
    system = load_data()
    
    while True:
        print("\n" + "="*45)
        print(" SMART AGRICULTURE MONITORING SYSTEM ")
        print("="*45)
        print("1. Farmer Management")
        print("2. Technician Management")
        print("3. Task Management")
        print("4. Observations")
        print("5. Financials")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            farmer_menu(system)
        elif choice == '2':
            tech_menu(system)
        elif choice == '3':
            task_menu(system)
        elif choice == '4':
            obs_menu(system)
        elif choice == '5':
            fin_menu(system)
        elif choice == '6':
            save_data(system)
            print("\nData saved successfully. Goodbye!")
            break
        else:
            print("\n[!] INVALID CHOICE. Please select a number between 1 and 6.")


def farmer_menu(sys):
    while True:
        print("\n--- Farmer Management ---")
        print("1. Add Farmer")
        print("2. View Farmers (All Details)")
        print("3. Remove Farmer")
        print("4. Back to Main Menu")
        c = input("Choice: ")

        if c == '1':
            fid = input("Enter ID: ")
            if any(f.id == fid for f in sys.farmers):
                print("\n[!] ERROR: This Farmer ID already exists!")
                continue
            name = input("Enter Name: ")
            ftype = input("Enter Type: ")
            sys.farmers.append(Farmer(fid, name, ftype))
            print("Farmer added successfully.")
        elif c == '2':
            if not sys.farmers: print("\nNo farmer records found.")
            for f in sys.farmers:
                print(f"ID: {f.id} | Name: {f.name} | Type: {f.ftype}")
        elif c == '3':
            fid = input("Enter ID to remove: ")
            original_count = len(sys.farmers)
            sys.farmers = [f for f in sys.farmers if f.id != fid]
            if len(sys.farmers) < original_count:
                print("Farmer removed.")
            else:
                print("\n[!] Farmer ID not found.")
        elif c == '4':
            break
        else:
            print("\n[!] INVALID CHOICE. Please try again.")


def tech_menu(sys):
    while True:
        print("\n--- Technician Management ---")
        print("1. Add Technician")
        print("2. View Technicians (All Details)")
        print("3. Remove Technician")
        print("4. Back to Main Menu")
        c = input("Choice: ")

        if c == '1':
            tid = input("Enter ID: ")
            if any(t.id == tid for t in sys.technicians):
                print("\n[!] ERROR: This Technician ID already exists!")
                continue
            name = input("Enter Name: ")
            spec = input("Enter Specialization: ")
            sys.technicians.append(Technician(tid, name, spec))
            print("Technician added.")
        elif c == '2':
            if not sys.technicians: print("\nNo technician records found.")
            for t in sys.technicians:
                print(f"ID: {t.id} | Name: {t.name} | Specialization: {t.spec}")
        elif c == '3':
            tid = input("Enter ID to remove: ")
            original_count = len(sys.technicians)
            sys.technicians = [t for t in sys.technicians if t.id != tid]
            if len(sys.technicians) < original_count:
                print("Technician removed.")
            else:
                print("\n[!] Technician ID not found.")
        elif c == '4':
            break
        else:
            print("\n[!] INVALID CHOICE. Please try again.")


def task_menu(sys):
    while True:
        print("\n--- Task Management ---")
        print("1. Add Task")
        print("2. View Tasks (All Details)")
        print("3. Mark Task Completed")
        print("4. Back to Main Menu")
        c = input("Choice: ")

        if c == '1':
            tkid = input("Enter Task ID: ")
            if any(tk.id == tkid for tk in sys.tasks):
                print("\n[!] ERROR: This Task ID already exists!")
                continue
            desc = input("Description: ")
            tech = input("Assigned Tech: ")
            date = input("Date: ")
            sys.tasks.append(Task(tkid, desc, tech, date))
            print("Task created.")
        elif c == '2':
            if not sys.tasks: print("\nNo tasks found.")
            for t in sys.tasks:
                print(f"ID: {t.id} | Desc: {t.desc} | Tech: {t.tech} | Date: {t.date} | Status: {t.status}")
        elif c == '3':
            tkid = input("Enter Task ID to complete: ")
            found = False
            for t in sys.tasks:
                if t.id == tkid: 
                    t.status = "Completed"
                    found = True
                    print("Task status updated.")
            if not found: print("\n[!] Task ID not found.")
        elif c == '4':
            break
        else:
            print("\n[!] INVALID CHOICE. Please try again.")


def obs_menu(sys):
    while True:
        print("\n--- Observations ---")
        print("1. Add Observation to Farmer")
        print("2. View All Observations")
        print("3. Back to Main Menu")
        c = input("Choice: ")

        if c == '1':
            fid = input("Farmer ID: ")
            found = False
            for f in sys.farmers:
                if f.id == fid:
                    note = input("Observation Note: ")
                    f.observations.append(note)
                    print("Note added.")
                    found = True
                    break
            if not found: print("\n[!] Farmer ID not found.")
        elif c == '2':
            found_any = False
            for f in sys.farmers:
                if f.observations:
                    print(f"Farmer: {f.name} (ID: {f.id}) | Notes: {', '.join(f.observations)}")
                    found_any = True
            if not found_any: print("\nNo observations recorded.")
        elif c == '3':
            break
        else:
            print("\n[!] INVALID CHOICE. Please try again.")


def fin_menu(sys):
    while True:
        print("\n--- Financials ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Total Revenue")
        print("4. Back to Main Menu")
        c = input("Choice: ")

        if c == '1':
            trid = input("Transaction ID: ")
            if any(tr.id == trid for tr in sys.transactions):
                print("\n[!] ERROR: Transaction ID already exists!")
                continue
            farmer = input("Farmer Name: ")
            amt = input("Amount: ")
            sys.transactions.append(Transaction(trid, farmer, amt))
            print("Transaction recorded.")
        elif c == '2':
            if not sys.transactions: print("\nNo transactions recorded.")
            for t in sys.transactions:
                print(f"ID: {t.id} | Farmer: {t.farmer} | Amount: ${t.amount:.2f}")
        elif c == '3':
            total = sum(t.amount for t in sys.transactions)
            print(f"--- Total System Revenue: ${total:.2f} ---")
        elif c == '4':
            break
        else:
            print("\n[!] INVALID CHOICE. Please try again.")

if __name__ == "__main__":
    main()