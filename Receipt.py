import lib_Help
from datetime import datetime
def head(id):
    return '''<html>
    <head>
    <meta charset="UTF-8">
    <title>{}</title>
    </head>
    <body>'''.format(id)

def tabletdcolum(title,id,date):
    return '''
    <h2 style="font-family:Tahoma">{}</h2><br>
    <table>
    <tr>
    <td style="text-align: left">Order ID   : </td>
    <td>{}</td>
    </tr>
    <tr>
    <td style="text-align: left">Order Date   : </td>
    <td>{}</td>
    </tr>
    </table>'''.format(title,id,date)

def tablefooteline():
    return '''<table>
    <tr>
    <td>------------------------------------------</td>
    </tr>
    </table>
    <table>'''


def tablebody(lists):
    num = 0
    table = ''
    total = 0
    for i in lists:
        num += 1
        table = table + '<tr>'
        table = table + '<td>{}.) {}<br></td>'.format(num, i['name'])
        table = table + '<td>&nbsp{}&nbsp<br></td>'.format(i['amount'])
        table = table + '<td style="text-align: right">&nbsp{:,.2f}&nbsp</td>'.format(float(i['price']))
        total += float(i['price'])
        table = table + '</tr>'
    table = table + '</table>'
    table = table + '''<table>
    <tr>
    <td>------------------------------------------</td>
    </tr>
    </table>
    <table>
    <tr>
    <td>TOTAL PRICE : </td>
    <td style="text-align: right">&nbsp&nbsp&nbsp&nbsp&nbsp{:,.2f}</td>'''.format(total)
    table = table + '''</tr>
    </table>
    <table>
    <tr>
    <td>------------------------------------------</td>
    </tr>
    </table>
    </table>
    </body>
    </html>'''
    return table

def createReceipt():
    title = 'Order Pizza'
    id = lib_Help.toorder[0]
    date = str(datetime.now())[:19]
    lists = lib_Help.toorder[2]

    HTML = head(id) + \
           tabletdcolum(title,id,date) + \
           tablefooteline() + \
           tablebody(lists)
    # print(HTML)
    with open("receipt/OrderID_" + str(lib_Help.toorder[0]) + ".html", mode="w", newline="", encoding="utf8") as f:
        f.write(HTML)
