# discsearcher

## COLUMNS
| Disc | Manufacturer | Disc Type | Distance | HST (High Speed Turn) | LSF (Low Speed Fade) | Net |

## USAGE

```
➜~/git/discsearcher(master✗)» python3 discsearcher.py | grep Buzz                                                                                                                                                         [23:04:51]
Discraft	Buzzz	Mid-Range	296	-18%	23%	5%	Y	Buzzz	9-5
Discraft	Buzzz OS	Mid-Range	293	0%	58%	58%	Y	Buzzz OS	9-3
Discraft	Buzzz SS	Mid-Range	296	-32%	20%	-12%	Y	Buzzz SS	9-6
Discraft	Buzzz-GT	Mid-Range	290	-13%	23%	10%	Y	Buzzz-GT	9-5
➜~/git/discsearcher(master✗)»
```

```
➜~/git/discsearcher(master✗)» python3 discsearcher.py | grep Infinite                                                                                                                                                     [23:05:14]
Infinite Discs	Chariot	Mid-Range	299	0%	18%	18%	Y	Chariot	9-5
Infinite Discs	Exodus	Fairway Driver	332	-9%	37%	28%	Y	Exodus	7-4
Infinite Discs	Myth	Putt & Approach	240	0%	36%	36%	Y	Myth	11-4
Infinite Discs	Pharaoh	Distance Driver	439	-19%	39%	20%	Y	Pharaoh	2-5
Infinite Discs	Slab	Distance Driver	411	0%	78%	78%	Y	Slab	3-2
Infinite Discs	Sphinx	Fairway Driver	368	-57%	19%	-38%	Y	Sphinx	5-7
Infinite Discs	Tomb	Putt & Approach	261	0%	18%	18%	Y	Tomb	10-5
➜~/git/discsearcher(master✗)»
```

```
➜~/git/discsearcher(master)» python3 discsearcher.py | grep Mid-Range | column -s"     " -t | sort                                                                                                                        [23:07:30]
ABC                  Flying Squirrel              Mid-Range  295  -55%  18%  -37%  Y  Flying Squirrel     9-7
ABC                  The Mission                  Mid-Range  288  -18%  33%  15%   Y  The Mission         9-5
Aerobie              Sharpshooter #2              Mid-Range  263  0%    54%  54%   Y  Sharpshooter #2     10-3
AquaFlight Discs     Dragonfly                    Mid-Range  294  -46%  37%  -9%   Y  Dragonfly           9-6
Arsenal              Morningstar                  Mid-Range  294  -18%  37%  19%   Y  Morningstar         9-5
Axiom                Alias                        Mid-Range  280  -13%  13%  0%    Y  Alias               9-5
Axiom                Theory                       Mid-Range  289  -34%  16%  -18%  Y  Theory              9-6
CHING                Legacy                       Mid-Range  279  -18%  36%  18%   Y  Legacy              10-5
CHING                Oracle                       Mid-Range  279  -18%  32%  14%   Y  Oracle              10-5
CHING                Precision                    Mid-Range  292  -21%  34%  13%   Y  Precision           9-5
CHING                Sniper                       Mid-Range  295  0%    37%  37%   Y  Sniper              9-4
CHING                Stinger                      Mid-Range  271  -55%  18%  -37%  Y  Stinger             10-7
Crosslap             Lucky                        Mid-Range  297  -37%  18%  -19%  Y  Lucky               9-6
DGA                  Aftershock                   Mid-Range  283  -4%   36%  32%   Y  Aftershock          9-4
DGA                  Quake                        Mid-Range  291  0%    55%  55%   Y  Quake               9-3
DGA                  Shockwave                    Mid-Range  279  -2%   48%  46%   Y  Shockwave           10-4
DGA                  Squall                       Mid-Range  299  -18%  25%  7%    Y  Squall              9-5
DGA                  Tremor                       Mid-Range  312  -74%  18%  -56%  Y  Tremor              8-8
Daredevil            Caribou                      Mid-Range  280  -36%  27%  -9%   Y  Caribou             10-6
Daredevil            Grizzly                      Mid-Range  280  -13%  36%  23%   Y  Grizzly             9-5
Daredevil            Moose                        Mid-Range  283  0%    36%  36%   Y  Moose               9-4
Daredevil            Pteranodon                   Mid-Range  283  -36%  18%  -18%  Y  Pteranodon          9-6
Daredevil            Walrus                       Mid-Range  280  0%    55%  55%   Y  Walrus              10-3
Discmania            GM Gremlin                   Mid-Range  308  -7%   35%  28%   Y  GM Gremlin          8-4
Discmania            MD                           Mid-Range  282  -4%   9%   5%    Y  MD                  9-5
Discmania            MD1                          Mid-Range  284  0%    39%  39%   Y  MD1                 9-4
Discmania            MD2 Fiend                    Mid-Range  286  -6%   32%  26%   Y  MD2 Fiend           9-4
Discmania            MD3                          Mid-Range  299  0%    55%  55%   Y  MD3                 9-3
Discmania            MD4                          Mid-Range  294  0%    55%  55%   Y  MD4                 9-3
Discraft             Archer                       Mid-Range  312  -56%  18%  -38%  Y  Archer              8-7
Discraft             Breeze                       Mid-Range  269  -32%  18%  -14%  Y  Breeze              10-6
Discraft             Buzzz                        Mid-Range  296  -18%  23%  5%    Y  Buzzz               9-5
Discraft             Buzzz OS                     Mid-Range  293  0%    58%  58%   Y  Buzzz OS            9-3
Discraft             Buzzz SS                     Mid-Range  296  -32%  20%  -12%  Y  Buzzz SS            9-6
Discraft             Buzzz-GT                     Mid-Range  290  -13%  23%  10%   Y  Buzzz-GT            9-5
Discraft             Comet                        Mid-Range  283  -34%  20%  -14%  Y  Comet               9-6
Discraft             Drone                        Mid-Range  289  9%    74%  83%   Y  Drone               9-2
Discraft             Hawk                         Mid-Range  280  -34%  36%  2%    Y  Hawk                10-5
Discraft             Hornet                       Mid-Range  295  0%    68%  68%   Y  Hornet              9-3
Discraft             Impact                       Mid-Range  317  -37%  35%  -2%   Y  Impact              8-6
Discraft             MRV                          Mid-Range  276  -18%  46%  28%   Y  MRV                 10-4
Discraft             MRX                          Mid-Range  285  -10%  46%  36%   Y  MRX                 9-4
Discraft             Meteor                       Mid-Range  288  -50%  23%  -27%  Y  Meteor              9-7
Discraft             Nebula                       Mid-Range  280  -9%   36%  27%   Y  Nebula              9-4
Discraft             Stratus                      Mid-Range  300  -60%  18%  -42%  Y  Stratus             8-7
Discraft             Wasp                         Mid-Range  296  0%    51%  51%   Y  Wasp                9-3
Discwing             Transcend                    Mid-Range  281  -39%  18%  -21%  Y  Transcend           9-6
Dynamic Discs        EMAC Truth                   Mid-Range  300  0%    37%  37%   Y  EMAC Truth          8-4
Dynamic Discs        Evidence                     Mid-Range  294  -21%  15%  -6%   Y  Evidence            9-6
Dynamic Discs        Fugitive                     Mid-Range  299  -16%  32%  16%   Y  Fugitive            9-5
Dynamic Discs        Justice                      Mid-Range  274  9%    64%  73%   Y  Justice             10-3
Dynamic Discs        Proof                        Mid-Range  301  -55%  18%  -37%  Y  Proof               8-7
Dynamic Discs        Suspect                      Mid-Range  272  0%    52%  52%   Y  Suspect             10-3
Dynamic Discs        Truth                        Mid-Range  305  -2%   37%  35%   Y  Truth               8-4
Dynamic Discs        Verdict                      Mid-Range  289  0%    60%  60%   Y  Verdict             9-3
Dynamic Discs        Warrant                      Mid-Range  298  -37%  0%   -37%  Y  Warrant             9-7
EMSCO Group          ESP Midrange                 Mid-Range  294  -39%  27%  -12%  Y  ESP Midrange        9-6
Element Discs        Lithium                      Mid-Range  294  -37%  18%  -19%  Y  Lithium             9-6
Element Discs        Radium                       Mid-Range  310  -18%  56%  38%   Y  Radium              8-4
Element Discs        Uranium                      Mid-Range  272  0%    36%  36%   Y  Uranium             10-4
Essential Discs      Honey                        Mid-Range  277  0%    42%  42%   Y  Honey               10-4
Eurodisc             Transition                   Mid-Range  299  0%    18%  18%   Y  Transition          9-5
Fly High Discs       KGB                          Mid-Range  298  -18%  18%  0%    Y  KGB                 9-5
Fly High Discs       Pure O.G.                    Mid-Range  311  -18%  37%  19%   Y  Pure O.G.           8-5
Full Turn Discs      Navigator                    Mid-Range  294  -18%  37%  19%   Y  Navigator           9-5
Full Turn Discs      Passport                     Mid-Range  278  -18%  18%  0%    Y  Passport            10-5
GGGT                 Optimizer                    Mid-Range  277  -55%  0%   -55%  Y  Optimizer           10-8
Galaxy               Orbit                        Mid-Range  294  0%    55%  55%   Y  Orbit               9-3
Gateway              Demon                        Mid-Range  301  9%    69%  78%   Y  Demon               8-2
Gateway              Devil Hawk                   Mid-Range  268  3%    36%  39%   Y  Devil Hawk          10-4
Gateway              Element                      Mid-Range  302  -27%  23%  -4%   Y  Element             8-6
Gateway              Element-X                    Mid-Range  288  -23%  50%  27%   Y  Element-X           9-4
Gateway              Karma                        Mid-Range  310  -12%  43%  31%   Y  Karma               8-4
Gateway              Mystic                       Mid-Range  300  -34%  27%  -7%   Y  Mystic              8-6
Gateway              Prophecy                     Mid-Range  298  0%    37%  37%   Y  Prophecy            9-4
Gateway              Scout                        Mid-Range  330  -9%   28%  19%   Y  Scout               7-5
Gateway              War Spear                    Mid-Range  269  -24%  12%  -12%  Y  War Spear           10-6
Gateway              Warrior                      Mid-Range  304  -9%   51%  42%   Y  Warrior             8-4
Guru                 Thor                         Mid-Range  278  0%    36%  36%   Y  Thor                10-4
Hyzer Bomb           Mortar                       Mid-Range  283  3%    55%  58%   Y  Mortar              9-3
Infinite Discs       Chariot                      Mid-Range  299  0%    18%  18%   Y  Chariot             9-5
Innova               Atlas                        Mid-Range  299  -2%   20%  18%   Y  Atlas               9-5
Innova               Barracuda                    Mid-Range  292  -37%  55%  18%   Y  Barracuda           9-5
Innova               Bulldog                      Mid-Range  262  0%    45%  45%   Y  Bulldog             10-4
Innova               Caiman                       Mid-Range  298  0%    74%  74%   Y  Caiman              9-3
Innova               Classic Cobra                Mid-Range  296  -37%  37%  0%    Y  Classic Cobra       9-5
Innova               Cobra                        Mid-Range  290  -37%  41%  4%    Y  Cobra               9-5
Innova               Commander                    Mid-Range  294  0%    55%  55%   Y  Commander           9-3
Innova               Condor                       Mid-Range  286  -9%   46%  37%   Y  Condor              9-4
Innova               Coyote                       Mid-Range  286  -11%  18%  7%    Y  Coyote              9-5
Innova               Cro                          Mid-Range  295  0%    41%  41%   Y  Cro                 9-4
Innova               Foxbat                       Mid-Range  291  -27%  6%   -21%  Y  Foxbat              9-6
Innova               Gator                        Mid-Range  287  0%    55%  55%   Y  Gator               9-3
Innova               Gator3                       Mid-Range  288  0%    55%  55%   Y  Gator3              9-3
Innova               Goblin                       Mid-Range  273  -4%   22%  18%   Y  Goblin              10-5
Innova               Griffin                      Mid-Range  290  18%   55%  73%   Y  Griffin             9-3
Innova               Hydra                        Mid-Range  260  0%    36%  36%   Y  Hydra               10-4
Innova               Jaguar                       Mid-Range  287  -52%  37%  -15%  Y  Jaguar              9-6
Innova               King Cobra                   Mid-Range  284  -6%   40%  34%   Y  King Cobra          9-4
Innova               Kite                         Mid-Range  304  -53%  21%  -32%  Y  Kite                8-7
Innova               Lycan                        Mid-Range  287  -2%   20%  18%   Y  Lycan               9-5
Innova               Lynx                         Mid-Range  266  0%    36%  36%   Y  Lynx                10-4
Innova               Mako                         Mid-Range  288  0%    6%   6%    Y  Mako                9-5
Innova               Mako3                        Mid-Range  293  0%    4%   4%    Y  Mako3               9-5
Innova               Manta                        Mid-Range  297  -37%  18%  -19%  Y  Manta               9-6
Innova               Moray                        Mid-Range  278  0%    36%  36%   Y  Moray               10-4
Innova               Panther                      Mid-Range  302  -34%  20%  -14%  Y  Panther             8-6
Innova               Phantom Deuce                Mid-Range  254  -36%  18%  -18%  Y  Phantom Deuce       11-6
Innova               Puma                         Mid-Range  275  -18%  18%  0%    Y  Puma                10-5
Innova               Python                       Mid-Range  311  -18%  37%  19%   Y  Python              8-5
Innova               Roc                          Mid-Range  286  0%    53%  53%   Y  Roc                 9-3
Innova               Roc X3                       Mid-Range  291  0%    64%  64%   Y  Roc X3              9-3
Innova               Roc3                         Mid-Range  293  -3%   55%  52%   Y  Roc3                9-3
Innova               Scorpion                     Mid-Range  297  -18%  37%  19%   Y  Scorpion            9-5
Innova               Shark                        Mid-Range  283  -4%   36%  32%   Y  Shark               9-4
Innova               Shark3                       Mid-Range  294  0%    40%  40%   Y  Shark3              9-4
Innova               Skeeter                      Mid-Range  305  -21%  23%  2%    Y  Skeeter             8-5
Innova               Spider                       Mid-Range  295  -9%   23%  14%   Y  Spider              9-5
Innova               Stingray                     Mid-Range  303  -53%  23%  -30%  Y  Stingray            8-7
Innova               VRoc                         Mid-Range  281  -4%   36%  32%   Y  VRoc                9-4
Innova               Wolf                         Mid-Range  279  -64%  23%  -41%  Y  Wolf                10-7
Innova               Wombat                       Mid-Range  282  -27%  4%   -23%  Y  Wombat              9-6
Innova               Wombat3                      Mid-Range  302  -18%  0%   -18%  Y  Wombat3             8-6
Innova               Zephyr                       Mid-Range  264  -9%   4%   -5%   Y  Zephyr              10-6
Kastaplast           Kaxe                         Mid-Range  305  0%    44%  44%   Y  Kaxe                8-4
Kastaplast           Kaxe Z                       Mid-Range  305  -9%   32%  23%   Y  Kaxe Z              8-5
Latitude 64          Anchor                       Mid-Range  294  0%    55%  55%   Y  Anchor              9-3
Latitude 64          Claymore                     Mid-Range  286  -15%  24%  9%    Y  Claymore            9-5
Latitude 64          Compass                      Mid-Range  301  0%    18%  18%   Y  Compass             8-5
Latitude 64          Core                         Mid-Range  300  -16%  23%  7%    Y  Core                9-5
Latitude 64          Fuji                         Mid-Range  278  0%    36%  36%   Y  Fuji                10-4
Latitude 64          Fuse                         Mid-Range  300  -34%  20%  -14%  Y  Fuse                8-6
Latitude 64          Gobi                         Mid-Range  298  -27%  18%  -9%   Y  Gobi                9-6
Latitude 64          Mace                         Mid-Range  299  -4%   44%  40%   Y  Mace                9-4
Latitude 64          Medius                       Mid-Range  326  -14%  49%  35%   Y  Medius              7-4
Latitude 64          Pain                         Mid-Range  284  0%    36%  36%   Y  Pain                9-4
Latitude 64          Pearl                        Mid-Range  290  -55%  23%  -32%  Y  Pearl               9-7
Legacy               Gauge                        Mid-Range  296  -9%   18%  9%    Y  Gauge               9-5
Legacy               Ghost                        Mid-Range  286  -4%   50%  46%   Y  Ghost               9-4
Legacy               Pursuit                      Mid-Range  291  0%    55%  55%   Y  Pursuit             9-3
Lightning            #2 Hookshot                  Mid-Range  293  -13%  55%  42%   Y  #2 Hookshot         9-4
Lightning            #2 Hyzer                     Mid-Range  288  18%   74%  92%   Y  #2 Hyzer            9-2
Lightning            #2 Upshot                    Mid-Range  247  -18%  18%  0%    Y  #2 Upshot           11-5
Lightning            #3 Hookshot                  Mid-Range  281  -9%   36%  27%   Y  #3 Hookshot         9-4
MVP                  Axis                         Mid-Range  296  -18%  24%  6%    Y  Axis                9-5
MVP                  Deflector                    Mid-Range  292  0%    74%  74%   Y  Deflector           9-3
MVP                  Matrix                       Mid-Range  292  0%    37%  37%   Y  Matrix              9-4
MVP                  Tangent                      Mid-Range  294  -27%  22%  -5%   Y  Tangent             9-6
MVP                  Tensor                       Mid-Range  292  2%    55%  57%   Y  Tensor              9-3
MVP                  Vector                       Mid-Range  293  0%    52%  52%   Y  Vector              9-3
Millennium           Aurora MF                    Mid-Range  281  0%    36%  36%   Y  Aurora MF           9-4
Millennium           Aurora MS                    Mid-Range  285  -13%  13%  0%    Y  Aurora MS           9-5
Millennium           Sentinel MF                  Mid-Range  291  0%    69%  69%   Y  Sentinel MF         9-3
Millennium           Taurus                       Mid-Range  276  0%    73%  73%   Y  Taurus              10-3
Ozone Discs          Andro 1                      Mid-Range  310  -18%  37%  19%   Y  Andro 1             8-5
Ozone Discs          Andro C                      Mid-Range  311  -18%  37%  19%   Y  Andro C             8-5
Ozone Discs          Andro C (Retooled)           Mid-Range  311  -37%  18%  -19%  Y  Andro C (Retooled)  8-6
Pacific Cycle        Saturn                       Mid-Range  288  -47%  13%  -34%  Y  Saturn              9-7
Paradigm             Terrapin                     Mid-Range  276  0%    64%  64%   Y  Terrapin            10-3
Prodigy Disc         A1                           Mid-Range  273  0%    73%  73%   Y  A1                  10-3
Prodigy Disc         A2                           Mid-Range  277  0%    55%  55%   Y  A2                  10-3
Prodigy Disc         A3                           Mid-Range  274  -18%  36%  18%   Y  A3                  10-5
Prodigy Disc         A4                           Mid-Range  273  -36%  36%  0%    Y  A4                  10-5
Prodigy Disc         M1                           Mid-Range  286  0%    53%  53%   Y  M1                  9-3
Prodigy Disc         M2                           Mid-Range  293  -6%   43%  37%   Y  M2                  9-4
Prodigy Disc         M3                           Mid-Range  295  -21%  27%  6%    Y  M3                  9-5
Prodigy Disc         M4                           Mid-Range  295  -31%  24%  -7%   Y  M4                  9-6
Prodigy Disc         M5                           Mid-Range  290  -37%  27%  -10%  Y  M5                  9-6
Prodiscus            MIDARi                       Mid-Range  296  -11%  39%  28%   Y  MIDARi              9-4
Prodiscus            STARi                        Mid-Range  295  -37%  0%   -37%  Y  STARi               9-7
Quest AT             Backbone                     Mid-Range  307  -18%  35%  17%   Y  Backbone            8-5
Quest AT             Odyssey Midrange & Approach  Mid-Range  307  -51%  23%  -28%  Y  Odys. M&A           8-7
Quest AT             Rock-It                      Mid-Range  298  -41%  16%  -25%  Y  Rock-It             9-6
Quest AT             Wildfire                     Mid-Range  306  -49%  33%  -16%  Y  Wildfire            8-6
RPM Discs            Kea                          Mid-Range  297  0%    55%  55%   Y  Kea                 9-3
RPM Discs            Piwakawaka                   Mid-Range  285  -32%  27%  -5%   Y  Piwakawaka          9-6
RPM Discs            Te Moko                      Mid-Range  256  0%    22%  22%   Y  Te Moko             11-5
Reptilian Disc Golf  Gila                         Mid-Range  294  0%    55%  55%   Y  Gila                9-3
Salient Discs        Antidote                     Mid-Range  290  -41%  18%  -23%  Y  Antidote            9-6
Vibram               Crag                         Mid-Range  276  0%    73%  73%   Y  Crag                10-3
Vibram               Ibex                         Mid-Range  298  -11%  23%  12%   Y  Ibex                9-5
Vibram               Launch                       Mid-Range  297  -18%  37%  19%   Y  Launch              9-5
Vibram               Obex                         Mid-Range  294  0%    44%  44%   Y  Obex                9-4
Viking               Axe                          Mid-Range  276  0%    18%  18%   Y  Axe                 10-5
Viking               Nordic Warrior               Mid-Range  278  0%    36%  36%   Y  Nordic Warrior      10-4
Westside             Anvil                        Mid-Range  270  0%    73%  73%   Y  Anvil               10-3
Westside             Bard                         Mid-Range  277  13%   46%  59%   Y  Bard                10-3
Westside             Pine                         Mid-Range  295  0%    37%  37%   Y  Pine                9-4
Westside             Sling                        Mid-Range  299  0%    18%  18%   Y  Sling               9-5
Westside             Tursas                       Mid-Range  297  -53%  18%  -35%  Y  Tursas              9-7
Westside             Warship                      Mid-Range  314  -9%   25%  16%   Y  Warship             8-5
Wham-O               Mid Range Approach           Mid-Range  268  -4%   27%  23%   Y  Mid Range Approach  10-5
Wham-O               Touchline True               Mid-Range  280  -18%  36%  18%   Y  Touchline True      10-5
YiKun                Crossbow                     Mid-Range  268  9%    73%  82%   Y  Crossbow            10-2
YiKun                Kui                          Mid-Range  298  0%    46%  46%   Y  Kui                 9-4
YiKun                Wings                        Mid-Range  260  0%    36%  36%   Y  Wings               11-4
YiKun                Yao                          Mid-Range  282  0%    46%  46%   Y  Yao                 9-4
➜~/git/discsearcher(master)»
```
