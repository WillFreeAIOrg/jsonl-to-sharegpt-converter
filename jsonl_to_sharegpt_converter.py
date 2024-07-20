#!/usr/bin/env python3
# Copyright (c) 2024 Leo King
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Converts JSONL datasets to ShareGPT format for LLM import.

This script translates datasets from JSONL (JSON Lines) format to ShareGPT format
for importing into language learning models (LLMs). It performs the following tasks:
1. Reads JSONL files from an input folder.
2. Converts each JSONL entry to the ShareGPT format.
3. Writes the converted data to new files in an output folder.

The ShareGPT format structures conversations as an array of messages, each with
a "from" field (either "human" or "assistant") and a "value" field containing
the message text.

This script is compatible with Python 3.6 and above.

Typical usage example:

  python jsonl_to_sharegpt_converter.py
"""

import json
import os
from typing import Dict, Any, List


def convert_to_sharegpt_format(input_file: str, output_file: str) -> None:
    """Converts a single JSONL file to ShareGPT format.

    Args:
        input_file: Path to the input JSONL file.
        output_file: Path to the output ShareGPT format file.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data: Dict[str, Any] = json.loads(line)
            
            conversations: List[Dict[str, str]] = [
                {"from": "human", "value": data["instruction"]},
                {"from": "assistant", "value": data["response"]}
            ]
            
            sharegpt_format = {"conversations": conversations}
            json.dump(sharegpt_format, outfile, ensure_ascii=False)
            outfile.write('\n')


def process_files(input_folder: str, output_folder: str) -> None:
    """Processes all JSONL files in the input folder.

    Args:
        input_folder: Path to the folder containing input JSONL files.
        output_folder: Path to the folder where output files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jsonl'):
            input_file = os.path.join(input_folder, filename)
            output_filename = "sharegpt_{}".format(filename)
            output_file = os.path.join(output_folder, output_filename)
            convert_to_sharegpt_format(input_file, output_file)
            print("Converted {} to {}".format(filename, output_filename))


def main() -> None:
    """Main function to set up and initiate file processing."""
    input_folder = 'data/jsonl'
    output_folder = 'data/sharegpt'
    process_files(input_folder, output_folder)


if __name__ == '__main__':
    main()
