
Button('Create',text="""Create""",bg='green').grid(column='3',sticky='e',row='0')
Label('Type',text="""Button""",bg='yellow',fg='blue').grid(column='1',sticky='w',row='0')
Entry('Name').grid(column='1',columnspan='3',row='1')
Label('Label',text="""Class""").grid(row='0')
Label('Label',text="""Name""").grid(row='1')

### CODE ===================================================

# the class name is stored in mydata of widget('Name')
callback = lambda wname = widget("Name"): send('CREATE_WIDGET_REQUEST',(wname.mydata,wname.get()))

widget("Create").do_command(callback)
widget("Name").do_event("<Return>",callback)

# ---- Receiver for message 'CREATE_CLASS_SELECTED': changes the text of Label 'Type' to the Class name and stores the Class name in mydata of Entry 'Name'

def function(msg,wname,wtype):
    wname.mydata = msg
    wname.delete(0,END)
    wname.insert(0,msg)
    wtype['text'] = msg
    wname.focus_set()

do_receive('CREATE_CLASS_SELECTED',function,(widget('Name'),widget('Type')),wishMessage=True)

# ---- Initialization with Class 'Button' ---------------------------

send('CREATE_CLASS_SELECTED','Button')

### ========================================================
