#----------------
# Ten-per-line printing filter (assignment 6)
# ----------------
# Myra Jamison, February 19, CSCI151

#prints to stdout integers from randomintseq.py and formats them in rows of 10

import stdio

while stdio.isEmpty() == False:
    for i in range(10):
        if stdio.isEmpty() == True:
            break
        num = stdio.readInt()
        if num < 10:
            num = ' ' + str(num)
        stdio.write(str(num) + '   ')
    stdio.writeln()