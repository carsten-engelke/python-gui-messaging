Frame("LayoutOptions").rcgrid(0,0,sticky='nw')

### CODE ===================================================

Lock()
layouts = {
    NOLAYOUT : '',
    PACKLAYOUT : 'pack',
    GRIDLAYOUT : 'grid',
    PLACELAYOUT : 'place',
    PANELAYOUT : 'pane',
    TTKPANELAYOUT : 'pane',
    MENUITEMLAYOUT : 'menu item',
    MENULAYOUT : 'select menu',
    WINDOWLAYOUT : 'window',
    PAGELAYOUT : 'page',
    LAYOUTNEVER : '',
    }
    
about_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/about.gif')
help_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/help16.gif')
sticky_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/sticky.gif')
compound_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/view-fullscreen16.gif')
insert_image_gif = StatTkInter.PhotoImage(file = 'guidesigner/images/insert-image16.gif')

    
    
# -------------- this LabelFrame contains data for a layout value refresh ---------------------

# the data reference Entries for x,y,row,column,side, and index depending an the layout type
widget("LayoutOptions").mydata=[None,None,None,None,None,None]

# -------------- receiver for message 'LAYOUT_VALUES_REFRESH' ---------------------

def values_refresh(widget = widget("LayoutOptions")):
    mydata = widget.mydata
    if mydata[0] != None:
        mydata[0].delete(0,END)	
        mydata[0].insert(0,getlayout("x"))
    if mydata[1] != None:
        mydata[1].delete(0,END)	
        mydata[1].insert(0,getlayout("y"))
    if mydata[2] != None:
        mydata[2].delete(0,END)	
        mydata[2].insert(0,getlayout("row"))
    if mydata[3] != None:
        mydata[3].delete(0,END)	
        mydata[3].insert(0,getlayout("column"))
    if mydata[4] != None:
        mydata[4].delete(0,END)	
        mydata[4].insert(0,getlayout("side"))
    if mydata[5] != None:
        mydata[5].delete(0,END)	
        mydata[5].insert(0,getlayout("sticky"))

do_receive('LAYOUT_VALUES_REFRESH',values_refresh)

# -------------- receiver for message 'SHOW_LAYOUT' - help functions ------------------------------------

# another help function: for layout option sticky we show an info message box


def choose_image(entry,title,root=widget('/'),os=os):

    file_opt = {
        'defaultextension' : '.gif',
        'filetypes' : [('Graphics Interchange Format', '.gif'),('Portable Pixmap', '.ppm'),('Portable Graymap','.pgm'),('all files', '*')],
        'parent' : root,
        'title' : title,
        'initialdir' : os.path.join(os.getcwd(),'Images') }

    filename = tkFileDialog.askopenfilename(**file_opt)
    if filename:
        filename = os.path.relpath(filename)
        filename = filename.replace('\\','/')
        setlayout(entry.mydata[0],filename)
        entry.delete(0,END)	
        entry.insert(0,getlayout(entry.mydata[0]))

# for Return key or mouse klick: get active selection from the listbox, hide the listbox, set the layout and insert the text in the Entry for showing

def do_lbox_click(event,lbox,entry,isMouse):
    if isMouse: text = lbox.get(lbox.nearest(event.y))
    else: text = lbox.get(ACTIVE)
    setlayout(entry.mydata[0],text)
    entry.delete(0,END)
    entry.insert(0,text)
    lbox.unbind("<Return>")
    lbox.unbind("<Button-1>")
    lbox.unlayout()

def listbox_helpbutton(lbox,entry,lbox_click = do_lbox_click):
    lbox.select_clear(0,END) # clear a former listbox selection 
    lbox_index = lbox.getStringIndex(getlayout(entry.mydata[0])) # get the listbox index for the layout option
    lbox.select_set(lbox_index) # preselect the current layout option in the listbox
    lbox.activate(lbox_index) # and set the selection cursor to it
    lbox.rcgrid(0,3) # show the listbox
    lbox.focus_set() # and focus it
    lbox.do_event("<Return>",lbox_click,(lbox,entry,False),wishEvent=True)  # bind Return key to the listbox
    lbox.do_event("<Button-1>",lbox_click,(lbox,entry,True),wishEvent=True)  # bind mouse click to the listbox

def listbox_selection(helpbutton = listbox_helpbutton,about_gif = about_gif):
    Button(pady=1,padx=1,image=about_gif,bg='blue',text="?").rcgrid(0,2) # create a help button for showing the listbox
    do_command(helpbutton,(widget("listbox"),widget("Entry")))

# -------------- receiver for message 'SHOW_LAYOUT' ------------------------------------


def entry_event_insert(me):
    me.delete(0,END)
    me.insert(0,get_entry_as_string(getlayout(me.mydata[0])))
    me['bg']='gray'
    informLater(300,me,'color')
    send("LAYOUT_OPTIONS_CHANGED",this())


def entry_event(me,insert = entry_event_insert):
    setlayout(me.mydata[0],me.get())
    insert(me)

def set_entry(me,value,insert = entry_event_insert):
    setlayout(me.mydata[0],value)
    insert(me)

enable_flag = [False,False,False]

RefDict = {}

def can_update(linfo, RefDict=RefDict,thisframe=widget("LayoutOptions")):
    if len(RefDict) != len(linfo): return False
    for entry in linfo:
        if entry not in RefDict: return False
    for entry,value in linfo.items():
        RefDict[entry].mydata[1].set(get_entry_as_string(value))
        # reference update for a value refresh without new show layout option creation
        if entry == "x": thisframe.mydata[0]=RefDict[entry]
        elif entry == "y": thisframe.mydata[1]=RefDict[entry]
        elif entry == "row": thisframe.mydata[2]=RefDict[entry]
        elif entry == "column": thisframe.mydata[3]=RefDict[entry]
        elif entry == "side": thisframe.mydata[4]=RefDict[entry]
        elif entry == "sticky": thisframe.mydata[5]=RefDict[entry]
    return True

layout_before=[NOLAYOUT]

class ToggleButton(Label):

    def __init__(self,name,option):
        Label.__init__(self,name,bg = '#ffa000', activebackground = 'lightgreen',width=3)
        self.option = option
        self.bind('<Button-1>',self.toggle)
        

    def show_value(self):
        if self.value:
            self['state'] = 'active'
            self['relief'] = 'sunken'
            self['text'] = '1'
        else:
            self['state'] = 'normal'
            self['relief'] = 'raised'
            self['text'] = '0'

    def set(self,value):
        if isinstance(value,str):
            self.value = int(value)
        else:
            self.value = value
            
        self.show_value()

    def toggle(self,event):
        self.value = not self.value
        this().setlayout(self.option,self.value)
        self.show_value()


def show_layout(
    msg,
    onflag = enable_flag,
    cont = container(),
    thisframe=widget("LayoutOptions"),
    e_event=entry_event,
    lbox_select=listbox_selection,
    RefDict=RefDict,
    can_update=can_update,
    layout_before = layout_before,
    entry_width = 7,
    choose_image = choose_image,
    layouts = layouts,
    about_gif = about_gif,
    help_gif = help_gif,
    sticky_gif = sticky_gif,
    compound_gif = compound_gif,
    insert_image_gif = insert_image_gif,
    set_entry = set_entry,
    ToggleButton = ToggleButton,
    ):


    if isinstance(msg,bool):
        layout_before[0] = NOLAYOUT
        if msg:
            if not onflag[0]:
                onflag[0] = True
                send('SHOW_LAYOUT',this()) # resend message once more
        
        elif onflag[0]: #if shall switch off and SHOW_LAYOUT is on
            onflag[0]=False # switch flag to off
            cont.unlayout() # and unlayout the DetailedLayout frame
            thisframe.mydata=[None,None,None,None,None,None] # set references for value refresh  to not active

    elif type(msg) is tuple:
        layout_before[0] = NOLAYOUT

        if msg[1]:
            thisframe.grid()
            onflag[0] = onflag[1]
            onflag[2] = False
        else:
            if not onflag[2]: onflag[1] = onflag[0]
            onflag[0] = False
            onflag[2] = True
            thisframe.unlayout()
        
    elif onflag[0]: # a correct message arrived and show layout is on
        # reset references for value refresh  to not active
        thisframe.mydata = [None,None,None,None,None,None]
        # if the widget has a layout, then show it

        if msg.Layout & LAYOUTALL and msg.Layout not in (MENULAYOUT,MENUITEMLAYOUT,WINDOWLAYOUT,LABELLAYOUT):

            cont.grid()			

            # get layout_info
            linfo = layout_info()

            # remove, what we don't want
            if this().Layout in (PANELAYOUT,TTKPANELAYOUT):
                linfo.pop('pane',None)

            if this().Layout == PAGELAYOUT:
                linfo.pop('page',None)

            if layout_before[0] == this().Layout:
                # if possible set the values instead of new entry creation
                if can_update(linfo): return
            else:
                layout_before[0] = this().Layout


            RefDict.clear()
            current_selection = Selection() # save current selection
            setWidgetSelection(msg) # set selection for current user widget
            this_widget = this()

            maxlen = 0
            for entry in linfo: maxlen = max(maxlen,len(entry))

            # make a list of tuples of the layout dictionary and sort important options at the beginning
            layoutlist = []
            for entry in (
"sticky",
"anchor",
"text",
'underline',
"image",
"photoimage",
'compound',
'state',
"y",
"x",
"row",
"column",
"rowspan",
"columnspan",
"side",
'padding',
"stretch",
"hide",
"width",
"height",
'minsize',
"fill",
"expand",
"bordermode",
"padx",
"pady",
"ipadx",
"ipady",
"relx",
"rely",
"relwidth",
"relheight"):
                if entry in linfo: layoutlist.append((entry,linfo.pop(entry)))
            for layoutname,entry in linfo.items():layoutlist.append((layoutname,entry))
            # now delete all widgets in frame LayoutOptions and set selection to this frame
            deleteAllWidgets(thisframe) # Frame
            setWidgetSelection(thisframe,thisframe)

            entry_row = 0
            Label('Label',bg='blue',fg='yellow',font = 'TkDefaultFont 12 bold',text=layouts[layout_before[0]])
            rcgrid(entry_row,0,sticky='we')
            entry_row += 1
            
            for entry in layoutlist:
                # for each option, we make a frame an in this frame a label with the option name and an entry
                # for showing and changing the value
                Frame('Frame')
                goIn()
                Label(text=entry[0],width=maxlen,anchor=E).rcgrid(0,0)
                if entry[0] in (
"y", # Place Layout
"x", # Place Layout
"row", # Grid Layout
"column", # Grid Layout
"columnspan", # Grid Layout (Integer default 1)
"rowspan", 
"width", # Place Layout (Default leer "" oder Integer)
"height", # Place Layout (Default leer "" oder Integer)
"padx", # Pack Layout und Grid Layout (Integer default 0)
"pady", # Pack Layout und Grid Layout (Integer default 0)
"ipadx", # Pack Layout und Grid Layout (Integer default 0)
"ipady",
"weight",
'minsize'): # Pack Layout und Grid Layout (Integer default 0)
                    Spinbox("Entry",from_=0,to=3000,increment=1,width=entry_width)
                    do_command(e_event,wishWidget=True) # via return key the option value can be changed
                elif entry[0] in (
"relx", # Place Layout (Integer default 0)
"rely", # Place Layout (Integer default 0)
"relwidth", # Place Layout (Default leer "" oder Integer)
"relheight"):  # Place Layout (Default leer "" oder Integer): 
                    Spinbox("Entry",from_=0,to=1,increment=0.01,width=entry_width)
                    do_command(e_event,wishWidget=True) # via return key the option value can be changed
                elif entry[0] == "underline":
                    Spinbox("Entry",from_=-1,to=300,increment=1,width=entry_width)
                    do_command(e_event,wishWidget=True) # via up and down buttons the option value can be changed
                elif entry[0] in ("expand","hide"):
                    ToggleButton('Entry',entry[0])
                elif entry[0] == "text":
                    Entry("Entry",width=20)
                elif entry[0] == "photoimage":
                    Entry("Entry",width=16)
                elif entry[0] == "padding":
                    Entry("Entry",width=11)
                else:
                    Entry("Entry",width=entry_width)

                if not isinstance(this(),ToggleButton):
                    do_action('color',lambda me = this(): me.config(bg='white'))
                    var = StringVar()
                    var.set(get_entry_as_string(entry[1]))
                    this().mydata=[entry[0],var] # mydata shall also contain the option name
                    this()['textvariable'] = var
                    RefDict[entry[0]] = this()
                    rcgrid(0,1,sticky=E+W)
                    do_event("<Return>",e_event,wishWidget=True) # via return key the option value can be changed
                else:
                    this().set(entry[1])
                    this().mydata=[entry[0],this()] # mydata shall also contain the option name
                    RefDict[entry[0]] = this()
                    rcgrid(0,1,sticky=W,padx=1)
                    

                # reference update for a value refresh without new show layout option creation
                if entry[0] == "x": thisframe.mydata[0]=this()
                elif entry[0] == "y": thisframe.mydata[1]=this()
                elif entry[0] == "row": thisframe.mydata[2]=this()
                elif entry[0] == "column": thisframe.mydata[3]=this()
                elif entry[0] == "side": thisframe.mydata[4]=this()
                elif entry[0] == "sticky": thisframe.mydata[5]=this()

                # listboxes and readonly state for some options
                if entry[0] =="stretch":
                    Listbox(width=6,height=5).fillList(("always","first","last","middle",'never'))
                    lbox_select()

                elif entry[0] =="state":
                    Listbox(width=8,height=3).fillList(("normal","disabled","hidden"))
                    lbox_select()

                elif "photoimage" in entry[0]:
                    Button(pady=1,padx=1,image=insert_image_gif,text="?").rcgrid(0,2)
                    do_command(choose_image,(widget("Entry"),entry[0]))

                elif entry[0] =="side":
                    Listbox(width=7,height=4).fillList(("top","bottom","left","right"))
                    lbox_select()

                elif entry[0] =="in": this().config(state="readonly")
                elif entry[0] =="fill":
                    Listbox(width=4,height=4).fillList(("none","x","y","both"))
                    lbox_select()

                elif entry[0] =="bordermode":
                    Listbox(width=7,height=3).fillList(("inside","outside","ignore"))
                    lbox_select()

                # help info message box for sticky option
                elif entry[0] =="sticky":
                    Button(pady=0,padx=0, relief = 'flat', image=sticky_gif,text="?").rcgrid(0,2)

                    #grid_frame = widget('/','GuiFrame','Selection')
                    #col = grid_frame.getlayout('column')
                    #row = grid_frame.getlayout('row')

                    do_command(lambda grid_frame = this().master.master, root = widget('/','GuiFrame'): send('SELECT_STICKY',(
                        grid_frame.winfo_rootx() - root.winfo_rootx()+grid_frame.winfo_width(),
                        grid_frame.winfo_rooty() - root.winfo_rooty(),
                        'layout'
                      )))

                elif entry[0] =="compound":
                    Button(pady=0,padx=0, image=compound_gif,text="?").rcgrid(0,2)
                    grid_frame = widget('/','GuiFrame','Selection')
                    col = grid_frame.getlayout('column')
                    row = grid_frame.getlayout('row')
                    do_command(lambda col = col, row = row ,entry = widget('Entry'): send('SET_COMPOUND',(col,row,'layout',entry)))

                elif entry[0] =="anchor":
                    Button(pady=0,padx=0, relief = 'flat', image=sticky_gif,text="?").rcgrid(0,2)
                    do_command(lambda grid_frame = this().master.master, root = widget('/','GuiFrame'),entry = widget('Entry'): send('SET_ANCHOR',(
                        grid_frame.winfo_rootx() - root.winfo_rootx()+grid_frame.winfo_width(),
                        grid_frame.winfo_rooty() - root.winfo_rooty(),
                        "layout",entry
                        )))

                goOut() # leaving the frame for the option entry and pack it
                rcgrid(entry_row,0,sticky='nw')
                entry_row += 1

            setSelection(current_selection)
            #if thisframe['width'] < thisframe.winfo_reqwidth():
                #thisframe['width'] = thisframe.winfo_reqwidth()
                #cont.grid_columnconfigure(0,minsize = thisframe.winfo_reqwidth())

        else:   # if the widget doesn't have a layout, then disable value refresh and hide the layout options
            cont.unlayout()
            thisframe.mydata=[None,None,None,None,None,None]


do_receive('SHOW_LAYOUT',show_layout,wishMessage = True)

### ========================================================
