# 参数、解包和变量
# 运行本脚本，记得添加命令行参数，否则报错
# python ex13.py 1st 2nd 3rd

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
