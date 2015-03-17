# saved as greeting.py
import Pyro4
import datetime

import pygame
pygame.mixer.init()
pygame.mixer.music.load("school_bell.ogg")

class meznar(object):
  def play(self):
    if pygame.mixer.music.get_busy():
      print("still playing")
      return("still playing")
    else:
      pygame.mixer.music.play()
      print("play", datetime.datetime.now())
      return("play")
  def stop(self):
    if pygame.mixer.music.get_busy() == 0:
      print("nothing is playing")
      return("nothing is playing")
    else:
      pygame.mixer.music.stop()
      print("stop")
      return("stop")

zvonar = meznar()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
uri=daemon.register(zvonar)   # register the greeting object as a Pyro object

print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
try:
  daemon.requestLoop()                  # start the event loop of the server to wait for calls
except KeyboardInterrupt:
  print("Bye.")
