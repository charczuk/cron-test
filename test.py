from datetime import datetime
import csv
#today = datetime.now()
with open('output.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting = csv.QUOTE_MINIMAL)
    filewriter.writerow(['Last time run:', datetime.now()])



