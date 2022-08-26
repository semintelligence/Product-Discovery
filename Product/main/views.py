from django.shortcuts import render
from django.http import HttpResponse
from SPARQLWrapper import SPARQLWrapper, JSON
import numpy as np
import urllib.parse

# Create your views here.

def main(request):
    if request.method == 'POST':
        #get the data of all the field in the from
        
        keyword = request.POST.get('keyword')
        
        
        
        query = """
            PREFIX pro: <http://purl.org/hpi/patchr#>
            PREFIX pr: <http://purl.org/ontology/prv/core#>
            prefix schema: <http://schema.org/>
            prefix eeo: <https://github.com/semintelligence/Product-Discovery/>
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            prefix owl: <http://www.w3.org/2002/07/owl#>
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            prefix foaf: <http://xmlns.com/foaf/0.1/>
            prefix base: <http://127.0.0.1:3333/>

            select ?color  ?dimension  ?weight ?title ?brandname ?storage
                    ?ramsize ?screenType ?ramType ?processorName  ?image ?modelNumber
            where{	
                
                ?product eeo:hasBrand ?brand;
                    eeo:hasVendor ?PS ; 
                    eeo:image ?image ;

                    eeo:hasTitle ?title .
            
            
                ?brand eeo:hasBrandName ?brandname .
                    
                    
                ?device rdfs:subClassOf ?product ;
                    eeo:hasSeries ?series ;
                    eeo:color     ?color ;
                    eeo:ModelNumber ?modelNumber;
                    eeo:hasProcessor ?processor ;
                    eeo:hasMemory ?memory ;
                    eeo:weight ?weight ;
                    eeo:hasScreenType ?screenType ;
                    eeo:hasDimension ?dimension .
            ?ram rdfs:subClassOf ?memory ;
                a eeo:PrimaryMemory;
                eeo:hasRAMSize ?ramsize ;
                eeo:hasRAMType ?ramType.
            
            ?SecondaryStorage rdfs:subClassOf ?memory;
                                eeo:hasSMSize ?storage .
            
            ?processor eeo:ProcessorName ?processorName.
            
            
            ?PS eeo:hasVendorDetials ?VendorDetails ;
                    eeo:hasVendorProductDetials ?VendorProductDeatils .
            
            ?VendorDetails eeo:hasName ?VendorName .
  			?VendorProductDeatils eeo:hasVendorProductPrice ?price ;
                           		eeo:hasProductProductQuantity ?stock .
            
  



            
        """
        
       
        query += f"filter contains(lcase(?title),'{keyword.lower()}')"
                    
        
        query += "\n}"
        
        
        sparql = SPARQLWrapper(
             "https://product-sparql001.herokuapp.com/ds/sparql"
        )
        sparql.setReturnFormat(JSON)
        
        
        sparql.setQuery(query)
        results = sparql.query().convert()

        try:
            ret = sparql.queryAndConvert()
    
            Title = []
            ModelNumber = []
            
            Image = []
            
            for r in ret["results"]["bindings"]:
                    
                    
                    Title.append(r["title"]['value'])
                    ModelNumber.append(r["modelNumber"]['value'])
                    Image.append(r["image"]['value'])
                    
                    
            
                                
        except Exception as e:
            print(e)
        
        Title = np.unique(Title)
        Image = np.unique(Image)
        ModelNumber = np.unique(ModelNumber)
        ModelNumber = [urllib.parse.quote(x,safe='') for x in   ModelNumber]
        details =zip(Title  ,  ModelNumber , Image )
        
        return render(request, 'product.html' , context = {"detail":details})
    
    
    return render(request, 'index.html')

def index(request):
    context = {
        'headings':["Product Name","Color","Weight","Brand","RAM Size","Storage","Processor Name"]
    }
    
    if request.method == 'POST':
        #get the data of all the field in the from
        title = request.POST.get('Product Name').lower()
        
        #dimensions = request.POST.get('Dimensions').title()
        color = request.POST.get('Color').lower()
        weight = request.POST.get('Weight')
        brand = request.POST.get('Brand').lower()
        ram_size = request.POST.get('RAM Size')
        memory = request.POST.get('Storage')
        processor_name = request.POST.get('Processor Name').lower()
        

        
        query = """
            PREFIX pro: <http://purl.org/hpi/patchr#>
            PREFIX pr: <http://purl.org/ontology/prv/core#>
            prefix schema: <http://schema.org/> 
            prefix eeo: <https://github.com/semintelligence/Product-Discovery/> 
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            prefix owl: <http://www.w3.org/2002/07/owl#> 
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            prefix foaf: <http://xmlns.com/foaf/0.1/> 
            prefix base: <http://127.0.0.1:3333/>

            select ?color  ?dimension  ?weight ?title ?brandname ?storage
                    ?ramsize ?screenType ?ramType ?processorName  ?image ?modelNumber
            where{	
                
                ?product eeo:hasBrand ?brand;
                    eeo:hasVendor ?PS;
                    eeo:image ?image ;

                    eeo:hasTitle ?title .
            
            
                ?brand eeo:hasBrandName ?brandname .
                    
                    
                ?device rdfs:subClassOf ?product ;
                    eeo:hasSeries ?series ;
                    eeo:color     ?color ;
                    eeo:ModelNumber ?modelNumber;
                    eeo:hasProcessor ?processor ;
                    eeo:hasMemory ?memory ;
                    eeo:weight ?weight ;
                    eeo:hasScreenType ?screenType ;
                    eeo:hasDimension ?dimension .
            ?ram rdfs:subClassOf ?memory ;
                a eeo:PrimaryMemory;
                eeo:hasRAMSize ?ramsize ;
                eeo:hasRAMType ?ramType.
            
            ?SecondaryStorage rdfs:subClassOf ?memory;
                                eeo:hasSMSize ?storage .
            
            ?processor eeo:ProcessorName ?processorName.
            
            
            ?product eeo:hasBrand ?brand;
                    eeo:hasVendor ?PS ; 
                    eeo:image ?image ;

                    eeo:hasTitle ?title .
            
            
                ?brand eeo:hasBrandName ?brandname .
                    
                    
                ?device rdfs:subClassOf ?product ;
                    eeo:hasSeries ?series ;
                    eeo:color     ?color ;
                    eeo:ModelNumber ?modelNumber;
                    eeo:hasProcessor ?processor ;
                    eeo:hasMemory ?memory ;
                    eeo:weight ?weight ;
                    eeo:hasScreenType ?screenType ;
                    eeo:hasDimension ?dimension .
            ?ram rdfs:subClassOf ?memory ;
                a eeo:PrimaryMemory;
                eeo:hasRAMSize ?ramsize ;
                eeo:hasRAMType ?ramType.
            
            ?SecondaryStorage rdfs:subClassOf ?memory;
                                eeo:hasSMSize ?storage .
            
            ?processor eeo:ProcessorName ?processorName.
            
            
            ?PS eeo:hasVendorDetials ?VendorDetails ;
                    eeo:hasVendorProductDetials ?VendorProductDeatils .
            
            ?VendorDetails eeo:hasName ?VendorName .
  			?VendorProductDeatils eeo:hasVendorProductPrice ?price ;
                           		eeo:hasProductProductQuantity ?stock .
            
  



            
        """
        if title != "":
            query += "\nFILTER contains(lcase(?title) , '"+title+"')."
        
        
        if color !="" :
            query += "\nFILTER contains(lcase(?color) , '"+color+"')"
        if weight !="" :
            query += "\nFILTER(?weight = "+weight+")"
        if brand !="" :
            query += "\nFILTER contains(lcase(?brandname) , '"+brand+"')"
        if ram_size !="" :
            query += "\nFILTER(?ramsize = "+ram_size+")"
        if memory !="" :
            query += "\nFILTER(?storage = "+memory+")"
        if processor_name !="" :
            query += "\nFILTER contains(lcase(?processorName) , '"+processor_name+"')"
        
        
        query += "\n}"
        
        
        
        sparql = SPARQLWrapper(
             "https://product-sparql001.herokuapp.com/ds/sparql"
        )
        sparql.setReturnFormat(JSON)
        
        
        sparql.setQuery(query)
        results = sparql.query().convert()

        try:
            ret = sparql.queryAndConvert()
    
            Title = []
            ModelNumber = []
            
            Image = []
            
            for r in ret["results"]["bindings"]:
                    
                    
                    Title.append(r["title"]['value'])
                    ModelNumber.append(r["modelNumber"]['value'])
                    Image.append(r["image"]['value'])
                    
                    
            
                                
        except Exception as e:
            print(e)
        
        Title = np.unique(Title)
        Image = np.unique(Image)
        ModelNumber = np.unique(ModelNumber)
        ModelNumber = [urllib.parse.quote(x,safe='') for x in   ModelNumber]
        details =zip(Title  ,  ModelNumber , Image )
        
        return render(request, 'product.html' , context = {"detail":details})

        
    return render(request, 'search.html', context)


def detail(request,ModelNumber ):
    ModelNumber = (urllib.parse.unquote_plus(ModelNumber))
    query = """
   PREFIX pro: <http://purl.org/hpi/patchr#>
            PREFIX pr: <http://purl.org/ontology/prv/core#>
            prefix schema: <http://schema.org/> 
            prefix eeo: <https://github.com/semintelligence/Product-Discovery/> 
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            prefix owl: <http://www.w3.org/2002/07/owl#> 
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            prefix foaf: <http://xmlns.com/foaf/0.1/> 
            prefix base: <http://127.0.0.1:3333/>

            select ?color  ?dimension ?title  ?weight  ?brandname ?storage
                    ?ramsize ?screenType ?ramType ?processorName  ?image ?VendorName ?price ?stock
            where{	
                
                ?product eeo:hasBrand ?brand;
                    eeo:hasVendor ?PS ; 
                    eeo:image ?image ;

                    eeo:hasTitle ?title .
            
            
                ?brand eeo:hasBrandName ?brandname .
                    
                    
                ?device rdfs:subClassOf ?product ;
                    eeo:hasSeries ?series ;
                    eeo:color     ?color ;
                    eeo:ModelNumber ?modelNumber;
                    eeo:hasProcessor ?processor ;
                    eeo:hasMemory ?memory ;
                    eeo:weight ?weight ;
                    eeo:hasScreenType ?screenType ;
                    eeo:hasDimension ?dimension .
            ?ram rdfs:subClassOf ?memory ;
                a eeo:PrimaryMemory;
                eeo:hasRAMSize ?ramsize ;
                eeo:hasRAMType ?ramType.
            
            ?SecondaryStorage rdfs:subClassOf ?memory;
                                eeo:hasSMSize ?storage .
            
            ?processor eeo:ProcessorName ?processorName.
            
            
            ?PS eeo:hasVendorDetials ?VendorDetails ;
                    eeo:hasVendorProductDetials ?VendorProductDeatils .
            
            ?VendorDetails eeo:hasName ?VendorName .
  			?VendorProductDeatils eeo:hasVendorProductPrice ?price ;
                           		eeo:hasProductProductQuantity ?stock .
            
  
    """
    query += f"filter (?modelNumber = '{ModelNumber}')."
    query+="\n}"
  
        
    sparql = SPARQLWrapper(
            "https://product-sparql001.herokuapp.com/ds/sparql"
    )
    sparql.setReturnFormat(JSON)
    
    
    sparql.setQuery(query)
    results = sparql.query().convert()

    try:
        ret = sparql.queryAndConvert()

        
        VendorName = []
        VendorPrice = []
        Stock = []
        
        
        for r in ret["results"]["bindings"]:
                Title = r["title"]['value']
                Image = r["image"]['value']
                Brand = r["brandname"]['value']
                Color = r["color"]['value']
                Dimension = r["dimension"]['value']
                Weight = r["weight"]['value']
                RAMSize = r["ramsize"]['value']
                RAMType = r["ramType"]['value']
                ScreenType = r["screenType"]['value']
                ProcessorName = r["processorName"]['value']
                Storage = r["storage"]['value']
                VendorName.append(r["VendorName"]['value'])
                VendorPrice.append(r["price"]['value'])
                Stock.append(r["stock"]['value'])
                         
    except Exception as e:
        print("set")
        print(e)
        
    VendorDetails = zip( VendorName , VendorPrice , Stock )
    content = {
        "title":Title,
        "image":Image,
        "brand":Brand,
        "color":Color,
        "dimension":Dimension,
        "weight":Weight,
        "ramsize":RAMSize,
        "ramtype":RAMType,
        "screentype":ScreenType,
        "processorname":ProcessorName,
        "storage":Storage,
        "vendordetails":VendorDetails,
        
        
    }
    
    return render(request, "detail.html" ,content)
    
    
def sparql(request):
    return render(request, "sparql.html")

def login(requests):
    return render(requests, "login.html")