class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self, data):
        self.data.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for dataitem in self.data:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % dataitem['url'])
            fout.write('<td>%s</td>' % dataitem['title'])
            fout.write('<td>%s</td>' % dataitem['datetime'])
            fout.write('<td>%s</td>' % dataitem['visitcount'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()