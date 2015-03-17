# saved as client.py
import Pyro4

#uri=input("What is the Pyro uri of the greeting object? ").strip()

zvonar=Pyro4.Proxy("PYRONAME:meznar")          # get a Pyro proxy to the greeting object
try:
  while 1:
    command = input("$ ")
    if command == "play":
      print(zvonar.play())   # call method normally
    elif command == "stop":
      print(zvonar.stop())   # call method normally
    elif command == "load":
      filename = input("deni tocan relative path ili bolje apsolut: ")
      zvonar.load(filename)
except KeyboardInterrupt:
  print("Bye.")
