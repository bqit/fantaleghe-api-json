import pandas as panda
import requests
import json
import os

url = "https://www.fantacalcio.it/api/v1/Excel/prices/21/1"
excelFile = "players.xlsx"
jsonFile = "players.json"

def downloadExcel():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.fantacalcio.it/quotazioni-fantacalcio',
        'Cookie': os.getenv('COOKIE')
    }
    response = requests.get(url, headers = headers)
    
    if response.status_code == 200:
        with open(excelFile, 'wb') as file:
            file.write(response.content)
            return True
    else:
        return False
    
def consumeData():
        df = panda.read_excel(excelFile, skiprows = 1)
        df = df.fillna(0)
        
        players = []
        
        for index, row in df.iterrows():
            playerId = str(row['Id'])
            
            if playerId == '0' or playerId == '0.0' or playerId == 'nan':
                continue
            
            player = {
                "id": int(float(playerId)),
                "name": str(row['Nome']),
                "position": str(row['R']),
                "team": str(row['Squadra']),
                "qt_att": int(row["Qt.A"]),
                "qt_i": int(row["Qt.I"]),
                "diff": int(row["Diff."]),
                "qt_att_m": int(row["Qt.A M"]),
                "qt_i_m": int(row["Qt.I M"]),
                "diff_m": int(row["Diff.M"]),
                "fvm": int(row["FVM"]),
                "fvm_m": int(row["FVM M"]),
                "playerImage": f"https://content.fantacalcio.it/web/campioncini/21/medium/{int(float(playerId))}.png?v=640"
            }
            
            players.append(player)
            
        with open(jsonFile, 'w', encoding = 'utf-8') as file:
            json.dump(players, file, ensure_ascii = False, indent = 4)
    
if __name__ == "__main__":
    if downloadExcel():
        consumeData()
        
        if os.path.exists(excelFile):
            os.remove(excelFile)