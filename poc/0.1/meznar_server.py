# saved as greeting.py
import Pyro4

class meznar(object):
  def play(self):
    print("play")
    return("play")
  def stop(self):
    print("stop")
    return("stop")

zvonar = meznar()

daemon=Pyro4.Daemon()                 # make a Pyro daemon
uri=daemon.register(zvonar)   # register the greeting object as a Pyro object

print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
daemon.requestLoop()                  # start the event loop of the server to wait for calls
