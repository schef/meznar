# saved as greeting.py
import Pyro4
import datetime

import pygame
pygame.mixer.init()
songname = "school_bell.ogg"
pygame.mixer.music.load(songname)

class meznar(object):
  def play(self):
    if pygame.mixer.music.get_busy():
      #time = datetime.timedelta(pygame.mixer.music.get_pos()/1000000)
      time = pygame.mixer.music.get_pos()/1000
      text = ("still playing", songname, "at", str(time), "seconds")
      print(text)
      return(text)
    else:
      pygame.mixer.music.play()
      text = ("playing", songname, "at", datetime.datetime.now())
      print(text)
      return(text)
  def stop(self):
    if pygame.mixer.music.get_busy() == 0:
      text = ("nothing is playing")
      print(text)
      return(text)
    else:
      pygame.mixer.music.fadeout(1000)
      text = ("stoping by force")
      print(text)
      return(text)
  def load(self, filename):
    global songname
    songname = filename
    text = ("changing song to", songname)
    pygame.mixer.music.load(songname)
    print(text)
    return(text)

zvonar = meznar()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()
uri=daemon.register(zvonar)   # register the greeting object as a Pyro object
ns.register("meznar", uri)

#print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
try:
  print("Ready.")
  daemon.requestLoop()                  # start the event loop of the server to wait for calls
except KeyboardInterrupt:
  print("Bye.")
