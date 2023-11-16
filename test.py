from googleapiclient.discovery import build

def main():
    service = build("sheets", "v4")
    spreadsheet = {"properties": {"title": "My beloved sheet"}}
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
    )
    spreadsheet_id = spreadsheet.get("spreadsheetId")
    body = {"valueInputOption": "USER_ENTERED", "data": [{"range": "A1:C2", "majorDimension": "ROWS", "values": [["Hello", "World", "!"], ["Python", "is", "Fun"]]}]}

    res = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
    print(res)

if __name__ == "__main__":
  main()

