# Description: This file contains the functions to interact with GCP projects through the CLI
import os
import subprocess
import json

def get_projects(search):
    command = 'gcloud projects list --format="json(name,projectId,parent.id)"'
    if search:
        command = f'{command} --filter={search}'
    pr = subprocess.check_output(command, shell=True)
    projects = json.loads(pr)
    projects = sorted(projects, key=lambda x: x["name"])
    return projects

def get_current_project_id():
    try:
        pr = subprocess.check_output('gcloud config get-value project', shell=True)
        return pr.decode("utf-8").strip()
    except:
        return None
    
def check_if_gcloud_is_installed():
    try:
        subprocess.check_output("gcloud --version", shell=True)
    except:
        print("Gcloud is not installed, please install it first")
        exit()

def switch_project(projectId):
    try:
        os.system(f'gcloud config set project "{projectId}"')
        print(f'Successfully switched to "{projectId})')
    except:
        print("Error while switching project")
    return True