import re

kad_num = []
abbrv = []
strings = []

def FindKadNum(string):
    p = re.findall(r"\d{2}:\d{2}:\d{6,7}:\d{1,}", string)
    if p: kad_num.extend(p)

def SeparateStr(string):
    string = string.replace("о...", "о.", 1)
    string = string.replace("уч.", "участок")
    res_string = re.split(r"[.?!]\s", string)
    for i in range(len(res_string)):
        if res_string[i]:
            res_string[i] = res_string[i].replace("\n", "")
            if res_string[i] == "":
                res_string.pop(i)
            strings.append(res_string[i])
        
def FindAbbrv(string):
    p = re.findall(r"[А-Я]{2,}", string) 
    p1 = re.findall(r"[^.?!]\s[А-Я][а-я]{1,}", string) 
    for i in range(len(p1)):
        p1[i] = p1[i][2:]
    if p: abbrv.extend(p)
    if p1: abbrv.extend(p1)


with open("text.txt", "r", encoding = "utf-8") as r:
    s = r.readlines()
    for i in range(len(s)):
        string = s[i]
        FindKadNum(string)
        SeparateStr(string)
        FindAbbrv(string)

    with open("textNEW.txt", "w", encoding = "utf-8") as w:
        w.write("Kad num: \n")
        n = 1
        for i in kad_num:
            w.write("\t{:2}:  {}\n".format(n, i))
            n += 1
        w.write("\n")

        w.write("Separate syntax: \n")
        n = 1
        for i in strings:
            if i[-1] != ":":
                w.write("\t{:2}:  {}\n".format(n, i+"."))
            else:
                w.write("\t{:2}:  {}\n".format(n, i))
            n += 1
        w.write("\n")

        w.write("Abbrv and names: \n")
        n = 1
        for i in abbrv:
            w.write("\t{:2}:  {}\n".format(n, i))
            n += 1