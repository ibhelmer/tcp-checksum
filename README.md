# TCP Checksum

Et lille Python-program til undervisning og demonstration af **16-bit 1-komplement-summering** og den checksum-metode, der anvendes i bl.a. TCP, UDP og IPv4-headeren.

Programmet:

- modtager et vilkårligt antal 16-bit hexadecimale tal,
- lægger dem sammen,
- venter med at folde carry tilbage, til der trykkes **Enter** uden et tal,
- udfører end-around carry, indtil resultatet igen er 16 bit,
- viser både den foldede 16-bit sum og den afsluttende 1-komplement-checksum.

## Kør programmet

Kræver Python 3.

```bash
python tcp_checksum.py
```

Eksempel:

```text
Hex-tal: FFFF
Tilføjet:      FFFF
Foreløbig sum: FFFF

Hex-tal: 0001
Tilføjet:      0001
Foreløbig sum: 10000

Hex-tal:

Carry fold:
  Carry:       1
  Lower 16 bit:0000
  New sum:     1

Resultat
--------------------------------
16-bit 1-komplement sum: 0001
1-komplement checksum:   FFFE
```

## Princip

Ved almindelig 16-bit addition ville carry-bitten over bit 15 blive kasseret. Ved 1-komplement-addition anvendes **end-around carry**, hvor carry lægges tilbage til de nederste 16 bit.

Eksempel:

```text
  FFFF
+ 0001
------
 10000

carry = 0001
lower = 0000

 0000
+0001
-----
 0001
```

Selve checksummen findes derefter ved at invertere alle 16 bit:

```text
0001 -> FFFE
```

## Licens

Copyright 2026 Ib Helmer Nielsn

Projektet er udgivet under [Apache License 2.0](LICENSE).
