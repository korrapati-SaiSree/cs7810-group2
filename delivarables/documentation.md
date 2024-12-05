
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

## Driver Condition
####   Source Pattern: AgentRole Pattern from MODL.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description:<br/>
Driver Condition captures the state of the driver at the time of the crash, including factors like distraction, fatigue, alcohol or drug influence, and overall experience. Drivers are often the most critical factor in accidents, and the knowledge graph needs to model how different states of driver impairment or distraction influence the likelihood and severity of crashes. The relationship between driver condition and environmental factors (like weather or road infrastructure) can reveal new insights into high-risk scenarios that traditional analyses may overlook.<br/>

![Driver Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Driver/Driver_Schema_Final.png)


### Axioms

1. Driver → hasDrivingHistory → DrivingHistory
* `Driver SubClassOf hasDrivingHistory some DrivingHistory`<br/> 
  Every driver must have at least one associated driving history.
* `Driver SubClassOf hasDrivingHistory only DrivingHistory`<br/>
  Every driver is associated with a driving history, and if they have any driving history, it must be represented as an instance of the DrivingHistory class.

2. Driver → hasImpairments → Impairments
* `Driver SubClassOf hasImpairments min 0 Impairments`<br/>
  A driver may have impairments.
* `Driver SubClassOf hasImpairments only Impairments`<br/>
  All drivers can have impairments, and if they do, those impairments must be instances of the Impairments class.

3. Driver → hasLicenseType → xsd:string
* `Driver SubClassOf hasLicenseType exactly 1 xsd:string`<br/>
  Each driver must have exactly one license type.
* `Driver SubClassOf hasLicenseType only xsd:string`<br/>
  Every driver can have a license type, and it must be recorded as a string.

4. Driver → hasLicenseStatus → xsd:string
* `Driver SubClassOf hasLicenseStatus exactly 1 xsd:string`<br/>
  Each driver must have exactly one license status.
* `Driver SubClassOf hasLicenseStatus only xsd:string`<br/>
  Every driver can have a license status, and it must be recorded as a string.

5. Driver → hasWeight → xsd:integer
* `Driver SubClassOf hasWeight exactly 1 xsd:integer`<br/>
  Each driver must have exactly one weight.
* `owl.Thing SubClassOf hasWeight only xsd:integer`<br/>
  Everything that have a weight must be recorded as a integer.

6. Driver → hasHeight → xsd:integer
* `Driver SubClassOf hasHeight exactly 1 xsd:integer`<br/> 
  Each driver must have exactly one height.
* `owl.Thing SubClassOf hasHeight only xsd:integer`<br/>
  Everything that have a weight must be recorded as a integer.

7. DrivingHistory → totalPreviousAccidentRecord → xsd:integer
* `DrivingHistory SubClassOf totalPreviousAccidentRecord exactly 1 xsd:integer`<br/>
  Each driving history must have exactly one total previous accident record.
* `DrivingHistory SubClassOf totalPreviousAccidentRecord only xsd:integer`<br>
  A driving history can have a total previous accident record, and it must be recorded as an integer.

8. DrivingHistory → totalPreviousDWI → xsd:integer
* `DrivingHistory SubClassOf totalPreviousDWI exactly 1 xsd:integer`<br/>
  Each driving history must have exactly one total previous DWI record.
* `DrivingHistory SubClassOf totalPreviousDWI only xsd:integer`<br/>
  A driving history can have a total previous DWI record, and it must be recorded as an integer.

9. DrivingHistory → totalPreviousSpeeding → xsd:integer
* `DrivingHistory SubClassOf totalPreviousSpeeding exactly 1 xsd:integer`<br/>
  Each driving history must have exactly one total previous speeding record.
* `DrivingHistory SubClassOf totalPreviousSpeeding only xsd:integer`<br/>
  A driving history can have a total previous speeding record, and it must be recorded as an integer.

10. DrivingHistory → hasFirstDrivingConviction → FirstDrivingConviction
* `DrivingHistory SubClassOf hasFirstDrivingConviction exactly 1 FirstDrivingConviction`<br/>
  Each driving history must have exactly one total previous speeding record.
* `DrivingHistory SubClassOf hasFirstDrivingConviction only FirstDrivingConviction`<br/>
  A driving history can have a total previous speeding record, and it must be recorded as an instance of FirstDrivingConviction.

11. DrivingHistory → hasRecentDrivingConviction → RecentDrivingCondition
* `DrivingHistory SubClassOf hasRecentDrivingConviction exactly 1 RecentDrivingCondition`<br/>
  Each driving history must have exactly one total previous speeding record.
* `DrivingHistory SubClassOf hasRecentDrivingConviction only RecentDrivingCondition`<br/>
  A driving history can have a total previous speeding record, and it must be recorded as an instance of RecentDrivingConviction.

12. FirstDrivingConviction → atMonth → xsd:integer
* `FirstDrivingConviction SubClassOf atMonth exactly 1 xsd:integer`<br>
  Each first driving conviction must have exactly one associated month.
* `owl:Thing SubClassOf atMonth only xsd:integer`<br>
  Everthing in ontology may have atMonth, if it does, it must be of datatype integer.

13. FirstDrivingConviction → atYear → xsd:integer
* `FirstDrivingConviction SubClassOf atYear exactly 1 xsd:integer`<br>
  Each first driving conviction must have exactly one associated year.
* `owl:Thing SubClassOf atYear only xsd:integer`<br>
  Everthing in ontology may have atYear, if it does, it must be of datatype integer.

14. RecentDrivingConviction → atYear → xsd:integer
* `RecentDrivingConviction SubClassOf atYear exactly 1 xsd:integer`<br/>
  Each recent driving Conviction must have exactly one associated month.

15. RecentDrivingConviction → atMonth → xsd:integer
* `RecentDrivingConviction SubClassOf atMonth exactly 1 xsd:integer`<br/>
  Each recent driving Conviction must have exactly one associated month.


## EMS

####   Source Pattern:Spatiotemporal-Extent from MODL.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description:
The time from crash reporting to on-scene arrival and transportation to treatment facilities significantly affects the survival result. Capturing the EMS-related data in the graph will allow us to examine the impact of response delays or inefficiencies on fatality rates, providing important information for improving emergency response systems <br/>

![EMS](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/EMS/EMS_Final_Schema.png)


### Axioms

1. EmergencyMedicalService → hasNotificationTime → PointInTime
* `EmergencyMedicalService SubClassOf hasNotificationTime exactly 1 PointInTime`<br />
  Every emergency medical service must have at exactly one notification time.  
* `EmergencyMedicalService SubClassOf hasNotificationTime only PointInTime`<br />
  Every emergency medical service can have notification time, only if its instance of PointInTime.  

2. EmergencyMedicalService → hasArrivalTime → PointInTime
* `EmergencyMedicalService SubClassOf hasArrivalTime exactly 1 PointInTime`<br />
  Every emergency medical service must have exactly one arrival time to the crash site.  
* `EmergencyMedicalService SubClassOf hasArrivalTime only PointInTime`<br />
  Every emergency medical service can have hasArrivalTime, only if its instance of PointInTime.

3. EmergencyMedicalService → hasArrivalTimeToHospital → PointInTime
* `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital exactly 1 PointInTime`<br />
  Every emergency medical service must have exactly one arrival time to the hospital.  
* `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital only PointInTime`<br />
  Every emergency medical service can have arrivalTimeToHospital, only if its instance of PointInTime.

## Impairment

####   Source Pattern: Description Situation Pattern from MODL.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description: 
Road crashes are largely caused by driver impairments like weariness, drug or alcohol usage, and distractions. By capturing these variables, the knowledge graph can show relationships between particular impairments and the chance of a crash, supporting focused awareness campaigns and the implementation of policies.
<br/>

![Impairment](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Impairment/Impairment_Final_Schema.png)

### Axioms

1. Impairments → impairmentsAsString → xsd:string
* `Impairments SubClassOf impairmentsAsString exactly 1 xsd:string`<br />
  Each impairment can have exactly one associated string description. 
* `Impairments SubClassOf impairmentsAsString only xsd:string`<br />
  Each impairment mmay have exactly description, if it does, it must be in string.  

2. SubstanceImpairments → Impairments
* `SubstanceImpairments SubClassOf Impairments`<br />
  Every SubstanceImpairments are Impairments.

3. SubstanceImpairments → substanceImpairmentAsString → xsd:string
* `SubstanceImpairments SubClassOf substanceImpairmentAsString exactly 1 xsd:string`<br />
  Each SubstanceImpairments can have exactly one associated string description. 
* `SubstanceImpairments SubClassOf substanceImpairmentAsString only xsd:string`<br />
  Each SubstanceImpairments mmay have exactly description, if it does, it must be in string. 

4. Distraction → Impairments
* `Distraction SubClassOf Impairments`<br />
  Every Distractions are Impairment.

5. Distraction → distractionAsString → xsd:string
* `Distraction SubClassOf distractionAsString exactly 1 xsd:string`<br />
  Each Distraction can have exactly one associated string description. 
* `Distraction SubClassOf distractionAsString only xsd:string`<br />
  Each Distraction mmay have exactly description, if it does, it must be in string. 


## Person

####   Source Pattern: Agent role Pattern from MODL.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description:
A critical part of any crash data includes the persons involved in a collision: drivers, passengers, and pedestrians. Modeling of person-specific data-such as age, gender, and degree of injury-allows analysis of how demographic characteristics affect collision outcomes and hazards.<br/>

![Person](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Person/Person_Final_Schema.png)

### Axioms

1. Person → hasGender → xsd:string
* `Person SubClassOf hasGender exactly 1 xsd:string`<br/>
  Every Person must have exactly one associated gender, represented as a string.
* `Person SubClassOf hasGender only xsd:string`<br/>
  Every Person may have a hasGender property, and if it exists, it must be a string.

2. Person → hasAge → xsd:integer
* `Person SubClassOf hasAge exactly 1 xsd:integer`<br/>
  Every Person must have exactly one associated age, represented as an integer.
* `Person SubClassOf hasAge only xsd:integer`<br/>
  Every Person may have a hasAge property, and if it exists, it must be an integer.

3. Person → performsPersonInCrash → PersonInCrash
* `Person SubClassOf performsPersonInCrash some PersonInCrash`<br/>
  Every Person must perform at least one PersonInCrash in the context of a crash.
* `Person SubClassOf performsPersonInCrash only PersonInCrash`<br/>
  Every Person may have a performsPersonInCrash property, and if it exists, it must be an instance of PersonInCrash.

4. Crash → providesPersonInCrash → PersonInCrash
* `Crash SubClassOf providesPersonInCrash some PersonInCrash`<br/>
  Every Crash must provide at least one PersonInCrash role.
* `Crash SubClassOf providesPersonInCrash only PersonInCrash`<br/>
  Every Crash may have a providesPersonInCrash property, and if it exists, it must be an instance of PersonInCrash.

5. PersonInCrash → hasInjurySeverity → xsd:string
* `PersonInCrash SubClassOf hasInjurySeverity some xsd:string`<br/>
  Every PersonInCrash must have at least one associated xsd:string.
* `PersonInCrash SubClassOf hasInjurySeverity only xsd:string`<br/>
  Every PersonInCrash may have a hasInjurySeverity property, and if it exists, it must be of type xsd:string.

6. PersonInCrash → hasLagTime → PointInTime  
* `PersonInCrash SubClassOf hasLagTime min 0 PointInTime`<br/>
  Every PersonInCrash may have associated PointInTime representing the lag time between the crash and the fatality.  
* `PersonInCrash SubClassOf hasLagTime only PointInTime`<br/>
  Every PersonInCrash may have the relation hasLagTime; if it does, it must be an instance of PointInTime.

7. NonOccupant → PersonInCrash
* `NonOccupant SubClassOf PersonInCrash`<br/>
  Every NonOccupant is a subclass of PersonInCrash.

8. NonOccupant → locationDuringCrash → xsd:string
* `NonOccupant SubClassOf locationDuringCrash exactly 1 xsd:string`<br/> 
  Every NonOccupant must have exactly one associated location during the crash, represented as a string.
* `NonOccupant SubClassOf locationDuringCrash only xsd:string`<br/>
  Every NonOccupant may have a locationDuringCrash property, and if it exists, it must be a string.

9. Pedestrian → NonOccupant
* `Pedestrian SubClassOf NonOccupant`<br/>
Every Pedestrian is a subclass of NonOccupant.

10. Cyclist → NonOccupant
* `Cyclist SubClassOf NonOccupant`<br/>
  Every Cyclist is a subclass of NonOccupant.

11. Other/PersonalConveyance → NonOccupant
* `Other/PersonalConveyance SubClassOf NonOccupant`<br/>
  Every Other/PersonalConveyance is a subclass of NonOccupant.

12. Occupant → PersonInCrash
* `Occupant SubClassOf PersonInCrash`<br/>
  Every Occupant is a subclass of PersonInCrash.

13. Occupant → seatPosition → xsd:string
* `Occupant SubClassOf seatPosition exactly 1 xsd:string`<br/>
  Every Occupant must have exactly one associated seat position, represented as a string.
* `Occupant SubClassOf seatPosition only xsd:string `<br /> 
  Every Occupant may have a seatPosition property, and if it exists, it must be a string.

14. Occupant → safetyRestraintUsed → xsd:string
* `Occupant SubClassOf safetyRestraintUsed exactly 1 xsd:string`<br/>
  Every Occupant must have exactly one associated safety restraint used, represented as a string.
* `Occupant SubClassOf safetyRestraintUsed only xsd:string`<br/>
  Every Occupant may have a safetyRestraintUsed property, and if it exists, it must be a string.

15. Occupant → hasAirbagDeployed → xsd:string
* `Occupant SubClassOf hasAirbagDeployed exactly 1 xsd:string`<br/>
  Every Occupant must have exactly one associated string value indicating whether an airbag was deployed.
* `Occupant SubClassOf hasAirbagDeployed only xsd:string`<br/>
  Every Occupant may have a hasAirbagDeployed property, and if it exists, it must be a string.

16. Occupant → hasEjectionStatus → xsd:string
* `Occupant SubClassOf hasEjectionStatus exactly 1 xsd:string`<br/>
  Every Occupant must have exactly one associated ejection status, represented as a string.
* `Occupant SubClassOf hasEjectionStatus only xsd:string`<br/>
  Every Occupant may have a hasEjectionStatus property, and if it exists, it must be a string.

17. Driver → Occupant
* `Driver SubClassOf Occupant`<br/>
  Every Driver is a subclass of Occupant.

18. Passenger → Occupant
* `Passenger SubClassOf Occupant`<br/>
Every Passenger is a subclass of Occupant.


## Time

####   Source Pattern: Temporal extent pattern from MODL.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description:
Temporal parameters, such as time of day, season, and day of the week, significantly affect the probability of an accident. The modeling of temporal patterns enables targeted preventive actions to be implemented and helps discover tendencies such as crash peak hours or heightened hazards under particular weather conditions.<br/>

![Time](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Time/Time_Final_Schema.png)

### Axioms

1. PointInTime → TemporalExtent
* `PointInTime SubClassOf TemporalExtent`<br/>
Every PointInTime is a specific instance of TemporalExtent, implying that all PointInTime instances are part of the broader TemporalExtent class.

2. TimeInterval → TemporalExtent
* `TimeInterval SubClassOf TemporalExtent`<br/>
Every TimeInterval is a subclass of TemporalExtent, representing a span or interval of time within the broader temporal framework.

3. PointInTime → hasTimeOfTheDay → xsd:string
* `PointInTime SubClassOf hasTimeOfTheDay only xsd:string<`br/>
  The range of the hasTimeOfTheDay property must belong to the class xsd:string.
* `PointInTime SubClassOf hasTimeOfTheDay some xsd:string`<br/>
  Every PointInTime must have at least one associated xsd:string.

4. PointInTime → hasDayOfTheWeek → xsd:string
* `PointInTime SubClassOf hasDayOfTheWeek only xsd:string`<br/>
  The range of the hasDayOfTheWeek property must belong to the xsd:string.
* `PointInTime SubClassOf hasDayOfTheWeek exactly 1 xsd:string`<br/>
  Every PointInTime must have at max one associated to xsd:string.

5. PointInTime → hasSeason → xsd:string
* `PointInTime SubClassOf hasSeason only xsd:string`<br/>
  The range of the hasSeason property must belong to the xsd:string.
* `PointInTime SubClassOf hasSeason exactly 1 xsd:string`<br/>
  Every PointInTime must have at least one associated xsd:string.

6. TimeInterval → startsAt → xsd:time
* `TimeInterval SubClassOf startsAt only xsd:time`<br/>
  The range of the startsAt property must belong to the class xsd:time.
* `TimeInterval SubClassOf startsAt exactly 1 xsd:time`<br/>
  Every TimeInterval must start at a single specific xsd:time.

7. TimeInterval → endsAt → xsd:time
* `TimeInterval SubClassOf endsAt only xsd:time`<br/>
  The range of the endsAt property must belong to the class xsd:time.
* `TimeInterval SubClassOf endsAt exactly 1 xsd:time`<br/>
  Every TimeInterval must end at a single specific xsd:time.

8. PointInTime → inMinutes → xsd:integer
* `PointInTime SubClassOf inMinutes only xsd:integer`<br/>
  The duration in minutes must be an integer value.
* `PointInTime SubClassOf inMinutes some xsd:integer`<br/>
  Every PointInTime must have at least one associated value in minutes.

9. PointInTime → inHours → xsd:integer
* `PointInTime SubClassOf inHours only xsd:integer`<br/>
  The duration in hours must be an integer value.
* `PointInTime SubClassOf inHours some xsd:integer`<br/>
  Every PointInTime must have at least one associated value in hours.
    

## Crash

####   Source Pattern: Event Pattern from MODL.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description:
The Crash Event is the focal point of the entire knowledge graph. Every piece of data—whether it's about driver behavior, vehicle condition, or road infrastructure—ultimately ties back to the crash event. Modeling a crash event allows us to ask critical questions like "What caused this crash?", "Where and when did it happen?", and "Who was involved?". Understanding each crash as a distinct event with its own unique set of contributing factors is essential to uncover patterns in road accidents, identify high-risk conditions, and develop preventive measures.<br/>

![Crash](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Crash/Crash_Final_Schema.png)



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

9. WeatherCondition → Condition  
* `WeatherCondition SubClassOf Condition`<br/>
  Every weather condition is Condition.

10. WeatherCondition → weatherConditionAsString → xsd:string  
* `WeatherCondition SubClassOf weatherConditionAsString only xsd:string`<br/>
  WeatherCondition may have weatherConditionAsString, if it does it must be a string.
* `WeatherCondition SubClassOf weatherConditionAsString some xsd:string`<br/>
  WeatherCondition must have atleast one weatherConditionAsString and it must be a string.

11. RoadCondition → Condition  
* `RoadCondition SubClassOf Condition`<br/>
  Every Road condition is Condition.

12. RoadCondition → roadConditionAsString → xsd:string  
* `RoadCondition SubClassOf roadConditionAsString only xsd:string`<br/>
  RoadCondition may have roadConditionAsString, if it does it must be a string.
* `RoadCondition SubClassOf roadConditionAsString some xsd:string`<br/>
  RoadCondition must have atleast one roadConditionAsString and it must be a string.

13. LightingCondition → Condition  
* `LightingCondition SubClassOf Condition`<br/>
  Every LightingCondition is Condition.

14. LightingCondition → weatherConditionAsString → xsd:string  
* `LightingCondition SubClassOf lightingConditionAsString only xsd:string`<br/>
  LightingCondition may have LightingConditionAsString, if it does it must be a string.
* `LightingCondition SubClassOf lightingConditionAsString some xsd:string`<br/>
  LightingCondition must have atleast one LightingConditionAsString and it must be a string.

## Location

####   Source Pattern: Spatial Extent Pattern from MODl.<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description:
Geographic Location is crucial for understanding where crashes occur. By linking crash events to specific locations, we can analyze regional accident patterns, assess the impact of urban versus rural roads, and identify accident-prone zones. This helps local authorities prioritize infrastructure improvements and safety interventions. Geographic location also interacts with other factors, such as socioeconomic conditions, traffic density, and weather patterns, to provide a complete picture of crash risks.<br/>

![Location](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Location/Location_Final_Schema.png)


### Axioms

1. Location → hasCoordinates → Coordinates
* `Location SubClassOf hasCoordinates only Coordinates`<br />
  The range of the property hasCoordinates must belong to the class Coordinates.
* `Location SubClassOf hasCoordinates exactly 1 Coordinates`<br />
  Every Location must have exactly one set of Coordinates.

2. Coordinates → hasLatitude → xsd:float
* `Coordinates SubClassOf hasLatitude only xsd:float`<br />
  The range of the property hasLatitude must be a float value.
* `Coordinates SubClassOf hasLatitude some xsd:float` <br />
  Every Coordinates must have at least one Latitude.

3. Coordinates → hasLongitude → xsd:float
* `Coordinates SubClassOf hasLongitude only xsd:float`<br />
  The range of the property hasLongitude must be a float value.
* `Coordinates SubClassOf hasLongitude some xsd:float`<br />
  Every Coordinates must have atleast one Longitude.

4. Location → hasState → State
* `Location SubClassOf hasState only State`<br />
  The range of the property hasState must belong to the class State.
* `Location SubClassOf hasState some State`<br />
  Every Location must have at least one State.

5. State → hasStateName → xsd:string
* `State SubClassOf hasStateName only xsd:string` <br />
  The range of the property hasStateName must be a string value.
* `State SubClassOf hasStateName exactly 1 xsd:string` <br />
  Every State must have exactly one StateName.

6. State → hasCity → City
* `State SubClassOf hasCity only City` <br />
  The range of the property hasCity must belong to the class City.
* `State SubClassOf hasCity some City` <br />
  Every State must have at least one City.

7. City → hasCityName → xsd:string
* `City SubClassOf hasCityName only xsd:string`<br />
  The range of the property hasCityName must be a string value.
* `City SubClassOf hasCityName exactly 1 xsd:string `<br />
  Every City must have exactly one CityName.

8. City → hasCounty → County
* `City SubClassOf hasCounty some County`<br />
  Every City must be associated with at least one County.
* `City SubClassOf hasCounty only County`<br/>
  Every City may be associated with County, if it does, it must be instance of class County.

9. County → hasCountyName → xsd:string
* `County SubClassOf hasCountyName exactly 1 xsd:string`<br />
  Every County must have exactly one CountyName.
* `County SubClassOf hasCountyName only xsd:string`<br />
  Every County may have CountyName, if it does, it must be of type xsd:string.


## SocioEconomic Condition

####   Source Pattern: Description Situation Pattern from MODL.<br/>
####   Data Source: Census Data. <br/>
#### Description:
Rationale: Socioeconomic Factors such as income level, education, and infrastructure investment in a region have a direct impact on road safety. Poorer regions may have older, less safe vehicles and poorly maintained roads, leading to higher accident rates. Understanding the socioeconomic context of crashes helps policymakers target investments and interventions to reduce disparities in road safety across different regions.
<br/>

![SocioEconomicCondition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/SocioEconomic/socioEconomicCondition_Final_Schema.png)

### Axioms

1.Location → hasSocioEconomicCondition → SocioEconomicCondition 
* `Location SubClassOf hasSocioEconomicCondition only SocioEconomicCondition`<br /> 
  The socioeconomic condition of any location must be of type SocioEconomicCondition.
* `Location SubClassOf hasSocioEconomicCondition some SocioEconomicCondition`<br /> 
  Location must have at least one socioeconomic condition.

2. IncomeHouseHoldMedian → SocioEconomicCondition
* `IncomeHouseHoldMedium SubClassOf SocioEconomicCondition`<br />
  Every IncomeHouseHoldMedium is SocioEconomicCondition

3. IncomeHouseHoldMedian → HouseholdIncomeAsInteger → xsd:integer
* `IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal only xsd:decimal`<br /> 
  Every IncomeHouseholdMedian can only have HouseholdIncomeAsInteger values of type xsd:integer
* `IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal some xsd:decimal`<br /> 
  Every IncomeHouseholdMedian must have atleast HoudeholdIncomeAsInteger values of type xsd:integer
    
4. EmploymentRate → SocioEconomicCondition 
* `EmploymentRate SubClassOf SocioEconomicCondition`<br/>
  Every EmploymentRate is SocioEconomicCondition

5. EmploymentRate → employmentRateAsDecimal → xsd:decimal  
* `EmploymentRate SubClassOf employmentRateAsDecimal only xsd:decimal`<br/> 
  Every EmploymentRate can only have employmentRateAsString values of type xsd:decimal.
* `EmploymentRate SubClassOf employmentRateAsDecimal some xsd:decimal`<br/>
  Every EmploymentRate must have employmentRateAsString values of type xsd:decimal.

6. PopulationDensity → SocioEconomicCondition   
* `PopulationDensity SubClassOf SocioEconomicCondition`<br />
  Every PopulationDensity is SocioEconomicCondition

7. PopulationDensity → populationDensityAsDecimal → xsd:decimal 
* `PopulationDensity SubClassOf populationDensityAsDecimal only xsd:decimal`<br /> 
  Every PopulationDensity can only have populationDensityAsString values of type xsd:decimal.
* `PopulationDensity SubClassOf populationDensityAsDecimal some xsd:decimal`<br />
  Every PopulationDensity must have populationDensityAsString values of type xsd:decimal.

8. EducationLevel → SocioEconomicCondition  
* `EducationLevel SubClassOf SocioEconomicCondition`<br />
  Every EducationLevel is SocioEconomicCondition

9. EducationLevel → highSchoolOrHigher → xsd:decimal
* `EducationLevel SubClassOf highSchoolOrHigher only xsd:decimal`<br /> 
  Every EducationLevel can only have highSchoolOrHigher values of type xsd:decimal.
* `EducationLevel SubClassOf highSchoolOrHigher some xsd:decimal`<br />
  Every PopulationDensity must have highSchoolOrHigher values of type xsd:decimal.

10. EducationLevel → bachelorsDegreeOrHigher → xsd:decimal
* `EducationLevel SubClassOf bachelorsDegreeOrHigher only xsd:decimal`<br /> 
  Every EducationLevel can only have bachelorsDegreeOrHigher values of type xsd:decimal.
* `EducationLevel SubClassOf bachelorsDegreeOrHigher some xsd:decimal`<br />
  Every PopulationDensity must have bachelorsDegreeOrHigher values of type xsd:decimal.


## Vehicle

####   Source Pattern: CS-MODL Car (from CS-MODL).<br/>
####   Data Source: Fatality Analysis Reporting System(FARS).<br/>
#### Description: 
Vehicle Condition encompasses the mechanical state of the vehicle, such as the quality of its brakes, tires, and safety features (like airbags or ABS). A well-maintained vehicle can reduce crash severity, while poorly maintained vehicles are more prone to malfunctions that could lead to a crash. In this knowledge graph, capturing vehicle conditions provides insights into how different types of vehicle defects—combined with other factors like road or weather conditions—contribute to accidents. It’s essential to model these conditions dynamically, as vehicle conditions change over time and can vary significantly from one crash event to another.<br/>

![Vehicle](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/Vehicle/Vehicle_Scheme_Final.png)


### Axioms
   
1. Vehicle → hasBodyType → xsd:string
* `Vehicle SubClassOf hasBodyType Exactly 1 xsd:string` <br/>
  Every Vehicle must have exactly one BodyType, represented as a string.
* `Vehicle SubClassOf hasBodyType only xsd:string`<br/>
  Every Vehicle may have a BodyType, and it should be represented as a string.

2. Vehicle → hasVehicleModel → xsd:string
* `hasVehicleModel some xsd:string SubClassOf Vehicle` <br/>
  Anything that has a VehicleModel is classified as a Vehicle.
* `Vehicle SubClassOf hasVehicleModel Exactly 1 xsd:string`<br/>
  Every Vehicle must have exactly one VehicleModel, represented as a string.
* `Vehicle SubClassOf hasVehicleModel only xsd:string` <br/>
  Every Vehicle may have a VehicleModel, and it should be represented as a string.

3. Vehicle → hasVehicleMake → xsd:string
* `hasVehicleMake some xsd:string SubClassOf Vehicle`<br/>
  Anything that has a VehicleMake is classified as a Vehicle.
* `Vehicle SubClassOf hasVehicleMake Exactly 1 xsd:string`<br/>
  Every Vehicle must have exactly one VehicleMake, represented as a string.
* `Vehicle SubClassOf hasVehicleMake only xsd:string`<br/>
  Every Vehicle may have a VehicleMake, and it should be represented as a string.

4. Vehicle → hasVehicleManufacturingYear → xsd:string
* `hasVehicleManufacturingYear some xsd:string SubClassOf Vehicle`<br/>
  Anything that has a VehicleManufacturingYear is classified as a Vehicle.
* `Vehicle SubClassOf hasVehicleManufacturingYear Exactly 1 xsd:string`<br/>
  Every Vehicle must have exactly one VehicleManufacturingYear, represented as a string.
* `Vehicle SubClassOf hasVehicleManufacturingYear only xsd:string`<br/>
  Every Vehicle may have a VehicleManufacturingYear, and it should be represented as a string.

5. Vehicle → hasWeightRange → xsd:string
* `Vehicle SubClassOf hasWeightRange Exactly 1 xsd:string`<br/>
  Every Vehicle must have exactly one WeightRange, represented as a string.
* `Vehicle SubClassOf hasWeightRange only xsd:string`<br/>
  Every Vehicle may have a WeightRange, and it should be represented as a string.

6. Vehicle → hasVIN → xsd:string
* `hasVIN some xsd:string SubClassOf Vehicle`<br/>
  Anything that has a VIN is classified as a Vehicle.
* `Vehicle SubClassOf hasVIN Exactly 1 xsd:string`<br/>
  Every Vehicle must have exactly one VIN, represented as a string.
* `Vehicle SubClassOf hasVIN only xsd:string`<br/>
  Every Vehicle may have a VIN, and it should be represented as a string.

7. VehicleInCrash → hasMannerOfCollision → xsd:string
* `VehicleInCrash SubClassOf hasMannerOfCollision Exactly 1 xsd:string`<br/>
  Every VehicleInCrash must have exactly one MannerOfCollision, represented as a string.
* `VehicleInCrash SubClassOf hasMannerOfCollision only xsd:string` <br/>
  Every VehicleInCrash may have a MannerOfCollision, and it should be represented as a string.

8. VehicleInCrash → hasSpeed → xsd:integer
* `VehicleInCrash SubClassOf hasSpeed Exactly 1 xsd:integer`<br/>
  Every VehicleInCrash must have exactly one Speed, represented as an integer.
* `VehicleInCrash SubClassOf hasSpeed only xsd:integer`<br/>
  Every VehicleInCrash may have a Speed, and it should be represented as an integer.

9. VehicleInCrash → involvedInHitAndRun → xsd:boolean
* `VehicleInCrash SubClassOf involvedInHitAndRun only xsd:boolean`<br/>
  VehicleInCrash involved in hit-and-run must be represented as a boolean value.
* `VehicleInCrash SubClassOf involvedInHitAndRun some xsd:boolean` <br/>
  Every VehicleInCrash must have a Hit and Run status.

10. VehicleInCrash → hasTrailingUnit → xsd:string
* `VehicleInCrash SubClassOf hasTrailingUnit Exactly 1 xsd:string`<br/>
  Every VehicleInCrash must have exactly one TrailingUnit, represented as a string.
* `VehicleInCrash SubClassOf hasTrailingUnit only xsd:string`<br/>
  Every VehicleInCrash may have a TrailingUnit, and it should be represented as a string.

11. Vehicle → performsVehicleInCrash → VehicleInCrash
* `performsVehicleInCrash some VehicleInCrash SubClassOf Vehicle`<br/>
  Anything that performs a VehicleInCrash is classified as a Vehicle.
* `Vehicle SubClassOf performsVehicleInCrash Exactly 1 VehicleInCrash`<br/>
  Every Vehicle must have exactly one performsVehicleInCrash, represented as an instance of VehicleInCrash.
* `Vehicle SubClassOf performsVehicleInCrash only VehicleInCrash`<br/>
  Every Vehicle may perform a VehicleInCrash, and it should be represented as an instance of class VehicleInCrash.

12. Crash → providesVehicleInCrash → VehicleInCrash
* `providesVehicleInCrash some VehicleInCrash SubClassOf Crash` <br/>
  Anything that provides a VehicleInCrash is classified as a Crash.
* `Crash SubClassOf providesVehicleInCrash some VehicleInCrash`<br/>
  Every Crash must provide at least one VehicleInCrash, represented as a string.
* `Crash SubClassOf providesVehicleInCrash only VehicleInCrash`<br/>
  Every Crash may provide a VehicleInCrash, and it should be represented as an instance of VehicleInCrash.


## The Overall Knowledge Graph
### Namespaces
* @base <http://www.soloflife.org> .
* @prefix sol-ont: <http://soloflife.org/lod/ontology/> .
* @prefix sol-qk: <http://soloflife.org/lod/quantitykinds> .
* @prefix sol-unit: <http://soloflife.org/lod/units> .
* @prefix solr: <http://soloflife.org/lod/resource/> .

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


