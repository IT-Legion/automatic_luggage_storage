from transitions import Machine
import tkinter as tk
import time

class Door(object):
    states = ['closed', 'opened', 'locked']
    pin = '0000'

    def __init__(self):
        self.machine = Machine(model=self, states=Door.states, initial='locked')
        self.machine.add_transition('open_storage', 'closed', 'opened')
        self.machine.add_transition('close_storage', 'opened', 'closed')
        self.machine.add_transition('block_storage', 'closed', 'locked')
        self.machine.add_transition('unblock_storage', 'locked', 'closed')

door = Door()

def blocking():
    if door.state != 'opened':
        door.block_storage()
        print(door.state)
    else:
        blocking()

def unlock(pin,code):
    if pin == code:
        door.unblock_storage()
        print(door.state)
        time.sleep(45)
        blocking()

    else:
        scoreboard.delete(0, tk.END)
        scoreboard.insert(0, 'Xpin')


def light():
    ''' должно менять цвет кнопки'''
    if door.state == 'unblocked':
       return 'green'
    else:
       return 'red'

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


win = tk.Tk()
win.title('Хранилище')

scoreboard = tk.Entry(win, justify=tk.LEFT,font=('Arial',15),width=4)
scoreboard.grid(row=1, column=4, sticky='e')
win.grid_columnconfigure(4, minsize=4)

col = 1
row = 1
for i in range(1, 10):
    tk.Button(win, text="{}".format(i), command=lambda i=i: add_digit(i)).grid(row=row, column=col, sticky='we')
    col += 1
    if col == 4:
        col = 1
        row += 1
tk.Button(win, text="{}".format(0),command=lambda i=0: add_digit(i)).grid(row=row, column=col, sticky='we')
tk.Button(win, text="{}".format('<=|')).grid(row=row, column=col+1, columnspan=2, sticky='we')
tk.Button(win, text="{}".format('O\np\ne\nn'),foreground=light(),command=lambda: unlock(scoreboard.get(),door.pin)).grid(row=2, column=4, rowspan=4, sticky='ns')

print(scoreboard.get())


win.mainloop()