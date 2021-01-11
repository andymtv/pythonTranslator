from translate import Translator
translator = Translator(to_lang='pl')

try:
    with open('translateMe.txt', 'r+') as text:
        txt = []
        i = 0
        k = 30
        for line in text:
            while i < len(line):
                # Because of Google Translate line length restrictions we need to crop our text on lines of 50 characters
                cropped_line = line[i:k]
                i += 30
                k += 31
                txt.append(cropped_line)
    print(txt)
    for s in range(len(txt)):
        li = translator.translate(txt[s])
        print(li)
except FileNotFoundError as err:
    print('File does not exist')
    raise err
