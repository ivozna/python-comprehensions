from typing import Dict
import sys


def encode(text: str, codes: Dict[str,str]) -> str:
    encoded_text = text
    for word, code in codes.items():
        if word in text:
            encoded_text = encoded_text.replace(word, code)
    return encoded_text
            
def read_input(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read()


def read_codes(file_name: str) -> Dict[str,str]:
    with open(file_name, 'r') as f:
        lines = f.read().split('\n')
        words = [line.split(',') for line in lines]
    
        dic = {}
        for line_index, line in enumerate(words):
            for word_index, word in enumerate(line):
                code = str(line_index)+str(word_index)
                dic[word] = code
    return dic 

def write_output(file_name: str, encoded_text: str) -> None:
    with open(file_name, 'w') as f:
        f.write(encoded_text)


def main() -> None:
    #python encode.py input.txt codes.txt output.txt
    text = read_input(sys.argv[1])
    code = read_codes(sys.argv[2])
    encoded_text = encode(text, code)
    print(f"Encoded text: {encoded_text}")
    write_output(sys.argv[3], encoded_text)

if __name__ == "__main__":
    main()
