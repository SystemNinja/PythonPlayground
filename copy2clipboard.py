# This program demonstrates how to copy text to clipboard
# Reference:
# Native -> https://www.codegrepper.com/code-examples/python/python+copy+string+to+clipboard
# Library pyperclip -> https://pypi.org/project/pyperclip/
# pip install pyperclip

from subprocess import check_call
import pyperclip

#Native
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)

sentence = "some sentence"
copy2clip(sentence)

#Library pyperclip
pyperclip.copy(sentence)