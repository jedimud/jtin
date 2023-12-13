Small unicode maps loaded into the right panel using `#split`. 

![](https://github.com/jedimud/jtin/blob/main/docs/map.png)

<br/> 

# Usage

`jt map <state>`

**`state`**
* `enabled`: Allow maps to be loaded
* `disabled`: Close and unload mapping features

<br/> 

# Getting started

```sh
jt map enabled;
map split {0 1 0 -90};
map offset {1 91 -1 -1}; 
map open midgaard 1;
```

<br/> 

# Aliases

Map features can be called with `room` or `map` aliases.

| Alias                          | Description |
| :----------------------------- | :---------- |
| `map show`                     | Show current map on right side of terminal |
| `map hide`                     | Remove map from terminal |
| `map open <map> <room>`        | Open `<map>` and center on `<room>` |
| `map edit`                     | Update map using player's movements |
| `map read`                     | Read-only mode for map |
| `map save`                     | Save changes to map |
| `map create <name>`            | Create a new map with `<name>` |
| `map split { <value> }`        | Configure a new terminal split, default is `0 1 0 -90` |
| `map offset { <value> }`       | Configure a new map offset, default is `1 91 -1 -1` |
| `map locate`                   | Enable MSDP and find current map location |
| `room door <dir>`              | Create door at `<dir>` |
| `room lock <dir>`              | Create locked door at `<dir>` |
| `room fog <dir>`               | Change room at `<dir>` to undiscovered |
| `room dt <dir>`                | Change room at `<dir>` to death trap |
| `room void <dir>`              | Create void room at `<dir>`, effectively inserting a gap between rooms |
| `room unvoid <dir>`            | Remove void room at `<dir>` |
| `room link <dir> <map> <room>` | Link current room to another `<room>` on a different `<map>` at `<dir>` |
| `room shop`                    | Change current room to shop symbol |
| `room inn`                     | Change current room to innkeeper symbol |
| `room master`                  | Change current room to guild master symbol |
| `room fountain`                | Change current room to fountain symbol |
| `room bank`                    | Change current room to bank symbol |
| `room path`                    | Change current room to path symbol |
| `room donation`                | Change current room to donation symbol |

<br/> 

# Legend

| Symbol              | Description   |
| :------------------ | :------------ |
| `[ ]`               | Basic Path    |
| `DT`                | Death Trap    |
| `[$]`               | Bank          |
| `[M]`               | Guild Master  |
| `[*]`               | Path Point    |
| `[&]`               | Innkeeper     |
| `[D]`               | Donation      |
| `[#]`               | Shop/Vendor   |
| `[%]`               | Fountain      |
| `[ ]+`              | Exit up       |
| `[ ]-`              | Exit down     |

<br/>

# Terrain

| Symbol | Terrain |
| :----- | :------ |
| `=` | CITY |
| `·` | FIELD |
| `⍋` | FOREST |
| `︵` | HILLS |
| `≡` | INSIDE |
| `⊰` | MIDAIR |
| `◮` | MOUNTAINS |
| `~` | NOSWIM |
| `~` | SWIM |

<br/> 

# Status

