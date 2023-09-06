import requests
import json,os

def create_issue(summary,discription,priority,ext):
    
    priority = priority[0] + priority[1:].lower()
    with open("config.json", "r") as f:
        config = json.load(f)

    token = config.get("token")
    id = config.get("username")
    jira_url = config.get("jira_url")

    #company authentication credentials
    JIRA_URL = jira_url
    USERNAME = id
    API_TOKEN = token

    # Construct the API endpoint URL for creating issues
    CREATE_ISSUE_API = f"{JIRA_URL}/rest/api/3/issue/"

    headers = {
        "X-Atlassian-Token": "no-check",  # Disable CSRF token check for attachments
    }

    issue_data2 = {
        "fields": {
            "project": {
                "id": "10233"
            },
            "issuetype": {
                "id": "10004"
            },
            "summary": summary,
            "description": {
                "version": 1,
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": discription
                            }
                        ]
                    }
                ]
            },
            "priority": {
                "id": "3",
                "name": priority,
                "iconUrl": "https://tatadigital.atlassian.net/images/icons/priorities/medium.svg"
            },
            "fixVersions": [
                {
                    "id": "10962"
                }
            ],
            "components": [
                {
                    "id": "12354",
                    "name": "Brand - Westside"
                }
            ],
            "customfield_10040": {
                "id": "10036",
                "value": "Functional"
            },
            "customfield_10061": {
                "id": "10880",
                "value": "CFT"
            },
            "customfield_10102": {
                "id": "10962"
            },
            "customfield_10100": {
                "id": "10406",
                "value": "Android",
                "child": {
                    "id": "10913",
                    "value": "Samsung Galaxy S21 FE"
                }
            },
            "customfield_10086": "NA",
            "customfield_10096": [
                {
                    "id": "10305",
                    "value": "Android 12.0"
                }
            ],
            "customfield_10093": [],
            "customfield_10097": [
                "CFT_4.0.0"
            ]
        },
        "update": {}
    }

    # Make the API request to create the issue
    response = requests.post(
        CREATE_ISSUE_API,
        headers=headers,
        auth=(USERNAME, API_TOKEN),
        json=issue_data2
    )

    # Check the API response
    if ext!="nothing":
        if response.status_code == 201:
            filename = "issue"+ext
            print("Issue created successfully.")
            issue_key = response.json()["key"]
            print(f"Issue key: {issue_key}")

            # Attach the file to the created issue
            attachment_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/attachments"
            files = {'file': (filename, open(filename, 'rb'))}
            
            attachment_response = requests.post(
                attachment_url,
                headers=headers,
                auth=(USERNAME, API_TOKEN),
                files=files
            )
            
            if attachment_response.status_code == 200:
                print("Attachment added successfully.")
            else:
                print("Attachment addition failed.")
            os.remove(filename)
    
        else:
            print("Issue creation failed.")
            print("Response:", response.text)
    else:
        print("Nothing to upload")

