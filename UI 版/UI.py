from tkinter import *
from graph import *


class Gui():
    def __init__(self, window):
        self.myGraph = Graph()
        self.window = window
        self.window.title("Shanghai Metro")
        self.window.geometry('1024x676+20+20')
        self.searchButton = Button(
            self.window, text="bellman-ford search", width=32, command=self.bsearch)
        self.searchButton.grid(row=0, column=0)
        self.searchButton = Button(
            self.window, text="dijkstra search", width=32, command=self.dsearch)
        self.searchButton.grid(row=0, column=1)
        self.entry1 = Entry(self.window, width=100)
        self.entry1.grid(row=1, column=0, columnspan=3)
        self.text = Text(self.window, width=120, height=40)
        self.text.grid(row=2, column=0, columnspan=12)

    def bsearch(self):
        self.myGraph = Graph()
        self.myGraph.readIn()
        all = self.entry1.get()
        if all:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myGraph.navigateBellmanFord(all))

    def dsearch(self):
        self.myGraph = Graph()
        self.myGraph.readIn()
        all = self.entry1.get()
        if all:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myGraph.navigateDijkstra(all))


window = Tk()
root = Gui(window)
window.mainloop()
