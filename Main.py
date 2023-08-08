from tkinter import *
from tkinter import ttk
from Functions import * 
        
#Tkinter 
root = Tk()
root.title( "Calculator" )
root.geometry( "373x575" )
root.resizable( width = False, height = False )

# MIAKING LABELS
lbl_0 = ttk.Label(root, text = "Programmer", font = ( "Helvetica", 18 ) )
lbl_0.grid( row = 0, column = 0, sticky = W, padx = 10, pady = 10 )

# MAKING FRAMES
frame1 = ttk.LabelFrame( root )
frame2 = ttk.LabelFrame( root )
frame1.grid( row = 2, column = 0, columnspan = 2 )
frame2.grid( row = 3, columnspan = 2, column = 0 )

# ENTRY BOX CREATE
entry_bin = ttk.Entry( frame1, width = 33, font = ( "Helvetica", 10 ) )
entry_oct = ttk.Entry( frame1, width = 33, font = ( "Helvetica", 10 ) )
entry_dec = ttk.Entry( frame1, width = 33, font = ( "Helvetica", 10 ) )
entry_hex = ttk.Entry( frame1, width = 33, font = ( "Helvetica", 10 ) )
entry = ttk.Entry( frame1, width = 24, font = ( "Helvetica", 20 ), justify = "right" )

lst = [ entry, entry_bin, entry_oct, entry_dec, entry_hex ]
for i in lst: i.bind( "<Key>", lambda e: "break" )
 
#ENTRY BOX BOX GRID
entry_bin.grid( row = 4, column = 2, columnspan = 2, pady = 3 )
entry_oct.grid( row = 3, column = 2, columnspan = 2, pady = 3 )
entry_dec.grid( row = 2, column = 2, columnspan = 2, pady = 3 )
entry_hex.grid( row = 1, column = 2, columnspan = 2, pady = 3 )
entry.grid( row = 0, column = 0, columnspan = 4, padx = ( 2, 0 ) , pady = 3 )

# VARIABLES
val = IntVar()
operated = False 
dic = { 1 : entry_bin, 2 : entry_oct, 3 : entry_dec, 4 : entry_hex }

# BUTTON FUNCTIONS
def s_clear():
    lst = [ entry_bin, entry_oct, entry_dec, entry_hex ]
    for i in lst: i.delete( 0, END )

def clear():
    for i in lst: 
        i.delete( 0, END )

def operate():
    result = arithmetic( p_num[0], entry_dec.get().replace(",", ""), p_num[1] )
    clear()
    entry_dec.insert( 0, result )
    start( 3 )
    entr_instr = dic[ val.get() ]
    entry.insert( 0, entr_instr.get() )

def ar_enter( number ):
    global p_num 
    p_num = [ entry_dec.get().replace(",", ""), number ]
    s_clear()
    current = entry.get()
    entry.delete( 0, END )
    entry.insert( 0, str( current ) + str( number ) )

def enter( number ):
    dic_dig = { 1 : 2, 2 : 8, 3 : 10, 4 : 16 }
    entr_instr = dic[ val.get() ]
    lst = [ entry, entr_instr ]
    for i in lst:
        current = i.get()
        i.delete( 0, END )
        if( i == entry ):
            i.insert( 0, str( current ) + str( number ) )
        else:
            i.insert( 0, formatter ( str( current ) + str( number ), dic_dig[ val.get() ] ) )
    
    start( val.get() )

def clear_one():
    entr_instr = dic[ val.get() ]
    lst_entr = [ entry, entr_instr ]
    for i in lst_entr:
        removed = i.get()
        i.delete( 0, END )
        i.insert( 0, removed[0 : -1] )
    
    if( entry.get().isnumeric() ):
        entr_instr.delete( 0, END )
        entr_instr.insert( 0, entry.get() )
        
    if not( entr_instr.get() == "" ): start( val.get() )
    else: s_clear()

def start( val ):
    if( val == 1 ):
        entry_oct.delete( 0, END )
        entry_oct.insert( 0, formatter( dec_any( int( any_dec( entry_bin.get(), 2, 0 ) ), 8 ), 8 ) )
        entry_dec.delete( 0, END )
        entry_dec.insert( 0, formatter( any_dec( entry_bin.get(), 2, 0 ), 10 ) )
        entry_hex.delete( 0, END )
        entry_hex.insert( 0, formatter( dec_any( int( any_dec( entry_bin.get(), 2, 0 ) ), 16 ), 16 ) )

    if( val == 2 ):
        entry_bin.delete( 0, END )
        entry_bin.insert( 0, formatter( dec_any( int( any_dec( entry_oct.get(), 8, 0 ) ), 2 ), 2 ) )
        entry_dec.delete( 0, END )
        entry_dec.insert( 0, formatter( any_dec( entry_oct.get(), 8, 0 ), 10 ) )
        entry_hex.delete( 0, END )
        entry_hex.insert( 0, formatter( dec_any( int( any_dec( entry_oct.get(), 8, 0 ) ), 16 ), 16 ) )

    if( val == 3 ):
        entry_oct.delete( 0, END )
        entry_oct.insert( 0, formatter( dec_any( entry_dec.get(), 8 ), 8 ) )
        entry_hex.delete( 0, END )
        entry_hex.insert( 0, formatter( dec_any( entry_dec.get(), 16 ), 16 ) )
        entry_bin.delete( 0, END )
        entry_bin.insert( 0, formatter( dec_any( entry_dec.get(), 2 ), 2 ) )

    if( val == 4 ):
        entry_bin.delete( 0, END )
        entry_bin.insert( 0, formatter( dec_any( int( any_dec( entry_hex.get(), 16, 0 ) ), 2 ), 2 ) )
        entry_oct.delete( 0, END )
        entry_oct.insert( 0, formatter( dec_any( int( any_dec( entry_hex.get(), 16, 0 ) ), 8 ), 8 ) )
        entry_dec.delete( 0, END )
        entry_dec.insert( 0, formatter( any_dec( entry_hex.get(), 16, 0 ), 10 ) )

def state():
    if( val.get() == 1 ):
        button_0["state"] = NORMAL
        button_1["state"] = NORMAL
        button_2["state"] = DISABLED
        button_3["state"] = DISABLED
        button_4["state"] = DISABLED
        button_5["state"] = DISABLED
        button_6["state"] = DISABLED
        button_7["state"] = DISABLED
        button_8["state"] = DISABLED
        button_9["state"] = DISABLED
        button_A["state"] = DISABLED 
        button_B["state"] = DISABLED 
        button_C["state"] = DISABLED 
        button_D["state"] = DISABLED 
        button_E["state"] = DISABLED 
        button_F["state"] = DISABLED

    if( val.get() == 2 ):
        button_0["state"] = NORMAL
        button_1["state"] = NORMAL
        button_2["state"] = NORMAL
        button_3["state"] = NORMAL
        button_4["state"] = NORMAL
        button_5["state"] = NORMAL
        button_6["state"] = NORMAL
        button_7["state"] = NORMAL
        button_8["state"] = DISABLED
        button_9["state"] = DISABLED
        button_A["state"] = DISABLED
        button_B["state"] = DISABLED 
        button_C["state"] = DISABLED 
        button_D["state"] = DISABLED 
        button_E["state"] = DISABLED 
        button_F["state"] = DISABLED

    if( val.get() == 3 ):
        button_0["state"] = NORMAL
        button_1["state"] = NORMAL
        button_2["state"] = NORMAL
        button_3["state"] = NORMAL
        button_4["state"] = NORMAL
        button_5["state"] = NORMAL
        button_6["state"] = NORMAL
        button_7["state"] = NORMAL
        button_8["state"] = NORMAL
        button_9["state"] = NORMAL
        button_A["state"] = DISABLED 
        button_B["state"] = DISABLED 
        button_C["state"] = DISABLED 
        button_D["state"] = DISABLED 
        button_E["state"] = DISABLED 
        button_F["state"] = DISABLED

    if( val.get() == 4 ):
        button_0["state"] = NORMAL
        button_1["state"] = NORMAL
        button_2["state"] = NORMAL
        button_3["state"] = NORMAL
        button_4["state"] = NORMAL
        button_5["state"] = NORMAL
        button_6["state"] = NORMAL
        button_7["state"] = NORMAL
        button_8["state"] = NORMAL
        button_9["state"] = NORMAL
        button_A["state"] = NORMAL 
        button_B["state"] = NORMAL 
        button_C["state"] = NORMAL 
        button_D["state"] = NORMAL 
        button_E["state"] = NORMAL 
        button_F["state"] = NORMAL

    clear()

# RADIO BUTTONS CREATE
r_1 = ttk.Radiobutton( frame1, text = "Binary", variable = val, value = 1, command = state )
r_2 = ttk.Radiobutton( frame1, text = "Octal", variable = val, value = 2, command = state )
r_3 = ttk.Radiobutton( frame1, text = "Decimal", variable = val, value = 3, command = state )
r_4 = ttk.Radiobutton( frame1, text = "Hexadecimal", variable = val, value = 4, command = state )

# RADIO BUTTONS GRID
r_1.grid( row = 4, column = 0, columnspan = 2,  padx = 15, sticky = W )
r_2.grid( row = 3, column = 0, columnspan = 2,  padx = 15, sticky = W )
r_3.grid( row = 2, column = 0, columnspan = 2,  padx = 15, sticky = W )
r_4.grid( row = 1, column = 0, columnspan = 2,  padx = 15, sticky = W )

#STYLES FOR BUTTONS
stl = ttk.Style()
stl_0 = ttk.Style()
stl.configure( 'my.TButton', font = ('Helvetica', 10 ) )
stl_0.configure( 'my_0.TButton', font = ('Helvetica', 12 ), width = 7 )

# BUTTONS CREATE
button_1 = ttk.Button( frame2, width = 9, text = "1", style = 'my.TButton', command = lambda: enter( 1 ), state = DISABLED )
button_2 = ttk.Button( frame2, width = 9, text = "2", style = 'my.TButton', command = lambda: enter( 2 ), state = DISABLED )
button_3 = ttk.Button( frame2, width = 9, text = "3", style = 'my.TButton', command = lambda: enter( 3 ), state = DISABLED )
button_4 = ttk.Button( frame2, width = 9, text = "4", style = 'my.TButton', command = lambda: enter( 4 ), state = DISABLED )
button_5 = ttk.Button( frame2, width = 9, text = "5", style = 'my.TButton', command = lambda: enter( 5 ), state = DISABLED )
button_6 = ttk.Button( frame2, width = 9, text = "6", style = 'my.TButton', command = lambda: enter( 6 ), state = DISABLED )
button_7 = ttk.Button( frame2, width = 9, text = "7", style = 'my.TButton', command = lambda: enter( 7 ), state = DISABLED )
button_8 = ttk.Button( frame2, width = 9, text = "8", style = 'my.TButton', command = lambda: enter( 8 ), state = DISABLED )
button_9 = ttk.Button( frame2, width = 9, text = "9", style = 'my.TButton', command = lambda: enter( 9 ), state = DISABLED )
button_0 = ttk.Button( frame2, width = 9, text = "0", style = 'my.TButton', command = lambda: enter( 0 ), state = DISABLED )
button_A = ttk.Button( frame2, width = 9, text = "A", style = 'my.TButton', command = lambda: enter( "A" ), state = DISABLED )
button_B = ttk.Button( frame2, width = 9, text = "B", style = 'my.TButton', command = lambda: enter( "B" ), state = DISABLED )
button_C = ttk.Button( frame2, width = 9, text = "C", style = 'my.TButton', command = lambda: enter( "C" ), state = DISABLED )
button_D = ttk.Button( frame2, width = 9, text = "D", style = 'my.TButton', command = lambda: enter( "D" ), state = DISABLED )
button_E = ttk.Button( frame2, width = 9, text = "E", style = 'my.TButton', command = lambda: enter( "E" ), state = DISABLED )
button_F = ttk.Button( frame2, width = 9, text = "F", style = 'my.TButton', command = lambda: enter( "F" ), state = DISABLED )
button_equal = ttk.Button( frame2, text = "=", style = 'my_0.TButton', command = operate )
button_CR = ttk.Button( frame2, width = 9, text = "C", style = 'my.TButton', command = clear )
button_CE = ttk.Button( frame2, width = 9, text = u"\u003C", style = 'my.TButton', command = clear_one )
button_add = ttk.Button( frame2, text = "+", style = 'my_0.TButton', command = lambda: ar_enter( "+" ) )
button_exit = ttk.Button( frame2, width = 20, text = "Exit", style = 'my.TButton', command = root.destroy )
button_sub = ttk.Button( frame2, text = u"\u23BC", style = 'my_0.TButton', command = lambda: ar_enter( "-" ) )
button_div = ttk.Button( frame2, text = u"\u00F7", style = 'my_0.TButton', command = lambda: ar_enter( "/" ) )
button_mul = ttk.Button( frame2, text = u"\u00D7", style = 'my_0.TButton', command = lambda: ar_enter( "x" ) )
 
# BUTTONS GRID
button_1.grid( row = 6, column = 1, ipady = 20 )
button_2.grid( row = 6, column = 2, ipady = 20 )
button_3.grid( row = 6, column = 3, ipady = 20 )
button_4.grid( row = 5, column = 1, ipady = 20 )
button_5.grid( row = 5, column = 2, ipady = 20 )
button_6.grid( row = 5, column = 3, ipady = 20 )
button_7.grid( row = 4, column = 1, ipady = 20 )
button_8.grid( row = 4, column = 2, ipady = 20 )
button_9.grid( row = 4, column = 3, ipady = 20 )
button_0.grid( row = 7, column = 3, ipady = 20 )
button_A.grid( row = 4, column = 0, ipady = 20 )
button_B.grid( row = 5, column = 0, ipady = 20 )
button_C.grid( row = 6, column = 0, ipady = 20 )
button_D.grid( row = 7, column = 0, ipady = 20 )
button_E.grid( row = 7, column = 1, ipady = 20 )
button_F.grid( row = 7, column = 2, ipady = 20 )
button_CE.grid( row = 8, column = 3, ipady = 20 )
button_CR.grid( row = 8, column = 2, ipady = 20 )
button_add.grid( row = 4, column = 4, ipady = 19 )
button_sub.grid( row = 5, column = 4, ipady = 19 )
button_mul.grid( row = 6, column = 4, ipady = 19 )
button_div.grid( row = 7, column = 4, ipady = 19 )
button_equal.grid( row = 8, column = 4, ipady = 19 )
button_exit.grid( row = 8, column = 0, columnspan = 2, ipady = 20 )

root.mainloop()