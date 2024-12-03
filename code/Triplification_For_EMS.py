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

#EMS Dataset
EMS_dataset_file = os.path.join(data_path,"EMS.csv")
EMS_data = pd.read_csv(EMS_dataset_file)

for _,row in EMS_data.iterrows():
    crash_id = row["ST_CASE"]
    crash_uri = URIRef(pfs['rc-res'][f'Crash_{crash_id}'])

    participant_uri = URIRef(pfs['rc-res'][f'Participant_{crash_id}'])

    EMS_uri = URIRef(pfs['rc-res'][f'EmergencyMedicalService_{crash_id}'])
    graph.add((EMS_uri, a, pfs['rc-ont']['EmergencyMedicalService']))
    add_subclass_property(graph, EMS_uri,participant_uri)

    notification_time_uri = URIRef(pfs['rc-res'][f'NotificationTime_{crash_id}'])
    graph.add((notification_time_uri, a, pfs['rc-ont']['NotificationTime']))
    add_object_property(graph,EMS_uri,pfs['rc-ont']['hasNotificationTime'],notification_time_uri)
    add_literal_property(graph,notification_time_uri,pfs['rc-ont']['inHours'],row['NOT_HOUR'],pfs["xsd"].integer)
    add_literal_property(graph,notification_time_uri,pfs['rc-ont']['inMinutes'],row['NOT_MIN'],pfs["xsd"].integer)

    arrival_time_uri = URIRef(pfs['rc-res'][f'ArrivalTime_{crash_id}'])
    graph.add((arrival_time_uri, a, pfs['rc-ont']['ArrivalTime']))
    add_object_property(graph,EMS_uri,pfs['rc-ont']['hasArrivalTime'],arrival_time_uri)
    add_literal_property(graph,arrival_time_uri,pfs['rc-ont']['inHours'],row['ARR_HOUR'],pfs["xsd"].integer)
    add_literal_property(graph,arrival_time_uri,pfs['rc-ont']['inMinutes'],row['ARR_MIN'],pfs["xsd"].integer)

    hospital_arrival_time_uri = URIRef(pfs['rc-res'][f'ArrivalTimeToHospital_{crash_id}'])
    graph.add((hospital_arrival_time_uri, a, pfs['rc-ont']['ArrivalTimeToHospital']))
    add_object_property(graph,EMS_uri,pfs['rc-ont']['hasArrivalTimeToHospital'],hospital_arrival_time_uri)
    add_literal_property(graph,hospital_arrival_time_uri,pfs['rc-ont']['inHours'],row['HOSP_HR'],pfs["xsd"].integer)
    add_literal_property(graph,hospital_arrival_time_uri,pfs['rc-ont']['inMinutes'],row['HOSP_MN'],pfs["xsd"].integer)


# Serialize
output_file = os.path.join(output_path, "emergency_medical_service_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")