"""
guillaume@ubuntu:~/$ cat add_item.json
cat: add_item.json: No such file or directory

guillaume@ubuntu:~/$ ./7-add_item.py
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
[]

guillaume@ubuntu:~/$ ./7-add_item.py Best School
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School"]

guillaume@ubuntu:~/$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]

guillaume@ubuntu:~/$ 
"""