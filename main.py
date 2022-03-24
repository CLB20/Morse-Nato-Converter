import pandas

data = pandas.read_csv("alphabet.csv")

quit_ = "N"

while quit_ == "N":
    text = input("Input the text you want to translate:\n").upper()
    code_name = input("Do you want Morse code (M) or NATO (N) ? ").upper()
    if code_name == "M":
        code = "Morse"
    elif code_name == "N":
        code = "Nato"
    else:
        print("Invalid entry")
        break

    translated = ""
    for char in text:
        if char == " ":
            translated += "/"
            translated += " "
        else:
            try:
                translated += data.loc[data.Letter == char, code].values[0]
                translated += " "
            except IndexError:
                translated += "#"
                translated += " "
    print(f"Your text in {code} Code is:\n {translated}")
    quit_ = input("Do you want to quit? Y/N ").upper()



