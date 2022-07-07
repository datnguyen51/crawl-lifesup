import csv
from time import sleep


def write_data(timkiem, URL_all):
    STT = 0
    with open('data/' + timkiem + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['STT', 'link post']
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()
        for url in URL_all:
            STT += 1
            print(STT, url)
            thewriter.writerow({'STT': STT, 'link post': url})

    a = "\n"
    print(a.join(URL_all))
    sleep(5)
