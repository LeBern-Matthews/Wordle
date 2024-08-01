
import tkinter as tk
from time import sleep
from backend import *

#Colors
OFF_WHITE="#FAF9F6"
BACKGROUND="#121213"
HIGHLIGHT="#3a3a3c"
YELLOW='#b59f3b'
GREEN='#538d4e'
LIGHT_GREY='#3a3a3c'
ERROR_RED='#B22222'

#storing the position of buttons
entry_pos=[]
current_pos=0
game_round=1


#storing the current guess in a string
guess=""
guess_number=1
#rows and collumns
rows=6
columns=5

#creating a funtion to center the game window
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

#creating game window
game = tk.Tk() 
game.title("Wordle clone")
#game.geometry("450x500")


#a function that is called evertime a letter is pressed
def funtionality(event):
    global current_pos, guess, guess_number
    
    if int(current_pos)<=29:
        display=event.char

        print(guess_number)
        
        if (display!="'" and display!='"' and display!='][/;.,```````:'and display!='['
            and display!=']'and display!='{'and display!='}'and display!='`'
            and display!='/'and display!="\\"and display!='?'and display!='|'
            and display!='.'and display!=';'and display!='<'and display!='>'
            and display!=',') and (guess_number%6!=0) and display!=" ":
            entry_pos[current_pos]["text"]=display.upper()
            current_pos+=1
            guess+=display.lower()
            print(guess)
            guess_number+=1
    else:
        pass
    

def newround(event):
    global guess, current_pos, guess_number,game_round, game_state
    
    if guess_number%6==0:
        
        if iswords(guess):
            state(winner_word, list(guess))
            if game_state==[1,1,1,1,1]:
                end_frame=tk.Frame(game, bg=BACKGROUND, highlightthickness=2)
                win=tk.Label(end_frame,text="YOU WON!", font="helvatica, 35", bg=BACKGROUND,fg=OFF_WHITE )
                end_btn=tk.Button(end_frame, text="End", bg=BACKGROUND,fg=OFF_WHITE,activebackground=ERROR_RED, command= game.destroy)
                win.pack()
                end_btn.pack(padx=40)
                
                end_frame.place(x=100, y=260)
                highscore(game_round,getscore)
            guess=""

            guess_number+=1
            
            current_pos-=5
            for status in game_state:
                if status==1:
                    entry_pos[current_pos]["bg"]=GREEN
                elif status==0:
                    entry_pos[current_pos]["bg"]=YELLOW
                else:
                    entry_pos[current_pos]["bg"]=LIGHT_GREY    
                current_pos+=1
            
            if game_round==6:
                end_frame=tk.Frame(game, bg=BACKGROUND, highlightthickness=2)
                win=tk.Label(end_frame,text="YOU LOST!", font="helvatica, 35", bg=BACKGROUND,fg=OFF_WHITE )
                end_btn=tk.Button(end_frame, text="End", bg=BACKGROUND,fg=OFF_WHITE,activebackground=ERROR_RED, command= game.destroy)
                win.pack()
                end_btn.pack(padx=40)
                
                end_frame.place(x=100, y=260)
                highscore(game_round,getscore)
            game_round+=1
            
    else:
        print("no")
        
    
def nothing(event):
    pass

#filling grid grid
def layout():
    #label creation
    outline=tk.Frame(game,bg=BACKGROUND, name="rawwww")
    welcome=tk.Label(outline, text = "Welcome to wordle!",fg=OFF_WHITE,bg=BACKGROUND, font="calibri, 20",justify="left",width=25) 
    instruct=tk.Label(outline, text = "Enter a five letter word to begin",
                      fg=OFF_WHITE,
                    bg=BACKGROUND,
                    height=1,
                    font="calibri, 20",width=25)
    
    highscore=tk.Label(outline, text = f"Highscore={getscore}",fg=OFF_WHITE,bg=BACKGROUND, font="ComicSansMS, 10")
    if int(getscore)!=0:
        highscore.place(x=325,y=0)
    welcome.grid(pady=10,row=2, column=1)
    instruct.grid(row=3, column=1)
    outline.pack()

    
    #letter grid creation
    grid=tk.Frame(game)
    for ROW in range(rows):
        for COLUMNS in range(columns):
            entry=tk.Button(grid, width=3, 
                        bg=BACKGROUND, 	
                        highlightbackground=BACKGROUND,
                        highlightcolor=HIGHLIGHT,
                        highlightthickness=2,
                        font="ClearSans, 30",
                        justify="center",
                        fg=OFF_WHITE, relief="raised")
            entry.grid(row=ROW+5, column=COLUMNS)
            entry_pos.append(entry)
    grid.pack()
    center_window(game)
layout()

#function to delete the last position when backspace is clicked
def delete(event):
    global current_pos,guess,guess_number, game_round
    
    def dlt():
        global current_pos,guess,guess_number, game_round
        guess_number-=1
        current_pos-=1
        entry_pos[current_pos]["text"]=""
        guess = guess[:-1]
        print(guess)
        
    match game_round:
        case 1:
            if current_pos!=0:
                dlt()
        case 2:
            if current_pos!=5:
                dlt()
        case 3:
            if current_pos!=10:
                dlt()
        case 4:
            if current_pos!=15:
                dlt()
        case 5:
            if current_pos!=20:
                dlt()
        case 6:
            if current_pos!=25:
                dlt()
        
    
def Keybinds():
    global current_pos
    game.bind('<BackSpace>',delete)

    game.bind("<Return>",newround)
    
    game.bind("<Cancel>",nothing)
    game.bind("<Tab>",nothing)
    game.bind("<Shift_L>",nothing)
    game.bind("<Control_L>",nothing)
    game.bind("<Alt_L>",nothing)
    game.bind("<Pause>",nothing)
    game.bind("<Caps_Lock>",nothing)
    game.bind("<Escape>",nothing)
    game.bind("<Prior>",nothing)
    game.bind("<Next>",nothing)
    game.bind("<End>",nothing)
    game.bind("<Home>",nothing)
    game.bind("<Left>",nothing)
    game.bind("<Up>",nothing)
    game.bind("<Right>",nothing)
    game.bind("<Down>",nothing)
    game.bind("<Print>",nothing)
    game.bind("<Insert>",nothing)
    game.bind("<Delete>",nothing)
    game.bind("<F1>",nothing)
    game.bind("<F2>",nothing)
    game.bind("<F3>",nothing)
    game.bind("<F4>",nothing)
    game.bind("<F5>",nothing)
    game.bind("<F6>",nothing)
    game.bind("<F7>",nothing)
    game.bind("<F8>",nothing)
    game.bind("<F9>",nothing)
    game.bind("<F10>",nothing)
    game.bind("<F11>",nothing)
    game.bind("<F12>",nothing)
    game.bind("<Num_Lock>",nothing)
    game.bind("<Scroll_Lock>",nothing)

    game.bind("<Key>",funtionality)
Keybinds()        

game['background']=BACKGROUND
game.resizable(False, False)

game.mainloop() 