# saved as client.py
import Pyro4
import schedule
import time

#uri=input("What is the Pyro uri of the greeting object? ").strip()

def hajde_pozvoni():
  name = zvonar.play()
  print(name)
  print(schedule.next_run())

zvonar=Pyro4.Proxy("PYRONAME:meznar")

schedule.every().day.at("07:00").do(hajde_pozvoni)
schedule.every().day.at("12:00").do(hajde_pozvoni)
schedule.every().day.at("19:00").do(hajde_pozvoni)
schedule.every().day.at("17:15").do(hajde_pozvoni)

try:
  while 1:
    schedule.run_pending()
    time.sleep(1)
except KeyboardInterrupt:
  print("Bye.")
