import nltk
from nltk.tree import Tree

N = 0  # 何行目か

s_exp = []
for line in open('test_result', 'r'):
    line = line.rstrip()
    s_exp.append(line)

t = Tree.fromstring(s_exp[N])
t.draw()