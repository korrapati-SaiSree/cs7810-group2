# Validation

## Collision Fatality Analysis
**Competency Question:** "How do different types of collisions (like head-on or rear-end) and seat positions affect fatality rates?"

**Bridged Datasets:** dataset 1, dataset 2, ...

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

**Bridged Datasets:** dataset 1, dataset 2, ...

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


## Competency Question Name
**Competency Question:** "What am I?"

**Bridged Datasets:** dataset 1, dataset 2, ...

**SPARQL Query:**
```
SELECT * WHERE {
	?s ?p ?o .
}
```

**Results:**
| Header |
| :----: |
| Result |
| Result |
| Result |
| Result |
| Result |
