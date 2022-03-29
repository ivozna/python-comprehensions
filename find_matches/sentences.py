import sys

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return tuple(f.readlines())


def read_sentences(files):
    return [read_text_file(filename) for filename in files]                                                                                                                                                                                                      
    

def find_matches(sentences):
    result = set(sentences[0])
    for s in sentences[1:]:
        result.intersection_update(s)
    return list(result)


def main():
    ss = read_sentences(sys.argv[1:])
    common = find_matches(ss)
    print(common)


if __name__ == "__main__":
    main()



# написати bash script який приймає шлях до директорії, знаходить 
# всі текстові файли у ній, та передає їх у скрипт вище., 
# результат записує у файл з назвою "{назва_директорії(або шляху)}_results.txt"