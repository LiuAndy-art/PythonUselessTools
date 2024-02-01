import os
import graphviz
import sys
# 生成流程图，需要电脑安装graphviz程序并且添加到环境变量

filename = sys.argv[0].split(".")[0]
u = graphviz.Digraph(
    filename,
    filename='{}'.format(filename),
    node_attr={
        'color': 'lightblue2',
        'style': 'filled',
        'fontname': 'SimSun'},
    edge_attr={
        'fontname': 'FangSong'})

u.edge('概率空间', '样本空间', label="def")
u.edge('概率空间', 'σ代数', label="def")
u.edge('概率空间', '概率', label="def")
u.edge('σ代数', '补集封闭', label="def")
u.edge('σ代数', '包含全集', label="def")
u.edge('σ代数', '可列并封闭', label="def")
u.edge('概率', 'σ代数', label="定义域")
u.edge('概率', '[0,1]区间', label="值域")
u.edge('概率', '测度', label="包含于")
u.edge('测度', '可测空间', label="定义域")
u.edge('可测空间', '样本空间', label="包含")
u.edge('可测空间', 'σ代数', label="包含")
u.edge('测度', '[0,oo]', label="值域")
u.edge('概率', '可列可加性', label="性质")
u.edge('概率', '有限可加性', label="性质")
u.edge('概率', '可列次可加性', label="性质")
u.edge('概率', '有限次可加性', label="性质")
u.edge('概率', '单调性', label="性质")
u.edge('概率', '从上连续性', label="性质")
u.edge('概率', '从下连续性', label="性质")
u.edge('概率', '容斥公式', label="性质")
u.view()
os.system("dot -Tpng {} -o {}.png".format(filename, filename))
