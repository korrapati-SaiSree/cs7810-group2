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

# Load Vehicle Dataset
vehicle_dataset_file = os.path.join(data_path,"vehicle_data.csv")
vehicle_data = pd.read_csv(vehicle_dataset_file)

for _,row in vehicle_data.iterrows():
    crash_id = row["ST_CASE"]
    crash_uri = URIRef(pfs["rc-res"][f"Crash_{crash_id}"])

    participant_uri = URIRef(pfs["rc-res"][f"Participant_{crash_id}"])

    #vehicle_uri
    vehicle_uri = URIRef(pfs['rc-res'][f"Vehicle_{crash_id}_{row['VEH_NO']}"])
    graph.add((vehicle_uri, a, pfs["rc-ont"]["Vehicle"]))
    add_subclass_property(graph, vehicle_uri, participant_uri)

    #vehicle in accident_uri
    vehicle_in_accident_uri = URIRef(pfs['rc-res'][f"VehicleInAccident_{crash_id}_{row['VEH_NO']}"])
    graph.add((vehicle_in_accident_uri, a, pfs["rc-ont"]["VehicleInAccident"]))
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasMannerOfCollision'],row['MAN_COLLNAME'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['involvedInHitAndRun'],row['HIT_RUN'],pfs["xsd"].boolean)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasVehicleMake'],row['MAKENAME'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasVehicleModel'],row['MAK_MODNAME'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasVehicleType'],row['BODY_TYPNAME'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasVIN'],row['VIN'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasWeightRange'],row['GVWR_TONAME'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasMannerOfCollision'],row['TOW_VEHNAME'],pfs["xsd"].string)
    add_literal_property(graph, vehicle_in_accident_uri, pfs['rc-ont']['hasSpeed'],row['TRAV_SP'],pfs["xsd"].integer)

    #subclass property of vehicle
    add_object_property(graph,vehicle_uri,pfs['rc-ont']['performsVehicleInAccident'],vehicle_in_accident_uri)
    add_object_property(graph,crash_uri,pfs['rc-ont']['providesVehicleInAccident'],vehicle_in_accident_uri)

    #person_uri
    person_uri = URIRef(pfs['rc-res'][f"Person_{crash_id}_{row['VEH_NO']}_1"])

    #person_in_crash_uri
    person_in_crash_uri = URIRef(pfs['rc-res'][f"PersonInCrash_{crash_id}_{row['VEH_NO']}_1"])

    #Occupant_uri
    occupant_uri = URIRef(pfs['rc-res'][f"Occupant_{crash_id}_{row['VEH_NO']}_1"])

    #driver uri
    driver_uri = URIRef(pfs['rc-res'][f"Driver_{crash_id}_{row['VEH_NO']}_1"])
    add_object_property(graph, driver_uri, pfs["rc-ont"]['isInVehicle'],vehicle_uri)
    add_literal_property(graph, driver_uri, pfs['rc-ont']['hasLicenseStatus'],row['L_STATUSNAME'],pfs["xsd"].string)
    add_literal_property(graph, driver_uri, pfs['rc-ont']['hasLicenseType'],row['L_TYPENAME'],pfs["xsd"].string)
    add_literal_property(graph, driver_uri, pfs['rc-ont']['hasWeight'],row['DR_WGT'],pfs["xsd"].integer)
    add_literal_property(graph, driver_uri, pfs['rc-ont']['hasHeight'],row['DR_HGT'],pfs["xsd"].integer)

    #driving history uri
    driving_history_uri = URIRef(pfs['rc-res'][f"DrivingHistory_{crash_id}_{row['VEH_NO']}_1"]) #_1 is added as all driver has index of 1 in every vehicle
    graph.add((driving_history_uri, a, pfs["rc-ont"]["DrivingHistory"]))
    add_object_property(graph, driver_uri,pfs['rc-ont']['hasDrivingHistory'],driving_history_uri)
    add_literal_property(graph, driving_history_uri, pfs['rc-ont']['totalPreviousAccidentRecord'],row['PREV_ACC'],pfs["xsd"].integer)
    add_literal_property(graph, driving_history_uri, pfs['rc-ont']['totalPreviousDWI'],row['PREV_DWI'],pfs["xsd"].integer)
    add_literal_property(graph, driving_history_uri, pfs['rc-ont']['totalPreviousSpeeding'],row['PREV_SPD'],pfs["xsd"].integer)

    #first driving conviction
    first_driving_conviction_uri = URIRef(pfs['rc-res'][f"FirstDrivingConviction_{crash_id}_{row['VEH_NO']}_1"]) #_1 is added as all driver has index of 1 in every vehicle
    graph.add((first_driving_conviction_uri, a, pfs["rc-ont"]["FirstDrivingConviction"]))
    add_literal_property(graph, first_driving_conviction_uri, pfs['rc-ont']['atMonth'],row['FIRST_MO'],pfs["xsd"].integer)
    add_literal_property(graph, first_driving_conviction_uri, pfs['rc-ont']['atYear'],row['FIRST_YR'],pfs["xsd"].integer)
    add_object_property(graph, driving_history_uri,pfs['rc-ont']['hasFirstDrivingConviction'],first_driving_conviction_uri)

    #recent driving conviction
    recent_driving_conviction_uri = URIRef(pfs['rc-res'][f"FirstDrivingConviction_{crash_id}_{row['VEH_NO']}_1"]) #_1 is added as all driver has index of 1 in every vehicle
    graph.add((recent_driving_conviction_uri, a, pfs["rc-ont"]["RecentDrivingConviction"]))
    add_literal_property(graph, recent_driving_conviction_uri, pfs['rc-ont']['atMonth'],row['LAST_MO'],pfs["xsd"].integer)
    add_literal_property(graph, recent_driving_conviction_uri, pfs['rc-ont']['atYear'],row['LAST_YR'],pfs["xsd"].integer)
    add_object_property(graph, driving_history_uri,pfs['rc-ont']['hasRecentDrivingConviction'],recent_driving_conviction_uri)

    #subclassOf person
    add_subclass_property(graph, occupant_uri,person_in_crash_uri)
    add_subclass_property(graph, driver_uri,occupant_uri)

    #Participant_uri
    participant_uri = URIRef(pfs['rc-res'][f"Participant_{crash_id}"])

    #subclasses of participant
    add_subclass_property(graph, vehicle_uri,participant_uri)
    add_subclass_property(graph, person_uri,participant_uri)

    #road condition uri
    road_condition_uri = URIRef(pfs['rc-res'][f"RoadCondition_{crash_id}"])
    graph.add((road_condition_uri, a, pfs["rc-ont"]["RoadCondition"]))
    add_literal_property(graph, road_condition_uri,pfs['rc-ont']['hasRoadwayAlignment'],row['VALIGNNAME'],pfs["xsd"].string)
    add_literal_property(graph, road_condition_uri,pfs['rc-ont']['hasRoadwayGrade'],row['VPROFILENAME'],pfs["xsd"].string)
    add_literal_property(graph, road_condition_uri,pfs['rc-ont']['hasRoadSurfaceType'],row['VPAVETYPNAME'],pfs["xsd"].string)
    add_literal_property(graph, road_condition_uri,pfs['rc-ont']['hasRoadSurfaceCondition'],row['VSURCONDNAME'],pfs["xsd"].string)

    add_object_property(graph, crash_uri,pfs['rc-ont']['hasRoadCondition'],road_condition_uri)

# Serialize
output_file = os.path.join(output_path, "vehicle_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")