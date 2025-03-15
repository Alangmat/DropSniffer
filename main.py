from tkinter import *
import threading
import time

from check_drop_packets import *
from print_stats_drop import printDrop

def start_sniff():
    thread = threading.Thread(target=main, daemon=True)
    thread.start()
    e = threading.Thread(target=eventHandler, args=(printedDrop, ), daemon=True)
    e.start()
    btn_start["state"] = "disabled"

def eventHandler(msg):
    while True:
        event.wait()
        updatelbl(msg["value"])
        time.sleep(1)

def updatelbl(msg):
    last_drop['text'] = msg

def printPlotDrop():
    printDrop(False)

def printPlotDropCat():
    printDrop(True)

def update_status():
    from check_drop_packets import isWorking  # Импортируем переменную
    if isWorking:
        status_label.config(text="Статус: Работает")
    else:
        status_label.config(text="Статус: Не работает")
    root.after(1000, update_status)  # Проверяем статус каждую секунду

root = Tk()

root.title("Снифер дропа")
root.geometry("450x250")

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root)
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

btn_start = Button(frame, text="Начать снюх", bg="green", command=start_sniff)
btn_start.pack()

label_last_drop = Label(frame, text="Последний дроп")
label_last_drop.pack()

last_drop = Label(frame)
last_drop.pack(pady=10)

status_label = Label(frame, text="Статус: Не работает")
status_label.pack(pady=10)

btn_print_drop_all = Button(frame, text="График по дропу", command=printPlotDrop)
btn_print_drop_all.pack(pady=5)

# btn_print_drop_all = Button(frame, text="График по категориям", command=printPlotDropCat)
# btn_print_drop_all.pack()

root.after(1000, update_status)  # Запускаем проверку статуса через 1 секунду
root.mainloop()