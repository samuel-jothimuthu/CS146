print("Hello, What assignment number is this?")
a = input()
ac = "a" + a + "c.txt"
f = open(ac, "w+")
print("How many questions are there?")
questionNum = int(input(), 10)
for i in range(questionNum):
    f.write(str(i + 1) + ") ")
    print("What are the answers to " + str(i+1) + "?")
    ans = input()
    f.write(str(ans) + "\n")

f.close()
