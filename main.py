import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

# Create the initial lists with data

# Create the Tkinter application window
import subprocess

window = tk.Tk()
window.title("Grocery List")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 300
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")



list1 = [["Potatoes",400, "g"], ["Red onion", 1, "pieces"], ["Chicken breast", 250, "g"], ["Lemon", 1, "pieces"], ["Carrot", 2, "pieces"], ["Garlic", 2, "pieces"], ['Shepherd cheese', 100, "g"], ["Black olives", 70, 'g']]
list2 = [["Chicken breast", 250, "g"], ["Shallot", 1, "pieces"], ["Carrot", 2, "pieces"], ["Bush beans", 200, "g"], ["Garlic", 2, "pieces"], ["Tomato", 1, "pieces"], ["Balsamic cream", 12, "g"], ["Parsnip",1, "pieces"]]
list3 = [["Pork filet", 250, "g"], ["Onions", 1, "pieces"], ["Mushrooms", 150, "g"], ["Bush beans", 150, "g"], ["Rice", 150, "g"], ["Garlic", 1, "pieces"], ["Lime", 1, "pieces"]]
list4 = [["Chicken breast", 250, "g"], ["Corn", 100, "g"], ["Hard cheese", 20, "g"], ["Tomato", 2, "pieces"],["Avocado", 1, "pieces"], ["Romana salat", 1, "pieces"], ["Garlic", 1, "pieces"], ["Mayo", 17, "ml"]]
list5 = [["Brioche buns", 2, "Pieces"], ["Red onion", 1, "pieces"], ["Romana salat", 1, "pieces"], ["Radish", 100, "g"], ["Camembert", 250, "g"], ["Grainy mustard", 17, "g"], ["Mayo", 34, "ml"]]
list6 = [["Chicken breast", 250, "g"], ["Potatoes", 400, "g"], ["Cooking cream", 150, "g"], ["Baby spinach", 50,"g"], ["Onion", 1, "pieces"],  ["Garlic", 1, "pieces"], ["Lemon", 1, "pieces"], ["Cherry tomatoes", 125, "g"]]
list7 = [["Beef", 200, "g"], ["Rice", 150, "g"], ["Bell pepper", 2, "Pieces"], ["Tomato paste", 35, "g"], ["Red onion", 1, "pieces"], ['Mustard', 10, 'ml'], ['Parsley', 10, 'g']]
list8 = [["Bush beans", 200, "g"], ["Pork filet", 250, "g"], ["Potatoes", 400, "g"], ['Parsley', 10, 'g'], ["Garlic", 1, "pieces"], ["Tomato", 1, "pieces"]]
list9 =  [["blank", 0, 'g']]
list10 = [["Salmon", 300, 'g'], ["Linguine", 250, 'g'], ['Broccoli', 1, 'pieces'], ["Garlic", 1, "pieces"], ["Lemon", 1, "pieces"], ['Cooking cream', 150, 'g']]
list11 = [["Rice", 150, 'g'], ['Pak Choi', 2,'peices'], ["Beef", 200, 'g'], ["Lime", 1, "pieces"], ['Beef broth', 4, 'g'], ["Hoisin sause", 25, 'ml']]
list12 = [["Shrimp", 150, 'g'], ["Teriyaki", 50, 'ml'], ["Lime", 1, "pieces"], ['Pack Choi', 75, 'g'], ["Carrot", 1, "pieces"], ["Rice", 150, 'g'], ["Zucchini", 1, 'pieces'], ['Spring Onion', 1, "pieces"], ["Garlic", 1, "cloves"]]
list13 = [["Chicken breast", 250, "g"],  ["Carrot", 2, "pieces"], ["Garlic", 1, "cloves"], ["Potatoes", 400, "g"], ["Lime", 1, "pieces"], ["Lamb's lettuce", 75, "g"], ["Yogurt", 100, "g"], ['Parsley', 10, 'g']]
list14 = [["Bell Pepper", 2, 'pieces'], ["Coconut milk", 250, 'ml'], ['Red Beans',200, 'g'], ['Lime', 1, 'pieces'],['Chunky tomatoes', 200, 'g'], ['Tortilla',2, 'pieces'] ]
list15 = [["Shrimp", 150, 'g'], ["Dried tomatoes", 50, 'g'], ['Cooking cream', 150, 'g'], ['Hard cheese', 20,"g"], ['Linguine', 375,'g'], ['Cherry tomatoes', 125, 'g'], ['Lemon', 1, 'pieces'] ]


# Store the lists in a dictionary for easy access
lists = {
    "Lemon Chicken + Oven Veggies": list1,
    "Harissa Chicken + Parsnip": list2,
    "Stir Fry Pork + Mushrooms + Beans": list3,
    "American Bowl Avocado": list4,
    "Camembert Burger ": list5,
    "Florentine Chicken": list6,
    "Bell Pepper + Beef Balls": list7,
    "Pork Steak + Green Beans": list8,
    "blank": list9,
    "Salmon Linguine": list10,
    "Asian Beef + Pak Choi": list11,
    "Sesame Shrimp + Veggies": list12,
    "Chicken + Carrot + Lamb's lettuce": list13,
    "Comfy Coconut Soup": list14,
    "Shrimp Linguine": list15,
}


def get_section(product_name):
    # You might need to customize this based on the actual sections in your grocery store
    produce_keywords = ["Avocado", "Bell pepper", "Broccoli", "Bush beans", "Carrot", "Cherry tomatoes", "Garlic",
                        "Lemon","Potatoes","Shalott", "Bell Pepper", "Onion", "Parsley", "Parsnip", "Lamb's lettuce", "Radish", "Mushrooms", "Tomato","Romana salat", "Zucchini","Lime", "Pack Choi"]
    dairy_keywords = ["Camembert", "Cooking cream", "Hard cheese", "Shepherd cheese", "Yogurt"]
    meat_keywords = ["Beef", "Chicken breast", "Pork filet", "Salmon", "Shrimp"]
    canned_goods_keywords = ["Balsamic cream", "Olives", "Chunky tomatoes", "Coconut milk", "Red Beans", "Tomato paste",
                             "Tortilla", "Corn", "Dried tomatoes"]
    condiments_keywords = ["Grainy mustard", "Hoisin sauce", "Mayonnaise", "Mustard", "Teriyaki"]
    pasta_rice_keywords = ["Linguine", "Rice"]

    if any(keyword in product_name for keyword in produce_keywords):
        return "Produce Section"
    elif any(keyword in product_name for keyword in dairy_keywords):
        return "Dairy and Cheese Section"
    elif any(keyword in product_name for keyword in meat_keywords):
        return "Meat and Seafood Section"
    elif any(keyword in product_name for keyword in canned_goods_keywords):
        return "Canned Goods Section"
    elif any(keyword in product_name for keyword in condiments_keywords):
        return "Condiments and Sauces Section"
    elif any(keyword in product_name for keyword in pasta_rice_keywords):
        return "Pasta and Rice Section"
    else:
        return "Miscellaneous/General Aisles"


def on_select():
    selected_lists = []
    for var in dropdown_vars:
        list_names = var.get().split(", ")
        for list_name in list_names:
            if list_name in lists:
                selected_lists.append(lists[list_name])
            else:
                messagebox.showerror("Error", "Please try again.")
                return

    product_quantities = {}
    for selected_list in selected_lists:
        for product in selected_list:
            product_name = product[0]
            quantity = product[1]
            unit = product[2]
            key = (product_name, unit)  # Use product name and unit as a key

            if key in product_quantities:
                product_quantities[key] += quantity
            else:
                product_quantities[key] = quantity

    grocery_list_by_section = {
        "Produce Section": [],
        "Dairy and Cheese Section": [],
        "Meat and Seafood Section": [],
        "Canned Goods Section": [],
        "Condiments and Sauces Section": [],
        "Pasta and Rice Section": [],
        "Miscellaneous/General Aisles": [],
    }

    for (product_name, unit), quantity in product_quantities.items():
        section = get_section(product_name)
        grocery_list_by_section[section].append([product_name, quantity, unit])

    grocery_list = []
    for section, items in grocery_list_by_section.items():
        for item in items:
            grocery_list.append(item)

    # Create the grocery list window
    grocery_window = tk.Toplevel()
    grocery_window.title("Grocery List")

    grocery_window_width = 300
    grocery_window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    grocery_x = (screen_width - grocery_window_width) // 2
    grocery_y = (screen_height - grocery_window_height) // 2

    # Set the grocery list window position
    grocery_window.geometry(f"{grocery_window_width}x{grocery_window_height}+{grocery_x}+{grocery_y}")

    canvas = tk.Canvas(grocery_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    scrollbar = tk.Scrollbar(grocery_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    def send_to_notes():
        notes_applescript = """
            tell application "Notes"
                activate
                set grocery_list to "{list_items}" as string
                make new note with properties {{body:grocery_list}}
            end tell
        """
        shopping_list = "\n".join([f"- {item[0]}: {item[1]} {item[2]}" for item in grocery_list])

        script = notes_applescript.format(list_items=shopping_list)
        subprocess.run(["osascript", "-e", script])

    def check_all():
        for var in checkboxes:
            var.set(1)
        grocery_window.destroy()

    checkboxes = []

    for section, items in grocery_list_by_section.items():
        if items:
            tk.Label(frame, text=f"{section}:", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=5)
            for item in items:
                var = tk.IntVar(value=0)
                checkbox_text = "{} - {} {}".format(item[0], item[1], item[2])
                checkbox = tk.Checkbutton(frame, text=checkbox_text, variable=var)
                checkbox.pack(anchor=tk.W, padx=20, pady=2)
                checkboxes.append(var)

    check_all_button = tk.Button(frame, text="Check All", command=check_all)
    check_all_button.pack(pady=10)

    send_to_notes_button = tk.Button(frame, text="Send to Notes", command=send_to_notes)
    send_to_notes_button.pack(pady=10)

    # Configure grid weights to allow resizing
    grocery_window.grid_rowconfigure(len(checkboxes), weight=1)
    grocery_window.grid_columnconfigure(0, weight=1)

# Create the Tkinter application window
window = tk.Tk()
window.title("Grocery List")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 300
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the dropdown menus
dropdown_vars = []
for i in range(5):
    label = tk.Label(window, text="Meal {}:".format(i + 1))
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    var = tk.StringVar(window)
    dropdown_vars.append(var)
    dropdown = tk.OptionMenu(window, var, *lists.keys())
    dropdown.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

# Create the "Generate List" button
generate_button = ttk.Button(window, text="Generate List", style="RoundedButton.TButton", command=on_select)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Configure grid weights to allow resizing
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
window.mainloop()
