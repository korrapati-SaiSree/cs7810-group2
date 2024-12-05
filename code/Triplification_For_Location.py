import os
import pandas as pd
from rdflib import URIRef
from helper.init_kg import init_kg, add_literal_property, add_object_property, sanitize_label, pfs

# Paths
data_path = "./dataset/"
output_path = "./output/"
os.makedirs(output_path, exist_ok=True)

# Initialize Graph
graph = init_kg()
a = pfs["rdf"]["type"]

#Location Dataset
location_dataset_file = os.path.join(data_path,"location_data.csv")
location_data = pd.read_csv(location_dataset_file)

for _,row in location_data.iterrows():
    crash_id = row["ST_CASE"]
    crash_uri = URIRef(pfs['rc-res'][f'Crash_{crash_id}'])

    location_uri = URIRef(pfs['rc-res'][f'Location_{crash_id}'])
    graph.add((location_uri, a, pfs['rc-ont']['Location']))
    add_object_property(graph,crash_uri,pfs['rc-ont']['occuredAt'],location_uri)
    
    coordinates_uri = URIRef(pfs['rc-res'][f'Coordinates_{crash_id}'])
    graph.add((coordinates_uri, a, pfs['rc-ont']['Coordinates']))
    add_object_property(graph,location_uri,pfs['rc-ont']['hasCoordinates'],coordinates_uri)
    add_literal_property(graph,coordinates_uri, pfs['rc-ont']['hasLatitude'],row['Latitude'],pfs["xsd"].float)
    add_literal_property(graph,coordinates_uri, pfs['rc-ont']['hasLongitude'],row['Longitude'],pfs["xsd"].float)

    state_uri = URIRef(pfs['rc-res'][f'State_{sanitize_label(row['StateName'])}'])
    graph.add((state_uri,a,pfs['rc-ont']['State']))
    add_literal_property(graph,state_uri,pfs['rc-ont']['hasStateName'],row['StateName'],pfs["xsd"].string)
    add_object_property(graph,location_uri,pfs['rc-ont']['hasState'],state_uri)

    city_uri = URIRef(pfs['rc-res'][f'City_{sanitize_label(row['StateName'])}_{crash_id}'])
    graph.add((city_uri,a,pfs['rc-ont']['City']))
    add_literal_property(graph,city_uri,pfs['rc-ont']['hasCityName'],row['CityName'],pfs["xsd"].string)
    add_object_property(graph,state_uri,pfs['rc-ont']['hasCity'],city_uri)

    county_uri = URIRef(pfs['rc-res'][f'County_{sanitize_label(row['StateName'])}_{crash_id}'])
    graph.add((county_uri,a,pfs['rc-ont']['County']))
    add_literal_property(graph,county_uri,pfs['rc-ont']['hasCountyName'],row['CountyName'],pfs["xsd"].string)
    add_object_property(graph,city_uri,pfs['rc-ont']['hasCounty'],county_uri)

    socio_economic_condition_uri = URIRef(pfs['rc-res'][f'SocioEconomicCondition_{sanitize_label(row['StateName'])}'])
    add_object_property(graph,state_uri, pfs['rc-ont']['hasSocioEconomicCondition'], socio_economic_condition_uri)


# Serialize
output_file = os.path.join(output_path, "location_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")