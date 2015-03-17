# meznar
Python implementacija crkvenih zvona.

## Dependencies:

`sudo pacman -S python-pip`

`sudo pip install schedule`

`sudo pacman -S python-pyro`

`yaourt -S python-serpent`

`yaourt -S python-pygame-hg`

## Run:

prvo pokreni URI nameserver `python -m Pyro4.naming`

pa server `python meznar-server.py`

i onda mores `python meznar-shell.py` i/ili `python meznar-clock.py`

### meznar-shell.py
komande su play, stop i load za promjenu pjesme zvonjenja

### meznar-clock.py
u tom se fajlu definira kad bu zvonilo. mores sprobati deti vuru tipa koja bude dosla 17:47 u `schedule.every().day.at("17:15").do(hajde_pozvoni)`
## Reference:
[pygame.mixer.music](http://www.pygame.org/docs/ref/music.html)
[pygame.mixer](http://www.pygame.org/docs/ref/mixer.html)
[Pyro4](https://pythonhosted.org/Pyro4/intro.html)
[schedule](https://github.com/dbader/schedule)
