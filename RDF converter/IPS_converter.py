from rdflib import URIRef,Namespace,RDF,Graph,Literal,BNode,OWL
import pandas as pd

def convert_csv_to_rdf(excel_file_path, rdf_file_path):
    # Load the tabular data from CSV into an RDF graph
    g = Graph()

    # Bind namespaces
    dicv = Namespace("https://w3id.org/digitalconstruction/0.5/Variables#")
    dicp = Namespace("https://w3id.org/digitalconstruction/0.5/Processes#")
    dice = Namespace("https://w3id.org/digitalconstruction/0.5/Entities#")
    dici = Namespace("https://w3id.org/digitalconstruction/0.5/Information#")
    ex = Namespace("https://example.aalto.fi/")
    unit = Namespace("http://qudt.org/vocab/unit/")

    # parse the csv data
    listOb = pd.read_excel(excel_file_path,
                           names=['Agent','Property','State','Observation','Start','End','Duration','Location','Sensor'])
    Agentread = list(listOb['Agent'])
    Sensorread = list(listOb['Sensor'])
    Observationread = list(listOb['Observation'])
    Propertyread = list(listOb['Property'])
    Stateread = list(listOb['State'])
    Locationread = list(listOb['Location'])

    Startread = list(listOb['Start'])
    Endread = list(listOb['End'])
    Durationread = list(listOb['Duration'])


    # Conversion
    for item in range(len(Agentread)):
        Agenturl = URIRef(str(Agentread[item]))
        Locationurl = URIRef(str(Locationread[item]))
        Sensorurl = URIRef(str(Sensorread[item]))
        Observationyurl = URIRef(str(Observationread[item]))
        Propertyurl = URIRef(str(Propertyread[item]))
        Stateurl = URIRef(str(Stateread[item]))

        Startstr = str(Startread[item])
        Endstr = str(Endread[item])
        Durationstr = str(Durationread[item])

        g.add((Agenturl, RDF.type, dice.Agent))
        g.add((Agenturl, dicv.hasProperty, Propertyurl))

        g.add((Locationurl, RDF.type, dice.Location))


        g.add((Propertyurl, RDF.type, dicv.Property))
        g.add((Propertyurl, dicv.hasPropertyState, Stateurl))

        g.add((Stateurl, RDF.type, dicv.PropertyState))
        g.add((Stateurl, ex.hasStartTime, Literal(Startstr)))
        g.add((Stateurl, ex.hasEndTime, Literal(Endstr)))
        g.add((Stateurl, ex.hasDuration, Literal(Durationstr)))
        g.add((Stateurl, dicv.hasResult,Locationurl ))

        g.add((Sensorurl, RDF.type, dice.Sensor))

        g.add((Observationyurl, RDF.type, dicp.Observation))
        g.add((Observationyurl, dicp.hasObservedProperty, Propertyurl))
        g.add((Observationyurl, dicp.hasObservedResult, Stateurl))
        g.add((Observationyurl, dicp.isObservedBy, Sensorurl))


    # Serialize the RDF graph and save it to a file
    g.serialize(rdf_file_path, format="turtle")
