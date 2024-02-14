import tkinter as tk
from tkinter import ttk
from Dealership import Dealership
from Car import Car

def update_models(event):
    selected_make = make_combobox.get()
    models = car_models.get(selected_make, [])
    model_combobox.config(values=models)
    model_combobox.current(0)

def add_car():
    make = make_combobox.get()
    model = model_combobox.get()
    year = year_combobox.get()

    car = Car(make, model, year)
    dealership.add_car(car)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, dealership.display_inventory())

# GUI code here
root = tk.Tk()
root.title("Car Dealership")

# Dealership instance
dealership = Dealership()

# Make selection
make_label = tk.Label(root, text="Make:")
make_label.grid(row=0, column=0, padx=5, pady=5)
makes = ["Toyota", "Honda", "Audi", "Lexus"]
make_combobox = ttk.Combobox(root, values=makes)
make_combobox.grid(row=0, column=1, padx=5, pady=5)
make_combobox.bind("<<ComboboxSelected>>", update_models)

# Model selection
model_label = tk.Label(root, text="Model:")
model_label.grid(row=1, column=0, padx=5, pady=5)
car_models = {"Toyota": ["Camry", "Corolla", "RAV4"],
              "Honda": ["Civic", "Accord", "CR-V"],
              "Audi": ["A3", "A4", "Q5"],
              "Lexus": ["IS", "RX", "NX"]}
model_combobox = ttk.Combobox(root)
model_combobox.grid(row=1, column=1, padx=5, pady=5)

# Year selection
year_label = tk.Label(root, text="Year:")
year_label.grid(row=2, column=0, padx=5, pady=5)
years = [str(year) for year in range(2000, 2031)]
year_combobox = ttk.Combobox(root, values=years)
year_combobox.grid(row=2, column=1, padx=5, pady=5)
year_combobox.current(0)

# Add Car button
add_button = tk.Button(root, text="Add Car", command=add_car)
add_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Display inventory
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
