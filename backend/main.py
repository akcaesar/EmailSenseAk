"""
Author: Akshay NS

Contains API routes for the FastAPI application
API Routes for getting stats of the emails fetched from the user's Gmail inbox.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from components.email_df import email_df
import utilities as utilities

app = FastAPI()

origins = [
    "https://your-vercel-frontend.vercel.app",  ##My Vercel Frontend URL
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to EmailSense API!"}, status_code=200)

@app.get("/emails")
async def get_emails():
    try:
        return JSONResponse(content=email_df.to_json(orient="table"), status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": f"Error in fetching emails: {str(e)}"}, status_code=500)

@app.get("/emails/count")
async def get_emails_count():
    try:
        return JSONResponse(content={"count": utilities.get_emails_count(email_df)}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": f"Error in fetching emails count: {str(e)}"}, status_code=500)