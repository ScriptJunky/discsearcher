# Discsearcher

### USAGE

##### Standard Queries
```
➜~/git/discsearcher(master✗)» python3 discsearcher.py --turn -2.0 --mfgr Discraft
    Manufacturer     Name  Speed  Glide  Turn  Fade
145     Discraft  Spectra   11.8    4.9  -2.0   2.0
149     Discraft  Wildcat   11.0    5.0  -2.0   3.0
153     Discraft  Eclipse    6.8    5.0  -2.0   1.9
167     Discraft       XS    8.0    4.9  -2.0   3.0
192     Discraft   Fierce    3.0    4.0  -2.0   0.0
196     Discraft   Putt'r    2.0    3.1  -2.0   0.9
➜~/git/discsearcher(master✗)»
```

##### RegEx Queries
```
➜~/git/discsearcher(master✗)» python3 discsearcher.py --mfgrrx '^(Axiom|MVP)' --turnrx '^-2\.[0-9]'
    Manufacturer        Name  Speed  Glide  Turn  Fade
11         Axiom      Excite   13.9    5.3  -2.2   2.0
16         Axiom    Tenacity   13.0    5.0  -2.4   2.0
18         Axiom      Vanish   11.5    5.0  -2.7   1.9
22         Axiom    Insanity    9.8    4.9  -2.0   1.4
614          MVP    Catalyst   13.0    5.5  -2.0   1.6
617          MVP     Impulse   10.0    4.9  -2.9   1.1
626          MVP  Relativity   13.9    5.1  -2.5   1.6
631          MVP       Relay    6.1    5.0  -2.4   1.0
645          MVP      Vertex    4.2    4.0  -2.3   0.6
➜~/git/discsearcher(master✗)»
```

##### Compound Queries
```
➜~/git/discsearcher(master✗)» python3 discsearcher.py --turnrx '^-2\.[0-9]' --mfgr Discraft --mfgr Innova
    Manufacturer        Name  Speed  Glide  Turn  Fade
131     Discraft  Avenger SS    9.8    4.9  -2.9   1.0
133     Discraft    Crank SS   12.6    4.7  -2.8   1.8
145     Discraft     Spectra   11.8    4.9  -2.0   2.0
148     Discraft    Thrasher   11.9    5.1  -2.8   1.9
149     Discraft     Wildcat   11.0    5.0  -2.0   3.0
153     Discraft     Eclipse    6.8    5.0  -2.0   1.9
154     Discraft        Heat    9.0    5.7  -2.9   1.0
160     Discraft       Sting    6.8    4.9  -2.2   0.9
167     Discraft          XS    8.0    4.9  -2.0   3.0
182     Discraft      Meteor    4.2    4.9  -2.8   1.0
184     Discraft         Sol    4.0    4.8  -2.9   0.4
192     Discraft      Fierce    3.0    4.0  -2.0   0.0
196     Discraft      Putt'r    2.0    3.1  -2.0   0.9
332       Innova       Beast   10.0    5.0  -2.0   1.9
342       Innova      Katana   13.0    5.0  -2.7   2.9
348       Innova     Mystere   11.0    6.0  -2.2   1.9
350       Innova      Shryke   12.9    6.0  -2.0   2.0
355       Innova        Tern   12.0    6.0  -2.1   2.0
357       Innova       Wahoo   11.9    6.0  -2.1   2.0
362       Innova     Cheetah    6.0    4.0  -2.0   2.0
363       Innova      Dragon    7.9    4.9  -2.3   1.8
374       Innova       Raven    6.0    4.0  -2.0   2.0
377       Innova  Sidewinder    9.0    5.0  -2.8   1.1
384       Innova    Valkyrie    8.9    4.1  -2.0   2.0
390       Innova   Barracuda    5.0    4.0  -2.0   3.0
393       Innova       Cobra    4.0    5.0  -2.0   1.9
405       Innova        Kite    5.0    6.0  -2.9   1.0
408       Innova      Makani    2.0    7.0  -2.0   0.0
411       Innova       Manta    5.0    5.0  -2.7   1.0
424       Innova    Stingray    4.0    5.0  -2.8   1.0
432       Innova         Ace    2.0    3.0  -2.1   1.0
➜~/git/discsearcher(master✗)»
```
