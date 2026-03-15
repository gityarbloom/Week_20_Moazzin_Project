import base64



def decryp_base_64(enc_txt):

    base64_string = enc_txt
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")

    return sample_string


def encryp_base_64(str_txt):

    sample_string = str_txt
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string


##################################################


# c1 = "aba"
# print(c1 in ["aba", "aima"])

# words_string = "aaa, bbb ccc"

# words_string = words_string.split(",")

# for i in range(len(words_string)):
#     words_string[i] = words_string[i].split()
# print(words_string)