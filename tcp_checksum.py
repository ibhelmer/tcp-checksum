#!/usr/bin/env python3
# Copyright 2026 Ib Helmer Nielsn
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demonstration of 16-bit one's-complement addition.

The program accepts 16-bit hexadecimal words. When Enter is pressed
without a value, any carry is folded back into the low 16 bits
(end-around carry). Finally, the one's-complement checksum is shown.
"""


def fold_carry(total: int) -> int:
    """Fold carry bits back into the low 16 bits until 16 bits remain."""
    while total > 0xFFFF:
        carry = total >> 16
        lower_16 = total & 0xFFFF

        print("\nCarry fold:")
        print(f"  Carry:       {carry:X}")
        print(f"  Lower 16 bit:{lower_16:04X}")

        total = lower_16 + carry
        print(f"  New sum:     {total:X}")

    return total


def main() -> None:
    print("16-bit 1-komplement summering")
    print("--------------------------------")
    print("Indtast 16-bit hexadecimale tal (0000-FFFF).")
    print("Du kan også skrive tal med 0x-prefix, fx 0x1234.")
    print("Tryk ENTER uden et tal for at afslutte og folde carry tilbage.\n")

    total = 0
    count = 0

    while True:
        raw = input("Hex-tal: ").strip()

        if raw == "":
            break

        try:
            value = int(raw, 16)
        except ValueError:
            print("Fejl: Indtast et gyldigt hexadecimalt tal.")
            continue

        if not 0 <= value <= 0xFFFF:
            print("Fejl: Tallet skal være mellem 0000 og FFFF.")
            continue

        total += value
        count += 1

        print(f"Tilføjet:      {value:04X}")
        print(f"Foreløbig sum: {total:X}")

    print("\n================================")
    print(f"Antal tal: {count}")
    print(f"Sum før carry fold: {total:X}")

    folded_sum = fold_carry(total)
    checksum = (~folded_sum) & 0xFFFF

    print("\nResultat")
    print("--------------------------------")
    print(f"16-bit 1-komplement sum: {folded_sum:04X}")
    print(f"1-komplement checksum:   {checksum:04X}")


if __name__ == "__main__":
    main()
