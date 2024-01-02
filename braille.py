import serial
# Open serial port (replace 'COMx' and baud rate with your printer's port and settings)
COMx=input("Enter the appropriate serial port identifier of your Braille printer :")
baudrate=int(input("Enter the Baudrate according to the printer settings:"))

ser = serial.Serial(COMx, baudrate, timeout=1)


braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': '⠀'
}

def text_to_braille(text):
    braille_text = ''
    for char in text.lower():
        if char in braille_dict:
            braille_text += braille_dict[char]
        else:
            braille_text += char
    return braille_text

text=input("Enter the text you want to translate in Braille: ")
braille_result = text_to_braille(text)
print(braille_result)
ser.write(braille_result)
ser.close 