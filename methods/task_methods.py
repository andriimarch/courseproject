import requests
from faker import Faker

fake = Faker()

HEADERS = {
    "Authorization": "pk_188648872_RAUMQD7FOHL5JHKE26AJOWM65XQAFH0M",
    "Content-Type": "application/json"
}

API_BASE = "https://api.clickup.com/api/v2"

def get_team_id():
    response = requests.get(f"{API_BASE}/team", headers=HEADERS)
    response.raise_for_status()
    return response.json()['teams'][0]['id']

def get_first_space_id(team_id):
    response = requests.get(f"{API_BASE}/team/{team_id}/space", headers=HEADERS)
    response.raise_for_status()
    return response.json()['spaces'][0]['id']

def create_space():
    team_id = get_team_id()
    random_space_name = fake.name()
    body = {
        "name": random_space_name
    }
    response = requests.post(f"{API_BASE}/team/{team_id}/space", headers=HEADERS, json=body)
    return response.json()

def get_spaces():
    team_id = get_team_id()
    response = requests.get(f"{API_BASE}/team/{team_id}/space", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_folder():
    team_id = get_team_id()
    space_id = get_first_space_id(team_id)
    folder_name = fake.name()
    body = {
        "name": folder_name
    }
    response = requests.post(f"{API_BASE}/space/{space_id}/folder", headers=HEADERS, json=body)
    return response.json()

def get_folders():
    team_id = get_team_id()
    space_id = get_first_space_id(team_id)
    response = requests.get(f"{API_BASE}/space/{space_id}/folder", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_list(folder_id):
    list_name = fake.word().capitalize() + " List"
    body = {
        "name": list_name
    }
    response = requests.post(f"{API_BASE}/folder/{folder_id}/list", headers=HEADERS, json=body)
    return response.json()

def get_lists(folder_id):
    response = requests.get(f"{API_BASE}/folder/{folder_id}/list", headers=HEADERS)
    response.raise_for_status()
    return response.json()

# ----------------------- POST: Create Task -----------------------
def create_task(list_id, task_name, task_description=""):
    url = f"{API_BASE}/list/{list_id}/task"
    body = {
        "name": task_name,
        "description": task_description
    }
    response = requests.post(url, headers=HEADERS, json=body)
    return response.json()

# ----------------------- GET: Get Tasks -----------------------
def get_tasks(list_id):
    url = f"{API_BASE}/list/{list_id}/task"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

