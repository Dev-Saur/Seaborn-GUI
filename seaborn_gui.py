import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import seaborn as sns
import pandas as pd
import tkcolorpicker
import matplotlib.pyplot as plt 

def generate_seaborn_graph(data, x_col, y_col, hue_col, palette, style, title, x_label, y_label):
    sns.set(style=style)

    if hue_col:
        sns.scatterplot(data=data, x=x_col, y=y_col, hue=hue_col, palette=palette)
    else:
        sns.scatterplot(data=data, x=x_col, y=y_col, palette=palette)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def pick_palette_color():
    color = tkcolorpicker.askcolor()[1]
    if color:
        palette_entry.delete(0, tk.END)
        palette_entry.insert(0, color)

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            data = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
            data_preview.config(text=f"Loaded {len(data)} rows from {file_path}")
            return data
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {str(e)}")
    return None


window = tk.Tk()
window.title("Seaborn Graph Generator")


load_data_button = tk.Button(window, text="Load Data", command=load_data)
load_data_button.pack(pady=10)


data_preview = tk.Label(window, text="")
data_preview.pack()


tk.Label(window, text="X Column:").pack()
x_col_entry = tk.Entry(window)
x_col_entry.pack()


tk.Label(window, text="Y Column:").pack()
y_col_entry = tk.Entry(window)
y_col_entry.pack()


tk.Label(window, text="Hue Column (optional):").pack()
hue_col_entry = tk.Entry(window)
hue_col_entry.pack()


tk.Label(window, text="Palette Color:").pack()
palette_entry = tk.Entry(window)
palette_entry.pack()


palette_button = tk.Button(window, text="Pick Palette Color", command=pick_palette_color)
palette_button.pack()


tk.Label(window, text="Seaborn Style:").pack()
seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
style_combobox = ttk.Combobox(window, values=seaborn_styles)
style_combobox.set('darkgrid')
style_combobox.pack()


tk.Label(window, text="Graph Title:").pack()
title_entry = tk.Entry(window)
title_entry.pack()


tk.Label(window, text="X-axis Label:").pack()
x_label_entry = tk.Entry(window)
x_label_entry.pack()


tk.Label(window, text="Y-axis Label:").pack()
y_label_entry = tk.Entry(window)
y_label_entry.pack()


generate_button = tk.Button(window, text="Generate Seaborn Graph", command=lambda: generate_seaborn_graph(
    data=load_data(),
    x_col=x_col_entry.get(),
    y_col=y_col_entry.get(),
    hue_col=hue_col_entry.get(),
    palette=palette_entry.get(),
    style=style_combobox.get(),
    title=title_entry.get(),
    x_label=x_label_entry.get(),
    y_label=y_label_entry.get()
))
generate_button.pack(pady=10)

window.mainloop()
