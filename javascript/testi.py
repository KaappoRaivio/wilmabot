import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('NoSocksForYou', '181ecbfe6f3f5216063b74c7d6bbdcc6')

    client.setOrientation('landscape')
    client.setNoMargins(True)

    # run the conversion and write the result to a file
    client.convertStringToFile(open('/home/kaappo/git/wilmabot/temp.html', 'r').read(), 'HelloWorld.pdf')
except pdfcrowd.Error as why:
    # report the error to the standard error stream
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
