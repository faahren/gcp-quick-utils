import sys, json, os
import subprocess
search = sys.argv[1]

def main():
    pr = subprocess.check_output(f'gcloud projects list --filter={search} --format="json(name,projectId,parent.id)"', shell=True)
    projects = json.loads(pr)
    for id, project in enumerate(projects):
        print(f'[{id}]: {project["name"]} ({project["projectId"]})')
    projNum = input("Enter project number to switch to: ")
    os.system(f'gcloud config set project "{projects[int(projNum)]["projectId"]}"')
