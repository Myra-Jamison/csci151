import sys
import stdio
#module
def farh_to_celsius(farh):
    return (farh-32)/1.8
def celsius_to_farh(celsius):
    return (celsius*1.8+32)

#test client
def main(a,b,c,d):
    stdio.writeln(celsius_to_farh(a))
    stdio.writeln(celsius_to_farh(b))
    stdio.writeln(farh_to_celsius(c))
    stdio.writeln(farh_to_celsius(d))

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

main(a,b,c,d)