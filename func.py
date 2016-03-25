def newLine():
    print

print "First Line"
newLine()
print "Second Line"

print "First Line"
newLine()
newLine()
newLine()
print "Second Line"

def threeLines():
  newLine()
  newLine()
  newLine()

print "First Line"
threeLines()
print "Second Line"

def printTwice(bruce):
    print bruce, bruce

printTwice('spam')
printTwice(5)
printTwice('spam'*4)
ramesh = "Hello Python."
printTwice(ramesh)

def doTwice(part1, part2):
    do = part1 + part2
    printTwice(do)

c1 = "Hi,"
c2 = "Hello."
doTwice(c1, c2)
