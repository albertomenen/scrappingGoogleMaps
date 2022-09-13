import gspread

gc = gspread.service_account(filename="credentials.json")

#Abrir por titulo 

sh= gc.open_by_key("11Mf75VD7y4IKbgsBoimSfriRthDCxKzxf1hTNPLTz-0")

worksheet = sh.sheet1


res = worksheet.get_all_records()

print(res)
