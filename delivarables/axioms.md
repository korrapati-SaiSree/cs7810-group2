# Road Crashes Ontology

![Road Crashes all together](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/Schema_Diagram/All_Together/All_Together_Final_Schema.png)

## Driver Condition

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
  Each Distraction may have description, if it does, it must be in string. 


## Person

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
