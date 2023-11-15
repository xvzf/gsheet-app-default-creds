from googleapiclient.discovery import build

def main():
    service = build("sheets", "v4")
    spreadsheet = {"properties": {"title": "Hello world"}}
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
    )
    print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
    return spreadsheet.get("spreadsheetId")


if __name__ == "__main__":
  main()

