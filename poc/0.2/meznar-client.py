# saved as client.py
import Pyro4

uri=input("What is the Pyro uri of the greeting object? ").strip()

zvonar=Pyro4.Proxy(uri)          # get a Pyro proxy to the greeting object
try:
  while 1:
    command = input("$ ")
    if command == "play":
      print(zvonar.play())   # call method normally
    elif command == "stop":
      print(zvonar.stop())   # call method normally
except KeyboardInterrupt:
  print("Bye.")
