# tintin-maps

Unicode maps for Jedimud generated with TinTin++.

![](midgaard.png)

## Legend

| Symbol              | Description   |
| ------------------- | ------------- |
| `[ ]`               |  Basic Path   |
| `[$]`               |  Bank         |
| `[M]`               |  Guild Master |
| `[*]`               |  Recall/Login |
| `[&]`               |  Innkeeper    |
| `[D]`               |  Donation     |
| `[#]`               |  Shop/Vendor  |
| `[%]`               |  Fountain     |
| `[ ]+`              |  Exit up      |
| `[ ]-`              |  Exit down    |
| `↖ ↑ ↗ ← · → ↙ ↓ ↘` | One-way path  |


## Usage

Start TinTin++ from terminal

`$ tt++`

Then create a session using the `jedimud.tin` file

`#session j jedimud.com 4000 jedimud.tin`

## Aliases

| Alias           | Description                                         |
| --------------- | --------------------------------------------------- |
| `rc`            | Cast group recall and center on Temple of Midgaard  |
| `open_midgaard` | Open midgaard.map at Temple of Midgaard             |
| `map_show`      | Show current map on right side of terminal          |
| `map_hide`      | Remove map from terminal                            |
| `map_create`    | Initialize a new map, useful for mapping a new zone |
| `map_edit`      | Automatically track movements and update map        |
| `map_read`      | Read-only mode for map                              |
| `map_save`      | Save current map to disc                            |
| `room_exit`     | Change room to one-way path                         |
| `room_shop`     | Change room to shop symbol                          |
| `room_inn`      | Change room to innkeeper symbol                     |
| `room_master`   | Change room to guild master symbol                  |
| `room_fountain` | Change room to fountain symbol                      |
| `room_bank`     | Change room to bank symbol                          |
| `room_recall`   | Change room to recall symbol                        |
| `room_donation` | Change room to donation symbol                      |

## Zones

| Zone     | Issues   | 
| Midgaard | #1 #2 #3 |