import xlsxwriter
from scraping_func import array


"""
    def write_to_excel(parametr)
    Takes a generator as input and writes extracted book data into an Excel file.
"""

def write_to_excel(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\momen\Desktop\our_file.xlsx")
    page = book.add_worksheet("item")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)
    page.set_column("E:E", 50)


    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])

        row += 1

    book.close()

write_to_excel(array)