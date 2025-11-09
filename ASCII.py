def encodeString(stringVal):
    # Your code goes here.
    encodedList = []
    prevChar = stringVal[0]
    count = 0

    for char in stringVal:
        if prevChar != char: #C != A
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1

    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedString = ''
    for item in encodedList:
        decodedString = decodedString + item[0] * item[1]
    return decodedString

art = '''
        .8888.
  __...d8O8888b
,""""888888' '8b
      `Y8Y.. .d8b
       / .8888888b
      |  888888888b
      |  8888888888
      |  8888888888
      | .8888888888
      | d8888888888
      | 88881888888
      | 88881888888
      | 88881888888
      | Y8818888888
      \ 'Y81888888Y
       \ 'Y1888888'
        |  8888888
     ,mm8'.8888888

'''

encodedString = encodeString(art)
print(decodeString(encodedString))