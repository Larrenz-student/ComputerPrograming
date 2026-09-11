import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("MiniMart Inventory System")
root.geometry("900x500")
root.configure(bg="#d9d4cf")

# --------- DATA STORAGE ----------
products = []

# --------- MAIN CARD ----------
card = tk.Frame(root, bg="#efebe7", bd=1, relief="solid")
card.place(relx=0.5, rely=0.5, anchor="center", width=750, height=350)

top_bar = tk.Frame(card, bg="#c7b8ab", height=30)
top_bar.pack(fill="x")

for _ in range(4):
    tk.Label(top_bar, text="●", bg="#c7b8ab", fg="#5c5147").pack(side="left", padx=2)

# --------- PAGE SWITCHER ----------
def show_page(page):
    main_page.pack_forget()
    add_page.pack_forget()
    view_page.pack_forget()
    update_page.pack_forget()
    report_page.pack_forget()
    page.pack(fill="both", expand=True)

# --------- MAIN PAGE ----------
main_page = tk.Frame(card, bg="#efebe7")
main_page.pack(fill="both", expand=True)

content = tk.Frame(main_page, bg="#efebe7")
content.pack(fill="both", expand=True, padx=30, pady=20)

left = tk.Frame(content, bg="#efebe7")
left.pack(side="left", anchor="n")

tk.Label(
    left,
    text="MiniMart Inventory\nSystem",
    font=("Arial", 16, "bold"),
    bg="#efebe7",
    justify="left"
).pack(anchor="w", pady=(0, 20))

right = tk.Frame(content, bg="#efebe7")
right.pack(side="right", padx=20)

try:
    img = tk.PhotoImage(file="minimart.png").subsample(3, 3)
    tk.Label(right, image=img, bg="#efebe7").pack()
except:
    tk.Label(right, text="No Image", bg="#efebe7").pack()

# --------- BUTTON FUNCTIONS ----------
def add_product(event=None):
    show_page(add_page)

def view_inventory(event=None):
    load_inventory()
    show_page(view_page)

def update_stock(event=None):
    show_page(update_page)

def view_report(event=None):
    load_report()
    show_page(report_page)

# --------- DELETE PRODUCT ----------
def delete_product():
    name = simpledialog.askstring("Delete Product", "Enter product name to delete:", parent=root)

    if not name:
        return

    for i, product in enumerate(products):
        if product["name"].lower() == name.lower():
            del products[i]
            messagebox.showinfo("Success", "Product deleted successfully!", parent=root)
            load_inventory()
            return

    messagebox.showerror("Error", "Product not found", parent=root)

# --------- BUTTON DESIGN ----------
def rounded_button(parent, text, row, col, command):
    canvas = tk.Canvas(parent, width=140, height=45,
                       bg="#efebe7", highlightthickness=0)
    canvas.grid(row=row, column=col, padx=10, pady=10)

    canvas.create_oval(5, 5, 45, 45, fill="#6b4c3b", outline="")
    canvas.create_oval(95, 5, 135, 45, fill="#6b4c3b", outline="")
    canvas.create_rectangle(25, 5, 115, 45, fill="#6b4c3b", outline="")

    canvas.create_text(70, 23, text=text,
                       fill="white", font=("Arial", 8, "bold"))

    canvas.bind("<Button-1>", command)

btn_frame = tk.Frame(left, bg="#efebe7")
btn_frame.pack()

rounded_button(btn_frame, "ADD PRODUCT", 0, 0, add_product)
rounded_button(btn_frame, "VIEW INVENTORY", 0, 1, view_inventory)
rounded_button(btn_frame, "UPDATE STOCK", 1, 0, update_stock)
rounded_button(btn_frame, "VIEW REPORT", 1, 1, view_report)

# --------- ADD PRODUCT PAGE ----------
add_page = tk.Frame(card, bg="#efebe7")

form_frame = tk.Frame(add_page, bg="#efebe7")
form_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(form_frame, text="ADD PRODUCT",
         font=("Arial", 18, "bold"),
         bg="#efebe7").grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(form_frame, text="Product Name:", bg="#efebe7").grid(row=1, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, width=30, bd=1, relief="solid")
name_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Price:", bg="#efebe7").grid(row=2, column=0, sticky="w", pady=5)
price_entry = tk.Entry(form_frame, width=30, bd=1, relief="solid")
price_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Quantity:", bg="#efebe7").grid(row=3, column=0, sticky="w", pady=5)
qty_entry = tk.Entry(form_frame, width=30, bd=1, relief="solid")
qty_entry.grid(row=3, column=1, pady=5)

error_label = tk.Label(form_frame, text="", fg="red", bg="#efebe7", font=("Arial", 10, "bold"))
error_label.grid(row=5, column=0, columnspan=2)

def save_product():
    name = name_entry.get().strip()
    price = price_entry.get().strip()
    qty = qty_entry.get().strip()

    if not name or not price or not qty:
        messagebox.showerror("Error", "Please fill all fields", parent=root)
        return

    for product in products:
        if product["name"].lower() == name.lower():
            messagebox.showerror("Error", "Product already exists!", parent=root)

            name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            qty_entry.delete(0, tk.END)

            return

    # FIXED: SAVE DATA
    products.append({
        "name": name,
        "price": price,
        "quantity": qty

    })

    error_label.config(text="")

    messagebox.showinfo("Success", "Product saved successfully!", parent=root)

    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)

# --------- BUTTONS ----------
btn_frame2 = tk.Frame(form_frame, bg="#efebe7")
btn_frame2.grid(row=4, column=0, columnspan=2, pady=20)

tk.Button(btn_frame2, text="SAVE", width=10,
          bg="#6b4c3b", fg="white",
          command=save_product).grid(row=0, column=0, padx=10)

tk.Button(btn_frame2, text="BACK", width=10,
          bg="#6b4c3b", fg="white",
          command=lambda: show_page(main_page)).grid(row=0, column=1, padx=10)

# --------- VIEW INVENTORY PAGE ----------
view_page = tk.Frame(card, bg="#efebe7")

view_container = tk.Frame(view_page, bg="#efebe7")
view_container.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(view_container, text="INVENTORY LIST",
         font=("Arial", 16, "bold"),
         bg="#efebe7").grid(row=0, column=0, columnspan=3, pady=(0, 20))

table_outer = tk.Frame(view_container, bg="#efebe7")
table_outer.grid(row=1, column=0, columnspan=3)

canvas = tk.Canvas(table_outer, width=500, height=150,
                   bg="#efebe7", highlightthickness=0)

scrollbar = tk.Scrollbar(table_outer, orient="vertical",
                         command=canvas.yview)

table_frame = tk.Frame(canvas, bg="#efebe7")

table_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=table_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left")
scrollbar.pack(side="right", fill="y")

headers = ["Product", "Price", "Quantity"]
for col, h in enumerate(headers):
    tk.Label(table_frame, text=h,
             bg="#6b4c3b", fg="white",
             width=20, height=2,
             font=("Arial", 10, "bold")).grid(row=0, column=col)

def load_inventory():
    for widget in table_frame.winfo_children():
        if int(widget.grid_info()["row"]) > 0:
            widget.destroy()

    for row, product in enumerate(products, start=1):
        tk.Label(table_frame, text=product["name"], bg="#efebe7", width=20, relief="solid").grid(row=row, column=0)
        tk.Label(table_frame, text="₱" + (product["price"]), bg="#efebe7", width=20, relief="solid").grid(row=row, column=1)
        tk.Label(table_frame, text=product["quantity"], bg="#efebe7", width=20, relief="solid").grid(row=row, column=2)

btn_frame4 = tk.Frame(view_container, bg="#efebe7")
btn_frame4.grid(row=2, column=0, columnspan=3, pady=20)

tk.Button(btn_frame4, text="ADD NEW", width=12,
          bg="#6b4c3b", fg="white",
          command=lambda: show_page(add_page)).grid(row=0, column=0, padx=10)

tk.Button(btn_frame4, text="DELETE", width=12,
          bg="#6b4c3b", fg="white",
          command=delete_product).grid(row=0, column=1, padx=10)

tk.Button(btn_frame4, text="BACK", width=12,
          bg="#6b4c3b", fg="white",
          command=lambda: show_page(main_page)).grid(row=0, column=2, padx=10)

# --------- UPDATE PAGE ----------
update_page = tk.Frame(card, bg="#efebe7")

update_frame = tk.Frame(update_page, bg="#efebe7")
update_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(update_frame, text="UPDATE PRODUCT",
         font=("Arial", 18, "bold"),
         bg="#efebe7").grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(update_frame, text="Product Name:", bg="#efebe7").grid(row=1, column=0, sticky="w", pady=5)
update_name = tk.Entry(update_frame, width=30, bd=1, relief="solid")
update_name.grid(row=1, column=1, pady=5)

tk.Label(update_frame, text="New Price:", bg="#efebe7").grid(row=2, column=0, sticky="w", pady=5)
update_price = tk.Entry(update_frame, width=30, bd=1, relief="solid")
update_price.grid(row=2, column=1, pady=5)

tk.Label(update_frame, text="New Quantity:", bg="#efebe7").grid(row=3, column=0, sticky="w", pady=5)
update_qty = tk.Entry(update_frame, width=30, bd=1, relief="solid")
update_qty.grid(row=3, column=1, pady=5)

def update_product_data():
    name = update_name.get()

    for i, product in enumerate(products):
        if product["name"].lower() == name.lower():
            products[i]["price"] = update_price.get() or product["price"]
            products[i]["quantity"] = update_qty.get() or product["quantity"]

            messagebox.showinfo("Success", "Product updated successfully!", parent=root)
            load_inventory()

            update_name.delete(0, tk.END)
            update_price.delete(0, tk.END)
            update_qty.delete(0, tk.END)

            return

    messagebox.showerror("Error", "Product not found", parent=root)

btn_frame3 = tk.Frame(update_frame, bg="#efebe7")
btn_frame3.grid(row=4, column=0, columnspan=2, pady=20)

tk.Button(btn_frame3, text="UPDATE", width=10,
          bg="#6b4c3b", fg="white",
          command=update_product_data).grid(row=0, column=0, padx=10)

tk.Button(btn_frame3, text="BACK", width=10,
          bg="#6b4c3b", fg="white",
          command=lambda: show_page(main_page)).grid(row=0, column=1, padx=10)

# --------- REPORT PAGE ----------
report_page = tk.Frame(card, bg="#efebe7")

tk.Label(report_page, text="INVENTORY REPORT",
         font=("Arial", 16, "bold"),
         bg="#efebe7").pack(pady=20)

report_container = tk.Frame(report_page, bg="#efebe7")
report_container.pack()

left_report = tk.Frame(report_container, bg="#efebe7")
left_report.grid(row=0, column=0, padx=50, sticky="w")

right_report = tk.Frame(report_container, bg="#efebe7")
right_report.grid(row=0, column=1, padx=50, sticky="e")

tk.Label(left_report, text="Total Products:", bg="#efebe7").pack(anchor="w", pady=5)
tk.Label(left_report, text="Total Quantity:", bg="#efebe7").pack(anchor="w", pady=5)
tk.Label(left_report, text="Total Value:", bg="#efebe7").pack(anchor="w", pady=5)

total_products_var = tk.StringVar()
total_qty_var = tk.StringVar()
total_value_var = tk.StringVar()

tk.Label(right_report, textvariable=total_products_var, bg="#efebe7").pack(anchor="e", pady=5)
tk.Label(right_report, textvariable=total_qty_var, bg="#efebe7").pack(anchor="e", pady=5)
tk.Label(right_report, textvariable=total_value_var, bg="#efebe7").pack(anchor="e", pady=5)

tk.Label(report_page, text="Low Stock Reminder:",
         font=("Arial", 12, "bold"),
         bg="#efebe7").pack(pady=(15, 5))

low_stock_label = tk.Label(report_page, text="", bg="#efebe7", justify="left")
low_stock_label.pack()

def load_report():
    total_products = len(products)
    total_qty = 0
    total_value = 0
    low_items = []

    for p in products:
        if p["quantity"].isdigit():
            q = int(p["quantity"])
            total_qty += q

            if q <= 5:
                low_items.append(f"- {p['name']} (Qty: {q})")

        if p["quantity"].isdigit() and p["price"].replace('.', '', 1).isdigit():
            total_value += int(p["quantity"]) * float(p["price"])

    total_products_var.set(total_products)
    total_qty_var.set(total_qty)
    total_value_var.set(f"₱{total_value:.2f}")

    low_stock_label.config(text="\n".join(low_items) if low_items else "No low stock items.")

tk.Button(report_page, text="BACK TO DASHBOARD",
          bg="#6b4c3b", fg="white",
          command=lambda: show_page(main_page)).pack(pady=10)

# --------- START ----------
show_page(main_page)
root.mainloop()