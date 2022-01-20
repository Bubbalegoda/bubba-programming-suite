import os

NONE = ""

VARIABLES = {}
FUNCTIONS = {}

print("Upgrading python - pip")
os.system("python -m pip install --upgrade pip")

def interpretCode(code, filename):
    codeReadable = code.split(".")
    print(codeReadable)
    if code == "\n" or code == "":
        pass
    elif codeReadable[0] == "print":
        print(codeReadable[1].split('"')[1])
    elif codeReadable[0] == "pymod":
        if codeReadable[1] == "install":
            os.system("python -m pip install --upgrade " + codeReadable[2].split('"')[1])
        elif codeReadable[1] == "uninstall":
            os.system("python -m pip uninstall " + codeReadable[2].split('"')[1])
        else:
            if filename == NONE:
                print(
                    f'Traceback (most recent call last):\nFile: "<bpl$shell>", line 1, in <module>\n"{codeReadable[1]}"\nSyntaxError: Not a vailid argument')
            else:
                print(
                    f'Traceback (most recent call last):\nFile: "<{filename}>", line 1, in <module>\n"{codeReadable[1]}"\nSyntaxError: Not a vailid argument')
    elif codeReadable[0] == "cmd":
        try:
            os.system(codeReadable[1].split('"')[1])
        except:
            print(f'Traceback (most recent call last):\nFile: "<{filename}>", line 1, in <module>\nSyntaxError: An unexpected error occurred')
    else:
        if filename == NONE:
            print(f'Traceback (most recent call last):\nFile: "<bpl$shell>", line 1, in <module>\n"{code}"\nSyntaxError: Invalid code')
        else:
            print(f'Traceback (most recent call last):\nFile: "<{filename}>", line 1, in <module>\n"{code}"\nSyntaxError: Invalid code')


def terminal():
    while True:
        interpretCode(input("$"), NONE)


if __name__ == "__main__":
    terminal()