# Google Cloud Platform CLI Utils

Have you ever struggled to switch between GCP projects locally ?
Are you constantly struggling with the interface of GCP when you want to switch between services and projects ?
Here is a simple CLI to simplify your daily life



## Requirements

GCLOUD SDK has to be installed on your machine and you have to be logged in

## Usage

### Switch between projects
If you want to list all projects before choosing one
```
gcpq s
```

If you want to search for a specific term in the project name or project id

```
gcpq s searchTerm
```

You will see the following output to choose your project rom:

```
$ gcpq mycompanyName
[0] : mycompany-380102 (mycompany)
[1] : mycompany-airbyte (mycompany-airbyte)
[2] : mycompany-chatbot (mycompany-chatbot)
[3] : mycompany-etl (mycompany-etl)
[4] : mycompany-ga4-lehoublon-flo (mycompany-ga4-lehoublon-flo)
[5] : mycompany-guillaume-pde (mycompany-guillaume-pde)
[6] : mycompany-n8n (mycompany-n8n)
[7] : mycompany-terraform (mycompany-terraform)
Enter project number to switch to: 
```

If you want to automatically switch to the first found project
```
gcpq searchTerm -a
```

### Opening Google Cloud Interface quickly

If you want to open a service quickly. When you don't specify projects, the current Gcloud set project will be used

```
gcpq bq
```

Open multiple services at the same time

```
gcpq bq,dataform,iam,build,gcs
```

Aliased have been created for the services. You can see them in the `services.yaml` file of the repo


Open services on a specific project (you will be able to choose the project matching the search result)

```
gcpq bq myCompanyName
```

Open services on a specific project automatically (Will open the first found project)

```
gcpq bq myCompanyName -a 
```

Create shortcuts of groups of services
- Open your config file located in `~/.gcpq/config.yaml`
- Add new groups of services in the file (follow current structure)


```
gcpq myGroupName 
```



# Modifying GCPQ

If you need to modify the package, you can test your modifications with poetry run gcpq

```
poetry run gcpq bq
```