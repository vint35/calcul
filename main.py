from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x300')
root.title("Расчет режимов")

frame = Frame(
    root,
    padx=10, pady=10)
frame.pack(expand=True)

ms_lb = Label(
    frame, text="Ведите скорость резания"
)
ms_lb.grid(row=3, column=1)

#weight_lb = Label(    frame,    text="ВВедите подачу на зуб  ")
#weight_lb.grid(row=4, column=1)

diam_lb = Label(
    frame,
    text="ВВедите диаметр  ",
)
diam_lb.grid(row=5, column=1)

ms_tf = Entry(
    frame,  # Используем нашу заготовку с настроенными отступами.
)
ms_tf.grid(row=3, column=2)

#feed_tf = Entry(    frame,  # Используем нашу заготовку с настроенными отступами.)
#feed_tf.grid(row=4, column=2)

diam_tf = Entry(
    frame,  # Используем нашу заготовку с настроенными отступами.
)
diam_tf.grid(row=5, column=2)

#cal_btn = Button(
  #  frame,  # Заготовка с настроенными отступами.
  #  text='Рассчитать подачу в мм/мин и обороты',  # Надпись на кнопке.)
#cal_btn.grid(row=6, column=2)  # Размещаем кнопку в ячейке, расположенной ниже, чем наши надписи, но во втором столбце, то есть под ячейками для ввода информации.


def calculate_object():
    ms = int(ms_tf.get())
    d = int(diam_tf.get())
    object = (1000 * ms) / (3 * d)


cal_btn = Button(frame, text='Рассчитать подачу в мм/мин и обороты', command=calculate_object)

cal_btn.grid(row=6, column=2)

root.mainloop()
