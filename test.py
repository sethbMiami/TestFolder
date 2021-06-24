# first local program

print("Hello Seth")

age = 30
location = "Miami"

print("You are " + str(age) + " years old and live in " + location)


def big_numbers(num, exponent):
    return num ** exponent

# with open('readThis.txt') as text_file:
#    text_data = text_file.read()
# print(text_data)


# with open('readThis.txt') as textf:
#    for line in textf.readlines():
#        print(line)

with open('newFile.txt', 'a') as writeThis:
    writeThis.write("\nWill this create a new file inside TestFolder?")
