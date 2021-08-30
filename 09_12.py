""" Bài 09: Viết hàm def extract_characters(*file) trả lại các kí tự trong các file"""

def extract_characters(*file):
    list=[*file]
    a=[]
    for i in range(len(list)):
        with open(list[i],mode='r',encoding='utf-8') as f:
            for line in f:
                h=line.split()
                for word in h:
                    for i in range(len(word)):
                        a.append(word[i])
    return set(a)

print(extract_characters('/Users/Asus/PycharmProjects/pythonCore/f.txt','/Users/Asus/PycharmProjects/pythonCore/vidu.txt'))
