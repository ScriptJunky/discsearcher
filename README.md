

## Running discsearcher
The manufacturers and discnames flags produce column values that are uniqued, and sorted, prior to output.

### Listing Manufacturers
Limiting to 15 w/ head
```
{20:16}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --manufacturers | head -15          
Above-Ground-Level
Alfa-Discs
AquaFlight
Axiom
Cheengz
DGA
Daredevil
Dino-Discs
Disc-Golf-UK
Discmania
Discraft
Disctroyer
Divergent-Discs
Dynamic-Discs
EV-7
{20:16}~/git/discsearcher:master ✗ ➭ 
```

### Listing Disc Models
Limiting to 15 w/ head
```
{20:18}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --discnames | head -15              
#1 Driver
#1 Flyer
#1 Helix
#1 Hookshot
#1 Hyzer
#1 Roller
#1 Slice
#2 Driver
#2 Flyer
#2 Helix
#2 Hookshot
#2 Hyzer
#2 Putter
#2 Roller
#2 Slice
{20:18}~/git/discsearcher:master ✗ ➭ 
```

### Getting Disc Models by Name
```
{20:20}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --name Paradox Uplink Theory 
Manufacturer    Name     Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
--------------  -------  -------  -------  ------  ------  ----------  --------  ----------  ----------  ----------------------------------------------------
Axiom           Paradox  5.0      4.0      -3.9    0.0     21.5        1.8       1.3         1.3         https://infinitediscs.com/Axiom-Paradox?tag=3c8c6529
Axiom           Theory   4.6      4.6      -1.8    0.7     21.5        1.9       1.3         1.2         https://infinitediscs.com/Axiom-Theory?tag=3c8c6529
MVP             Uplink   5.0      3.0      -2.0    2.0     21.5        1.8       1.4         1.3         https://infinitediscs.com/MVP-Uplink?tag=3c8c6529
{20:22}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --namerx '^(Paradox|Uplink|Theory)'
Manufacturer    Name     Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
--------------  -------  -------  -------  ------  ------  ----------  --------  ----------  ----------  ----------------------------------------------------
Axiom           Paradox  5.0      4.0      -3.9    0.0     21.5        1.8       1.3         1.3         https://infinitediscs.com/Axiom-Paradox?tag=3c8c6529
Axiom           Theory   4.6      4.6      -1.8    0.7     21.5        1.9       1.3         1.2         https://infinitediscs.com/Axiom-Theory?tag=3c8c6529
MVP             Uplink   5.0      3.0      -2.0    2.0     21.5        1.8       1.4         1.3         https://infinitediscs.com/MVP-Uplink?tag=3c8c6529
{20:22}~/git/discsearcher:master ✗ ➭ 
```

### Getting Disc Manufacturers by Name
```
{21:06}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --mfgr EV-7 Kastaplast                     
Manufacturer    Name     Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
--------------  -------  -------  -------  ------  ------  ----------  --------  ----------  ----------  --------------------------------------------------------
EV-7            Penrose  2.0      4.0      0.0     1.9     21.1        2.1       1.5         1.1         https://infinitediscs.com/EV-7-Penrose?tag=3c8c6529
EV-7            Phi      1.3      1.5      0.0     0.2     21.0        2.0       1.5         1.1         https://infinitediscs.com/EV-7-Phi?tag=3c8c6529
Kastaplast      Grym     13.0     5.0      -1.3    2.0     21.2        1.6       1.1         2.2         https://infinitediscs.com/Kastaplast-Grym?tag=3c8c6529
Kastaplast      Grym X   12.4     5.0      -0.3    2.6     21.2        1.6       1.1         2.2         https://infinitediscs.com/Kastaplast-Grym-X?tag=3c8c6529
Kastaplast      Rask     13.7     3.1      0.0     4.3     21.1        1.6       1.1         2.2         https://infinitediscs.com/Kastaplast-Rask?tag=3c8c6529
Kastaplast      Falk     8.9      5.8      -2.3    1.3     21.1        1.8       1.1         1.9         https://infinitediscs.com/Kastaplast-Falk?tag=3c8c6529
Kastaplast      Lots     9.0      5.0      -1.0    1.9     21.1        1.5       1.1         1.9         https://infinitediscs.com/Kastaplast-Lots?tag=3c8c6529
Kastaplast      Stal     9.0      4.0      0.0     3.1     21.1        1.8       1.1         1.9         https://infinitediscs.com/Kastaplast-Stal?tag=3c8c6529
Kastaplast      Gote     4.0      5.0      -0.2    0.9     21.9        2.1       1.3         1.3         https://infinitediscs.com/Kastaplast-Gote?tag=3c8c6529
Kastaplast      Kaxe     6.0      4.2      0.0     2.9     21.0        1.9       1.3         1.5         https://infinitediscs.com/Kastaplast-Kaxe?tag=3c8c6529
Kastaplast      Kaxe Z   6.0      5.0      -0.1    1.9     21.1        1.9       1.3         1.5         https://infinitediscs.com/Kastaplast-Kaxe-Z?tag=3c8c6529
Kastaplast      Svea     5.0      6.0      -1.0    0.1     21.9        2.1       1.3         1.3         https://infinitediscs.com/Kastaplast-Svea?tag=3c8c6529
Kastaplast      Berg     1.1      1.4      0.0     1.8     21.1        2.0       1.4         0.9         https://infinitediscs.com/Kastaplast-Berg?tag=3c8c6529
Kastaplast      Reko     3.0      3.2      -0.2    1.2     21.2        1.8       1.4         1.0         https://infinitediscs.com/Kastaplast-Reko?tag=3c8c6529
{21:07}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --mfgrrx '^(EV-7|Kastaplast)'
Manufacturer    Name     Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
--------------  -------  -------  -------  ------  ------  ----------  --------  ----------  ----------  --------------------------------------------------------
EV-7            Penrose  2.0      4.0      0.0     1.9     21.1        2.1       1.5         1.1         https://infinitediscs.com/EV-7-Penrose?tag=3c8c6529
EV-7            Phi      1.3      1.5      0.0     0.2     21.0        2.0       1.5         1.1         https://infinitediscs.com/EV-7-Phi?tag=3c8c6529
Kastaplast      Grym     13.0     5.0      -1.3    2.0     21.2        1.6       1.1         2.2         https://infinitediscs.com/Kastaplast-Grym?tag=3c8c6529
Kastaplast      Grym X   12.4     5.0      -0.3    2.6     21.2        1.6       1.1         2.2         https://infinitediscs.com/Kastaplast-Grym-X?tag=3c8c6529
Kastaplast      Rask     13.7     3.1      0.0     4.3     21.1        1.6       1.1         2.2         https://infinitediscs.com/Kastaplast-Rask?tag=3c8c6529
Kastaplast      Falk     8.9      5.8      -2.3    1.3     21.1        1.8       1.1         1.9         https://infinitediscs.com/Kastaplast-Falk?tag=3c8c6529
Kastaplast      Lots     9.0      5.0      -1.0    1.9     21.1        1.5       1.1         1.9         https://infinitediscs.com/Kastaplast-Lots?tag=3c8c6529
Kastaplast      Stal     9.0      4.0      0.0     3.1     21.1        1.8       1.1         1.9         https://infinitediscs.com/Kastaplast-Stal?tag=3c8c6529
Kastaplast      Gote     4.0      5.0      -0.2    0.9     21.9        2.1       1.3         1.3         https://infinitediscs.com/Kastaplast-Gote?tag=3c8c6529
Kastaplast      Kaxe     6.0      4.2      0.0     2.9     21.0        1.9       1.3         1.5         https://infinitediscs.com/Kastaplast-Kaxe?tag=3c8c6529
Kastaplast      Kaxe Z   6.0      5.0      -0.1    1.9     21.1        1.9       1.3         1.5         https://infinitediscs.com/Kastaplast-Kaxe-Z?tag=3c8c6529
Kastaplast      Svea     5.0      6.0      -1.0    0.1     21.9        2.1       1.3         1.3         https://infinitediscs.com/Kastaplast-Svea?tag=3c8c6529
Kastaplast      Berg     1.1      1.4      0.0     1.8     21.1        2.0       1.4         0.9         https://infinitediscs.com/Kastaplast-Berg?tag=3c8c6529
Kastaplast      Reko     3.0      3.2      -0.2    1.2     21.2        1.8       1.4         1.0         https://infinitediscs.com/Kastaplast-Reko?tag=3c8c6529
{21:07}~/git/discsearcher:master ✗ ➭ 
```

### Searching for Discs by Flight Numbers
```
{22:51}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --speedrx '10\.(1|3)'
Manufacturer    Name      Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
--------------  --------  -------  -------  ------  ------  ----------  --------  ----------  ----------  ------------------------------------------------------
Axiom           Wrath     10.1     4.3      -0.9    2.1     21.0        1.4       1.2         2.0         https://infinitediscs.com/Axiom-Wrath?tag=3c8c6529
DGA             Hellfire  10.1     3.1      0.0     4.8     21.1        1.6       1.2         2.2         https://infinitediscs.com/DGA-Hellfire?tag=3c8c6529
Discraft        Flick     10.1     3.4      0.9     4.4     21.1        1.3       1.1         2.1         https://infinitediscs.com/Discraft-Flick?tag=3c8c6529
Innova          Invictus  10.3     4.3      -0.3    2.7     21.2        1.5       1.2         2.1         https://infinitediscs.com/Innova-Invictus?tag=3c8c6529
Innova          Monster   10.1     2.9      0.1     4.9     21.2        1.4       1.2         2.0         https://infinitediscs.com/Innova-Monster?tag=3c8c6529
Yikun           Wei       10.1     5.0      -2.9    1.9     21.1        1.7       1.1         2.0         https://infinitediscs.com/Yikun-Wei?tag=3c8c6529
{22:51}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --speed 10.1 10.3    
Manufacturer    Name      Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
--------------  --------  -------  -------  ------  ------  ----------  --------  ----------  ----------  ------------------------------------------------------
Axiom           Wrath     10.1     4.3      -0.9    2.1     21.0        1.4       1.2         2.0         https://infinitediscs.com/Axiom-Wrath?tag=3c8c6529
DGA             Hellfire  10.1     3.1      0.0     4.8     21.1        1.6       1.2         2.2         https://infinitediscs.com/DGA-Hellfire?tag=3c8c6529
Discraft        Flick     10.1     3.4      0.9     4.4     21.1        1.3       1.1         2.1         https://infinitediscs.com/Discraft-Flick?tag=3c8c6529
Innova          Invictus  10.3     4.3      -0.3    2.7     21.2        1.5       1.2         2.1         https://infinitediscs.com/Innova-Invictus?tag=3c8c6529
Innova          Monster   10.1     2.9      0.1     4.9     21.2        1.4       1.2         2.0         https://infinitediscs.com/Innova-Monster?tag=3c8c6529
Yikun           Wei       10.1     5.0      -2.9    1.9     21.1        1.7       1.1         2.0         https://infinitediscs.com/Yikun-Wei?tag=3c8c6529
{22:51}~/git/discsearcher:master ✗ ➭ 
```

### Getting Disc Info of Discs With Speed 10.0-10.9, and Sorting Fastest to Slowest
Limiting to 15 w/ head
```
{22:54}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --speedrx '10\.\d' --sortby speed --sortorder desc | head -15
Manufacturer             Name                  Speed    Glide    Turn    Fade    Diameter    Height    RimDepth    RimWidth    Purchase Url
-----------------------  --------------------  -------  -------  ------  ------  ----------  --------  ----------  ----------  ----------------------------------------------------------------------------
Prodigy                  H2 V2                 10.9     4.9      -0.2    2.4     21.4        1.6       1.2         2.0         https://infinitediscs.com/Prodigy-H2-V2?tag=3c8c6529
Discmania                PDx                   10.9     4.0      -0.1    3.0     21.1        1.9       1.2         2.1         https://infinitediscs.com/Discmania-PDx?tag=3c8c6529
Skyquest                 Medusa                10.9     5.0      -2.1    1.9     21.2        1.5       1.1         2.1         https://infinitediscs.com/Skyquest-Medusa?tag=3c8c6529
Discmania                CD3                   10.9     5.0      -1.0    2.1     21.1        2.0       1.2         2.1         https://infinitediscs.com/Discmania-CD3?tag=3c8c6529
Millennium               Astra                 10.9     5.1      -2.0    1.9     21.1        1.5       1.2         2.2         https://infinitediscs.com/Millennium-Astra?tag=3c8c6529
Sune-Sport               Short Slacker         10.9     5.0      -1.3    1.9     21.0        1.4       1.2         2.1         https://infinitediscs.com/Sune-Sport-Short-Slacker?tag=3c8c6529
Discraft                 Pulse                 10.9     3.9      0.0     3.0     21.2        1.7       1.3         2.1         https://infinitediscs.com/Discraft-Pulse?tag=3c8c6529
Dynamic-Discs            Renegade              10.9     5.0      -2.1    2.6     21.1        1.7       1.1         2.1         https://infinitediscs.com/Dynamic-Discs-Renegade?tag=3c8c6529
Prodigy                  H1 V2                 10.8     4.0      0.0     3.0     21.4        1.6       1.2         2.0         https://infinitediscs.com/Prodigy-H1-V2?tag=3c8c6529
Westside                 Boatman               10.8     5.1      -0.1    2.1     21.4        1.9       1.3         2.2         https://infinitediscs.com/Westside-Boatman?tag=3c8c6529
Prodigy                  H3 V2                 10.7     5.0      -1.0    2.1     21.3        1.8       1.2         2.0         https://infinitediscs.com/Prodigy-H3-V2?tag=3c8c6529
Discraft                 Machete               10.6     3.7      0.2     3.9     21.1        1.6       1.1         2.1         https://infinitediscs.com/Discraft-Machete?tag=3c8c6529
Gateway                  Ninja                 10.6     4.9      -0.1    2.1     21.0        1.9       1.2         2.0         https://infinitediscs.com/Gateway-Ninja?tag=3c8c6529
{22:55}~/git/discsearcher:master ✗ ➭ 
```

Limiting to last 15 w/ tail
```
{22:57}~/git/discsearcher:master ✗ ➭ ./discsearcher.py --speedrx '10\.\d' --sortby speed --sortorder desc | tail -15
Prodigy                  F Model S             10.0     4.9      0.3     2.9     21.0        1.5       1.2         2.0         https://infinitediscs.com/Prodigy-F-Model-S?tag=3c8c6529
Prodigy                  F Model OS            10.0     5.0      1.4     3.6     21.3        1.5       1.1         2.1         https://infinitediscs.com/Prodigy-F-Model-OS?tag=3c8c6529
Mint-Discs               Freetail              10.0     6.0      -3.2    1.8     21.1        1.7       1.2         2.0         https://infinitediscs.com/Mint-Discs-Freetail?tag=3c8c6529
Millennium               Aquarius              10.0     5.1      -3.7    1.8     21.0        1.9       1.2         2.0         https://infinitediscs.com/Millennium-Aquarius?tag=3c8c6529
MVP                      Tesla                 10.0     4.6      -0.6    2.3     21.0        1.4       1.2         2.0         https://infinitediscs.com/MVP-Tesla?tag=3c8c6529
MVP                      Impulse               10.0     4.9      -2.9    1.1     21.1        1.4       1.2         2.0         https://infinitediscs.com/MVP-Impulse?tag=3c8c6529
DGA                      Undertow              10.0     4.1      -1.0    1.1     21.2        1.5       1.2         1.8         https://infinitediscs.com/DGA-Undertow?tag=3c8c6529
Discmania                TD                    10.0     5.8      -1.8    1.1     21.2        1.6       1.1         1.9         https://infinitediscs.com/Discmania-TD-Rush?tag=3c8c6529
Skyquest                 Lucky 13              10.0     5.0      -3.0    2.0     21.2        1.5       1.1         2.1         https://infinitediscs.com/Skyquest-Lucky-13?tag=3c8c6529
Latitude-64              Musket                10.0     4.9      -0.7    2.2     21.2        1.8       1.1         2.0         https://infinitediscs.com/Latitude-64-Musket?tag=3c8c6529
Discmania                CD                    10.0     4.8      -0.9    2.0     21.2        1.3       1.1         1.9         https://infinitediscs.com/Discmania-CD-Craze?tag=3c8c6529
Dino-Discs               Pterodactylus         10.0     5.0      -3.3    1.1     21.1        2.0       1.1         1.9         https://infinitediscs.com/Dino-Discs-Pterodactylus?tag=3c8c6529
Kaufinator-Discs         Kaufinator Vengeance  10.0     5.0      0.0     2.0     21.1        1.7       1.7         2.0         https://infinitediscs.com/Kaufinator-Discs-Kaufinator Vengeance?tag=3c8c6529
Kaufinator-Discs         Kaufinator Nemesis    10.0     6.0      -4.0    2.0     21.3        1.5       1.1         2.0         https://infinitediscs.com/Kaufinator-Discs-Kaufinator-Nemesis?tag=3c8c6529
RPM-Discs                Taniwha               10.0     5.0      -2.1    1.8     21.1        1.4       1.2         2.0         https://infinitediscs.com/RPM-Discs-Taniwha?tag=3c8c6529
{22:57}~/git/discsearcher:master ✗ ➭ 
```
