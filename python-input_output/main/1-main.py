#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

"""
OUTPUT

guillaume@ubuntu:~/$ ./1-main.py
24
guillaume@ubuntu:~/$ cat my_first_file.txt
This School is so cool!

"""