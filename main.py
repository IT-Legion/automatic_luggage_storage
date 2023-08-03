import tkinter as tk
from storage import Door

class MyButton:
    def __init__(self, win):
        self.win = win
        self.state_value = tk.StringVar()
        self.state_value.set('Open')
        self.main_button()

    def main_button(self):
        tk.Checkbutton(self.win, textvariable=self.state_value, indicatoron=0, text='Close', offvalue="Open", onvalue='Close', command=self.change_state).grid(row=2, column=4, rowspan=4, sticky='nswe')

    def change_state(self):
        if door.state == 'locked':
            scoreboard.delete(0, tk.END)
            scoreboard.insert(0, 'EROR')
        else:
            if self.state_value.get() == 'Open':
                door.open_storage()
                self.state_value.set('Close')
                print(door.state)

            else:
                door.close_storage()
                self.state_value.set('Open')
                print(door.state)

    def button(self):
        col = 1
        row = 1
        for i in range(1, 10):
            tk.Button(self.win, text="{}".format(i), command=lambda i=i: add_digit(i)).grid(row=row, column=col, sticky='we')
            col += 1
            if col == 4:
                col = 1
                row += 1
        tk.Button(self.win, text="{}".format(0), command=lambda i=0: add_digit(i)).grid(row=row, column=col, sticky='we')
        tk.Button(self.win, text="{}".format('=>'), command=lambda: unlock(scoreboard.get(), door.pin)).grid(row=row,
                                                                                                        column=col + 1,
                                                                                                        columnspan=2,
                                                                                                        sticky='we')

def blocking():
    if door.state != 'opened':
        door.block_storage()
        print(door.state)
    else:
        blocking()

def unlock(pin, code):
    if pin == code:
        door.unblock_storage()
        print(door.state)
        #time.sleep(45)
        #blocking()
    else:
        scoreboard.delete(0, tk.END)
        scoreboard.insert(0, 'Xpin')

#def light(): # на доработку
#    ''' должно менять цвет кнопки'''
#    if door.state == 'unblocked':
#       return 'green'
#    else:
#       return 'red'

def add_digit(digit):
    '''
    Выводит на табло
    :param digit: цифры
    '''
    value = scoreboard.get()+ str(digit)
    if len(value)== 5:
        value = digit
    scoreboard.delete(0,tk.END)
    scoreboard.insert(0,value)
    print(scoreboard.get())

door = Door()
win = tk.Tk()
win.title('Хранилище')

scoreboard = tk.Entry(win, justify=tk.LEFT, font=('Arial',15), width=4)
scoreboard.grid(row=1, column=4, sticky='e')
win.grid_columnconfigure(4, minsize=4)

but = MyButton(win)
but.button()

win.mainloop()