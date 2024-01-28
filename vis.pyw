import random
from statistics import median
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
build_exe_options = {"packages": ["numpy", "matplotlib", "pandas"]}
def generate_plot():
    plt.clf()
    plt.title('Измерения')
    plt.xlabel('Упругие деформации | Неупругие деформации')
    plt.ylabel('Осевая сжимающая нагрузка, P, кН')

    step_data = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5]
    dict_data = {}
    N = int(entry.get())

    for i in range(N):
        dict_data[i] = []

    for i in range(N):
        N_exp = 11
        for j in range(N_exp):
            exp = float(entry_data[i][j].get())
            dict_data[i].append(exp)

    randomlist = ['ro', 'g^', 'b*', 'ys']
    Middle = []
    c = 0

    while c < 11:
        mid = 0
        for i in range(N):
            mid += dict_data[i][c]
        Middle.append(mid / N)
        c += 1

    # Создайте фигуру и холст для встраивания графика в приложение Tkinter
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    widget = canvas.get_tk_widget()
    widget.pack()

    for i in range(N):
        ax.plot(step_data, dict_data[i], randomlist[random.randint(0, 3)])

    ax.plot(step_data, Middle)
    ax.grid(True)
    canvas.draw()
    root.update_idletasks()
    root.geometry("1800x1200")

root = tk.Tk()
root.title("GUI Application")

label = tk.Label(root, text="Введите количество экспериментов:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Генерировать график", command=generate_plot)
button.pack()

# Список для хранения объектов Entry
entry_data = []

def create_entry_fields():
    N = int(entry.get())
    for i in range(N):
        frame = tk.Frame(root)
        frame.pack(side=tk.TOP, padx=5, pady=5)  # Adjust padx and pady as needed
        entry_row = []
        res = f'{i+1} эксперимент: '
        label = tk.Label(frame,text=res)
        label.pack(side=tk.LEFT, padx=5, pady=5)
        for j in range(11):
            entry_cell = tk.Entry(frame)
            entry_cell.pack(side=tk.LEFT, padx=5, pady=5)  # Adjust padx and pady as needed
            entry_row.append(entry_cell)
        entry_data.append(entry_row)
    root.update_idletasks()
    root.geometry(root.geometry())

# Кнопка для создания полей ввода после ввода количества экспериментов
create_fields_button = tk.Button(root, text="Создать поля ввода", command=create_entry_fields)
create_fields_button.pack()

root.mainloop()