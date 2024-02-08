function _onTrigger() {
  const response = UrlFetchApp.fetch("https://raw.githubusercontent.com/styrix560/captions/main/data.json")
  const rawData = response.getContentText();
  const data = JSON.parse(rawData);

  if (data.length == 0) return;

  const maxRowLength = Math.max(...data.map(row => row.length));

  const paddedData = data.map((row) => {
    while (row.length < maxRowLength) {
      row.push("");
    }
    return row
  }); // data filled with empty cells to become rectangular

  // write to sheet
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const range = sheet.getRange(1, 1, data.length, maxRowLength);
  range.setValues(paddedData);
}
