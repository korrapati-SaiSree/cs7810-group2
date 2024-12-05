
# Road Crashes
**Authors:** Suyes Sapkota, Ruman Dangol, Sai Sree Korrapati

## Use Case Scenario
### Narrative 
With over 1.35 million deaths and countless injuries annually, road crashes have been one of the most critical global concerns that bring financial and psychological hardship. Road accidents continue to happen due to the complex interaction of factors such as driver behavior, environmental circumstances, and socioeconomic inequality, even with technical breakthroughs in vehicles and infrastructure. A Knowledge Graph (KG) can be a game-changer in addressing these problems since it captures the interactions between various factors in a sophisticated and integrated manner.

By offering a structured, semantic framework for crash data analysis, the Road Crashes Knowledge Graph seeks to assist stakeholders including emergency responders, urban planners, transportation agencies, researchers, and insurance. The KG helps stakeholders find trends and obtain useful insights by displaying things like drivers, road conditions, weather, and socioeconomic aspects, as well as the connections between them. For instance, it can show how socioeconomic inequality affects crash frequency or how weather and EMS response times affect survival rates.

Unlike other conventional relational databases, a KG can easily represent and query complex relationships. A KG represents the dynamic, interconnected character of crash data, whereas tabular data models are limited to static and linear representations. Its powerful querying capabilities enable the detection of hidden patterns and trends, while its schema-less structure lets it adapt to new kinds of data and relationships as they develop. Due to this, it can be considered the ideal tool to address the complex nature of road traffic accidents and design effective treatments.

Because it incorporates elements that are frequently disregarded in current models, such as inadequate road maintenance, socioeconomic circumstances, and driver distractions, this initiative is both innovative and timely. The KG offers a thorough viewpoint by integrating these less obvious reasons with more conventional elements like the weather and vehicle conditions. This all-encompassing strategy might greatly improve road safety programs, lower the number of fatalities, and guide the development of life-saving and transportation-improving laws globally.

### Competency Questions
1. How do different types of collisions (like head-on or rear-end) and seat positions affect fatality rates?
2. What patterns can be seen between weather conditions, seasons, and the chances of fatalities in crashes?
3. How do EMS response times (from being notified to arriving at the crash site and transporting to a hospital) affect survival rates?
4. How does driver impairment (from alcohol, drugs, or fatigue) impact crash rates?
5. Which drivers involved in crashes have a history of prior accidents, Driving While Intoxicated (DWI) offenses, or speeding violations, and how do their past records compare?
6. How do a driver's license status and type relate to the rate of crashes?
7. How do specific road conditions affect the likelihood and severity of crashes?
8. How do a state's income levels influence the rate of crashes?
9. How do driver attributes such as age, sex, weight, and height impact the severity of injuries sustained in road crashes?
10. How does the speed of the vehicle and age of the occupant during the crash relate to the Fatality?


### Integrated Datasets
Source: Fatality Analysis Reporting System(FARS) : https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars
Source: census data for socioeconomic conditions: https://www.census.gov/

## Modules
<!-- There should be one module section per module (essentially per key-notion) -->

### Crash
**Source Pattern:** Event Pattern from MODL 
**Source Data:** Fatality Analysis Reporting System (FARS)  

#### Description
The Crash Event is the focal point of the entire knowledge graph. Every piece of data—whether it's about driver behavior, vehicle condition, or road infrastructure—ultimately ties back to the crash event. Modeling a crash event allows us to ask critical questions like "What caused this crash?", "Where and when did it happen?", and "Who was involved?". Understanding each crash as a distinct event with its own unique set of contributing factors is essential to uncover patterns in road accidents, identify high-risk conditions, and develop preventive measures.
![image](https://github.com/user-attachments/assets/de6e6fd3-dcae-448b-b353-e656679e51a2)

### Axioms

1. Crash → hasTemporalExtent → TemporalExtent  
* `owl:Thing SubClassOf hasTemporalExtent only TemporalExtent`<br/>
  The range of the property hasTemporalExtent must belong to the class TemporalExtent.  
* `Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent`<br/> 
  Every Crash must have exactly one associated temporal extent.

2. Crash → occurredAt → Location  
* `Crash SubClassOf occurredAt only Location`<br/> 
  The range of the property occurredAt must belong to the class Location.  
* `Crash SubClassOf occurredAt exactly 1 Location`<br/>
  Every Crash must occur at exactly one location.

3. Crash → hasTotalFatalities → xsd:integer  
* `Crash SubClassOf hasTotalFatalities only xsd:integer`<br/>
  The range of the property hasTotalFatalities must be an integer.  
* `Crash SubClassOf hasTotalFatalities min 0 xsd:integer`<br/>
  Every Crash may have an associated integer value representing total fatalities.

4. Crash → hasTotalPeopleInvolved → xsd:integer  
* `Crash SubClassOf hasTotalPeopleInvolved only xsd:integer`<br/> 
  The range of the property hasTotalPeopleInvolved must be an integer.  
* `Crash SubClassOf hasTotalPeopleInvolved some xsd:integer`<br/>
  Every Crash must have an associated integer value representing total people involved.

4. Crash → hasTotalVehiclesInvolved → xsd:integer
* `Crash SubClassOf hasTotalVehiclesInvolved only xsd:integer` <br/>
  The range of the property hasTotalVehiclesInvolved must be an integer.  
* `Crash SubClassOf hasTotalVehiclesInvolved some xsd:integer` <br/>
  Every Crash must have an associated integer value representing total vehicles.

5. Crash → hasParticipant → Participant  
* `Crash SubClassOf hasParticipant only Participant`<br/> 
  The range of the property hasParticipant must belong to the class Participant.  
* `Crash SubClassOf hasParticipant some Participant`<br>
  Every Crash must have at least one associated Participant.

6. Crash → isNearWorkZone → xsd:string  
* `Crash SubClassOf isNearWorkZone only xsd:string`<br/>
  The value of the property isNearWorkZone must be a string.
* `Crash SubClassOf isNearWorkZone some xsd:string`<br/>
  Crash must have atleast one isNearWorkZone and it must be a string.

7. Crash → occurredInIntersection → xsd:string  
* `Crash SubClassOf occurredInIntersection only xsd:string`<br/>
  The value of the property occurredInIntersection must be a string.
* `Crash SubClassOf occurredInIntersection some xsd:string`<br/>
  Crash must have atleast one occurredInIntersection and it must be a string.

8. Crash → hasCondition → Condition  
* `Crash SubClassOf hasCondition only Condition`<br/>
  The condition of any Crash must be of type Condition.
* `Crash SubClassOf hasCondition some Condition`<br/>
  Every Crash must have at least one Condition.


# All Together Schema

![image](https://github.com/user-attachments/assets/06e2175c-eca5-47ab-9f56-a7cb7c1e14ac)




# Materialization

Following contains all the triplification code

Insert materialization link here.

# Validation

## Collision Fatality Analysis
**Competency Question:** "How do different types of collisions (like head-on or rear-end) and seat positions affect fatality rates?"

**Bridged Datasets:** Crash.csv, vehicle.csv, person.csv

**SPARQL Query:**
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?mannerOfCollision ?seatPosition 
       (COUNT(?occupant) AS ?totalOccupants)
       (SUM(IF(REGEX(?injSev, "Fatal", "i"), 1, 0)) AS ?fatalities)
       (SUM(IF(REGEX(?injSev, "Fatal", "i"), 1, 0)) * 100 / COUNT(?occupant) AS ?fatalityRate)
WHERE {
  # Crash instance with vehicles
  ?crash a rc-ont:Crash ;
         rc-ont:providesVehicleInCrash ?vehicleInCrash ;
         rc-ont:providesPersonInCrash ?personInCrash .

  # Vehicle collision type
  ?vehicleInCrash a rc-ont:VehicleInCrash ;
                     rc-ont:hasMannerOfCollision ?mannerOfCollision .
                     
  # Person and occupant details
  ?personInCrash a rc-ont:PersonInCrash ;
                 rc-ont:hasInjurySeverity ?injSev .
  ?occupant a rc-ont:Occupant ;
            rdfs:subClassOf ?personInCrash ;
            rc-ont:isInVehicleInCrash ?vehicleInCrash;
            rc-ont:seatPosition ?seatPosition .
            
  # Exclude unknown collision types
  FILTER(!CONTAINS(?mannerOfCollision, 'Unknown'))
}
GROUP BY ?mannerOfCollision ?seatPosition
ORDER BY DESC(?fatalities)
```

**Results:**
![image](https://github.com/user-attachments/assets/6e2bb8d1-29d9-4e4c-a1f1-fdfc690ac800)


## Weather Fatality Patterns
**Competency Question:** "What patterns can be seen between weather conditions, seasons, and the chances of fatalities in crashes?

**Bridged Datasets:** Crash.csv, time.csv

**SPARQL Query:**
```
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?weatherConditionData ?season (SUM(?fatalities) AS ?totalFatalities) (COUNT(?crash) AS ?crashCount)
WHERE {
    ?crash a rc-ont:Crash ;
           rc-ont:hasTemporalExtent ?temporalExtent ;
           rc-ont:hasCondition ?condition ;
           rc-ont:hasTotalFatalities ?fatalities .
  
  ?weatherCondition a rc-ont:WeatherCondition;
           rc-ont:weatherConditionAsString ?weatherConditionData;
    		rdfs:subClassOf ?condition .

    ?pointInTime rdfs:subClassOf ?temporalExtent;
                 rc-ont:season ?season.
}
GROUP BY ?weatherConditionData ?season
ORDER BY DESC(?totalFatalities)
```

**Results:**
![image](https://github.com/user-attachments/assets/93a14421-58e1-48c2-a231-a4aff2761813)


## EMS Impact on Survival
**Competency Question:** "How do EMS response times (from being notified to arriving at the crash site and transporting to a hospital) affect survival rates?"

**Bridged Datasets:** Crash.csv, EMS.csv

**SPARQL Query:**
```
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?crash ?responseTimeInMinutes ?transportTimeInMinutes ?totalFatalities
#SELECT *
WHERE {
  # Link to crash and survival outcome
    ?crash a rc-ont:Crash ; 
    		rc-ont:hasTotalFatalities ?totalFatalities;
           rc-ont:hasParticipant ?participant.
  
    ?ems a rc-ont:EmergencyMedicalService ;
         rdfs:subClassOf ?participant;
         rc-ont:hasNotificationTime ?notificationTime ;
         rc-ont:hasArrivalTime ?arrivalTime ;
         rc-ont:hasArrivalTimeToHospital ?hospitalArrivalTime .

    ?notificationTime rc-ont:inHours ?notHour ;
                      rc-ont:inMinutes ?notMin .
    ?arrivalTime rc-ont:inHours ?arrHour ;
                 rc-ont:inMinutes ?arrMin .
    ?hospitalArrivalTime rc-ont:inHours ?hospHour ;
                         rc-ont:inMinutes ?hospMin .

    BIND(IF((xsd:integer(?arrHour) * 60 + xsd:integer(?arrMin)) <
          (xsd:integer(?notHour) * 60 + xsd:integer(?notMin)),
          (xsd:integer(?arrHour) * 60 + xsd:integer(?arrMin) + 1440) - 
          (xsd:integer(?notHour) * 60 + xsd:integer(?notMin)),
          (xsd:integer(?arrHour) * 60 + xsd:integer(?arrMin)) - 
          (xsd:integer(?notHour) * 60 + xsd:integer(?notMin))) AS ?responseTimeInMinutes)

  # Calculate transport time in minutes, considering midnight wrap-around
  BIND(IF((xsd:integer(?hospHour) * 60 + xsd:integer(?hospMin)) <
          (xsd:integer(?arrHour) * 60 + xsd:integer(?arrMin)),
          (xsd:integer(?hospHour) * 60 + xsd:integer(?hospMin) + 1440) - 
          (xsd:integer(?arrHour) * 60 + xsd:integer(?arrMin)),
          (xsd:integer(?hospHour) * 60 + xsd:integer(?hospMin)) - 
          (xsd:integer(?arrHour) * 60 + xsd:integer(?arrMin))) AS ?transportTimeInMinutes)
  	
}
ORDER BY DESC(?totalFatalities)
LIMIT 15
```

**Results:**
![image](https://github.com/user-attachments/assets/96cb66af-eee6-4d21-b22b-b16f1a01fdda)


## Impairment Crash Rate
**Competency Question:** "How does driver impairment (from alcohol, drugs, or fatigue) impact crash rates?"

**Bridged Datasets:** Crash.csv, Person.csv, impairment.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?impairmentType (COUNT(?crash) as ?totalCrash)
WHERE {
      ?crash a rc-ont:Crash ;
           rc-ont:hasParticipant ?participant.
      ?person rdfs:subClassOf ?participant;
              rc-ont:performsPersonInCrash ?personInCrash .
  	?occupant rdfs:subClassOf ?personInCrash .
      
  # Driver and Impairment relationship
    ?driver a rc-ont:Driver ;
            rc-ont:hasImpairment ?impairment ;
            rdfs:subClassOf ?occupant.
    
    ?impairment a rc-ont:Impairment .
    ?impairment rc-ont:impairmentAsString ?impairmentType .
    
  FILTER(!contains(?impairmentType,"Reported"))
  FILTER(!contains(?impairmentType,"None"))

}
GROUP BY ?impairmentType
ORDER BY DESC(?totalCrash)
```

**Results:**
![image](https://github.com/user-attachments/assets/e2192d4f-0308-45dd-8ac5-eb5e58001790)


## Drivers with Prior Records
**Competency Question:** "Which drivers involved in crashes have a history of prior accidents, Driving While Intoxicated (DWI) offenses, or speeding violations, and how do their past records compare?"

**Bridged Datasets:** Crash.csv, Vehicle.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?crash ?driver ?prevAccidents ?prevDWI ?prevSpeeding
WHERE {
      ?crash a rc-ont:Crash ;
           rc-ont:hasParticipant ?participant.
      ?person rdfs:subClassOf ?participant;
              rc-ont:performsPersonInCrash ?personInCrash .
  	?occupant rdfs:subClassOf ?personInCrash .
      
  # Driver and Impairment relationship
    ?driver a rc-ont:Driver ;
            rdfs:subClassOf ?occupant;
  			rc-ont:hasDrivingHistory ?drivingHistory .

    # Driving history details
    ?drivingHistory a rc-ont:DrivingHistory ;
                    rc-ont:totalPreviousAccidentRecord ?prevAccidents ;
                    rc-ont:totalPreviousDWI ?prevDWI ;
                    rc-ont:totalPreviousSpeeding ?prevSpeeding .
    
    FILTER(?prevAccidents > 0 || ?prevDWI > 0 || ?prevSpeeding > 0)
    FILTER(?prevAccidents != 98 && ?prevAccidents != 99 && ?prevAccidents != 998)
    FILTER(?prevDWI != 98 && ?prevDWI != 99 && ?prevDWI != 998)
    FILTER(?prevSpeeding != 98 && ?prevSpeeding != 99 && ?prevSpeeding != 998)

}
ORDER BY DESC(?prevAccidents) DESC(?prevDWI) DESC(?prevSpeeding)
limit 10
}
```

**Results:**
![image](https://github.com/user-attachments/assets/03b93603-a213-495e-8da8-52a8f25430c8)


## License Status Crash Rate
**Competency Question:** "How do a driver's license status and type relate to the rate of crashes?"

**Bridged Datasets:** Crash.csv, Vehicle.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?licenseType ?licenseStatus (COUNT(?crash) as ?totalCrash) (COUNT(?driver) as ?totalDriver) 
WHERE {
      ?crash a rc-ont:Crash ;
           rc-ont:hasParticipant ?participant.
      ?person rdfs:subClassOf ?participant;
              rc-ont:performsPersonInCrash ?personInCrash .
  	?occupant rdfs:subClassOf ?personInCrash .
      
    ?driver a rc-ont:Driver ;
            rdfs:subClassOf ?occupant;
            rc-ont:hasLicenseStatus ?licenseStatus;
         	rc-ont:hasLicenseType ?licenseType;
  			rc-ont:hasDrivingHistory ?drivingHistory .

}
GROUP BY ?licenseStatus ?licenseType
ORDER BY DESC(?totalCrash)
```

**Results:**
![image](https://github.com/user-attachments/assets/69a53f77-1662-4c0c-8229-dd682a50490a)


## Road Condition Impact
**Competency Question:** "How do specific road conditions affect the likelihood and severity of crashes?"

**Bridged Datasets:** Crash.csv, Vehicle.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?grade ?surfaceType ?surfaceCondition (COUNT(?crash) AS ?crashCount)
WHERE {
    # Retrieve crashes and their associated road conditions
    ?crash a rc-ont:Crash ;
           rc-ont:hasCondition ?condition .
    ?roadCondition a rc-ont:RoadCondition ;
                   rdfs:subClassOf ?condition ;
                   rc-ont:hasRoadwayAlignment ?alignment ;
                   rc-ont:hasRoadwayGrade ?grade ;
                   rc-ont:hasRoadSurfaceType ?surfaceType ;
                   rc-ont:hasRoadSurfaceCondition ?surfaceCondition .
}
GROUP BY ?alignment ?grade ?surfaceType ?surfaceCondition
ORDER BY DESC(?crashCount)

```

**Results:**
![image](https://github.com/user-attachments/assets/2da2ab3d-bc84-4d75-bf62-ba556b92ac41)


## Socioeconomic Impact on Crashes
**Competency Question:** "How do a state's income levels influence the rate of crashes?"

**Bridged Datasets:** Crash.csv, location.csv, socioeconomiccondition.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?state ?medianIncomeAsDecimal (COUNT(?crash) AS ?crashCount)
WHERE {  	
  	?crash a rc-ont:Crash;
           rc-ont:occuredAt ?location.
  	?location rc-ont:hasState ?state.
  	?state a rc-ont:State ;
    		rc-ont:hasStateName ?stateName;
           rc-ont:hasPopulation ?population ;
           rc-ont:hasSocioEconomicCondition ?socioEconomicCondition .
	 
    # Socio-economic indicators
    ?socioEconomicCondition a rc-ont:SocioEconomicCondition .
  	
  	?medianIncome a rc-ont:IncomeHouseHoldMedian;
           rdfs:subClassOf ?socioEconomicCondition;
           rc-ont:incomeHouseHoldMedianAsDecimal ?medianIncomeAsDecimal .

}
GROUP BY ?state ?medianIncomeAsDecimal
ORDER BY DESC(?medianIncomeAsDecimal)
```

**Results:**
![image](https://github.com/user-attachments/assets/c234d1cf-05e3-49c2-8bab-e157f1a535e4)


## Driver Attributes and Injuries
**Competency Question:** "How do driver attributes such as age, sex, weight, and height impact the severity of injuries sustained in road crashes?"

**Bridged Datasets:** crash.csv, Person.csv, Vehicle.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?age ?sex (COUNT(?driver) AS ?driverCount) ?injurySeverity
#SELECT *
WHERE {
  # Link to crashes
  ?crash a rc-ont:Crash ;
  		rc-ont:hasParticipant ?participant.
#         rc-ont:hasTotalFatalities ?fatalities .
 
  ?person rdfs:subClassOf ?participant;
          a rc-ont:Person;
          rc-ont:hasAge ?age ;
          rc-ont:hasGender ?sex ;
          rc-ont:performsPersonInCrash ?personInCrash.
  ?personInCrash a rc-ont:PersonInCrash;
    rc-ont:hasInjurySeverity ?injurySeverity.
  
  ?occupant rdfs:subClassOf ?personInCrash.
  
#  # Retrieve driver information
  ?driver a rc-ont:Driver ;
          rc-ont:hasWeight ?weight ;
          rc-ont:hasHeight ?height ;
          rdfs:subClassOf ?occupant.
  
  # Exclude invalid height and weight values
  FILTER(?age != 998 && ?age != 999)
#  FILTER(?height NOT IN (998, 999))
#  FILTER(?weight NOT IN (997, 998, 999))
}
GROUP BY ?age ?sex ?injurySeverity
#GROUP BY ?age ?sex ?weight ?height ?injurySeverity
ORDER BY DESC(?driverCount)
#LIMIT 15

```

**Results:**
![image](https://github.com/user-attachments/assets/4de78b4e-e4f3-4ad8-9729-f588869e9540)

## Speed and Fatalities
**Competency Question:** "How does the speed of the vehicle and age of the occupant during the crash relate to the Fatality?"

**Bridged Datasets:** Crash.csv, Person.csv, Vehicle.csv

**SPARQL Query:**
```
PREFIX rc-res: <http://roadcrash.org/resource/>
PREFIX rc-ont: <http://roadcrash.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?speed ?age (COUNT(?person) AS ?FatalityCount) 
#SELECT *
WHERE {
  # Link to crashes
  ?crash a rc-ont:Crash ;
  		rc-ont:hasParticipant ?participant.
 
  ?person rdfs:subClassOf ?participant;
          a rc-ont:Person;
          rc-ont:hasAge ?age ;
          rc-ont:hasGender ?sex ;
          rc-ont:performsPersonInCrash ?personInCrash.
  ?personInCrash a rc-ont:PersonInCrash;
    rc-ont:hasInjurySeverity ?injurySeverity.
  
  ?occupant rdfs:subClassOf ?personInCrash;
  			rc-ont:isInVehicleInCrash ?vehicleInCrash.
  ?vehicleInCrash a rc-ont:VehicleInCrash;
     				rc-ont:hasSpeed ?speed.
  FILTER(?speed != 998 && ?speed != 999)
  FILTER(?age != 998 && ?age != 999)
  FILTER(CONTAINS(?injurySeverity,'Fatal'))
}
GROUP BY ?speed ?age
ORDER BY DESC(?FatalityCount)
#LIMIT 15

```

**Results:**
![image](https://github.com/user-attachments/assets/0f624fad-7f0f-41ba-93c3-e25920460dd9)


