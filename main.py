"""
Author: Akshay NS

Contains API routes for the FastAPI application
API Routes for getting stats of the emails fetched from the user's Gmail inbox.


"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
from EmailSense_cp.components.email_df import email_df
import utilities

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/emails")
async def get_emails():
    try:
        return JSONResponse(content=email_df.to_json(orient="table"), status_code=200)
    except:
        return JSONResponse(content={"message": "Error in fetching emails"}, status_code=500)


@app.get("/emails/count")
async def get_emails_count():
    try:
        return JSONResponse(content={"count": utilities.get_emails_count(email_df)}, status_code=200)
    except:
        return JSONResponse(content={"message": "Error in fetching emails count"}, status_code=500)


    