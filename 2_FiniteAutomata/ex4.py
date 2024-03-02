import graphviz  # doctest: +NO_EXE
dot = graphviz.Digraph(comment='The Round Table')
dot  #doctest: +ELLIPSIS

dot.node('A', 'King Arthur')  # doctest: +NO_EXE
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)  # doctest: +NORMALIZE_WHITESPACE +NO_EXE

# doctest_mark_exe()

dot.render('doctest-output/round-table.gv').replace('\\', '/')
'doctest-output/round-table.gv.pdf'

# doctest_mark_exe()

dot.render('doctest-output/round-table.gv', view=True)  # doctest: +SKIP
'doctest-output/round-table.gv.pdf'