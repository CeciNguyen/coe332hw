# Say It Ain't Genes, but in Kubernetes and an image! - Homework 08

## Gene Party: Parsing the HGNC Data Set
This project features a single script that utilizes Flask to create an application with diverse routes, providing users with distinct information pieces about the HGNC data obtained from HUGO. To ease accessibility, the project also includes a Dockerfile enabling users to retrieve and run the image on their personal machines, as well as a Docker-compose file that streamlines the container's launch process.

The significance of the Flask application routes lies in the extensive amount of data contained within HGNC, which could be overwhelming to the user. The routes streamline the process of obtaining targeted information, minimizing the need for manual data sifting. Furthermore, the application employs Redis database capabilities, enabling users to conveniently store and revisit data.

The Dockerfile adds to the user experience by providing easy accessibility to the application and its features. The Docker-compose file further simplifies the process by automating deployment, allowing the container to launch seamlessly.

## The Data
The datas set, the HGNC complete set achrive, can be directly accessed from the [HGNC
website](https://www.genenames.org/download/archive/). The specific data set used in
this homework set was a [JSON based library](https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc\_complete\_set.json).

What exactly can you expect from this data?
According to the archive, there are two main types of data files pertaining to HGNC (excluding file format distinctions): hgnc_complete_set and withdraw. The hgnc_complete_set is a comprehensive collection of approved gene symbol reports sourced from both the GRCh38 reference and alternative reference loci. For the purposes of this homework, the current HGNC complete set fil in JSON format was explored. Within the data set, the user is able to interface with different found genes and its locations.

## The Flask Application and How to Access it 
### What is it?

The Flask application is written in the python script "gene_api.py". It is mainly used for querying the differen HGNC IDs through the various app routes! 

### How do you access it?

In order to run the application:

1. Log into your vm in two seperate command line windows using: ``username-vm``
2. Pull the data from the repository
3. Then in one of the windows build and run the Redis and Flask debugger server:
``docker-compose up --build``
4. Once the server is running, you can start inputting the different queries in the other window you logged into
5. To run the queries, you muse use the command:
``curl localhost:5000``

Note, that in order to run the script you must have the docker files ready to go! 
So, how exactly do you so that?

## The Docker Image and How to Access it
### What is it?

Docker is a containerization platform that can package software called containers for
others to use! The Dockerfile included in the repository helps to build the docker
image that was used for gene_api.py.

### How do you access it? 

In order to obtain the container and run the docker image, there are two ways!

If you would like to just obtain the Docker Image and run the code:
1. pull the docker image in your vm with the handle:
``docker pull dcn558/gene_api:1.0`` 
2. run the image in seperate vm window with the command: 
``docker run -it --rm -p 5000:5000 dcn558/gene_api:1.0``
3. run the different routes

If you would like to start from the Dockerfile and build your own image:
1. clone the repository to obtain the Dockerfile and the python script in one vm
window
2. create your own docker hub account
3. once you modify the code or make your own code, you can build your own image
using:
``docker build -t <dockerhubusername>/gene_api:<version>`` 
4. then to check if you have created your image run the line: ``docker images``
5. then to test your image, open another vm window and type the command:
``docker run -it --rm -p 5000:5000 username/gene_api:<version>``
6. now you can interface with the container and the code in the other vm window!
 
## Kubernetes and How to Use it

Kubernetes is a container orchestration platform that automates the deployment, scaling, and management of containerized applications. While Kubernetes itself is not specific to Python coding, Python developers can use Kubernetes to deploy and manage their Python applications that have been containerized using tools like Docker.

Python developers can interact with Kubernetes using the Kubernetes Python client, which provides an API for Python programs to access Kubernetes resources like pods, services, and deployments. This allows Python developers to programmatically manage their Kubernetes infrastructure and automate tasks such as scaling up or down the number of replicas of a deployment, rolling out new versions of an application, or monitoring the health of their application in the cluster.

1. Clone the repository and follow the instructions above to pull the image.
2. Check the Kubernetes file and ensure no changes are needed. However, you may need to modify the host of the Redis client in the Python script.
3. Use the command "kubectl get services" to obtain the IP address of your Redis service. Replace the current host in the Python script with this new IP address.
4. Once you've made the necessary changes to the Python script, use the instructions provided above to build a new Docker image from the Dockerfile.

## The Image: How do You Pull it and Run it?
To install the project, begin by cloning the repository.

Next, pull a copy of the container using the command "docker pull avlavelle/gene_api". Then, execute "docker-compose up --build" to launch the container with the compose file, build the image, and map the appropriate port inside the container to the corresponding port on the host.

To interact with the routes, open a new terminal window and use the "curl localhost:5000/<route>" command. This will allow you to easily access the desired routes and perform the necessary actions.

## The Image Route

The route helps to read the date of each gene entry of when they were first approved form the database, tabulates how many genes were approved each year, an then creates a bar graph of the data, which it writes into anouther database.

The default GET request for the route allows users to retrieve a plot image from the server. To use this route, the user must provide a name for their plot image when calling the route using the "curl" command. For example, executing the command ``curl localhost:5000/image>>myimage.png`` will create a new plot image named "myimage.png" and make it available in the repository on the VM.

To view the plot image, two scp actions are required. These actions allow the user to securely transfer the image from the server to their local machine. Once the transfer is complete, the user can view the image using their preferred image viewer or editor.

Within your the virtual machine (VM)

``scp ./ <image_name.png> username@address.edu:./``

You should then recieve a confirmation!

After you recieve the confirmation, you can input your local machine: 

``scp username@address.edu:./<image_name.png> ./``

The computer should return confirmation ffor the scp, and you should be able to access the plot image from their file explorer.

## What are the Different Queries and Their Results?

In this python script, there are eight different routes you can experiment with.

1. If you would like to retrieve the data int a Redis database:

``curl localhost:5000/data -X POST`` 

This will give you a messaage that says:

> data loaded

If you recieve this message, it means it has properly retrieved all the data and you are good to interface with it. It does take a while but that is because it is a larger data set so, do not worry!

2. If you would like to return all the data from Redis

``curl localhost:5000/data``

This will return the whole entire data base to you.

3. If you would like to delete the data:

``curl localhost:5000/data``

This will give you a messaage that says:

> data deleted


4. If you would like to see all of the possible HGNC IDs that you can look into:

``curl localhost:5000/genes``

This will return a list with all the HGNC IDs that are in the data set.
Your output may look something like this:

>  "HGNC:32058",
>
>  "HGNC:38032",
>
>  "HGNC:25820",
>
>  "HGNC:13200",
>
>  "HGNC:51695",
>
>  "HGNC:29027",
>
>  "HGNC:24523"
>
> ] 

5. Let's say out of that list, you wanted to see all the information for HGNC:24523.
Well, you would input this:

``curl localhost:5000/genes/HGNC:24523``

This will return the key data for HGNC:24523!

> "hgnc_id": "HGNC:24523",
>
>  "location": "1p31.1",
>
>  "location_sortable": "01p31.1",
>
>  "locus_group": "protein-coding gene",
>
>  "locus_type": "gene with protein product",
>
>  "mane_select": [
>
>    "ENST00000370801.8",
>
>    "NM_015534.6"
>
>  ],
>
>  "mgd_id": [
>
>    "MGI:1920453"
>
>  ],
>
>  "name": "zinc finger ZZ-type containing 3",
>
>  "omim_id": [
>
>    "619892"
>
>  ],
>
>  "pubmed_id": [
>
>    16428443,
>
>    21304275
>
>  ],
>
>  "refseq_accession": [
>
>    "NM_015534"
>
>  ],
>
>  "rgd_id": [
>
>    "RGD:1565468"
>
>  ],
>
>  "status": "Approved",
>
>  "symbol": "ZZZ3",
>
>  "ucsc_id": "uc001dhq.4",
>
>  "uniprot_ids": [
>
>    "Q8IYH5"
>
>  ],
>
>  "uuid": "1d5bbcb9-60fe-4686-b543-69375a16e33f",
>
>  "vega_id": "OTTHUMG00000009652"
>
> }

6. If you would like to create the plot image and load it into the Redis

``curl localhost:5000/image -X POST"``

This will give you a message:

> Image created

7. If you want to retrieve the plot:

Follow the instrustions above and this return will not return a visible result.

8. If you would like to remove the image:

``curl localhost:5000/image -X DELETE``

This will return a confirmation message:

> Image deleted, there are 0 keys in the db

