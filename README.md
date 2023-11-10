# Simple GCP Project Project Switcher

Have you ever struggled to switch between GCP projects locally ?
Here is a simple CLI to switch between GCP projects easily.


## Requirements

GCLOUD SDK has to be installed on your machine and you have to be logged in

## Usage

If you want to list all projects before choosing one
```
pswitch
```

If you want to search for a specific term in the project name or project id

```
pswitch searchTerm
```

You will see the following output to choose your project rom:

```
$ pswitch mycompanyName
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

If you prefer ordering by name than ordering by id
```
pswitch --name
```

If you want to automatically switch to the first found project
```
pswitch searchTerm -a
```
