import click

import gcpq.console_utils as console_utils
import gcpq.gcp_cli_service as gcp_cli_service
import gcpq.gcp_sections_service as gcp_sections_service
from gcpq.cfg_service import config, add_friendly_name


def switch_command(search, auto):
    projects_from_friendly = [x for x in config["projects"] if search.lower() in x["friendly_name"].lower()]
    projects = gcp_cli_service.get_projects(search, projects_from_friendly)
    if not projects:
        print("No projects found")
        return
    if auto:
        projNum = 0
    else:
        projNum = console_utils.get_choice(projects)
    gcp_cli_service.switch_project(projects[int(projNum)]["projectId"])



def open_service_command(services, search, auto, force):
    if not search and not force:
        projectId = gcp_cli_service.get_current_project_id()
    else:
        projects_from_friendly = [x for x in config["projects"] if search.lower() in x["friendly_name"].lower()]
        projects = gcp_cli_service.get_projects(search, projects_from_friendly)

        if not projects:
            print("No projects found")
            return

        if auto:
            projNum = 0
        else:
            projNum = console_utils.get_choice(projects)

        projectId = projects[int(projNum)]["projectId"]

    for service in services:
        gcp_sections_service.open_service(service, projectId)
    return


def add_friendly_name_command(search):
    projects = gcp_cli_service.get_projects(search)

    if not projects:
        print("No projects found")
        return
    projNum = console_utils.get_choice(projects)
    project = projects[int(projNum)]

    friendly_name = input("Enter friendly name for project: ")
    project["friendly_name"] = friendly_name

    add_friendly_name(project)

    return


@click.command()
@click.argument("command", default="", required=False)
@click.argument("search", default="", required=False)
@click.option('--auto/--choose', '-a', default=False, help="Will select the first found project")
@click.option('--force/--noforce', '-f', default=False, help="Will force the project search even with an empty search string")
def main(command, search, auto, force):
    
    gcp_cli_service.check_if_gcloud_is_installed()
    try:
        if command == "a":
            add_friendly_name_command(search)
            return

        if command == "s":
            switch_command(search, auto)
            return

        services = gcp_sections_service.find_matching_services(command.split(","))
        if services:
            open_service_command(services, search, auto, force)
            return

    except SystemExit:
        print("Program exited")
    except KeyboardInterrupt:
        print("Program exited")

    print("Invalid command, please use 's' to switch projects or any service name to open it in the browser")

if __name__ == "__main__":
    main()