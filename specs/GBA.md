# GBA Cartridge Header

The first 192 bytes at 8000000h-80000BFh in ROM are used as cartridge header.
The same header is also used for Multiboot images at 2000000h-20000BFh (plus
some additional multiboot entries at 20000C0h and up).


## Header Overview

Address Bytes Expl.
```
  000h    4     ROM Entry Point  (32bit ARM branch opcode, eg. "B rom_start")
  004h    156   Nintendo Logo    (compressed bitmap, required!)
  0A0h    12    Game Title       (uppercase ascii, max 12 characters)
  0ACh    4     Game Code        (uppercase ascii, 4 characters)
  0B0h    2     Maker Code       (uppercase ascii, 2 characters)
  0B2h    1     Fixed value      (must be 96h, required!)
  0B3h    1     Main unit code   (00h for current GBA models)
  0B4h    1     Device type      (usually 00h) (bit7=DACS/debug related)
  0B5h    7     Reserved Area    (should be zero filled)
  0BCh    1     Software version (usually 00h)
  0BDh    1     Complement check (header checksum, required!)
  0BEh    2     Reserved Area    (should be zero filled)
  --- Additional Multiboot Header Entries ---
  0C0h    4     RAM Entry Point  (32bit ARM branch opcode, eg. "B ram_start")
  0C4h    1     Boot mode        (init as 00h - BIOS overwrites this value!)
  0C5h    1     Slave ID Number  (init as 00h - BIOS overwrites this value!)
  0C6h    26    Not used         (seems to be unused)
  0E0h    4     JOYBUS Entry Pt. (32bit ARM branch opcode, eg. "B joy_start")
```

Note: With all entry points, the CPU is initially set into system mode.


## 0A0h - Game Title, Uppercase Ascii, max 12 characters

Space for the game title, padded with 00h (if less than 12 chars).


## 0ACh - Game Code, Uppercase Ascii, 4 characters

This is the same code as the AGB-UTTD code which is printed on the package and
sticker on (commercial) cartridges (excluding the leading "AGB-" part).

```
  U  Unique Code          (usually "A" or "B" or special meaning)
  TT Short Title          (eg. "PM" for Pac Man)
  D  Destination/Language (usually "J" or "E" or "P" or specific language)
```

The first character (U) is usually "A" or "B", in detail:

```
  A  Normal game; Older titles (mainly 2001..2003)
  B  Normal game; Newer titles (2003..)
  C  Normal game; Not used yet, but might be used for even newer titles
  F  Famicom/Classic NES Series (software emulated NES games)
  K  Yoshi and Koro Koro Puzzle (acceleration sensor)
  P  e-Reader (dot-code scanner)
  R  Warioware Twisted (cartridge with rumble and z-axis gyro sensor)
  U  Boktai 1 and 2 (cartridge with RTC and solar sensor)
  V  Drill Dozer (cartridge with rumble)
```

The second/third characters (TT) are:

```
  Usually an abbreviation of the game title (eg. "PM" for "Pac Man") (unless
  that gamecode was already used for another game, then TT is just random)
```

The fourth character (D) indicates Destination/Language:

```
  J  Japan             P  Europe/Elsewhere   F  French          S  Spanish
  E  USA/English       D  German             I  Italian
```
[source](http://problemkaputt.de/gbatek.htm#gbacartridgeheader)
