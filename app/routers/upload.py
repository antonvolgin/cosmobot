import codecs
import csv
from fastapi import APIRouter, BackgroundTasks, UploadFile, File

router = APIRouter()

# https://stackoverflow.com/questions/70617121/how-to-upload-a-csv-file-in-fastapi-and-convert-it-into-json
@router.post("/upload/csv/")
def upload_csv(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file:
        return {"message": "No file sent"}
    else:
        csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        background_tasks.add_task(file.file.close)
        # return {'status': 200}
        return list(csvReader)