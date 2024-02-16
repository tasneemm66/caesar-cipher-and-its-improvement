letters = "abcdefghijklmnopqrstuvwxyz"
letters_map = letters * 2
key = "supermario"
message = input("enter the message you want to encrypt: ")

#attack
#[0] + [19] = 19 . [20]+[21]  
#before improve: p(find_key)= 1/26  ..  
#after improve:  p(find_key)= 1/26*10
while len(key) < len(message):
     key+= key


def encrypt(message, key):
    enc_message = ""
    for key_index, char in enumerate(message):
        if char in letters:
            index = letters.find(char)
            password_index = letters.find(key[key_index])
            enc_message += letters_map[index+password_index]
    return enc_message

def decrypt(message, key):
     dec_message = ""
     for key_index, char in enumerate(message):
            if char in letters:
                index = letters.find(char)
                password_index = letters.find(key[key_index])
                dec_message += letters[index-password_index]
     return dec_message


enc_text = encrypt(message, key)
print("Cipher text is :" +enc_text)

dec_text = decrypt(enc_text, key)
print("Plain text is :" +dec_text)
