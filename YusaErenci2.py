__author__ = "Yüşa Erenci"

import random

hang0 = """
_____
|   |
|
|
|
⊥"""
hang1 = """
_____
|   |
|   ◯
|
|
⊥"""
hang2 = """
_____
|   |
|   ◯
|   |
|
⊥"""
hang3 = """
_____
|   |
|   ◯
| --|
|
⊥"""
hang4 = """
_____
|   |
|   ◯
| --|--
|  
⊥"""
hang5 = """
_____
|   |
|   ◯
| --|--
|  /
⊥"""
hang6 = """
_____
|   |
|   ◯
| --|--
|  / \\
⊥"""
hangLv = 0
hangPic = [hang0, hang1, hang2, hang3, hang4, hang5, hang6]
wordList = ["tavşan", "gökyüzü", "cumhuriyet", "bilgisayar", "hoşgörü"]
true = 0
lettersUsed = []
print("""
--------------------------------
Adam Asmaca Oyununa Hoşgeldiniz!
********************************""")
output = []
output1 = ["", "", "", "", "", ""]
output2 = ["", "", "", "", "", "", ""]
output3 = ["", "", "", "", "", "", "", "", "", ""]
output4 = ["", "", "", "", "", "", "", "", "", ""]
output5 = ["", "", "", "", "", "", ""]

pickedWord = random.choice(wordList)
if pickedWord == wordList[0]:
    output = output1
if pickedWord == wordList[1]:
    output = output2
if pickedWord == wordList[2]:
    output = output3
if pickedWord == wordList[3]:
    output = output4
if pickedWord == wordList[4]:
    output = output5
# gameloop
while True:
    false = 0
    word = str(input("bir harf giriniz: "))
    if len(word) == len(pickedWord):
        if word == pickedWord:
            print("Doğru tahmin ettiniz!!\nTebrikler kazandınız!")
            break
        else:
            print("yanlış tahmin ettiniz ve kaybettiniz :(")
            break
    elif len(word) > 1:
        print("tahminde bulunduysanız eksik harf, harf yazdıysanız aynı anda fazla harf girdiniz.")
    if word in lettersUsed:
        print("yazdın bunu zaten")
    else:
        for i in range(len(pickedWord)):
            # print(true)
            for char in pickedWord[i]:
                # print()
                if word != char:
                    false += 1
                else:
                    del output[i]
                    output.insert(i, word)
                    true += 1
                    lettersUsed.append(word)
                if false == len(pickedWord):
                    hangLv += 1
                    lettersUsed.append(word)
        print(hangPic[hangLv])
        if hangLv != 6:
            print(output)
    # kazanma-kaybetme
        if true == len(pickedWord):
            print("""
            Tebrikler!!!
            Kelimeyi Bildiniz, Kazandınız!
            """)
            break
        if hangLv == 6:
            print('''
            Adam asıldı. Kaybettiniz :(
            Kelime:''', pickedWord)
            break