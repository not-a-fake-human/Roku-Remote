from roku import Roku
from tkinter import *
import pygame

def tsearch():
    global sq
    sq = entry.get()
    roku.literal(sq)

#def setIP():
#    global mIP
#    mIP = entry.get()
#    global roku
#    roku = Roku(mIP)
#    entry.delete()

def IPSearch():
    global IPs
    global IPString
    IPs = roku.discover(timeout=10)
    IPString = ''.join(str(IP) for IP in IPs)
    entry.insert(0, IPString)

mIP = "0.0.0.0"
roku = Roku(mIP)
IPs = []
IPString = ""
screen_size = (700, 700)
pyrun = True
window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
twindow = Tk()
twindow.title("Text Box")
search = Button(twindow, text="Search", command=tsearch)
search.pack(side="right")
searchIPs = Button(twindow, text="Seach IPs", command=IPSearch)
searchIPs.pack(side="right")
#EnterIP = Button(twindow, text="Set IP", command=setIP)
#EnterIP.pack(side="right")
entry = Entry()
entry.config(font=("WimpyKid", 30))
entry.config(bg="#9121ad")
entry.pack()
sq = "hello"
yt = roku['YouTube']
disney = roku['Disney Plus']
netflix = roku['Netflix']
rokuChannel = roku['The Roku Channel']

pygame.init()
pygame.display.set_caption("Roku Remote")

while pyrun == True:
    window.fill((145, 33, 173))
    pygame.display.flip()
    twindow.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                roku.select()

            if event.key == pygame.K_LEFT:
                roku.left()

            if event.key == pygame.K_RIGHT:
                roku.right()

            if event.key == pygame.K_UP:
                roku.up()

            if event.key == pygame.K_DOWN:
                roku.down()

            if event.key == pygame.K_ESCAPE:
                roku.back()

            if event.key == pygame.K_F3:
                roku.home()

            if event.key == pygame.K_BACKSPACE:
                roku.backspace()

            if event.key == pygame.K_COMMA:
                roku.volume_down()

            if event.key == pygame.K_PERIOD:
                roku.volume_up()

            if event.key == pygame.K_F4:
                roku.info()

            if event.key == pygame.K_F1:
                roku.power()

            if event.key == pygame.K_F2:
                roku.volume_mute()

            if event.key == pygame.K_y:
                yt.launch()

            if event.key == pygame.K_d:
                disney.launch()

            if event.key == pygame.K_n:
                netflix.launch()

            if event.key == pygame.K_r:
                rokuChannel.launch()
