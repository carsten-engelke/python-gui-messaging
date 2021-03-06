Button("save",text="save")
pack(side=LEFT,anchor=W)

Button("load",text="load & run")
pack(side=LEFT,anchor=W)

Button("loadedit",text="load & edit")
pack(side=LEFT,anchor=W)

Button('code',text="""code""",state="disabled")
pack(side=LEFT)

### CODE ===================================================

goto('code')
DynLoad('guidesigner/Button_code.py')

def do_save():
    if this() == container(): send("SAVE_WIDGET",None)
    else: send("SAVE_WIDGET",getNameAndIndex())

widget("save").do_command(do_save)

def do_load():
    selection = Selection()
    goOut()
    if this() == container():
        if this() == _AppRoot._widget:
            send('LOAD_WIDGET','Application Window')
        else: send('LOAD_WIDGET','Toplevel Window')
    else: send('LOAD_WIDGET',"Container: " + getNameAndIndex()[0])
    setSelection(selection)

widget("load").do_command(do_load)

def do_loadedit():
    selection = Selection()
    goOut()
    if this() == container():
        if this() == _AppRoot._widget:
            send('LOAD_EDIT','Application Window')
        else: send('LOAD_EDIT','Toplevel Window')
    else: send('LOAD_EDIT',"Container: " + getNameAndIndex()[0])
    setSelection(selection)

widget("loadedit").do_command(do_loadedit)

### ========================================================

