# player1,blue
from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player = 0 #which player
turn = 1 #check turn (game finished or not)
redScore =0
blueScore =0
flag=0      # indicates all button pressed
peep= [0]*31
poop = [0]*31

def win(player):
    messagebox.showinfo(title="Winner Winner Chicken Dinner",
                        message="Winner is player: " + str(player) + "\nwith score: " + str(
                            redScore) if player == 1 else str(blueScore))
    wind.destroy()


# counting how many squares each player got "score" and move the turn
def check():
    global turn
    global blueScore
    global redScore
    global flag
    global peep
    global poop
    turn +=1
        
    b1=bt1['bg']
    b2=bt2['bg']
    b3=bt3['bg']
    b4=bt4['bg']
    b5=bt5['bg']
    b6=bt6['bg']
    b7=bt7['bg']
    b8=bt8['bg']
    b9=bt9['bg']
    b10 = bt10['bg']
    b11 = bt11['bg']
    b12 = bt12['bg']
    b13 = bt13['bg']
    b14 = bt14['bg']
    b15 = bt15['bg']
    b16 = bt16['bg']
    b17 = bt17['bg']
    b18 = bt18['bg']
    b19 = bt19['bg']
    b20 = bt20['bg']
    b21 = bt21['bg']
    b22 = bt22['bg']
    b23 = bt23['bg']
    b24 = bt24['bg']
    b25 = bt25['bg']
    b26 = bt26['bg']
    b27 = bt27['bg']
    b28 = bt28['bg']
    b29 = bt29['bg']
    b30 = bt30['bg']
    b31 = bt31['bg']

    # calculate score
    if (b4==b1==b5==b8=='blue') and not peep[0]:
        blueScore +=1
        peep[0]=1
        score()
    elif(b4==b1==b5==b8=='red') and not poop[0]:
        redScore +=1
        poop[0]=1
    if (b6==b5==b2==b9=='blue') and not peep[1]:
        blueScore+=1
        peep[1]=1
        score()
    elif (b6 == b5 == b2 == b9 == 'red') and not poop[1]:
        redScore += 1
        poop[1]=1
    if (b3==b10==b6==b7=='blue') and not peep[2]:
        blueScore +=1
        peep[2]=1
        score()
    elif (b3==b10==b6==b7=='red') and not poop[2]:
        redScore +=1
        poop[2]=1
    if (b8==b15== b11==b12 =='blue') and not peep[3]:
        blueScore+=1
        peep[3]=1
        score()
    elif(b8==b15== b11==b12 =='red') and not poop[3]:
        redScore+=1
        poop[3]=1
    if (b9==b16== b13==b12 =='blue') and not peep[4]:
        blueScore+=1
        peep[4]=1
        score()
    elif(b9==b16== b13==b12 =='red') and not poop[4]:
        redScore+=1
        poop[4]=1
    if (b9 == b16 == b13 == b12 == 'blue') and not peep[5]:
        blueScore += 1
        peep[5]=1
        score()
    elif (b9 == b16 == b13 == b12 == 'red') and not poop[5]:
        redScore += 1
        poop[5]=1
    if (b9==b16== b13==b12 =='blue')and not peep[6]:
        blueScore+=1
        peep[6]=1
        score()
    elif(b9==b16== b13==b12 =='red') and not poop[6]:
        redScore+=1
        poop[6]=1
    if (b10==b17== b13==b14 =='blue')and not peep[7]:
        blueScore+=1
        peep[7]=1
        score()
    elif(b10==b17== b13==b14 =='red') and not poop[7]:
        redScore+=1
        poop[7]=1
    if (b15==b22== b18==b19 =='blue')and not peep[8]:
        blueScore+=1
        peep[8]=1
        score()
    elif(b15==b22== b18==b19 =='red') and not poop[8]:
        redScore+=1
        poop[8]=1
    if (b16==b23== b19==b20 =='blue')and not peep[9]:
        blueScore+=1
        peep[9]=1
        score()
    elif(b16==b23== b19==b20 =='red') and not poop[9]:
        redScore+=1
        poop[9]=1
    if (b17==b24== b20==b21 =='blue')and not peep[10]:
        blueScore+=1
        peep[10]=1
        score()
    elif(b17==b24== b20==b21 =='red') and not poop[10]:
        redScore+=1
        poop[10]=1
    if (b22==b29== b25==b26 =='blue')and not peep[11]:
        blueScore+=1
        peep[11]=1
        score()
    elif(b22==b29== b25==b26 =='red') and not poop[11]:
        redScore+=1
        poop[11]=1
    if (b23==b30== b26==b27 =='blue')and not peep[12]:
        blueScore+=1
        peep[12]=1
        score()
    elif(b23==b30== b26==b27=='red') and not poop[12]:
        redScore+=1
        poop[12]=1
    if (b24==b31== b27==b28 =='blue')and not peep[13]:
        blueScore+=1
        peep[13]=1
        score()
    elif(b24==b31== b27==b28  =='red') and not poop[13]:
        redScore+=1
        poop[13]=1

    # find a winner
    if flag == 16:
        if redScore > blueScore:
            win(2)
        elif blueScore > redScore:
            win(1)

# on click event, according to the player change the background
def clicked1():
    global player
    global flag
    if bt1['bg']=="white":
        if player == 1:
            player=2
            flag+=1
            bt1['bg']='blue'
            send_play(1)
        check()

def clicked2():
    global player
    global flag
    if bt2['bg']=="white":
        if player == 1:
            player=2
            flag+=1
            bt2['bg']='blue'
            send_play(2)
        check()

def clicked3():
    global player
    global flag
    if bt3['bg']=="white":
        if player == 1:
            player=2
            flag+=1
            bt3['bg']='blue'
            send_play(3)
        check()

def clicked4():
    global player
    global flag
    if bt4['bg']=="white":
        if player == 1:
            player=2
            flag+=1
            bt4['bg']='blue'
            send_play(4)
        check()

def clicked5():
    global player
    global flag
    if bt5['bg']=="white":
        if player == 1:
            player=2
            flag+=1
            bt5['bg']='blue'
            send_play(5)
        check()

def clicked6():
    global player
    global flag
    if bt6['bg']=="white":
        if player == 1:
            player=2
            flag+=1
            bt6['bg']='blue'
            send_play(6)
        check()

def clicked7():
    global player
    global flag
    if bt7['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt7['bg'] = 'blue'
            send_play(7)
        check()

def clicked8():
    global player
    global flag
    if bt8['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt8['bg'] = 'blue'
            send_play(8)
        check()

def clicked9():
    global player
    global flag
    if bt9['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt9['bg'] = 'blue'
            send_play(9)
        check()

def clicked10():
    global player
    global flag
    if bt10['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt10['bg'] = 'blue'
            send_play(10)
        check()

def clicked11():
    global player
    global flag
    if bt11['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt11['bg'] = 'blue'
            send_play(11)
        check()

def clicked12():
    global player
    global flag
    if bt12['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt12['bg'] = 'blue'
            send_play(12)
        check()

def clicked13():
    global player
    global flag
    if bt13['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt13['bg'] = 'blue'
            send_play(13)
        check()

def clicked14():
    global player
    global flag
    if bt14['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt14['bg'] = 'blue'
            send_play(14)
        check()

def clicked15():
    global player
    global flag
    if bt15['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt15['bg'] = 'blue'
            send_play(15)
        check()

def clicked16():
    global player
    global flag
    if bt16['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt16['bg'] = 'blue'
            send_play(16)
        check()

def clicked17():
    global player
    global flag
    if bt17['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt17['bg'] = 'blue'
            send_play(17)
        check()

def clicked18():
    global player
    global flag
    if bt18['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt18['bg'] = 'blue'
            send_play(18)
        check()

def clicked19():
    global player
    global flag
    if bt19['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt19['bg'] = 'blue'
            send_play(19)
        check()

def clicked20():
    global player
    global flag
    if bt20['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt20['bg'] = 'blue'
            send_play(20)
        check()

def clicked21():
    global player
    global flag
    if bt21['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt21['bg'] = 'blue'
            send_play(21)
        check()

def clicked22():
    global player
    global flag
    if bt22['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt22['bg'] = 'blue'
            send_play(22)
        check()

def clicked23():
    global player
    global flag
    if bt23['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt23['bg'] = 'blue'
            send_play(23)
        check()

def clicked24():
    global player
    global flag
    if bt24['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt24['bg'] = 'blue'
            send_play(24)
        check()

def clicked25():
    global player
    global flag
    if bt25['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt25['bg'] = 'blue'
            send_play(25)
        check()

def clicked26():
    global player
    global flag
    if bt26['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt26['bg'] = 'blue'
            send_play(26)
        check()

def clicked27():
    global player
    global flag
    if bt27['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt27['bg'] = 'blue'
            send_play(27)
        check()

def clicked28():
    global player
    global flag
    if bt28['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt28['bg'] = 'blue'
            send_play(28)
        check()

def clicked29():
    global player
    global flag
    if bt29['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt29['bg'] = 'blue'
            send_play(29)
        check()

def clicked30():
    global player
    global flag
    if bt30['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt30['bg'] = 'blue'
            send_play(30)
        check()

def clicked31():
    global player
    global flag
    if bt31['bg'] == "white":
        if player == 1:
            player = 2
            flag+=1
            bt31['bg'] = 'blue'
            send_play(31)
        check()

# update score
def score():
    global blueScore
    lbl.config(text=str(blueScore))


# to inform the other player i already played in this button
def send_play(n):
    n = str(n)
    n = n.encode()
    s.send(n)

# book this location for server and move the turn to client
def handle_play(n):
    global player
    n = n-1
    button_list[n]["bg"] = "red"    # server colour
    player = 1

# receiving location played from server
def apply_play(p):
    p = p.decode()
    p = int(p)
    handle_play(p)

wind = Tk()

wind.title('Client: Colour Lines')
wind.geometry('450x450')

lb1 = Label(wind, text='player 1: BLUE',fg="blue", font=('Helvetica','15'))
lb1.grid(row=0, column=0)
sclbl = Label(wind, text='Score:' ,fg="blue", font=('Helvetica','15'))
sclbl.grid(row=1, column=0)
lbl = Label(wind, fg="blue", font=('Helvetica', '15'))
lbl.grid(row=1, column=1)

button_list = list()


bt1=Button(wind, bg="white",width = 7, height = 1,command = clicked1)
bt1.grid(row = 4, column=3)

bt2=Button(wind, bg="white",width = 7, height = 1,command = clicked2)
bt2.grid(row = 4, column=5)

bt3=Button(wind,bg="white",width = 7, height = 1,command = clicked3)
bt3.grid(row = 4, column=7)

bt4=Button(wind, bg="white",width = 2, height = 3,command = clicked4)
bt4.grid(row = 5, column=2)

bt5=Button(wind,bg="white",width = 2, height = 3,command = clicked5)
bt5.grid(row = 5, column=4)

bt6=Button(wind,bg="white",width = 2, height = 3,command = clicked6)
bt6.grid(row = 5, column=6)

bt7=Button(wind,bg="white",width = 2, height = 3,command = clicked7)
bt7.grid(row = 5, column=8)

bt8=Button(wind,bg="white",width = 7, height = 1,command = clicked8)
bt8.grid(row = 6, column=3)

bt9=Button(wind,bg="white",width = 7, height = 1,command = clicked9)
bt9.grid(row = 6, column=5)

bt10=Button(wind,bg="white",width = 7, height = 1,command = clicked10)
bt10.grid(row = 6, column=7)

bt11=Button(wind,bg="white",width = 2, height = 3,command = clicked11)
bt11.grid(row = 7, column=2)

bt12=Button(wind,bg="white",width = 2, height = 3,command = clicked12)
bt12.grid(row = 7, column=4)

bt13=Button(wind,bg="white",width = 2, height = 3,command = clicked13)
bt13.grid(row = 7, column=6)

bt14=Button(wind,bg="white",width = 2, height = 3,command = clicked14)
bt14.grid(row = 7, column=8)

bt15=Button(wind,bg="white",width = 7, height = 1,command = clicked15)
bt15.grid(row = 8, column=3)

bt16=Button(wind,bg="white",width = 7, height = 1,command = clicked16)
bt16.grid(row = 8, column=5)

bt17=Button(wind,bg="white",width = 7, height = 1,command = clicked17)
bt17.grid(row = 8, column=7)

bt18=Button(wind,bg="white",width = 2, height = 3,command = clicked18)
bt18.grid(row = 9, column=2)

bt19=Button(wind,bg="white",width = 2, height = 3,command = clicked19)
bt19.grid(row = 9, column=4)

bt20=Button(wind,bg="white",width = 2, height = 3,command = clicked20)
bt20.grid(row = 9, column=6)

bt21=Button(wind,bg="white",width = 2, height = 3,command = clicked21)
bt21.grid(row = 9, column=8)

bt22=Button(wind,bg="white",width = 7, height = 1,command = clicked22)
bt22.grid(row = 10, column=3)

bt23=Button(wind,bg="white",width = 7, height = 1,command = clicked23)
bt23.grid(row = 10, column=5)

bt24=Button(wind,bg="white",width = 7, height = 1,command = clicked24)
bt24.grid(row = 10, column=7)

bt25=Button(wind,bg="white",width = 2, height = 3,command = clicked25)
bt25.grid(row = 11, column=2)

bt26=Button(wind,bg="white",width = 2, height = 3,command = clicked26)
bt26.grid(row = 11, column=4)

bt27=Button(wind,bg="white",width = 2, height = 3,command = clicked27)
bt27.grid(row = 11, column=6)

bt28=Button(wind,bg="white",width = 2, height = 3,command = clicked28)
bt28.grid(row = 11, column=8)

bt29=Button(wind,bg="white",width = 7, height = 1,command = clicked29)
bt29.grid(row = 12, column=3)

bt30=Button(wind,bg="white",width = 7, height = 1,command = clicked30)
bt30.grid(row = 12, column=5)

bt31=Button(wind,bg="white",width = 7, height = 1,command = clicked31)
bt31.grid(row = 12, column=7)

button_list.append(bt1)
button_list.append(bt2)
button_list.append(bt3)
button_list.append(bt4)
button_list.append(bt5)
button_list.append(bt6)
button_list.append(bt7)
button_list.append(bt8)
button_list.append(bt9)
button_list.append(bt10)
button_list.append(bt11)
button_list.append(bt12)
button_list.append(bt13)
button_list.append(bt14)
button_list.append(bt15)
button_list.append(bt16)
button_list.append(bt17)
button_list.append(bt18)
button_list.append(bt19)
button_list.append(bt20)
button_list.append(bt21)
button_list.append(bt22)
button_list.append(bt23)
button_list.append(bt24)
button_list.append(bt25)
button_list.append(bt26)
button_list.append(bt27)
button_list.append(bt28)
button_list.append(bt29)
button_list.append(bt30)
button_list.append(bt31)


    
s = socket(AF_INET, SOCK_STREAM)

s.connect(('127.0.0.1', 7000))

def receive_message():
    while True:
        p = s.recv(10)
        apply_play(p)
        

receive =Thread(target = receive_message)
receive.start()

wind.mainloop()