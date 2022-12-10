from alphabets import RUS, ENG


def encode(message: str, storage) -> str:
    """return morse string
    """
    out = []
    for i in message.upper():
        if (m := storage.get(i)) is None:
            raise NotImplementedError(f"letter {i} not supported")
        out += f" {m}"
    return "".join(out[1:]) if len(out) > 0 else ""


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
    print(decode('... --- ...', ENG) == 'SOS')
    print(encode('sos', ENG))
    try:
        print(encode('привет', ENG))
    except NotImplementedError as e:
        print(e)

    print(decode('... --- ...', RUS) == 'СОС')
    print(encode('сос', RUS))
    try:
        print(encode('hello', RUS))
    except NotImplementedError as e:
        print(e)
