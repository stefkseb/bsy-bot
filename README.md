# Controller and Bot for BSY

This is a simple implementation of a controller and a bot in Python. It uses a GitHub Gists for communication in a way, that it cannot be 
spotted on the first sight that there is exchange of commands and data giong on. Communication is hidden using plain text, for simplicity
lorem ipsum generated texts are used.

## Install

For proper functionality you need to insert a **valid GitHub token** to the controller and a bot, so it could post comments on gist.
[It uses a public gist owned by me.](https://gist.github.com/stefkseb/16f8ed1319b10a550451060d5a56d493)

You need to install the steganography library, the lorem library and the python GitHub API

`pip install pyUnicodeSteganography`

`pip install lorem`

`pip install PyGithub`

## Usage

All available commands for the controller are written out, when the controller starts or type (?).
