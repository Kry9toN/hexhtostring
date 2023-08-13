# This code is licensed under the GNU General Public License (GPL) version 3
# Copyright (C) 2023 Dhimas Bagus Prayoga (Kry9toN)
# SPDX-License-Identifier: GPL-3.0
# For details, please refer to the LICENSE file.

import re
import sys

def decode_code(match):
    if match.group(1):
        hex_value = match.group(2)[:2]
        unhex_value = chr(int(hex_value, 16))
        if len(match.group(2)) > 2:
            unhex_value += match.group(2)[2:]
        return unhex_value
    else:
        return chr(int(match.group(2), 8))

def main():
    if len(sys.argv) < 3:
        print("Usage: python decode.py input_file output_file")
        return

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    try:
        # Buka file input dalam mode membaca
        with open(input_file_path, "r") as input_file:
            # Baca isi file
            input_data = input_file.read()
            # Menerapkan fungsi dekode pada input
            decoded_output = re.sub(r'\\(x)?([0-9a-f]{2,3})', decode_code, input_data)
            # Simpan hasil dekode ke dalam file output
            with open(output_file_path, "w") as output_file:
                output_file.write(decoded_output)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
