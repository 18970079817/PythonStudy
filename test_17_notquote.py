def del_not_quote(s):
    if len(s.split(':')) > 1:
        return s
    else:
        return '\n'

with open('111.txt', 'r') as f:
    for i in f.readlines():
        s = del_not_quote(i)
        s = str(s)
        with open('re111.txt', 'a') as g:
            g.write(s)