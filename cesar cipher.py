letters = "abcdefghijklmnopqrstuvwxyz"
key = 3
message = input("enter the message you want to encrypt: ")

def encrypt(message, key):
    enc_message = ""
    for char in message:
        if char in letters:
            index = letters.find(char)
            enc_message += letters[index+key]
    return enc_message

def decrypt(message, key):
    dec_message = ""
    for char in message:
        if char in letters:
            index = letters.find(char)
            dec_message += letters[index-key]
    return dec_message

enc_text = encrypt(message, key)
print("Cipher text is :" +enc_text)

dec_text = decrypt(enc_text, key)
print("Plain text is :" +dec_text)
