from lists.Stack import Stack

import re

text = '''
<html>
    <head>
        <title>
            Example
        </title>
    </head>
    <body>
        <h1>Hello, world</h1>
    </body>
</html>'''


def check_html_balance(html):
    stck = Stack()
    preparedHtml = html.replace('<', ' <')
    preparedHtml = preparedHtml.replace('>', '> ')
    tags = [tag for tag in preparedHtml.split() if re.search('<\S+>', tag)]
    tagsOpen = [tagOpen for tagOpen in tags if "/" not in tagOpen]
    tagsCloses = [tagCloses for tagCloses in tags if "/" in tagCloses]
    for seq in html.split():
        if seq in tagsOpen:
            stck.push(seq)
        elif not stck.isEmpty() and (seq in tagsCloses) and (seq.replace('/', '') == stck.peek()):
            stck.pop()
    return stck.isEmpty()


print(check_html_balance(text))
