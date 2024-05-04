import webbrowser
from gcpq.cfg_service import config

# function to open a chrome tab with the service
def open_service(service, projectId = ""):
    try:
        url = f'https://console.cloud.google.com/{service}?project={projectId}'
        print(f'Opening {url} in browser')
        webbrowser.open_new(url)
    except:
        print("Could not open requested url")


def find_matching_services(aliases):
    services_aliases = config['services']
    all_services = []
    for alias in aliases:
        # getting custom groups
        if alias in config["groups"]:
            all_services.extend(x for x in config["groups"][alias] if x not in all_services)
        for service in services_aliases:
            if alias in service["aliases"] and service["id"] not in all_services:
                all_services.append(service["id"])

    return all_services
