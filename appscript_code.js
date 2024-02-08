function _onTrigger() {
  const response = UrlFetchApp.fetch("https://raw.githubusercontent.com/styrix560/captions/main/data.json")
  const rawData = response.getContentText();
  const data = JSON.parse(rawData);

  const percentages = data["percentages"];
  putDataIntoSheet("Percentages", percentages);
  
  const contributors = data["contributors"];
  putDataIntoSheet("Contributors", contributors);
}

/**
 * Takes data and puts it into the sheet with the specified name starting at cell A1. The data has to be a two dimensional array.
 * @param {string} sheetName - The name of the sheet.
 * @param {string[][]} author - The data to be written.
 */
function putDataIntoSheet(sheetName, data) {
  if (data.length == 0) return;

  const maxRowLength = Math.max(...data.map(row => row.length));

  const paddedData = data.map((row) => {
    while (row.length < maxRowLength) {
      row.push("");
    }
    return row
  }); // data filled with empty cells to become rectangular

  // write to sheet
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  const range = sheet.getRange(1, 1, data.length, maxRowLength);
  range.setValues(paddedData);
}
