import os

Shutdown = input("Do You Wish to shutdown, Your PC")

if Shutdown == 'nO':
    exit()
else:
    os.system("init 0")
