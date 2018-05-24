# The DMG/CGB Cartridge Header

An internal information area is located at 0100-014F in
each cartridge. It contains the following values:


## Header Overview

```
  0100-0103 - Entry Point
  0104-0133 - Nintendo Logo
  0134-0143 - Title
  013F-0142 - Manufacturer Code
  0143      - CGB Flag
  0144-0145 - New Licensee Code
  0146      - SGB Flag
  0147      - Cartridge Type
  0148      - ROM Size
  0149      - RAM Size
  014A      - Destination Code
  014B      - Old Licensee Code
  014C      - Mask ROM Version number
  014D      - Header Checksum
  014E-014F - Global Checksum
```


## 0134-0143 - Title

Title of the game in UPPER CASE ASCII. If it is less than 16 characters then
the remaining bytes are filled with 00's. When inventing the CGB, Nintendo
has reduced the length of this area to 15 characters, and some months later
they had the fantastic idea to reduce it to 11 characters only.


## 013F-0142 - Manufacturer Code

In older cartridges this area has been part of the Title (see above), in newer
cartridges this area contains an 4 character uppercase manufacturer code.
Purpose and Deeper Meaning unknown.

## 0143 - CGB Flag

In older cartridges this byte has been part of the Title (see above). In CGB
cartridges the upper bit is used to enable CGB functions. This is required,
otherwise the CGB switches itself into Non-CGB-Mode. Typical values are:

```
  80h - Game supports CGB functions, but works on old gameboys also.
  C0h - Game works on CGB only (physically the same as 80h).
```

Values with Bit 7 set, and either Bit 2 or 3 set, will switch the gameboy into
a special non-CGB-mode with uninitialized palettes. Purpose unknown, eventually
this has been supposed to be used to colorize monochrome games that include
fixed palette data at a special location in ROM.

[source](http://problemkaputt.de/pandocs.htm#thecartridgeheader)
