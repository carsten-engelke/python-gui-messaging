### CODE ===================================================
this_container=container()
### ========================================================
config(**{'grid_cols': '(9, 75, 0, 0)', 'grid_multi_cols': '[9, (0, 16, 0, 0), (1, 56, 0, 0), (8, 12, 0, 0)]', 'grid_multi_rows': '[13, (0, 12, 0, 0), (1, 23, 0, 0), (2, 11, 0, 0), (9, 11, 0, 0), (10, 21, 0, 0), (11, 16, 0, 0), (12, 12, 0, 0)]', 'grid_rows': '(13, 25, 0, 0)'})
Label('Label',**{'text': 'GuiDesigner after Start', 'font': 'TkDefaultFont 12 bold', 'fg': 'blue'}).grid(**{'column': '1', 'sticky': 'w', 'columnspan': '3', 'row': '1'})
Label('Label',**{'text': 'But here:', 'bg': 'white'}).grid(**{'column': '1', 'sticky': 'nsw', 'row': '11'})
LinkButton('LinkButton',**{'text': 'Create ON', 'bd': '3', 'bg': 'lightgreen', 'link': 'introduction/create.py'}).grid(**{'column': '2', 'sticky': 'nesw', 'row': '11'})
Message('Message',**{'text': "After you have started the GuiDesigner, it looks as you see above.\n\nThere is the Menu, the Path and the Selection Module. The path shows the Application and the Selection Module shows, it's empty.\n\nLet's change this.\n\nIn the Menu you see the entry 'Create ON'. So let's press it. Of course not in the photo image.\n", 'width': '550', 'bg': 'white'}).grid(**{'column': '1', 'columnspan': '7', 'row': '10'})
Label('designer_image',**{'photoimage': 'introduction/start_image.gif'}).grid(**{'rowspan': '6', 'column': '1', 'sticky': 'nw', 'columnspan': '7', 'row': '3'})
### CODE ===================================================
this_container.grid_remove()
this_container.after(100,this_container.grid)
### ========================================================
