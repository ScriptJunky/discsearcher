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

### COLUMNS
| Index | Name | Manufacturer | Type | Speed | Glide | Turn | Fade |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 47 | Archon | Innova | Distance | 11.0 | 5 | -2.0 | 2.0 |
| 367 | Medusa | Skyquest | Distance | 11.0 | 5 | -2.0 | 2.0 |
| 385 | Mystere | Innova | Distance | 11.0 | 6 | -2.0 | 2.0 |
| 490 | Renegade | Dynamic Discs | Distance | 11.0 | 5 | -2.0 | 3.0 |
| 682 | Wave | MVP | Distance | 11.0 | 5 | -2.0 | 2.0 |
| 687 | Wildcat | Discraft | Distance | 11.0 | 5 | -2.0 | 3.0 |

### USAGE
```
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --speed 11 --turn -2
         Name   Manufacturer      Type  Speed  Glide  Turn  Fade
47     Archon         Innova  Distance   11.0      5  -2.0   2.0
367    Medusa       Skyquest  Distance   11.0      5  -2.0   2.0
385   Mystere         Innova  Distance   11.0      6  -2.0   2.0
490  Renegade  Dynamic Discs  Distance   11.0      5  -2.0   3.0
682      Wave            MVP  Distance   11.0      5  -2.0   2.0
687   Wildcat       Discraft  Distance   11.0      5  -2.0   3.0
➜~/git/discsearcher(master✗)»
```

```
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --type Putter --glide 5 --turn 0 --mfgr 'Latitude 64'
       Name Manufacturer    Type  Speed  Glide  Turn  Fade
166  Dagger  Latitude 64  Putter    2.0      5   0.0   1.0
346  Macana  Latitude 64  Putter    2.0      5   0.0   1.0
➜~/git/discsearcher(master✗)»
```

#### AS OF 11/21/2020, COMPOUND SEARCHES ARE SUPPORTED!
```
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --turn -4 --turn -5 --speed 11 --speed 10 --fade 2                                                                                                                          [16:39:53]
         Name      Manufacturer      Type  Speed  Glide  Turn  Fade
29   Aquarius   Millenium Discs  Distance     10      5    -4   2.0
461   Nemesis      Legacy Discs  Distance     10      6    -4   2.0
462   Nemesis  Kaufinator Discs  Distance     10      6    -4   2.0
805       Wei       Yikun Discs  Distance     10      5    -5   2.0
➜~/git/discsearcher(master✗)»
```
