import os
import subprocess

file = open("env", "r")


for line in file:
    # remove all the unnecessary spaces
    y = line.strip()
    # remove all the quotations'
    y = y.replace("'", '')
    
    z = y.split('=')
    key_name = z[0]
    value_name = z[1]
    os.environ[key_name] = value_name
    print(key_name + ":" + value_name)

subprocess.run(['gnome-terminal'])

