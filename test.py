import json
import requests

URL = "http://localhost:3000/process"


def main():
    response = requests.post(URL, data={
        "data": "Привіт! Це файл для тестування роботи UDPipe. Боже допоможи.",
        "tokenizer": "",
        "tagger": "",
        "parser": "",
    })
    response.raise_for_status()

    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()