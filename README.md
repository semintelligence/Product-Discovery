# Product Search Using Linked Data 
This project is about how we can incoperate the linked data into a real-world product search engine where different seller and retialers can add thier project and based upon the query of user the revelant products be listed to the user . For this project we kept the domain of our data resticted to the Laptops.
## URL

* [http://product-search01.herokuapp.com/](http://product-search01.herokuapp.com/)
## Authors
***
* Sarika Jain 
# Data Scraping 
* The data of different laptop is collected over the internet using python.

## Data Source
***
*   [Laptop Data in CSV](https://drive.google.com/file/d/15bIXQGbJI5jvPqVc7StRdGvp-CQKa7yr/view?usp=sharing)
*   [RDF Turtle File](https://drive.google.com/file/d/1TyFVWbXpMe1yfpb0htKaamnQb3TySWFY/view?usp=sharing)

##  Libraries Used
****
* [Django](https://www.djangoproject.com/) - It is an free and Open-Source Web Development Framework in python which is used to create the backend of any application .
* [SPARQLWrapper](https://libraries.io/pypi/SPARQLWrapper) - It is an Open-Source python based library which is  used to query rdf data in python .
* [YASQE](https://github.com/pkleef/YASGUI.YASQE) - YASQE (Yet Another SPARQL Query Editor) is part of the the YASGUI suite of SPARQL tools. .
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) - It is python based library to handle html data and to get infomation out from a web page / HTML page..
* [Requests](https://pypi.org/project/requests/) - It is python based library to handle http requests.

## SPARQLWrapper
****
It is the python based library used to connect your turtle file with django backend so that we can query the data inside the triple using python .

### Sample Code
```python 
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    "http://vocabs.ardc.edu.au/repository/api/sparql/"
    "csiro_international-chronostratigraphic-chart_geologic-time-scale-2020"
)
sparql.setReturnFormat(JSON)

# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
sparql.setQuery("""
    PREFIX gts: <http://resource.geosciml.org/ontology/timescale/gts#>

    SELECT *
    WHERE {
        ?a a gts:Age .
    }
    ORDER BY ?a
    LIMIT 3
    """
)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)

```




## Sparql 
Few examples of the sparql queries that we have used in our project are - 
1. All the laptops that are silver in color and are of brand acer .
```
PREFIX pro: <http://purl.org/hpi/patchr#>
PREFIX pr: <http://purl.org/ontology/prv/core#>
PREFIX schema: <http://schema.org/>
PREFIX eeo: <https://github.com/semintelligence/Product-Discovery/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT  ?brandname ?series ?color ?processorName ?VendorName ?ramsize ?ramType ?storage
WHERE{    
        ?product eeo:hasBrand ?brand;
                 eeo:hasVendor ?PS ; 
                 eeo:hasTitle ?title .
        ?brand eeo:hasBrandName ?brandname .
        ?device rdfs:subClassOf ?product ;
                eeo:hasSeries ?series ;
                eeo:color     ?color ;
                eeo:ModelNumber ?modelNumber;
                eeo:hasProcessor ?processor ;
                eeo:hasMemory ?memory .
        ?ram rdfs:subClassOf ?memory ;
             a eeo:PrimaryMemory;
             eeo:hasRAMSize ?ramsize ;
             eeo:hasRAMType ?ramType .
        ?SecondaryStorage rdfs:subClassOf ?memory;
                          eeo:hasSMSize ?storage .
        ?processor eeo:ProcessorName ?processorName.
        ?PS eeo:hasVendorDetials ?VendorDetails ;
            eeo:hasVendorProductDetials ?VendorProductDeatils .
        ?VendorDetails eeo:hasName ?VendorName .
        ?VendorProductDeatils eeo:hasVendorProductPrice ?price ;
                           	  eeo:hasProductProductQuantity ?stock .
  		filter contains(?color , "Silver")
		filter contains(?brandname , "acer")  			
}
```
![App Screenshot](https://i.imgur.com/z8cx5qY.png)
2. All the laptops sold by Retailer Ret1 - 
```
PREFIX pro: <http://purl.org/hpi/patchr#>
PREFIX pr: <http://purl.org/ontology/prv/core#>
PREFIX schema: <http://schema.org/>
PREFIX eeo: <https://github.com/semintelligence/Product-Discovery/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT  ?brandname ?series ?color ?processorName ?VendorName ?ramsize ?ramType ?storage
WHERE{    
        ?product eeo:hasBrand ?brand;
                 eeo:hasVendor ?PS ; 
                 eeo:hasTitle ?title .
        ?brand eeo:hasBrandName ?brandname .
        ?device rdfs:subClassOf ?product ;
                eeo:hasSeries ?series ;
                eeo:color     ?color ;
                eeo:ModelNumber ?modelNumber;
                eeo:hasProcessor ?processor ;
                eeo:hasMemory ?memory .
        ?ram rdfs:subClassOf ?memory ;
             a eeo:PrimaryMemory;
             eeo:hasRAMSize ?ramsize ;
             eeo:hasRAMType ?ramType .
        ?SecondaryStorage rdfs:subClassOf ?memory;
                          eeo:hasSMSize ?storage .
        ?processor eeo:ProcessorName ?processorName.
        ?PS eeo:hasVendorDetials ?VendorDetails ;
            eeo:hasVendorProductDetials ?VendorProductDeatils .
        ?VendorDetails eeo:hasName ?VendorName .
        ?VendorProductDeatils eeo:hasVendorProductPrice ?price ;
                           	  eeo:hasProductProductQuantity ?stock .
  		filter contains(?color , "Silver")
        filter (?VendorName = "Ret1")		
}
```
![Query Result ](https://i.imgur.com/7qTdg4M.png)
## Environment Variables
To run this project, you will need to add the following environment variables to your .env file
- SECRET_KEY= Secret key of your django project


## Run The Project Locally 
Clone the project

```bash
  git clone https://github.com/semintelligence/Product-Discovery
```

Go to the project directory

```bash
  cd 120-years-olympics
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

## Contacts
### Dr. Sarika Jain  (National Institute of Technology, Kurukshetra, India ) 
-  Email - jasarika@nitkkr.ac.in
