from typing import Dict
from pathlib import Path


def read_file(filepath: Path) -> str:
    try:
        with open(filepath) as file:
            return file.read()
    except IOError as e:
        raise FileNotFoundError(f"Failed to open or read the file: {e}")


def save_text_to_file(filepath: Path, text: str) -> None:
    if not filepath.parent.exists():
        raise FileNotFoundError(f"The directory {filepath.parent} does not exist.")
    
    with open(filepath, "w") as file:
        file.write(text)


def sort_dict_by_value(dictionary: Dict, reverse: bool = True) -> Dict:
    return {
        k: v
        for k, v in sorted(
            dictionary.items(), key=lambda item: item[1], reverse=reverse
        )
    }


def normalize_text(input_text: str) -> str:
    output_text = "".join(
        [char.lower() for char in input_text if char.isalpha() or not char.isspace()]
    )
    return output_text
