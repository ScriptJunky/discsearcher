# Discsearcher

## discsearcher-inbounds.py
**discsearcher-inbounds.py** relies on external tools for filtering and sorting of output data (See USAGE below).
It pulls all of the flight chart data from inbounds disc golf.


### COLUMNS
| Manufacturer | Disc | Disc Type | Distance | HST (High Speed Turn) | LSF (Low Speed Fade) | Net Stability | ??? | Disc Name |  ??? |
| -------- | --------- | ------- | -------- | --------- | ------- | -------- | -------- | -------- | -------- |
| Discraft | Buzzz | Mid-Range | 296 | -18% | 23% | 5% | Y | Buzzz | 9-5 |
| Discraft | Buzzz OS | Mid-Range | 293 | 0% | 58% | 58% | Y | Buzzz OS | 9-3 |

### USAGE
```
➜~/git/discsearcher(master✗)» python3 discsearcher.py | grep Buzz
Discraft        Buzzz   Mid-Range       296     -18%    23%     5%      Y       Buzzz   9-5
Discraft        Buzzz OS        Mid-Range       293     0%      58%     58%     Y       Buzzz OS        9-3
Discraft        Buzzz SS        Mid-Range       296     -32%    20%     -12%    Y       Buzzz SS        9-6
Discraft        Buzzz-GT        Mid-Range       290     -13%    23%     10%     Y       Buzzz-GT        9-5
➜~/git/discsearcher(master✗)»
```

```
➜~/git/discsearcher(master✗)» python3 discsearcher.py | grep Infinite
Infinite Discs  Chariot Mid-Range       299     0%      18%     18%     Y       Chariot 9-5
Infinite Discs  Exodus  Fairway Driver  332     -9%     37%     28%     Y       Exodus  7-4
Infinite Discs  Myth    Putt & Approach 240     0%      36%     36%     Y       Myth    11-4
Infinite Discs  Pharaoh Distance Driver 439     -19%    39%     20%     Y       Pharaoh 2-5
Infinite Discs  Slab    Distance Driver 411     0%      78%     78%     Y       Slab    3-2
Infinite Discs  Sphinx  Fairway Driver  368     -57%    19%     -38%    Y       Sphinx  5-7
Infinite Discs  Tomb    Putt & Approach 261     0%      18%     18%     Y       Tomb    10-5
➜~/git/discsearcher(master✗)»
```

## discsearcher-local.py
**discsearcher-local.py** relies on CLI arguments for filtering and sorting of output data (See USAGE below).
It pulls all of the flight chart data from a local CSV file that has values sourced from Infinite Discs..

### USAGE

##### Standard Queries
```
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --turn -2.0 --mfgr Discraft
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
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --mfgrrx '^(Axiom|MVP)' --turnrx '^-2\.[0-9]'
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
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --turnrx '^-2\.[0-9]' --mfgr Discraft --mfgr Innova
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
