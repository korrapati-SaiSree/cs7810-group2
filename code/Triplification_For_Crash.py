import os
import pandas as pd
from rdflib import URIRef
from helper.init_kg import init_kg, add_literal_property, add_object_property, pfs

# Paths
data_path = "/home/ruman/ruman_v/nexus/wright/intro_to_knowledge_engineering/Project/cs7810-group2/code/data_processing/dataset/"
output_path = "./output/"
os.makedirs(output_path, exist_ok=True)

# Load Dataset
crash_dataset_file = os.path.join(data_path, "crash_data.csv")
crash_data = pd.read_csv(crash_dataset_file)

# Initialize Graph
graph = init_kg()
a = pfs["rdf"]["type"]

# Process Crash Data
for _, row in crash_data.iterrows():
    # Crash URI
    crash_id = row["ST_CASE"]
    crash_uri = URIRef(pfs["rc-res"][f"Crash_{crash_id}"])

    # Crash properties
    graph.add((crash_uri, a, pfs["rc-ont"]["Crash"]))
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["hasTotalVehicleInvolved"], row["VE_TOTAL"], pfs["xsd"].integer)
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["hasTotalPeopleInvolved"], row["PERSONS"], pfs["xsd"].integer)
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["hasWeatherCondition"], row["WEATHERNAME"], pfs["xsd"].string)
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["hasLightingCondition"], row["LGT_CONDNAME"], pfs["xsd"].string)
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["isNearWorkZone"], row["WRK_ZONENAME"], pfs["xsd"].string)
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["occuredInIntersection"], row["TYP_INTNAME"], pfs["xsd"].string)
    add_literal_property(graph, crash_uri, pfs["rc-ont"]["hasTotalFatalities"], row["FATALS"], pfs["xsd"].integer)

    #Participant_uri
    participant_uri = URIRef(pfs['rc-res'][f"Participant_{crash_id}"])
    graph.add((participant_uri, a , pfs["rc-ont"]["Participant"]))
    add_object_property(graph,crash_uri,pfs['rc-ont']['hasParticipant'],participant_uri)

# Serialize
output_file = os.path.join(output_path, "crash_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")