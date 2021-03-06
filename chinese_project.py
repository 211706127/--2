import re
var = {}
C_number = {"零c":0,"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9}
C_unit  = ["","十","百","千","万"]
def define(name,value):
    global var
    var[name] = value

def println(name):
    global var
    rule = r'“(.*?)”'
    try:
        print("\n")
        print(var[name])
    except:
        print("\n")
        print(re.find(rule))

def add(name,num):
    global var
    result = number([var[name]][0]) + number(num)
    var[name] =  chinese(result)

def subtract(name,num):
    global var, C_number
    result = number([var[name]][0]) - number(num)
    var[name] =  chinese(result)

def multiplication(name,num):
    global var, C_number
    result = number([var[name]][0]) * number(num)
    var[name] = chinese(result)

def division(name,num):
    global var, C_number
    result = number([var[name]][0]) / number(num)
    var[name] = chinese(result)

def ifelse(get_input):
    global var,C_number
    num = C_number[get_input[3]]
    rule = r'“(.*?)”'
    list = re.findall(rule,str(get_input))
    if get_input[2] == "大于":
        if C_number[var[get_input[1]]] > num:
            print(list[0])
        else :
            print(list[1])
    elif get_input[2] == "小于":
        if C_number[var[get_input[1]]] < num:
            print(list[0])
        else :
            print(list[1])
    elif get_input[2] == "等于":
        if C_number[var[get_input[1]]] == num:
            print(list[0])
        else :
            print(list[1])
    else:
        print("输入不符合规则")


def chinese(num):
    global C_number,C_unit
    if num <= 10:
        for x in C_number:
            if num == C_number[x]:
                return x
    else:
        num = str(num)
        n = len(num) - 1
        result = ""
        for x in range(len(num)):
            if chinese(int(num[x])) == "零":
                if x == len(num):
                    result = result
                else:
                    result = result + chinese(int(num[x]))
            else :
                result = result + chinese(int(num[x])) + C_unit[n]
            n = n - 1
        return result

def number(cnum):
    global C_number
     #传入的是一个list ，需选取出为str。
    num = 0
    if cnum:
        idx_q, idx_b, idx_s = cnum.find('千'), cnum.find('百'), cnum.find('十')
        if idx_q != -1:
            num += C_number[cnum[idx_q - 1:idx_q]] * 1000
        if idx_b != -1:
            num += C_number[cnum[idx_b - 1:idx_b]] * 100
        if idx_s != -1:
            num += C_number.get(cnum[idx_s - 1:idx_s], 1) * 10
        if cnum[-1] in C_number:
            num += C_number[cnum[-1]]
    return num

while True :
    get_input = input().split()
    try: rubbish = get_input[0]
    except:print("无输入")
    else:
        if get_input[0] == "整数":
            if get_input[2] != "等于":
                print("输入不符合规则")
            else :
                define(get_input[1],get_input[3])
        elif get_input[0] == "看看":
            println(get_input[1])
        elif get_input[0] == "如果":
            ifelse(get_input)
        else :
            if get_input[1] == "增加":
                add(get_input[0],get_input[2])
            elif get_input[1] == "减少":
                subtract(get_input[0],get_input[2])
            elif get_input[1] == "乘以":
                multiplication(get_input[0],get_input[2])
            elif get_input[1] == "除以":
                division(get_input[0],get_input[2])
            else :
                print("输入不符合规则")