"""
to get started run "python -m uvicorn main:app --reload --port 8000" in the terminal
"""


from typing import Union

from fastapi import FastAPI, HTTPException

import ReadFromDB as DB

app = FastAPI()

@app.get("/")
def read_root():
    return "QM Extractor is live! 🤘 V(🤷‍♀️ not prod) visit '/docs' endpoint for valid routes"

@app.get("/getAll/{file_name}")
def get_all_data_in_file(file_name: str):
    data = DB.getAllRecords(file_name)
    if data == {}:
         raise HTTPException(status_code=404, detail="File not found")
    else:
        return data
    
@app.get("/get/{file_name}")
def get_file(file_name: str, Id: str):
    data = DB.getARecord(file_name, Id)
    if data == {Id: {}}:
         raise HTTPException(status_code=404, detail="File not found")
    else:
        return data