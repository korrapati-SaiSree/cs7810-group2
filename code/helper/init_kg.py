import os
import pandas as pd
import rdflib
from rdflib import Namespace, URIRef, Literal, Graph
from rdflib import RDF, RDFS, XSD
from urllib.parse import quote
from datetime import datetime

# Namespace Definitions
base_uri = "http://roadcrash.org/"
pfs = {
    "rc-res": Namespace(f"{base_uri}resource/"),
    "rc-ont": Namespace(f"{base_uri}ontology/"),
    "xsd": XSD,
    "rdf": RDF,
    "rdfs": RDFS,
}

# Graph Initialization
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in prefixes:
        kg.bind(prefix, prefixes[prefix])
    return kg

# Helper Functions
def add_literal_property(graph, subject, property_uri, value, datatype):
    if pd.notna(value):
        graph.add((subject, property_uri, Literal(value, datatype=datatype)))

def add_object_property(graph, subject, property_uri, obj):
    graph.add((subject, property_uri, obj))

def add_subclass_property(graph, subject, obj):
    graph.add((subject, pfs['rdfs']['subClassOf'], obj))

def sanitize_label(label):
    return quote(label.replace(" ", "_"))

def convert_to_24_hour(time_str):
    try:
        return datetime.strptime(time_str, "%I:%M%p").strftime("%H:%M:%S")
    except ValueError:
        return None
    
def filter_hours_and_mins(time):
    invalid_values = {99, 98, 88}
    return time if time not in invalid_values else None
