from rdflib import URIRef,Namespace,RDF,Graph,Literal,BNode,OWL
import pandas as pd

def convert_csv_to_rdf(excel_file_path, rdf_file_path):
    # Load the tabular data from excel into an RDF graph
    g = Graph()

    # Bind namespaces
    dicv = Namespace("https://w3id.org/digitalconstruction/0.5/Variables#")
    dicp = Namespace("https://w3id.org/digitalconstruction/0.5/Processes#")
    dice = Namespace("https://w3id.org/digitalconstruction/0.5/Entities#")
    dici = Namespace("https://w3id.org/digitalconstruction/0.5/Information#")
    ex = Namespace("https://example.aalto.fi#")
    unit = Namespace("http://qudt.org/vocab/unit/")

    # parse the csv data
    listOb = pd.read_excel(excel_file_path,
                           names=['Location','Sensor','Observation','ObservedProperty','PropertyState','Value','Time'])
    Locationread = list(listOb['Location'])
    Sensorread = list(listOb['Sensor'])
    Observationread = list(listOb['Observation'])
    ObservedPropertyread = list(listOb['ObservedProperty'])
    PropertyStateread = list(listOb['PropertyState'])

    Valueread = list(listOb['Value'])
    Timeread = list(listOb['Time'])


    # Conversion
    for item in range(len(Locationread)):
        Locationurl = URIRef(str(Locationread[item]))
        Sensorurl = URIRef(str(Sensorread[item]))
        Observationyurl = URIRef(str(Observationread[item]))
        ObservedPropertyurl = URIRef(str(ObservedPropertyread[item]))
        PropertyStateurl = URIRef(str(PropertyStateread[item]))

        Timestr = str(Timeread[item])
        Valuestr = str(Valueread[item])


        g.add((Locationurl, RDF.type, dice.Location))
        g.add((Locationurl, dicv.hasProperty, ObservedPropertyurl))

        g.add((ObservedPropertyurl, RDF.type, dicv.QuantitativeProperty))
        g.add((ObservedPropertyurl, dicv.hasPropertyState, PropertyStateurl))

        g.add((PropertyStateurl, RDF.type, dicv.QuantitativeState))
        g.add((PropertyStateurl, dicv.hasValue, Literal(Valuestr)))
        g.add((PropertyStateurl, dicv.hasUnit, unit.DEG_C))
        g.add((PropertyStateurl, dicv.hasTimeOfCreation, Literal(Timestr)))

        g.add((Sensorurl, RDF.type, dice.Sensor))

        g.add((Observationyurl, RDF.type, dicp.Observation))
        g.add((Observationyurl, dicp.hasObservedProperty, ObservedPropertyurl))
        g.add((Observationyurl, dicp.hasObservedResult, PropertyStateurl))
        g.add((Observationyurl, dicp.isObservedBy, Sensorurl))


    # Serialize the RDF graph and save it to a file
    g.serialize(rdf_file_path, format="turtle")

csv_file_path = "/Users/yuanzheng/Desktop/CPL/CPL-Jatke_condition.xlsx"
rdf_file_path = "/Users/yuanzheng/Desktop/CPL/CPL_Jatke_condition.ttl"

convert_csv_to_rdf(csv_file_path, rdf_file_path)
