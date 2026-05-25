import json
import logging

logger = logging.getLogger(__name__)

INPUT_FILE = "Zabrodin_file_2.json"
OUTPUT_FILE = "Zabrodin_file_3.txt"


def load_json(file_path: str) -> dict:
    logger.info("Loading %s", file_path)
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def save_tokens(tokens: list[tuple[str, str]], file_path: str):
    with open(file_path, "w", encoding="utf-8") as f:
        for lemma, u_pos_tag in tokens:
            f.write(f"{lemma} {u_pos_tag}\n")

    logger.info("%d tokens written to %s", len(tokens), file_path)


def is_punctuation(pos_tag: str) -> bool:
    return pos_tag == "PUNCT"


def extract_tokens(json_data: str) -> list[tuple[str, str]]:
    tokens = []
    for line in json_data.splitlines():
        if not line or line.startswith("#"):
            continue

        fields = line.split("\t")
        if len(fields) < 10:
            continue

        lemma, u_pos_tag = fields[2], fields[3]
        if is_punctuation(u_pos_tag):
            continue

        tokens.append((lemma, u_pos_tag))

    return tokens


def main():
    json_data = load_json(INPUT_FILE)
    tokens = extract_tokens(json_data["result"])
    save_tokens(tokens, OUTPUT_FILE)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    main()
