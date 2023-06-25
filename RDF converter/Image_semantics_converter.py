from rdflib import URIRef,Namespace,RDF,Graph,Literal,BNode,OWL
import pandas as pd

def convert_csv_to_rdf(csv_file_path, rdf_file_path):
    # Load the tabular data from CSV into an RDF graph
    g = Graph()

    # Bind namespaces
    dicv = Namespace("https://w3id.org/digitalconstruction/0.5/Variables#")
    dicp = Namespace("https://w3id.org/digitalconstruction/0.5/Processes#")
    dice = Namespace("https://w3id.org/digitalconstruction/0.5/Entities#")
    dici = Namespace("https://w3id.org/digitalconstruction/0.5/Information#")
    ex = Namespace("https://example.aalto.fi#")

    # parse the csv data
    listOb = pd.read_excel(csv_file_path,
                           names=['Image','CreationTime','Apartment','Wall','Frame','FrameProperty','FrameState','FrameStateValue','Wire','WireProperty','WireState','WireStateValue','BackPanel','BackPanelProperty','BackPanelState','BackPanelStateValue','FrontPanel','FrontPanelProperty','FrontPanelState','FrontPanelStateValue'])
    Imageread = list(listOb['Image'])
    Creationread = list(listOb['CreationTime'])
    Apartmentread = list(listOb['Apartment'])
    Wallread = list(listOb['Wall'])

    Frameread = list(listOb['Frame'])
    FramePropertyread = list(listOb['FrameProperty'])
    FrameStateread = list(listOb['FrameState'])
    FrameStateValueread = list(listOb['FrameStateValue'])

    Wireread = list(listOb['Wire'])
    WirePropertyread = list(listOb['WireProperty'])
    WireStateread = list(listOb['WireState'])
    WireStateValueread = list(listOb['WireStateValue'])

    BackPanelread = list(listOb['BackPanel'])
    BackPanelPropertyread = list(listOb['BackPanelProperty'])
    BackPanelStateread = list(listOb['BackPanelState'])
    BackPanelStateValueread = list(listOb['BackPanelStateValue'])

    FrontPanelread = list(listOb['FrontPanel'])
    FrontPanelPropertyread = list(listOb['FrontPanelProperty'])
    FrontPanelStateread = list(listOb['FrontPanelState'])
    FrontPanelStateValueread = list(listOb['FrontPanelStateValue'])


    # Conversion
    for item in range(len(Imageread)):
        Imageurl = URIRef(str(Imageread[item]))
        Apturl = URIRef(str(Apartmentread[item]))
        Wallurl = URIRef(str(Wallread[item]))
        Creationstr = str(Creationread[item])

        Frameurl = URIRef(str(Frameread[item]))
        FramePropertyurl = URIRef(str(FramePropertyread[item]))
        FrameStateurl = URIRef(str(FrameStateread[item]))
        FrameStateValuestr = str(FrameStateValueread[item])

        Wireurl = URIRef(str(Wireread[item]))
        WirePropertyurl = URIRef(str(WirePropertyread[item]))
        WireStateurl = URIRef(str(WireStateread[item]))
        WireStateValuestr = str(WireStateValueread[item])

        BackPanelurl = URIRef(str(BackPanelread[item]))
        BackPanelPropertyurl = URIRef(str(BackPanelPropertyread[item]))
        BackPanelStateurl = URIRef(str(BackPanelStateread[item]))
        BackPanelStateValuestr = str(BackPanelStateValueread[item])

        FrontPanelurl = URIRef(str(FrontPanelread[item]))
        FrontPanelPropertyurl = URIRef(str(FrontPanelPropertyread[item]))
        FrontPanelStateurl = URIRef(str(FrontPanelStateread[item]))
        FrontPanelStateValuestr = str(FrontPanelStateValueread[item])


        g.add((Imageurl, RDF.type, dici.Image))
        g.add((Imageurl, dici.isAbout, FrameStateurl))
        g.add((Imageurl, dici.isAbout, WireStateurl))
        g.add((Imageurl, dici.isAbout, BackPanelStateurl))
        g.add((Imageurl, dici.isAbout, FrontPanelStateurl))

        g.add((Apturl, RDF.type, dice.Location))
        g.add((Apturl, dice.isLocationOf, Wallurl))

        g.add((Wallurl, RDF.type, dice.BuildingObject))
        g.add((Wallurl, dice.hasMemberpart, Frameurl))
        g.add((Wallurl, dice.hasMemberpart, BackPanelurl))
        g.add((Wallurl, dice.hasMemberpart, FrontPanelurl))
        g.add((Wallurl, dice.hasMemberpart, Wireurl))

        g.add((Frameurl, RDF.type, dice.BuildingObject))
        g.add((Frameurl, dicv.hasProperty, FramePropertyurl))
        g.add((FramePropertyurl, RDF.type, dicv.Property))
        g.add((FramePropertyurl, dicv.hasPropertyState, FrameStateurl))
        g.add((FrameStateurl, RDF.type, dicv.PropertyState))
        g.add((FrameStateurl, dicv.hasTimeOfCreation, Literal(Creationstr)))
        g.add((FrameStateurl, dicv.hasValue, Literal(FrameStateValuestr)))

        g.add((Wireurl, RDF.type, dice.BuildingObject))
        g.add((Wireurl, dicv.hasProperty, WirePropertyurl))
        g.add((WirePropertyurl, RDF.type, dicv.Property))
        g.add((WirePropertyurl, dicv.hasPropertyState, WireStateurl))
        g.add((WireStateurl, RDF.type, dicv.PropertyState))
        g.add((WireStateurl, dicv.hasTimeOfCreation, Literal(Creationstr)))
        g.add((WireStateurl, dicv.hasValue, Literal(WireStateValuestr)))

        g.add((BackPanelurl, RDF.type, dice.BuildingObject))
        g.add((BackPanelurl, dicv.hasProperty, BackPanelPropertyurl))
        g.add((BackPanelPropertyurl, RDF.type, dicv.Property))
        g.add((BackPanelPropertyurl, dicv.hasPropertyState, BackPanelStateurl))
        g.add((BackPanelStateurl, RDF.type, dicv.PropertyState))
        g.add((BackPanelStateurl, dicv.hasTimeOfCreation, Literal(Creationstr)))
        g.add((BackPanelStateurl, dicv.hasValue, Literal(BackPanelStateValuestr)))

        g.add((FrontPanelurl, RDF.type, dice.BuildingObject))
        g.add((FrontPanelurl, dicv.hasProperty, FrontPanelPropertyurl))
        g.add((FrontPanelPropertyurl, RDF.type, dicv.Property))
        g.add((FrontPanelPropertyurl, dicv.hasPropertyState, FrontPanelStateurl))
        g.add((FrontPanelStateurl, RDF.type, dicv.PropertyState))
        g.add((FrontPanelStateurl, dicv.hasTimeOfCreation, Literal(Creationstr)))
        g.add((FrontPanelStateurl, dicv.hasValue, Literal(FrontPanelStateValuestr)))


    # Serialize the RDF graph and save it to a file
    g.serialize(rdf_file_path, format="turtle")
