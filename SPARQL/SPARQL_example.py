import rdflib
import urllib.request
import ssl
from SPARQLWrapper import SPARQLWrapper, JSON



sparql = SPARQLWrapper("http://192.168.31.230:7200/repositories/0531-0610")


query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX yourNamespace: <yourNamespaceURI>

SELECT ?property ?value
WHERE {
  ?subject ?property ?value .
}
"""

# Set the SPARQL query and return format
sparql.setQuery(query)
sparql.setReturnFormat(JSON)

# Execute the SPARQL query
results = sparql.query().convert()

# Process the query results
for result in results["results"]["bindings"]:
    property_name = result["property"]["value"]
    value = result["value"]["value"]
    print(f"Property: {property_name} | Value: {value}")
