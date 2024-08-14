# todo:
#   Hoci je Morseova abeceda v súčasnosti väčšinou nahradená inými metódami prenosu údajov, stále sa používa v niektorých aplikáciách po celom svete.
#   Morseova abeceda zakóduje každý znak ako sériu „bodiek“ a „pomlčiek“. napr.:
#   A = ‘·−‘
#   Q = ‘−−·−‘
#   1 = ‘·−−−−‘
#   V Morseovej abecede sa nerozlišujú veľké a malé písmená a tradične sa používajú veľké písmená. Jedna medzera sa používa na
#   oddelenie písmenových kódov a 3 medzery sa používajú na slová.
#   HEY JUDE = ‘···· · −·−− ·−−− ··− −·· ·’
#   POZOR : Medzery navyše pred alebo za kódom nemajú žiadny význam a mali by byť ignorované.
#   Okrem písmen, číslic a interpunkčných znamienok existujú špeciálne signály. Najznámejší je medzinárodný núdzový signál SOS.
#   SOS = ‘···−−−···’
#   Tieto signály sa považujú za jednotlivé špeciálne znaky a zvyčajne sa prenášajú ako samostatné slová.
#   Vaše cvičenie je implementovať funkciu, ktorá bude akceptovať Morseov kód ako vstup a vráti dekódovaný reťazec ľudsky zrozumiteľných znakov.

# todo:
#   Algoritmus by mal fungovať nasledovne:
#   decode_morse('.... . -.--   .--- ..- -.. .')  ## => 'HEY JUDE'
#   decode_morse(' . ')  ## => 'E'
#   decode_morse('...   ---   ...')  ## => 'S O S'

# todo:
#   Užitočný bude aj slovník.

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_morse(morse_code: str) -> str:
    words = morse_code.strip().split('   ')
    result = ""

    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in MORSE_CODE:
                result += MORSE_CODE[letter]
            else:
                result += '?'
        result += " "

    return result.strip()


if __name__ == "__main__":
    morse_codes = ['.... . -.--   .--- ..- -.. .', ' . ', '...   ---   ...']
    for code in morse_codes:
        print(f"{code} -> '{decode_morse(code)}'")
