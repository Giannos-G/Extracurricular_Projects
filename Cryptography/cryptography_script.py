def code(message):
    baseupper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    baselower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    coded_message = ""
    #print(message)
    for letter_in_message in message:
        for j in range(len(baseupper)):
            if letter_in_message == baseupper[j]:
                coded_message = coded_message + baseupper[j - 1]
            elif letter_in_message == baselower[j]:
                coded_message = baselower[j - 1]
    #print(coded_message)
    return coded_message


message = open(r"C:\Users\User\Desktop\Test_Python.txt", "r")               # Open the file to be encrypted
new_file = open(r"C:\Users\User\Desktop\Test_Python_Encrypted.txt", "w")    # Save the encrypted sequence in another txt file
new_file.write(code(message.read()))
message.close()
new_file.close()
