import gspread
import csv


gc = gspread.service_account(filename='credentials.json')
sh = gc.open("SWE Test")
worksheet = sh.sheet1


def get_all_rows():
    return worksheet.get_all_values()

def import_csv():
    rows = get_all_rows()
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows) 

def insert_row(row):
    worksheet.append_row(row)


if __name__ == "__main__":
    import_csv()