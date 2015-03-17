# meznar
Python implementacija crkvenih zvona.

DPENDENCIES:
sudo pip install schedule
sudo pacman -S pygame python-pyro

RUN:
prvo pokreni URI nameserver
```bash
python -m Pyro4.naming
```

onda
```bash
python meznar-server.py
```

i onda mores meznar-shell.py i/ili meznar-clock.py

u meznar-shell.py
komande su play i stop

