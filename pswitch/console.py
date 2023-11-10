import sys, json, os
import subprocess


def switch_project():
    try:
        search = sys.argv[1]    
    except:
        search = ""
    pr = subprocess.check_output(f'gcloud projects list --filter={search} --format="json(name,projectId,parent.id)"', shell=True)
    projects = json.loads(pr)
    for id, project in enumerate(projects):
        print(f'[{id}] : {project["name"]} ({project["projectId"]})')
    projNum = input("Enter project number to switch to: ")
    try:
        os.system(f'gcloud config set project "{projects[int(projNum)]["projectId"]}"')
    except:
        print("Invalid Project Number")

def main():
    try:
        switch_project()
    except SystemExit:
        print("Program exited")
    except KeyboardInterrupt:
        print("Program exited")