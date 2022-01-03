'''
    csv 읽고 쓰기
'''

import csv


def passwd_to_csv():

    with open('/etc/passwd') as passwd, open('passwd.csv', 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')

        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


if __name__ == '__main__':

    passwd_to_csv()
