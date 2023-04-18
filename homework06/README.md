# Say It Ain't Genes - Homework 06

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
 

### What are the Different Queries and Their Results?

In this python script, there are five different routes you can experiment with.

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
>  "HGNC:38032",
>  "HGNC:25820",
>  "HGNC:13200",
>  "HGNC:51695",
>  "HGNC:29027",
>  "HGNC:24523"
> ] 

5. Let's say out of that list, you wanted to see all the information for HGNC:24523.
Well, you would input this:

``curl localhost:5000/genes/HGNC:24523``

This will return the key data for HGNC:24523!

> "hgnc_id": "HGNC:24523",
>  "location": "1p31.1",
>  "location_sortable": "01p31.1",
>  "locus_group": "protein-coding gene",
>  "locus_type": "gene with protein product",
>  "mane_select": [
>    "ENST00000370801.8",
>    "NM_015534.6"
>  ],
>  "mgd_id": [
>    "MGI:1920453"
>  ],
>  "name": "zinc finger ZZ-type containing 3",
>  "omim_id": [
>    "619892"
>  ],
>  "pubmed_id": [
>    16428443,
>    21304275
>  ],
>  "refseq_accession": [
>    "NM_015534"
>  ],
>  "rgd_id": [
>    "RGD:1565468"
>  ],
>  "status": "Approved",
>  "symbol": "ZZZ3",
>  "ucsc_id": "uc001dhq.4",
>  "uniprot_ids": [
>    "Q8IYH5"
>  ],
>  "uuid": "1d5bbcb9-60fe-4686-b543-69375a16e33f",
>  "vega_id": "OTTHUMG00000009652"
> }





