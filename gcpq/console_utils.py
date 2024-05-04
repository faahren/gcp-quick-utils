def get_choice(projects):
    for id, project in enumerate(projects):
        print(f'[{id}] : {project["projectId"]} ({project["name"]})')
    return input("Enter project number: ")