import os
import pandas as pd
from rdflib import URIRef
from helper.init_kg import init_kg, add_literal_property, add_object_property, add_subclass_property, pfs

# Paths
data_path = "./code/data_processing/dataset/"
output_path = "./output/"
os.makedirs(output_path, exist_ok=True)

# Initialize Graph
graph = init_kg()
a = pfs["rdf"]["type"]

#impairment dataset
impairments_dataset_file = os.path.join(data_path,"impairment_data.csv")
impairment_data = pd.read_csv(impairments_dataset_file)

for _,row in impairment_data.iterrows():
    crash_id = row["ST_CASE"]
    crash_uri = URIRef(pfs["rc-res"][f"Crash_{crash_id}"])

    #driver uri
    driver_uri = URIRef(pfs['rc-res'][f"Driver_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])

    impairment_uri = URIRef(pfs['rc-res'][f"Impairment_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
    graph.add((impairment_uri,a,pfs['rc-ont']['Impairment']))
    add_literal_property(graph,impairment_uri,pfs['rc-ont']['impairmentAsString'],row['DRIMPAIRNAME'],pfs["xsd"].string)

    distraction_uri = URIRef(pfs['rc-res'][f"Distraction_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
    graph.add((distraction_uri,a,pfs['rc-ont']['Distraction']))
    add_literal_property(graph,distraction_uri,pfs['rc-ont']['distractionAsString'],row['DRDISTRACTNAME'],pfs["xsd"].string)
    add_subclass_property(graph,distraction_uri,impairment_uri)

    drugs_uri = URIRef(pfs['rc-res'][f"SubstanceImpairment_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
    graph.add((drugs_uri,a,pfs['rc-ont']['SubstanceImpairment']))
    add_literal_property(graph,drugs_uri,pfs['rc-ont']['substanceImpairmentAsString'],row['DRUGRESNAME'],pfs["xsd"].string)
    add_subclass_property(graph,drugs_uri,impairment_uri)

    add_object_property(graph, driver_uri,pfs['rc-ont']['hasImpairment'],impairment_uri)


# Serialize
output_file = os.path.join(output_path, "Impairment_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")