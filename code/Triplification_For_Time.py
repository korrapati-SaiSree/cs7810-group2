import os
import pandas as pd
from rdflib import URIRef
from helper.init_kg import init_kg, add_literal_property, add_object_property, convert_to_24_hour, pfs

# Paths
data_path = "/home/ruman/ruman_v/nexus/wright/intro_to_knowledge_engineering/Project/cs7810-group2/code/data_processing/dataset/"
output_path = "./output/"
os.makedirs(output_path, exist_ok=True)

# Initialize Graph
graph = init_kg()
a = pfs["rdf"]["type"]

#time dataset
time_dataset_file = os.path.join(data_path,"time.csv")
time_data = pd.read_csv(time_dataset_file)

for _, row in time_data.iterrows():
    crash_id = row["ST_CASE"]
    crash_uri = URIRef(pfs["rc-res"][f"Crash_{crash_id}"])

    temporal_extent_uri = URIRef(pfs['rc-res'][f"TemporalExtent_{crash_id}"])
    graph.add((temporal_extent_uri,a,pfs['rc-ont']['TemporalExtent']))
    add_object_property(graph,crash_uri,pfs['rc-ont']['hasTemporalExtent'],temporal_extent_uri)

    # Convert time to 24-hour format
    start_time = convert_to_24_hour(row["Start_Time"])
    end_time = convert_to_24_hour(row["End_Time"])

    add_literal_property(graph,temporal_extent_uri, pfs["rc-ont"]["hasStartTime"], start_time, pfs["xsd"].time)
    add_literal_property(graph,temporal_extent_uri, pfs["rc-ont"]["hasEndTime"], end_time, pfs["xsd"].time)
    add_literal_property(graph,temporal_extent_uri, pfs["rc-ont"]["timeOfDay"], row['Time_of_the_day'],pfs["xsd"].string)
    add_literal_property(graph,temporal_extent_uri, pfs["rc-ont"]["dayOfWeek"], row['Day_of_the_Week'], pfs["xsd"].string)
    add_literal_property(graph,temporal_extent_uri, pfs["rc-ont"]["season"], row['Season'], pfs["xsd"].string)


# Serialize
output_file = os.path.join(output_path, "time_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")