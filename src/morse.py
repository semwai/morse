
STORAGE = {'A': '.-', 'B': '-...',
           'C': '-.-.', 'D': '-..', 'E': '.',
           'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-',
           'L': '.-..', 'M': '--', 'N': '-.',
           'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--',
           'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--',
           '4': '....-', '5': '.....', '6': '-....',
           '7': '--...', '8': '---..', '9': '----.',
           '0': '-----', ', ': '--..--', '.': '.-.-.-',
           '?': '..--..', '/': '-..-.', '-': '-....-',
           '(': '-.--.', ')': '-.--.-'}


def encode(message: str, storage) -> str:
    """return morse string
    """
    out = []
    for i in message.upper():
        if (m := storage.get(i)) is None:
            raise NotImplementedError(f"letter {i} not supported")
        out += m
    return " ".join(out)


def decode(message: str, storage) -> str:
    """return text string
    """
    out = []
    for combination in message.split(' '):
        s = [i[0] for i in storage.items() if i[1] == combination]
        if len(s) == 0:
            raise NotImplementedError(f"combination {combination} not supported")
        else:
            out += s[0]
    return "".join(out)


if __name__ == '__main__':
    print(decode('... --- ...', STORAGE) == 'SOS')
    print(encode('sos', STORAGE))
    try:
        print(encode('привет', STORAGE))
    except NotImplementedError as e:
        print(e)
