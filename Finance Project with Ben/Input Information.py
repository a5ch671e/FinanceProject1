from tkinter import *

root = Tk()

def encrypt(word):
    word = word.upper()
    alphabet_num = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    num_alphabet = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}    
    kachig = 11
    encodedList = []
    for i in range(len(word)):
        n = alphabet_num.get(word[i])
        n += kachig
        if kachig == 11:
            kachig = 1
        elif kachig == 1:
            kachig = 3
        elif kachig == 3:
            kachig = 8
        elif kachig == 8:
            kachig = 9
        elif kachig == 9:
            kachig = 7
        elif kachig == 7:
            kachig = 12
        elif kachig == 12:
            kachig = 22
        elif kachig == 22:
            kachig = 4
        elif kachig == 4:
            kachig = 19
        elif kachig == 19:
            kachig = 10
        elif kachig == 10:
            kachig = 2
        elif kachig == 2:
            kachig = 24
        elif kachig == 24:
            kachig = 15
        elif kachig == 15:
            kachig = 5
        elif kachig == 5:
            kachig = 16
        elif kachig == 16:
            kachig = 21
        elif kachig == 21:
            kachig = 6
        elif kachig == 6:
            kachig = 13
        elif kachig == 13:
            kachig = 23
        elif kachig == 23:
            kachig = 14
        elif kachig == 14:
            kachig = 17
        elif kachig == 17:
            kachig = 18
        elif kachig == 18:
            kachig = 20
        elif kachig == 20:
            kachig = 11    
        letter = num_alphabet.get(n, "NO")
        if letter == "NO":
            n = n - 26
            letter = num_alphabet.get(n, "Oops")
        encodedList.append(letter)
    sentence1 = ""
    for i in range(len(word)):
        sentence1 += encodedList[i]
    return sentence1 

def nameFunc():
    global name
    name = n.get()
    nameLabel2 = Label(root, text = "Thanks").grid(row = 3, column = 1)
    name = encrypt(name)

def countyFunc():
    global county
    county = c.get()
    countyLabel2 = Label(root, text = "Thanks(check spelling you can overwrite it)").grid(row = 7, column = 1)
    county = encrypt(county)

def salaryFunc():
    global salary
    salary = s.get()
    salaryLabel2 = Label(root, text = "Thanks(you may click the X now)").grid(row = 11, column = 1)
    salary = (int(salary) / 2) * 8
    
n = StringVar()
c = StringVar()
s = StringVar()
root.title("Survey on wages")
nameLabel = Label(root, text = "What is your name?").grid(row = 0, column = 1)
nameEntry = Entry(root, width = 20, textvariable = n).grid(row = 1, column = 1)
nameButton = Button(root, text = "Enter", command = nameFunc).grid(row = 2, column = 1)

countyLabel = Label(root, text = "What county in England do you live in? NO SPACES").grid(row = 4, column = 1)
countyEntry = Entry(root, width = 20, textvariable = c).grid(row = 5, column = 1)
countyButton = Button(root, text = "Enter", command = countyFunc).grid(row = 6, column = 1)

salaryLabel = Label(root, text = "What is your Yearly Salary?").grid(row = 8, column = 1)
salaryEntry = Entry(root, width = 20, textvariable = s).grid(row = 9, column = 1)
salaryButton = Button(root, text = "Enter", command = salaryFunc).grid(row = 10, column = 1)

root.mainloop()




file = open('Name, County, and Salary.txt','a')
file.write(("%s\n%s %s\n") % (name, county, salary))
file.close()
