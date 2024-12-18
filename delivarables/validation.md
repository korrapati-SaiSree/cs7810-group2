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
![image](https://github.com/user-attachments/assets/ed838b3c-e8a9-49ca-9df2-4c941ffbb3f4)



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

```

**Results:**
![image](https://github.com/user-attachments/assets/d4f6082f-1652-4f6d-9726-1c8f2259052d)


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
![image](https://github.com/user-attachments/assets/467bbe98-3f9b-4295-aacc-6a3c324d852b)



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
![image](https://github.com/user-attachments/assets/9335a075-139c-441e-9254-23ac17ebeb75)



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
![image](https://github.com/user-attachments/assets/cd8e0605-1315-42b3-9012-92ea20cf1aea)



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
![image](https://github.com/user-attachments/assets/aa6f49a1-c58f-491e-86c8-6beb0b474023)


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
![image](https://github.com/user-attachments/assets/8a6b0dc7-85a6-4cbe-b42e-d16b6d7e09fb)
