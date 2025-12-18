# from jira import JIRA
# from django.conf import settings

# def connect_to_jira():
#     options = {'server': settings.JIRA_SERVER}
#     jira = JIRA(options, basic_auth=(settings.JIRA_USER, settings.JIRA_API_TOKEN))
#     return jira

# def create_jira_project(name, key, description):
#     jira = connect_to_jira()
#     project_data = {
#         "key": key,
#         "name": name,
#         "projectTypeKey": "software",
#         "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic",
#         "description": description,
#         "leadAccountId": jira.myself()["accountId"],
#     }
#     return jira.create_project(**project_data)











# import requests
# import json
# from django.conf import settings

# def create_jira_project(name, key, description):
#     url = f"{settings.JIRA_SERVER}/rest/api/3/project"
#     headers = {
#         "Authorization": f"Basic {settings.JIRA_API_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "key": key,
#         "name": name,
#         "projectTypeKey": "software",
#         "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic",
#         "description": description,
#         "leadAccountId": "5f6c61591204bb00700426e5"  # Replace with actual Jira account ID
#     }

#     # Send the request
#     response = requests.post(url, headers=headers, json=payload)

#     # Log response status and content
#     print(f"Jira API Status: {response.status_code}")
#     print(f"Jira API Response: {response.text}")

#     # Try to parse the response JSON
#     try:
#         return response.json()
#     except json.JSONDecodeError:
#         print("Error: Jira API did not return a JSON response.")
#         return None







import requests
import base64
from django.conf import settings

def create_jira_project(name, key, description):
    url = f"{settings.JIRA_SERVER}/rest/api/3/project"
    
    # Encode authentication using Base64
    auth_string = f"{settings.JIRA_USER}:{settings.JIRA_API_TOKEN}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_encoded}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "key": key,
        "name": name,
        "projectTypeKey": "software",
        "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic",
        "description": description,
        "leadAccountId": "5f6c61591204bb00700426e5"  # Replace with actual Jira account ID
    }

    response = requests.post(url, headers=headers, json=payload)

    print(f"Jira API Status: {response.status_code}")
    print(f"Jira API Response: {response.text}")

    return response.json() if response.status_code == 201 else None
