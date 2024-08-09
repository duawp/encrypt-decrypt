import random
import string

print(r"""______            _     _  ______                 _           _ 
 _______   __    __   ______   __       __  _______  
|       \ |  \  |  \ /      \ |  \  _  |  \|       \ 
| $$$$$$$\| $$  | $$|  $$$$$$\| $$ / \ | $$| $$$$$$$\
| $$  | $$| $$  | $$| $$__| $$| $$/  $\| $$| $$__/ $$
| $$  | $$| $$  | $$| $$    $$| $$  $$$\ $$| $$    $$
| $$  | $$| $$  | $$| $$$$$$$$| $$ $$\$$\$$| $$$$$$$ 
| $$__/ $$| $$__/ $$| $$  | $$| $$$$  \$$$$| $$      
| $$    $$ \$$    $$| $$  | $$| $$$    \$$$| $$      
 \$$$$$$$   \$$$$$$  \$$   \$$ \$$      \$$ \$$      
                                                   """)
print("\n****************************************************************")
print("\n* Copyright of Malek, 2024                              *")
print("\n* https://x.com/FrankZane95                                  *")
print("\n* https://www.youtube.com/@duawp                          *")
print("\n****************************************************************")

def main():
    
    characters = " " + string.punctuation + string.digits + string.ascii_letters
    list_chars = list(characters)
    key = list_chars.copy()
    random.shuffle(key)
#Encrypt
    while True:
        plain_text = input("Enter a message to encrypt: \n")
        cipher_text = ""

        for i in plain_text:
            index = list_chars.index(i)
            cipher_text += key[index]


        print(f"original message: {plain_text}")
        print(f"encrypted message: {cipher_text}")
    
    #Decrypt:
        cipher_text = input("Enter a message to decrypt: \n")
        plain_text = ""
        for i in cipher_text:
            index = key.index(i)
            plain_text += list_chars[index]

        print(f"original message: {cipher_text}")
        print(f"decrypted message: {plain_text}")

if __name__ == "__main__":
    main()





