import time
print("\t\t\tMorse Code Converter")
class morseCode:
    codes_dict={
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    def codes(self,word,coding):
        print(" Converting....")
        time.sleep(2)
        if coding:
            code_list=[]
            for i in word.lower():
                if i in self.codes_dict:
                    code_list.append(self.codes_dict[i])
                else:
                    code_list.append('?')
            morsed=' '.join(code_list)
            print(f"\t\t\t\t{morsed}")
        else:
            for key,value in self.codes_dict.items():
                if value == word:
                    print(f"\t\t\t\t{word} = {key.upper()}")
def convert():
    morse_obj=morseCode()
    word=input("Enter the Word/morseCode: ")
    morse_obj.codes(word,coding)
while True:
    print("1. Word into Code\n2. Code into Word\n3. Exit")
    action=input("Enter command: ")
    if action=='1':
        coding=True
        convert()
    elif action=='2':
        coding=False
        convert()
    elif action=='3':
        print("Exiting the Program..")
        time.sleep(2)
        break
    else:
        print("Invalid input..")