import os

counter = 0

def treeStruct(_dir, _counter):
    dir = os.listdir(_dir)
    for folder in dir:
        if not os.path.isfile(_dir + "\\" + folder):
            _counter += 1
            treeStruct(_dir + "\\" + folder, _counter)
        else:

            print(_counter * " " + folder)

##Put your directory here
directory = "C:\\Users\\OEM\\Desktop\\TicTacToe-main"

treeStruct(directory, counter)
