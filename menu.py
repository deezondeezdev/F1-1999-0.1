from tkinter import *
f = open("car.txt", "w")
window = Tk()
window.geometry("1600x800+50+100")
bg = PhotoImage(file = "bg.png")
three_lap = PhotoImage(file = "imgs/3laps.png")
five_lap = PhotoImage(file = "imgs/5laps.png")
ten_lap = PhotoImage(file = "imgs/10laps.png")
albon = PhotoImage(file= "imgs/alabona.png")
bottas = PhotoImage(file= "imgs/Bottas.png")
Carlos = PhotoImage(file= "imgs/Carlos.png")
Charles = PhotoImage(file= "imgs/Charles.png")
Checo = PhotoImage(file= "imgs/Checo.png")
estenba = PhotoImage(file= "imgs/estenba.png")
Fernando = PhotoImage(file= "imgs/Fernando.png")
gasly = PhotoImage(file= "imgs/gasman.png")
george = PhotoImage(file= "imgs/George.png")
latifi = PhotoImage(file= "imgs/Goatifi.png")
kmag = PhotoImage(file= "imgs/K-mag.png")
jewis = PhotoImage(file= "imgs/Lewis.png")
Max = PhotoImage(file= "imgs/MaxVerstappen.png")
mick = PhotoImage(file= "imgs/mcik.png")
lando = PhotoImage(file= "imgs/Nando.png")
seb = PhotoImage(file= "imgs/seb.png")
stroll = PhotoImage(file= "imgs/stroll.png")
yuki = PhotoImage(file= "imgs/yuki.png")
Zhou = PhotoImage(file= "imgs/Zhou.png")
daniel = PhotoImage(file= "imgs/Daniel.png")
bg2 = PhotoImage(file= "bg2.png")
def leftchanger():
    if room == 1:
        driverroom2()
        driverroom2()
    if room == 2:
        driverroom3()
    if room == 3:
        driverroom4()
    if room == 4:
        driverroom5()
def rightchanger():

    if room == 1:
        print("ruhb")
    if room == 2:
        driverroom()
    if room == 3:
        driverroom2()
    if room == 4:
        driverroom3()
    if room == 5:
        driverroom4()
def ferrari():
    f.write("red")
    f.close()
    laproom()
def williams():
    f.write("williams")
    f.close()
    laproom()
def mclaren():
    f.write("mclaren")
    f.close()
    laproom()
def alpha():
    f.write("alphatauri")
    f.close()
    laproom()
def alfa():
    f.write("alfaromeo")
    f.close()
    laproom()
def merc():
    f.write("mercedes")
    f.close()
    laproom()
def alpine():
    f.write("alpine")
    f.close()
    laproom()
def aston():
    f.write("aston")
    f.close()
    laproom()
def haas():
    f.write("haas")
    f.close()
    laproom()
def redbull():
    f.write("redbull")
    f.close()
    laproom()
def laproom():
    buttonlando.place_forget()
    buttondaniel.place_forget()
    buttonbottas.place_forget()
    buttonzhou.place_forget()
    buttongasly.place_forget()
    buttonyuki.place_forget()
    buttonalbon.place_forget()
    buttonlatifi.place_forget()
    buttongeorge.place_forget()
    buttonjewis.place_forget()
    buttonfernando.place_forget()
    buttonestenba.place_forget()
    buttonseb.place_forget()
    buttonstroll.place_forget()
    buttonmick.place_forget()
    buttonmag.place_forget()
    buttoncarlos.place_forget()
    buttoncharles.place_forget()
    buttoncheco.place_forget()
    buttonmax.place_forget()
    leftbutton.place_forget()
    rightbutton.place_forget()
    button3laps.place(x= 50, y=200)
    button5laps.place(x=750, y=200)
    button10laps.place(x=1400, y=200)
arrowleft = PhotoImage(file="imgs/arrowleft.png")
arrowright = PhotoImage(file="imgs/arrowright.png")
label2 = Label(window, image= bg2)
button3laps = Button(window,image=three_lap)
button5laps = Button(window,image=five_lap)
button10laps = Button(window,image=ten_lap)
buttonalbon = Button(window,image= albon,command= williams)
buttonlatifi = Button(window,image= latifi,command= williams)
buttonmag = Button(window,image= kmag,command= haas)
buttonmick = Button(window,image= mick,command= haas)
buttonlando = Button(window,image= lando,command= mclaren)
buttondaniel = Button(window,image= daniel,command= mclaren)
buttonjewis = Button(window,image= jewis,command= merc)
buttongeorge = Button(window,image= george,command= merc)
buttonbottas = Button(window,image= bottas,command= alfa)
buttonzhou = Button(window,image= Zhou,command= alfa)
buttongasly = Button(window,image= gasly,command= alpha)
buttonyuki = Button(window,image= yuki,command= alpha)
buttonseb = Button(window,image= seb,command= aston)
buttonstroll = Button(window,image= stroll,command= aston)
buttonestenba = Button(window,image= estenba,command= alpine)
buttonfernando = Button(window,image= Fernando,command= alpine)
buttoncarlos = Button(window,image= Carlos,command=ferrari)
buttoncharles = Button(window,image= Charles,command=ferrari)
buttoncheco = Button(window,image= Checo,command=redbull)
buttonmax = Button(window,image= Max,command=redbull)
leftbutton = Button(window,image= arrowleft,command= leftchanger)
rightbutton = Button(window,image= arrowright,command= rightchanger)
def driverroom():
    global room
    room = 1
    label2.place(x=0,y=0)
    button2.place_forget()
    button1.place_forget()
    label1.place_forget()
    
    buttoncarlos.place(x= 50,y=200)
    leftbutton.place(x= 850, y= 600)
    rightbutton.place(x= 600, y= 600)
    buttoncharles.place(x= 400,y=200)
    buttoncheco.place(x= 850,y=200)
    buttonmax.place(x= 1200,y=200)
    
def driverroom2():
    global room
    room=2
    buttoncarlos.place_forget()
    buttoncharles.place_forget()
    buttoncheco.place_forget()
    buttonmax.place_forget()
    leftbutton.place_forget()
    buttongeorge.place(x= 50,y=200)
    buttonjewis.place(x= 400,y=200)
    buttonfernando.place(x= 850,y=200)
    buttonestenba.place(x= 1200,y=200)
    leftbutton.place(x= 850, y= 600)
    rightbutton.place(x= 600, y= 600)
def driverroom3():
    global room
    room=3
    buttongeorge.place_forget()
    buttonjewis.place_forget()
    buttonfernando.place_forget()
    buttonestenba.place_forget()
    buttonseb.place_forget()
    buttonstroll.place_forget()
    buttonmick.place_forget()
    buttonmag.place_forget()
    buttonlando.place(x= 50,y=200)
    buttondaniel.place(x= 400,y=200)
    buttonbottas.place(x= 850,y=200)
    buttonzhou.place(x= 1200,y=200)
def driverroom4():
    global room
    room=4
    buttonlando.place_forget()
    buttondaniel.place_forget()
    buttonbottas.place_forget()
    buttonzhou.place_forget()
    buttongasly.place_forget()
    buttonyuki.place_forget()
    buttonalbon.place_forget()
    buttonlatifi.place_forget()
    buttonseb.place(x= 50,y=200)
    buttonstroll.place(x= 400,y=200)
    buttonmick.place(x= 850,y=200)
    buttonmag.place(x= 1200,y=200)
def driverroom5():
    global room
    room=5
    buttonseb.place_forget()
    buttonstroll.place_forget()
    buttonmick.place_forget()
    buttonmag.place_forget()
    buttongasly.place(x= 50,y=200)
    buttonyuki.place(x= 400,y=200)
    buttonalbon.place(x= 850,y=200)
    buttonlatifi.place(x= 1200,y=200)




playbutton = PhotoImage(file= "imgs/playbutton.png")
settings = PhotoImage(file= "imgs/Settings.png")
label1 = Label(window, image = bg)
label1.place(x = 0, y = 0)
button1 = Button(window, image= playbutton,command=driverroom)
button1.place(x=100,y=250)
button2 = Button(window, image= settings)
button2.place(x=100,y=550)
window.mainloop()