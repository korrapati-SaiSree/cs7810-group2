import os
import pandas as pd
from rdflib import URIRef
from helper.init_kg import init_kg, add_literal_property, add_object_property, add_subclass_property, sanitize_label, pfs

# Paths
data_path = "./code/data_processing/dataset/"
output_path = "./output/"
os.makedirs(output_path, exist_ok=True)

# Initialize Graph
graph = init_kg()
a = pfs["rdf"]["type"]

#Socio Economic Condition dataset
socio_economic_dataset_file = os.path.join(data_path,"socio_economic_condition.csv")
socio_economic_data = pd.read_csv(socio_economic_dataset_file)

for _,row in socio_economic_data.iterrows():
    state_uri = URIRef(pfs['rc-res'][f"State_{sanitize_label(row['State'])}"])
    add_literal_property(graph, state_uri, pfs['rc-ont']['hasPopulation'], row['Population'],pfs['xsd'].integer)

    socio_economic_condition_uri = URIRef(pfs['rc-res'][f"SocioEconomicCondition_{sanitize_label(row['State'])}"])
    graph.add((socio_economic_condition_uri,a,pfs['rc-ont']["SocioEconomicCondition"]))
    add_object_property(graph, state_uri,pfs['rc-ont']['hasSocioEconomicCondition'],socio_economic_condition_uri)

    median_house_hold_income_uri = URIRef(pfs['rc-res'][f"IncomeHouseHoldMedian_{sanitize_label(row['State'])}"])
    graph.add((median_house_hold_income_uri,a,pfs['rc-ont']["IncomeHouseHoldMedian"]))
    add_literal_property(graph, median_house_hold_income_uri,pfs['rc-ont']['incomeHouseHoldMedianAsDecimal'],row['Median_Household_Income'],pfs["xsd"].decimal)
    add_subclass_property(graph, median_house_hold_income_uri,socio_economic_condition_uri)

    employment_rate_uri = URIRef(pfs['rc-res'][f"EmploymentRate_{sanitize_label(row['State'])}"])
    graph.add((employment_rate_uri,a,pfs['rc-ont']["EmploymentRate"]))
    add_literal_property(graph, employment_rate_uri,pfs['rc-ont']['employmentRateAsDecimal'],row['Employment_Rate'],pfs["xsd"].decimal)
    add_subclass_property(graph, employment_rate_uri,socio_economic_condition_uri)

    population_density_uri = URIRef(pfs['rc-res'][f"PopulationDensity_{sanitize_label(row['State'])}"])
    graph.add((population_density_uri,a,pfs['rc-ont']["PopulationDensity"]))
    add_literal_property(graph, population_density_uri,pfs['rc-ont']['populationDensityAsDecimal'],row['Population_Density'],pfs["xsd"].decimal)
    add_subclass_property(graph, population_density_uri,socio_economic_condition_uri)

    education_level_uri = URIRef(pfs['rc-res'][f"EducationLevel_{sanitize_label(row['State'])}"])
    graph.add((population_density_uri,a,pfs['rc-ont']["EducationLevel"]))
    add_literal_property(graph, education_level_uri,pfs['rc-ont']['highSchoolOrHigher'],row['High_School_or_Higher'],pfs["xsd"].decimal)
    add_literal_property(graph, education_level_uri,pfs['rc-ont']['bachelorsDegreeOrHigher'],row["Bachelor's_Degree_or_Higher"],pfs["xsd"].decimal)
    add_subclass_property(graph, education_level_uri,socio_economic_condition_uri)

# Serialize
output_file = os.path.join(output_path, "socio_economic_condition_data.ttl")
graph.serialize(destination=output_file, format="turtle", encoding="utf-8")
print(f"Crash data serialized to {output_file}")