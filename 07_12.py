
listfile=['/Users/Asus/PycharmProjects/pythonCore/f.txt','/Users/Asus/PycharmProjects/pythonCore/vidu.txt']
with open('/Users/Asus/PycharmProjects/pythonCore/outfile.txt', mode='a', encoding='utf-8') as wf:
    for i in range(len(listfile)):
        with open(listfile[i],mode='r', encoding='utf-8') as rf:
            line=rf.read()
            wf.write(line)
        wf.write('\n')


