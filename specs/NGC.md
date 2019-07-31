# NGC

total capacity of disc data is 1,459,978,240 bytes (1.5 GB approx.).
that's exactly 712880 DVD raw sectors (each 2048 bytes).


## DVD Structure

```
start       end         size        Description
0x00000000  ----------  0x0440      Disk header ("boot.bin")
0x00000440  ----------  0x2000      Disk header Information ("bi2.bin")
0x00002440  ----------  (0x2000 ?)  Apploader ("appldr.bin")
                                    FST ('fst.bin')
```


## Disk header

```
start   end     size    Description
0x0000  0x0003  0x0004  Game Code
                            |-  1 -  Console ID
                            |-  2 -  Gamecode
                            |-  1 -  Country Code
0x0004  0x0005  0x0002  Maker Code
0x0006  ------  0x0001  Disk ID
0x0007  ------  0x0001  Version
0x0008  ------  0x0001  Audio Streaming
0x0009  ------  0x0001  Stream Buffer Size
0x000a  0x001b  0x0012  unused (zeros)
0x001c  0x001f  0x0004  DVD Magic Word (0xc2339f3d)
0x0020  0x03ff  0x03e0  Game Name
0x0400  0x0403  0x0004  offset of debug monitor (dh.bin) ?
0x0404  0x0407  0x0004  addr (?) to load debug monitor ?
0x0408  0x041f  0x0018  unused (zeros)
0x0420  0x0423  0x0004  offset of main executable DOL (bootfile)
0x0424  0x0427  0x0004  offset of the FST ("fst.bin")
0x0428  0x042B  0x0004  size of FST
0x042C  0x042F  0x0004  maximum size of FST (usually its same as FST size) (*)
0x0430  0x0433  0x0004  user position (?)
0x0434  0x0437  0x0004  user length (?)
0x0438  0x043b  0x0004  (?)
0x043c  0x043f  0x0004  unused (zeros)
```

(\*) multiple DVDs must use it, to properly reside all FSTs.


[source](https://www.gc-forever.com/yagcd/chap13.html#sec13)
