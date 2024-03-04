from tkinter import *
import pygame

root = Tk()
root.title('mp3py')
root.iconbitmap('./mp3.ico')
root.geometry('500x400')

pygame.mixer.init()

def play():
  pygame.mixer.music.load("songs/song3.mp3")
  pygame.mixer.music.play(loops=0)

def pause():
  pygame.mixer.music.stop()

btnPlay = Button(root, text='play', font=('Helvetica',32),command=play)
btnPlay.pack(pady=20)

btnPause = Button(root, text='pause', font=('Helvetica',16), command=pause)
btnPause.pack(pady=20)



root.mainloop()