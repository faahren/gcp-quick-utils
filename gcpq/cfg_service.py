# Description: This file contains the configuration related functions
import os
import sys
import yaml

def get_full_config_dir():
    home = os.path.expanduser("~")
    return f"{home}/.gcpq"

def get_config_file_path():
    return f"{get_full_config_dir()}/config.yaml"

def install_command():
    config_dir = get_full_config_dir()
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)
    
    cfg_file_path = get_config_file_path()
    if not os.path.exists(cfg_file_path):
        with open(cfg_file_path, "w") as f:
            f.write(yaml.dump({"groups":{"dwh": ["bigquery", "dataform", "storage"] }}))

def load_config():
    cfg_file_path = get_config_file_path()
    if not os.path.exists(cfg_file_path):
        install_command()
    config = yaml.load(open(cfg_file_path, "r"), Loader=yaml.SafeLoader)
    with open(f'{os.path.dirname(__file__)}/config/services.yaml', 'r') as f:
        services = yaml.load(f, Loader=yaml.SafeLoader)
    
    config["services"] = services
    return config

def add_friendly_name(project):
    cfg_file_path = get_config_file_path()
    if not os.path.exists(cfg_file_path):
        install_command()
    personal_config = yaml.load(open(cfg_file_path, "r"), Loader=yaml.SafeLoader)
    # check if key exists
    if "projects" not in config:
        personal_config["projects"] = []
    
    for proj in personal_config["projects"]:
        if proj["projectId"] == project["projectId"]:
            print("Project already exists in config - Updating")
            proj.update(project)
            with open(cfg_file_path, "w") as f:
                f.write(yaml.dump(personal_config))
            return

    personal_config["projects"].append(project)
    with open(cfg_file_path, "w") as f:
        f.write(yaml.dump(personal_config))
    return

config = load_config()