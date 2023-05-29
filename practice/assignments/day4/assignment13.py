# Q1.
# Caesar cipher
import string


def alpha():
    res_low = ""
    for letter in string.ascii_lowercase:
        res_low = res_low+letter
    res_upp = ""
    for letter in string.ascii_uppercase:
        res_upp = res_upp+letter
    org_alpha = res_low+res_upp
    return org_alpha

def generate_ceasar_dict(shift):
    #org_alpha = alpha()
    org_alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    org_alpha_l = string.ascii_lowercase
    org_alpha_c = string.ascii_uppercase
    shifted_aplha = org_alpha_l[shift:] + org_alpha_l[:shift]+org_alpha_c[shift:] + org_alpha_c[:shift]
    caesar_dict = dict(zip(org_alpha, shifted_aplha))
    return caesar_dict


def rot13(message):
     rot13_dict=generate_ceasar_dict(13)
     result=""
     for char in message:
         if char in rot13_dict:
             result=result+rot13_dict[char]
         else:
             result=result+char
     return result
 
message="Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
decoded_message=rot13(message)
print("deconded message => ",decoded_message)
encoded_message=rot13(decoded_message)
print("encoded message => ",encoded_message)
