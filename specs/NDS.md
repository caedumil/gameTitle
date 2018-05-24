# DS Cartridge Header


## Header Overview

(loaded from ROM Addr 0 to Main RAM 27FFE00h on Power-up)

Address Bytes Expl.
```
  000h    12    Game Title  (Uppercase ASCII, padded with 00h)
  00Ch    4     Gamecode    (Uppercase ASCII, NTR-<code>)        (0=homebrew)
  010h    2     Makercode   (Uppercase ASCII, eg. "01"=Nintendo) (0=homebrew)
  012h    1     Unitcode    (00h=NDS, 02h=NDS+DSi, 03h=DSi) (bit1=DSi)
  013h    1     Encryption Seed Select (00..07h, usually 00h)
  014h    1     Devicecapacity         (Chipsize = 128KB SHL nn) (eg. 7 = 16MB)
  015h    7     Reserved    (zero filled)
  01Ch    1     Reserved    (zero)                      (except, used on DSi)
  01Dh    1     NDS Region  (00h=Normal, 80h=China, 40h=Korea) (other on DSi)
  01Eh    1     ROM Version (usually 00h)
  01Fh    1     Autostart (Bit2: Skip "Press Button" after Health and Safety)
                (Also skips bootmenu, even in Manual mode & even Start pressed)
  020h    4     ARM9 rom_offset    (4000h and up, align 1000h)
  024h    4     ARM9 entry_address (2000000h..23BFE00h)
  028h    4     ARM9 ram_address   (2000000h..23BFE00h)
  02Ch    4     ARM9 size          (max 3BFE00h) (3839.5KB)
  030h    4     ARM7 rom_offset    (8000h and up)
  034h    4     ARM7 entry_address (2000000h..23BFE00h, or 37F8000h..3807E00h)
  038h    4     ARM7 ram_address   (2000000h..23BFE00h, or 37F8000h..3807E00h)
  03Ch    4     ARM7 size          (max 3BFE00h, or FE00h) (3839.5KB, 63.5KB)
  040h    4     File Name Table (FNT) offset
  044h    4     File Name Table (FNT) size
  048h    4     File Allocation Table (FAT) offset
  04Ch    4     File Allocation Table (FAT) size
  050h    4     File ARM9 overlay_offset
  054h    4     File ARM9 overlay_size
  058h    4     File ARM7 overlay_offset
  05Ch    4     File ARM7 overlay_size
  060h    4     Port 40001A4h setting for normal commands (usually 00586000h)
  064h    4     Port 40001A4h setting for KEY1 commands   (usually 001808F8h)
  068h    4     Icon/Title offset (0=None) (8000h and up)
  06Ch    2     Secure Area Checksum, CRC-16 of [[020h]..00007FFFh]
  06Eh    2     Secure Area Delay (in 131kHz units) (051Eh=10ms or 0D7Eh=26ms)
  070h    4     ARM9 Auto Load List RAM Address (?)
  074h    4     ARM7 Auto Load List RAM Address (?)
  078h    8     Secure Area Disable (by encrypted "NmMdOnly") (usually zero)
  080h    4     Total Used ROM size (remaining/unused bytes usually FFh-padded)
  084h    4     ROM Header Size (4000h)
  088h    38h   Reserved (zero filled) (except, [88h..93h] used on DSi)
  0C0h    9Ch   Nintendo Logo (compressed bitmap, same as in GBA Headers)
  15Ch    2     Nintendo Logo Checksum, CRC-16 of [0C0h-15Bh], fixed CF56h
  15Eh    2     Header Checksum, CRC-16 of [000h-15Dh]
  160h    4     Debug rom_offset   (0=none) (8000h and up)       ;only if debug
  164h    4     Debug size         (0=none) (max 3BFE00h)        ;version with
  168h    4     Debug ram_address  (0=none) (2400000h..27BFE00h) ;SIO and 8MB
  16Ch    4     Reserved (zero filled) (transferred, and stored, but not used)
  170h    90h   Reserved (zero filled) (transferred, but not stored in RAM)
```

DSi Cartridges are using an extended cartridge header.


## NDS Gamecodes

This is the same code as the NTR-UTTD (NDS) or TWL-UTTD (DSi) code which is
printed on the package and sticker on (commercial) cartridges (excluding the
leading "NTR-" or "TWL-" part).

```
  U  Unique Code          (usually "A", "B", "C", or special meaning)
  TT Short Title          (eg. "PM" for Pac Man)
  D  Destination/Language (usually "J" or "E" or "P" or specific language)
```

The first character (U) is usually "A" or "B", in detail:

```
  A NDS common games
  B NDS common games
  C NDS common games
  D DSi-exclusive games
  H DSiWare (system utilities and browser) (eg. HNGP=browser)
  I NDS and DSi-enhanced games with built-in Infrared port
  K DSiWare (dsiware games and flipnote) (eg. KGUV=flipnote)
  N NDS nintendo channel demo's japan (NTR-NTRJ-JPN)
  T NDS many games
  U NDS utilities, educational games, or uncommon extra hardware?
  V DSi-enhanced games
  Y NDS many games
```

The second/third characters (TT) are:

```
  Usually an abbreviation of the game title (eg. "PM" for "Pac Man") (unless
  that gamecode was already used for another game, then TT is just random)
```

The fourth character (D) indicates Destination/Language:

```
  A Asian    E English/USA  I Italian   M Swedish  Q Danish   U Australian
  B N/A      F French       J Japanese  N Nor      R Russian  V EUR+AUS
  C Chinese  G N/A          K Korean    O Int      S Spanish  W..Z Europe #3..5
  D German   H Dutch        L USA #2    P Europe   T USA+AUS
```


## DS Cartridge Icon/Title

The ROM offset of the Icon/Title is defined in CartHdr[68h]. The size was
originally implied by the size of the original Icon/Title structure rounded to
200h-byte sector boundary (ie. A00h bytes for Version 1 or 2), however, later
DSi carts are having a size entry at CartHdr[208h] (usually 23C0h).

If it is present (ie. if CartHdr[68h]=nonzero), then Icon/Title are displayed
in the bootmenu.

```
  0000h 2     Version (0001h, 0002h, 0003h, or 0103h)
  0002h 2     CRC16 across entries 0020h..083Fh (all versions)
  0004h 2     CRC16 across entries 0020h..093Fh (Version 0002h and up)
  0006h 2     CRC16 across entries 0020h..0A3Fh (Version 0003h and up)
  0008h 2     CRC16 across entries 1240h..23BFh (Version 0103h and up)
  000Ah 16h   Reserved (zero-filled)
  0020h 200h  Icon Bitmap  (32x32 pix) (4x4 tiles, 4bit depth) (4x8 bytes/tile)
  0220h 20h   Icon Palette (16 colors, 16bit, range 0000h-7FFFh)
              (Color 0 is transparent, so the 1st palette entry is ignored)
  0240h 100h  Title 0 Japanese  (128 characters, 16bit Unicode)
  0340h 100h  Title 1 English   ("")
  0440h 100h  Title 2 French    ("")
  0540h 100h  Title 3 German    ("")
  0640h 100h  Title 4 Italian   ("")
  0740h 100h  Title 5 Spanish   ("")
  0840h 100h  Title 6 Chinese   ("")                 (Version 0002h and up)
  0940h 100h  Title 7 Korean    ("")                 (Version 0003h and up)
  0A40h 800h  Zerofilled (probably reserved for Title 8..15)
```

Below for animated DSi icons only (Version 0103h and up):

```
  1240h 1000h Icon Animation Bitmap 0..7 (200h bytes each, format as above)
  2240h 100h  Icon Animation Palette 0..7 (20h bytes each, format as above)
  2340h 80h   Icon Animation Sequence (16bit tokens)
```

Unused/padding bytes:

```
  0840h 1C0h  Unused/padding (FFh-filled) in Version 0001h
  0940h C0h   Unused/padding (FFh-filled) in Version 0002h
  23C0h 40h   Unused/padding (FFh-filled) in Version 0103h
```

Versions

```
  0001h = Original
  0002h = With Chinese Title
  0003h = With Chinese+Korean Titles
  0103h = With Chinese+Korean Titles and animated DSi icon
```

### Title Strings

Usually, for non-multilanguage games, the same (english) title is stored in all
title entries. The title may consist of ASCII characters 0020h-007Fh, character
000Ah (linefeed), and should be terminated/padded by 0000h.

The whole text should not exceed the dimensions of the DS cart field in the
bootmenu (the maximum number of characters differs due to non-proportional
font).

The title is usually split into a primary title, optional sub-title, and
manufacturer, each separated by 000Ah character(s). For example: "America",
000Ah, "The Axis of War", 000Ah, "Cynicware", 0000h.

[source](http://problemkaputt.de/gbatek.htm#dscartridgeheader)
