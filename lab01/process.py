import json
import logging

import requests

logger = logging.getLogger(__name__)

INPUT_FILE = "Zabrodin_file_1.txt"
OUTPUT_FILE = "Zabrodin_file_2.json"
URL = "http://localhost:3000/process"


def load_text(file_path: str) -> str:
    logger.info("Reading %s", file_path)
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def save_json(data: dict, file_path: str):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logger.info("Output written to %s", file_path)


def analyze(text: str, url: str) -> dict:
    logger.info("Sending %d characters to %s", len(text), URL)

    try:
        response = requests.post(url, data={
            "data": text,
            "tokenizer": "",
            "tagger": "",
            "parser": "",
        })
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        logger.error("Could not connect to %s", url)
        raise

    return response.json()


def main():
    text = load_text(INPUT_FILE)
    json_data = analyze(text, URL)
    save_json(json_data, OUTPUT_FILE)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    main()
