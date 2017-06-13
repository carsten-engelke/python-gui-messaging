Frame("Buttons",link="guidesigner/Buttons.py")
pack(anchor='nw')

Frame("SelectionShow",bg="white",link="guidesigner/SelectionShow.py")
pack(anchor='nw')

### CODE ===================================================

# ---- Receiver for message 'CREATE_WIDGET_REQUEST' - somewhere it has to be: 
# creates the widget with Class name and widget name in the current User selection and sends the message CREATE_WIDGET_DONE which contains the current user widget selection

def create_widget(msg):
    widget_type = msg[0]
    name = msg[1]
    kwargs = msg[2]

    if widget_type in ('cascade','radiobutton','command','separator','checkbutton','delimiter'):
        if isinstance(container(),Menu):
            if widget_type == 'separator':
                eval("MenuItem('{}','{}')".format(name,widget_type))
            elif widget_type == 'delimiter':
                eval("MenuDelimiter('{}')".format(name))
            else:
                eval("MenuItem('{}','{}',label = '{}')".format(name,widget_type,name))
            send('SELECTION_CHANGED')
        else:
            print("Wrong handling: cannot create a menu item outside a menu")
    elif isinstance(container(),Menu):
        print("Wrong handling: cannot create a widget inside a menu")
    elif isinstance(container(),ttk.PanedWindow):
        eval("{}('{}',**{})".format(widget_type,name,kwargs))
        text(name)
        send('SELECTION_CHANGED')
        
    elif isinstance(container(),PanedWindow):
        eval("{}('{}',**{})".format(widget_type,name,kwargs))
        text(name)
        pane()
        send('SELECTION_CHANGED')
        
    elif isinstance(container(),ttk.Notebook):
        eval("{}('{}',**{})".format(widget_type,name,kwargs))
        text(name)
        page(text=name)
        send('SELECTION_CHANGED')

    elif isinstance(container(),LiftWindow):
        eval("{}('{}',**{})".format(widget_type,name,kwargs))
        text(name)
        container().add(this())
        send('SELECTION_CHANGED')


    else:
        if widget_type == "Toplevel": cdApp()
        #eval("{}('{}')".format(widget_type,name))
        eval("{}('{}',**{})".format(widget_type,name,kwargs))
        text(name)
        if widget_type == 'Menu':
            select_menu()
            goIn()
        send('SELECTION_CHANGED')


do_receive('CREATE_WIDGET_REQUEST',create_widget,wishMessage=True)
do_receive("SELECTION_CHANGED", lambda: send('SHOW_SELECTION'))
do_receive("SELECTION_LAYOUT_CHANGED", lambda: send('SHOW_SELECTION'))

### ========================================================
