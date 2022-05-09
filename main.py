
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         " ",
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
              ".......",
              ". - - - -", ". . - - -", ". . . - -", ". . . . -", ". . . . .",
              "- . . . .", "- - . . .", "- - - . .", "- - - - .", "- - - - -"]

end = False

print("Welcome! This is a text-based text to morse-code converter. ")

while not end:
    text_string = input("Enter text to convert to Morse Code: \n")
    result = []

    for char in text_string:
        value = ""
        try:
            value = morse_code[alpha.index(char.upper())]
        except ValueError:
            value = char
        finally:
            result.append(value)

    print(" ".join(result))

    end = input("All done? (Y/N): \n").upper() == "Y"

