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

#Load Person Dataset
person_dataset_file = os.path.join(data_path,"person_data.csv")
person_data = pd.read_csv(person_dataset_file)

for _,row in person_data.iterrows():
    crash_id = row['ST_CASE']
    crash_uri = URIRef(pfs["rc-res"][f"Crash_{crash_id}"])
    participant_uri = URIRef(pfs['rc-res'][f"Participant_{crash_id}"])
    person_uri = URIRef(pfs['rc-res'][f"Person_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
    vehicleInCrash_uri = URIRef(pfs['rc-res'][f"VehicleInCrash_{crash_id}_{row['VEH_NO']}"])
    graph.add((person_uri, a, pfs['rc-ont']['Person']))
    add_subclass_property(graph,person_uri,participant_uri)
    add_literal_property(graph,person_uri,pfs['rc-ont']['hasAge'],row['AGE'],pfs["xsd"].integer)
    add_literal_property(graph,person_uri,pfs['rc-ont']['hasGender'],row['SEXNAME'],pfs["xsd"].string)

    person_in_crash_uri = URIRef(pfs['rc-res'][f"PersonInCrash_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
    graph.add((person_in_crash_uri, a, pfs['rc-ont']['PersonInCrash']))
    add_object_property(graph,person_uri,pfs['rc-ont']['performsPersonInCrash'],person_in_crash_uri)
    add_object_property(graph,crash_uri,pfs['rc-ont']['providesPersonInCrash'],person_in_crash_uri)
    add_literal_property(graph,person_in_crash_uri,pfs['rc-ont']['hasInjurySeverity'],row['INJ_SEVNAME'],pfs["xsd"].string)
    
    lag_time_uri = URIRef(pfs['rc-res'][f"LagTime_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
    graph.add((lag_time_uri,a,pfs['rc-ont']['LagTime']))
    add_object_property(graph,person_in_crash_uri,pfs['rc-ont']['hasLagTime'],lag_time_uri)
    add_literal_property(graph,lag_time_uri,pfs['rc-ont']['inHours'],row['LAG_HRSNAME'],pfs["xsd"].string)
    add_literal_property(graph,lag_time_uri,pfs['rc-ont']['inMinutes'],row['LAG_MINSNAME'],pfs["xsd"].string)

    if(row['REST_USENAME'] == 'Not a Motor Vehicle Occupant'):
        non_occupant_uri = URIRef(pfs['rc-res'][f"NonOccupant_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
        graph.add((non_occupant_uri,a,pfs['rc-ont']['NonOccupant']))
        add_subclass_property(graph,non_occupant_uri,person_in_crash_uri)
        add_literal_property(graph,non_occupant_uri,pfs['rc-ont']['locationDuringCrash'],row['LOCATIONNAME'],pfs["xsd"].string)

        if(row['PER_TYPNAME'] == 'Pedestrian' or row['PER_TYPNAME'] == 'Person In/On a Building' or row['PER_TYPNAME'] == 'Unknown Type of Non-Motorist' ):
            pedestrian_uri = URIRef(pfs['rc-res'][f'Pedestrian_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}'])
            graph.add((pedestrian_uri,a,pfs['rc-ont']['Pedestrian']))
            add_subclass_property(graph,pedestrian_uri,non_occupant_uri)

        elif(row['PER_TYPNAME'] == 'Bicyclist' or row['PER_TYPNAME'] == 'Other Pedalcyclist'):
            cyclist_uri = URIRef(pfs['rc-res'][f'Cyclist_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}'])
            graph.add((cyclist_uri,a,pfs['rc-ont']['Cyclist']))
            add_subclass_property(graph,cyclist_uri,non_occupant_uri)

        elif(row['PER_TYPNAME'] == 'Person on a Personal Conveyance' or row['PER_TYPNAME'] == 'Occupant of a Non-Motor Vehicle Transport Device'):
            personal_conveyer_uri = URIRef(pfs['rc-res'][f'Other/PersonalConveyance_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}'])
            graph.add((personal_conveyer_uri,a,pfs['rc-ont']['Other/PersonalConveyance']))
            add_subclass_property(graph,personal_conveyer_uri,non_occupant_uri)


    else:
        occupant_uri = URIRef(pfs['rc-res'][f"Occupant_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
        graph.add((occupant_uri,a,pfs['rc-ont']['Occupant']))
        add_subclass_property(graph,occupant_uri,person_in_crash_uri)
        add_object_property(graph, occupant_uri, pfs["rc-ont"]['isInVehicleInCrash'],vehicleInCrash_uri)
        add_literal_property(graph,occupant_uri,pfs['rc-ont']['seatPosition'],row['SEAT_POSNAME'],pfs["xsd"].string)
        add_literal_property(graph,occupant_uri,pfs['rc-ont']['safetyRestrainUsed'],row['REST_USENAME'],pfs["xsd"].string)
        add_literal_property(graph,occupant_uri,pfs['rc-ont']['hasAirbagDeployed'],row['AIR_BAGNAME'],pfs["xsd"].string)
        add_literal_property(graph,occupant_uri,pfs['rc-ont']['hasEjectionStatus'],row['EJECTIONNAME'],pfs["xsd"].string)

        if(row['PER_TYPNAME'] == 'Driver of a Motor Vehicle In-Transport'):
            driver_uri = URIRef(pfs['rc-res'][f"Driver_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
            graph.add((driver_uri, a, pfs["rc-ont"]["Driver"]))
            add_subclass_property(graph,driver_uri,occupant_uri)

        elif(row['PER_TYPNAME'] == 'Passenger of a Motor Vehicle In-Transport' or row['PER_TYPNAME']=='Occupant of a Motor Vehicle Not In-Transport' or row['PER_TYPNAME']=='Unknown Occupant Type in a Motor Vehicle In-Transport'):
            passenger_uri = URIRef(pfs['rc-res'][f"Passenger_{crash_id}_{row['VEH_NO']}_{row['PER_NO']}"])
            graph.add((passenger_uri,a,pfs['rc-ont']['Passenger'])) 
            add_subclass_property(graph,passenger_uri,occupant_uri)

# Serialize
output_file = os.path.join(output_path, "person_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")