from fastapi import FastAPI, File
from fastapi.responses import FileResponse
import uvicorn
import json
import csv

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(in_file: bytes = File()):

    # Dictionary of all the stickers in the album
    stickers = {
        "FWC": list(range(0, 19)),
        "QAT": list(range(1, 20)),
        "ECU": list(range(1, 20)),
        "SEN": list(range(1, 20)),
        "NED": list(range(1, 20)),
        "ENG": list(range(1, 20)),
        "IRN": list(range(1, 20)),
        "USA": list(range(1, 20)),
        "WAL": list(range(1, 20)),
        "ARG": list(range(1, 20)),
        "KSA": list(range(1, 20)),
        "MEX": list(range(1, 20)),
        "POL": list(range(1, 20)),
        "FRA": list(range(1, 20)),
        "AUS": list(range(1, 20)),
        "DEN": list(range(1, 20)),
        "TUN": list(range(1, 20)),
        "ESP": list(range(1, 20)),
        "CRC": list(range(1, 20)),
        "GER": list(range(1, 20)),
        "JPN": list(range(1, 20)),
        "BEL": list(range(1, 20)),
        "CAN": list(range(1, 20)),
        "MAR": list(range(1, 20)),
        "CRO": list(range(1, 20)),
        "BRA": list(range(1, 20)),
        "SRB": list(range(1, 20)),
        "SUI": list(range(1, 20)),
        "CMR": list(range(1, 20)),
        "POR": list(range(1, 20)),
        "GHA": list(range(1, 20)),
        "URU": list(range(1, 20)),
        "KOR": list(range(1, 20)),
        "TL": list(range(19, 30)),
    }

    with open('stickers.csv', 'w') as missing_stickers:
        # Load the stickers json file
        collected_stickers = json.loads(in_file.decode('utf8'))

        # Sort the stickers by country
        for collected_sticker in collected_stickers['stickers']:
            country, number = collected_sticker.split()
            stickers[country].remove(int(number))

        # Write the missing stickers to a csv file
        writer = csv.writer(missing_stickers)
        for country, numbers in stickers.items():
            row = [country if country != 'TL' else 'FWC'] + numbers
            writer.writerow(row)

    return FileResponse('stickers.csv')


uvicorn.run(app, host="0.0.0.0", port=8080)
