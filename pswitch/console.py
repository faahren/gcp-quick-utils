import json, os
import subprocess
import click


def switch_project(search, orderType, auto):
    command = 'gcloud projects list --format="json(name,projectId,parent.id)"'
    if search:
        command = f'{command} --filter={search}'
    pr = subprocess.check_output(command, shell=True)
    projects = json.loads(pr)
    projects = sorted(projects, key=lambda x: x["name"])
    if auto:
        projNum = 0
    else:
        projNum = get_choice(projects, orderType)
    try:
        os.system(f'gcloud config set project "{projects[int(projNum)]["projectId"]}"')
        print(f'Successfully switched to "{projects[int(projNum)]["name"]}" ({projects[int(projNum)]["projectId"]})')
    except:
        print("No project found with this number or search term")

def get_choice(projects, orderType):
    for id, project in enumerate(projects):
        if orderType:
            print(f'[{id}] : {project["name"]} ({project["projectId"]})')
        else:
            print(f'[{id}] : {project["projectId"]} ({project["name"]})')
    return input("Enter project number to switch to: ")

@click.command()
@click.argument("search", default="", required=False)
@click.option('--name/--id', default=False, help="Will order by name instead of id")
@click.option('--auto/--choose', '-a', default=False, help="Will select the first found project and switch to it")
def main(search, name, auto):
    try:
        switch_project(search, name, auto)
    except SystemExit:
        print("Program exited")
    except KeyboardInterrupt:
        print("Program exited")