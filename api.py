from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
import io
import jira_api as jira
import base64tofile as base64
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://broocode.github.io/jira-create-issue/home", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the path to your static directory
static_path = Path(__file__).parent / "static"

@app.post("/jira_create_issue")
async def form_post(request: Request):
    req_info = await request.json()
    summary = req_info["summary"]
    discription = req_info["description"]
    priority = req_info["priority"]
    if req_info["ext"] == "":
        ext = "nothing"
    else:
        ext = req_info["ext"]
        base64.convert(req_info["ext"], req_info["file"])
    jira.create_issue(summary, discription, priority, ext)
    return "Issue created successfully!"

@app.get("/jira_create_issue")
async def form_get(request: Request):
    return "Opps Use POST to create an issue!"

# Serve the home.html file
@app.get("/")
async def get_home_page():
    home_html = static_path / "home.html"
    return FileResponse(home_html)

@app.post("/demo")
async def form_post(request: Request):
    req_info = await request.json()
    if req_info["ext"] == "":
        ext = "nothing"
    else:
        ext = req_info["ext"]
    print(ext)
    base64.convert(ext, req_info["file"])
    return req_info
