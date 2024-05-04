import click

def get_choice(projects):
    for id, project in enumerate(projects):
        name = click.style(project["name"], fg='blue')
        base = click.style(f'[{id}] : {project["projectId"]} ({name})')
        if "friendly_name" in project:
            friendly = click.style(f"Friendly Name: {project['friendly_name']}", fg='green')
            base = f"{base} - {friendly}"
        click.echo(base)

    return input("Enter project number: ")