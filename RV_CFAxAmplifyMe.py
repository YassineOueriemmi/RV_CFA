import tkinter as tk
from tkinter import ttk


# RV FUNCTION

def calculate_rv():
    try:
        price_long = float(priceA_entry.get())
        price_short = float(priceB_entry.get())
        base_notional = float(notional_entry.get())
        net_expo = int(net_slider.get())  # 0 → 500k

        # Compute long/short notionals with tilt
        long_notional_value = base_notional + (net_expo / 2)
        short_notional_value = base_notional - (net_expo / 2)

        # Convert them into quantities
        long_qty = long_notional_value / price_long
        short_qty = short_notional_value / price_short

        # Update labels
        long_qty_label.config(text=f"{long_qty:,.2f} units")
        short_qty_label.config(text=f"{short_qty:,.2f} units")

        long_notional_label.config(text=f"${long_notional_value:,.2f}")
        short_notional_label.config(text=f"${short_notional_value:,.2f}")

        net_display_label.config(text=f"Net Exposure: ${net_expo:,.0f}")

    except Exception:
        long_qty_label.config(text="ERROR")
        short_qty_label.config(text="ERROR")


# UI SETUP
root = tk.Tk()
root.title("Relative Value Position Calculator")
root.geometry("550x620")
root.config(bg="#f1f3f4")

title = tk.Label(root, text="RV Notional Position Calculator",
                 font=("Arial", 20, "bold"), bg="#f1f3f4")
title.pack(pady=15)


# INPUT FRAME

frame = tk.Frame(root, bg="#f1f3f4")
frame.pack(pady=10)

# Price A (long)
tk.Label(frame, text="Long Ticker Price:", font=("Arial", 12),
         bg="#f1f3f4").grid(row=0, column=0, padx=10, pady=5)
priceA_entry = tk.Entry(frame, width=20)
priceA_entry.grid(row=0, column=1)

# Price B (short)
tk.Label(frame, text="Short Ticker Price:", font=("Arial", 12),
         bg="#f1f3f4").grid(row=1, column=0, padx=10, pady=5)
priceB_entry = tk.Entry(frame, width=20)
priceB_entry.grid(row=1, column=1)

# Base notional
tk.Label(frame, text="Base Notional ($):", font=("Arial", 12),
         bg="#f1f3f4").grid(row=2, column=0, padx=10, pady=5)
notional_entry = tk.Entry(frame, width=20)
notional_entry.grid(row=2, column=1)


# NET EXPOSURE SLIDER

slider_frame = tk.Frame(root, bg="#f1f3f4")
slider_frame.pack(pady=10)

tk.Label(slider_frame, text="Target Net Exposure ($):",
         font=("Arial", 12), bg="#f1f3f4").pack()

net_slider = tk.Scale(
    slider_frame,
    from_=0,
    to=500000,
    resolution=100000,  # step = 100k
    orient="horizontal",
    length=350,
    bg="#f1f3f4"
)
net_slider.pack()

net_display_label = tk.Label(slider_frame, text="Net Exposure: $0",
                             font=("Arial", 12), bg="#f1f3f4")
net_display_label.pack(pady=5)


# CALCULATE BUTTON

calc_btn = tk.Button(root, text="Calculate",
                     command=calculate_rv,
                     bg="lightblue", width=20)
calc_btn.pack(pady=20)


# OUTPUT SECTION

output = tk.Frame(root, bg="#f1f3f4")
output.pack(pady=10)

# Long quantity
tk.Label(output, text="Long Quantity:", font=("Arial", 12),
         bg="#f1f3f4").grid(row=0, column=0, padx=10, pady=5)
long_qty_label = tk.Label(output, text="--", font=("Arial", 12),
                          bg="#f1f3f4")
long_qty_label.grid(row=0, column=1)

# Short quantity
tk.Label(output, text="Short Quantity:", font=("Arial", 12),
         bg="#f1f3f4").grid(row=1, column=0, padx=10, pady=5)
short_qty_label = tk.Label(output, text="--", font=("Arial", 12),
                           bg="#f1f3f4")
short_qty_label.grid(row=1, column=1)

# Long notional
tk.Label(output, text="Long Notional:", font=("Arial", 12),
         bg="#f1f3f4").grid(row=2, column=0, padx=10, pady=5)
long_notional_label = tk.Label(output, text="--", font=("Arial", 12),
                               bg="#f1f3f4")
long_notional_label.grid(row=2, column=1)

# Short notional
tk.Label(output, text="Short Notional:", font=("Arial", 12),
         bg="#f1f3f4").grid(row=3, column=0, padx=10, pady=5)
short_notional_label = tk.Label(output, text="--", font=("Arial", 12),
                                bg="#f1f3f4")
short_notional_label.grid(row=3, column=1)

root.mainloop()
