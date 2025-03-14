"""
Author: Akshay NS

Contains API routes for the FastAPI application
API Routes for getting stats of the emails fetched from the user's Gmail inbox.


"""

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from components.pandas_df import email_df
import utilities

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/emails/count")
async def get_emails_count():
    len = utilities.get_emails_count(email_df)
    return len
    