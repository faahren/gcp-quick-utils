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
[0] : mycompany-terraformtests (mycompany-terraform)
[1] : mycompany-etl (mycompany-etl)
[2] : mycompany-guillaume-pde (mycompany-guillaume-pde)
[3] : mycompany-chatbot (mycompany-chatbot)
[4] : mycompany-ga4 (mycompany-ga4-lehoublon-flo)
[5] : mycompany-airbyte (mycompany-airbyte)
[6] : mycompany-n8n (mycompany-n8n)
[7] : mycompany (mycompany-380132)
Enter project number to switch to: 
```