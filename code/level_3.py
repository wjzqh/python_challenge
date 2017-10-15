# dane <<-- http://www.pythonchallenge.com/pc/def/equality.html
dane = ''.join(line.strip() for line in open("..\\data\\bodyguard.txt"))
znaki = [""] * 9
znalezione = ""
for znak in dane:
    del znaki[0]
    znaki.append(znak)
    if \
        not znaki[0].isupper() and\
            znaki[1].isupper() and\
            znaki[2].isupper() and\
            znaki[3].isupper() and\
            znaki[4].islower() and\
            znaki[5].isupper() and\
            znaki[6].isupper() and\
            znaki[7].isupper() and\
        not znaki[8].isupper()    \
    :
        znalezione += znaki[4]
print(znalezione) # -->> "linkedlist"