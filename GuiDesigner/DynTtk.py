import DynTkInter as tk
from tkinter import ttk as StatTtk
from tkinter.ttk import *

class Label(tk.GuiElement,StatTtk.Label):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Label,self,myname,"label")

class Button(tk.GuiElement,StatTtk.Button):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Button,self,myname,"button")

class Checkbutton(tk.GuiElement,StatTtk.Checkbutton):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Checkbutton,self,myname,"checkbutton")

class Radiobutton(tk.GuiElement,StatTtk.Radiobutton):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Radiobutton,self,myname,"radiobutton")

class Entry(tk.GuiElement,StatTtk.Entry):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Entry,self,myname,"entry")

class Scale(tk.GuiElement,StatTtk.Scale):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Scale,self,myname,"scale")

class Scrollbar(tk.GuiElement,StatTtk.Scrollbar):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Scrollbar,self,myname,"scrollbar")

class Frame(tk.GuiContainer,StatTtk.Frame):
    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.Frame,self,myname,"frame",True)

class LabelFrame(tk.GuiContainer,StatTtk.LabelFrame):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiContainer(kwargs,StatTtk.LabelFrame,self,myname,"labelframe",True)

class PanedWindow(tk.GuiElement,StatTtk.PanedWindow):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.PanedWindow,self,myname,"panedwindow",True)
        self.child_layouts = {}

    def trigger_sash_place(self,time,index,x_coord,y_coord):
        self.after(time,lambda i = index, x = x_coord, y=y_coord, function = self.sash_place: function(i,x,y))

    def add(self,child,*args,**kwargs):
        if child.Layout != tk.TTKPANELAYOUT:
            child._addToPackList()
            child.Layout = tk.TTKPANELAYOUT
            self.tkClass.add(self,child,*args,**kwargs)
            if 'weight' in kwargs:
                self.child_layouts[child] = kwargs['weight']

    def pane_layout(self,child):
        if child in self.child_layouts:
            return { 'weight' : self.child_layouts[child] }
        else:
            return {}

    def forget_layout(self,child):
        self.child_layouts.pop(child,None)

class Menubutton(tk.GuiElement,StatTtk.Menubutton):

    def __init__(self,myname=None,**kwargs):
        tk._initGuiElement(kwargs,StatTtk.Menubutton,self,myname,"menubutton",True)

