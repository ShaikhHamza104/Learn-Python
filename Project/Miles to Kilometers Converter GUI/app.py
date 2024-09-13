import tkinter as tk  # Using 'tk' as an alias for better readability

def miles_to_kilometer():
    """Calculates and displays the equivalent kilometers for entered miles."""
    try:
        miles = float(input_field.get())
        kilometers = round(miles * 1.60934, 4)  # Round to 4 decimal places
        kilo_result_label.config(text=f"{kilometers} Km")  # Display result with units
    except ValueError:
        kilo_result_label.config(text="Invalid input. Please enter a number.")

# Create the Tkinter window
window = tk.Tk()

# Set window title, size, and padding
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)
window.maxsize(width=900, height=300)
window.config(padx=20, pady=20)

# Set background color
window.config(bg="pink")


# Entry field with initial value and grid placement
input_field = tk.Entry(width=10)
input_field.insert(0, "0")  # Insert at index 0 (beginning)
input_field.grid(row=0, column=1, padx=5, pady=10)

# "Miles" label
miles_label = tk.Label(text="Miles", width=5)
miles_label.grid(row=1, column=0, padx=10, pady=10)

# "Is equal to" label
equal_label = tk.Label(text="is equal to")
equal_label.grid(row=1, column=1, padx=10, pady=10)

# Kilometer result label
kilo_result_label = tk.Label(text="0 Km")  # Initialize with units
kilo_result_label.grid(row=1, column=2, padx=10, pady=10)

# "Km" label
km_label = tk.Label(text="Km")
km_label.grid(row=1, column=3, padx=10, pady=10)

# Calculate button with command and grid placement
calculate_button = tk.Button(text="Calculate", command=miles_to_kilometer)
calculate_button.grid(row=2, column=2, padx=10, pady=10)

# Run the main event loop to display the window
window.mainloop()