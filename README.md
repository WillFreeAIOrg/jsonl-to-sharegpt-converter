# JSONL to ShareGPT Converter

This tool converts datasets from JSONL (JSON Lines) format to ShareGPT format for importing into language learning models (LLMs).

## Features

- Reads JSONL files from an input folder
- Converts each JSONL entry to the ShareGPT format
- Writes the converted data to new files in an output folder
- Handles multiple files in bulk
- Maintains original filename structure with "sharegpt_" prefix for output files

## Requirements

- Python 3.6 or higher

## Installation

Clone the repository:

```bash
git clone https://github.com/leoking/jsonl-to-sharegpt-converter.git
cd jsonl-to-sharegpt-converter
```

No additional dependencies are required beyond Python's standard library.

## Usage

1. Place your JSONL files in the `data/jsonl` directory.
2. Run the script:

   ```bash
   python jsonl_to_sharegpt_converter.py
   ```

3. Find the converted files in the `data/sharegpt` directory.

## Input Format

The input JSONL files should have the following structure:

```json
{"instruction": "Human message", "response": "Assistant response"}
```

## Output Format

The output files will be in ShareGPT format:

```json
{
  "conversations": [
    {"from": "human", "value": "Human message"},
    {"from": "assistant", "value": "Assistant response"}
  ]
}
```

## Customization

You can modify the input and output folder paths in the `main()` function of the script.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Leo King

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## Show Your Support

Give a ⭐️ if this project helped you!
