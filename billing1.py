import tkinter as tk
from tkinter import messagebox
import random

# ---------------- WINDOW SETUP ----------------
root = tk.Tk()
root.title("Billing System")
root.geometry("700x650")
root.configure(bg="#DDEEFF")
root.resizable(False, False)

# ---------------- TITLE ----------------
title_label = tk.Label(
    root,
    text="🧾 BILLING SYSTEM",
    font=("Arial", 22, "bold"),
    bg="blue",
    fg="white",
    pady=10
)
title_label.pack(fill="x")

# ---------------- CUSTOMER DETAILS SECTION ----------------
frame_customer = tk.LabelFrame(
    root,
    text="Customer Details",
    font=("Arial", 14, "bold"),
    bg="#DDEEFF",
    fg="black",
    padx=10,
    pady=10
)
frame_customer.place(x=30, y=70, width=640, height=80)

tk.Label(frame_customer, text="Customer Name:", font=("Arial", 12), bg="#DDEEFF").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame_customer, width=20, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=10)

tk.Label(frame_customer, text="Mobile Number:", font=("Arial", 12), bg="#DDEEFF").grid(row=0, column=2, padx=10, pady=5)
entry_mobile = tk.Entry(frame_customer, width=20, font=("Arial", 12))
entry_mobile.grid(row=0, column=3, padx=10)

# ---------------- ITEM SECTION ----------------
frame_items = tk.LabelFrame(
    root,
    text="Select Items",
    font=("Arial", 14, "bold"),
    bg="#DDEEFF",
    fg="black",
    padx=10,
    pady=10
)
frame_items.place(x=30, y=160, width=320, height=300)

# Items dictionary with prices
items = {
    "Namkeen": 50,
    "Soft Drink": 40,
    "Chocolates": 20,
    "Biscuits": 30,
    "Chips": 25,
    "Juice": 35
}

# Store quantity entries
item_vars = {}

# Display items with quantity fields
row = 0
for item, price in items.items():
    tk.Label(
        frame_items,
        text=f"{item} (₹{price})",
        font=("Arial", 12),
        bg="#DDEEFF"
    ).grid(row=row, column=0, padx=10, pady=5, sticky="w")

    qty_entry = tk.Entry(frame_items, width=10, font=("Arial", 12))
    qty_entry.grid(row=row, column=1, padx=10)
    item_vars[item] = qty_entry
    row += 1

# ---------------- BILL AREA ----------------
frame_bill = tk.LabelFrame(
    root,
    text="Generated Bill",
    font=("Arial", 14, "bold"),
    bg="#DDEEFF",
    fg="black",
    padx=10,
    pady=10
)
frame_bill.place(x=370, y=160, width=300, height=400)

bill_area = tk.Text(
    frame_bill,
    font=("Consolas", 11),
    width=35,
    height=20,
    bg="white",
    fg="black",
    bd=2,
    relief="sunken"
)
bill_area.pack(fill="both", expand=True)

# ---------------- FUNCTIONS ----------------
def clear_entries():
    for entry in item_vars.values():
        entry.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    bill_area.config(bg="white")
    bill_area.delete(1.0, tk.END)
    bill_area.insert(tk.END, "\n🧾 Bill cleared successfully.\n")

def generate_bill():
    name = entry_name.get().strip()
    mobile = entry_mobile.get().strip()

    if name == "" or mobile == "":
        messagebox.showwarning("Missing Info", "Please enter customer name and mobile number.")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showwarning("Invalid Mobile", "Please enter a valid 10-digit mobile number.")
        return

    # 🎨 Randomly change bill background color
    colors = ["#FFF9C4", "#C8E6C9", "#FFECB3", "#BBDEFB", "#F8BBD0", "#E1BEE7"]
    selected_color = random.choice(colors)
    bill_area.config(bg=selected_color)

    bill_area.delete(1.0, tk.END)
    bill_area.insert(tk.END, "======= BILL DETAILS =======\n")
    bill_area.insert(tk.END, f"Customer Name : {name}\n")
    bill_area.insert(tk.END, f"Mobile Number : {mobile}\n")
    bill_area.insert(tk.END, "-----------------------------\n")

    total = 0
    any_item = False

    for item, price in items.items():
        qty = item_vars[item].get().strip()
        if qty.isdigit() and int(qty) > 0:
            qty = int(qty)
            cost = qty * price
            bill_area.insert(tk.END, f"{item:<15} ₹{price:<5} x {qty:<3} = ₹{cost}\n")
            total += cost
            any_item = True

    if not any_item:
        messagebox.showwarning("Warning", "Please enter quantity for at least one item.")
        bill_area.config(bg="white")  # reset color if no bill generated
        return

    # ---------------- GST Calculation ----------------
    gst_rate = 0.18  # 18% GST
    gst_amount = total * gst_rate
    grand_total = total + gst_amount

    # ---------------- Display Final Bill ----------------
    bill_area.insert(tk.END, "\n-----------------------------")
    bill_area.insert(tk.END, f"\nTotal (Before GST): ₹{total:.2f}")
    bill_area.insert(tk.END, f"\nGST (18%): ₹{gst_amount:.2f}")
    bill_area.insert(tk.END, f"\nGrand Total: ₹{grand_total:.2f}")
    bill_area.insert(tk.END, "\n-----------------------------")
    bill_area.insert(tk.END, "\nThank you for shopping!\n")

# ---------------- BUTTON SECTION ----------------
frame_buttons = tk.Frame(root, bg="#DDEEFF")
frame_buttons.place(x=80, y=480, width=220, height=120)

btn_generate = tk.Button(
    frame_buttons,
    text="Generate Bill",
    font=("Arial", 12, "bold"),
    bg="#28A745",
    fg="white",
    width=15,
    command=generate_bill
)
btn_generate.grid(row=0, column=0, pady=10)

btn_clear = tk.Button(
    frame_buttons,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#DC3545",
    fg="white",
    width=15,
    command=clear_entries
)
btn_clear.grid(row=1, column=0, pady=10)

# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    font=("Arial", 10, "italic"),
    bg="#0047AB",
    fg="white"
)
footer.pack(side="bottom", fill="x")

# ---------------- RUN ----------------
root.mainloop()
