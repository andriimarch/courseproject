import pytest
from methods.task_methods import *

def test_get_team_id():
    team_id = get_team_id()
    assert team_id is not None

def test_get_first_space_id():
    team_id = get_team_id()
    # Перевіряємо чи є простори, щоб не було IndexError
    spaces = get_spaces().get('spaces', [])
    if not spaces:
        pytest.skip("No spaces found, skipping test")
    space_id = get_first_space_id(team_id)
    assert space_id is not None

def test_create_space():
    space = create_space()
    assert 'id' in space

def test_get_spaces():
    spaces = get_spaces()
    assert 'spaces' in spaces
    assert isinstance(spaces['spaces'], list)

def test_create_folder():
    team_id = get_team_id()
    spaces = get_spaces().get('spaces', [])
    if not spaces:
        pytest.skip("No spaces available for folder creation")
    folder = create_folder()
    assert 'id' in folder

def test_get_folders():
    team_id = get_team_id()
    spaces = get_spaces().get('spaces', [])
    if not spaces:
        pytest.skip("No spaces available to get folders")
    folders = get_folders()
    assert 'folders' in folders
    assert isinstance(folders['folders'], list)

def test_create_list():
    folders = get_folders().get('folders', [])
    if not folders:
        pytest.skip("No folders available for list creation")
    folder_id = folders[0]['id']
    new_list = create_list(folder_id)
    assert 'id' in new_list

def test_get_lists():
    folders = get_folders().get('folders', [])
    if not folders:
        pytest.skip("No folders available to get lists")
    folder_id = folders[0]['id']
    lists = get_lists(folder_id)
    assert 'lists' in lists
    assert isinstance(lists['lists'], list)

def test_create_task():
    folders = get_folders().get('folders', [])
    if not folders:
        pytest.skip("No folders available for task creation")
    folder_id = folders[0]['id']

    lists = get_lists(folder_id).get('lists', [])
    if not lists:
        pytest.skip("No lists available for task creation")
    list_id = lists[0]['id']

    task = create_task(list_id, "Test Task", "Test Description")
    assert 'id' in task

def test_get_tasks():
    folders = get_folders().get('folders', [])
    if not folders:
        pytest.skip("No folders available to get tasks")
    folder_id = folders[0]['id']

    lists = get_lists(folder_id).get('lists', [])
    if not lists:
        pytest.skip("No lists available to get tasks")
    list_id = lists[0]['id']

    tasks = get_tasks(list_id)
    assert 'tasks' in tasks
    assert isinstance(tasks['tasks'], list)


