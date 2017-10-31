class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def out_html(self):
        with open('output.html', 'w') as fout:

            fout.write("<html>")
            fout.write("<body>")
            fout.write("<table>")

            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>{}</td>".format(data['url']))
                fout.write("<td>{}</td>".format(data['title']))
                fout.write("<td>{}</td>".format(data['summary']))
                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")
            fout.write("</title>")
