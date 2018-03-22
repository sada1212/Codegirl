def encode(text):
    first=text[0]
    count=0
    encodedtext=""
    for i in text:
        if i==first:
            count=count+1
    for i in text:
        shiftedChar = chr(ord(i) + count)
        encodedtext= encodedtext+shiftedChar
    return encodedtext
print(encode("apple"))
print(encode("apple alarm"))
print(encode("zoo"))
