# Road Crashes Ontology

![Road Crashes all together](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/allTogether/allTogether.png)

## Driver Condition

![Driver Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/DriverCondition/DriverCondition.png)


### Axioms

1. Driver → hasDrivingHistory → DrivingHistory <br />
    * `Driver SubClassOf hasDrivingHistory some DrivingHistory` <br />
        Every driver must have at least one associated driving history.
    * `Driver SubClassOf hasDrivingHistory only DrivingHistory` <br />
        Every drivers are associated with a driving history, and if they have any driving history, it must be represented as an instance of the DrivingHistory class

2. Driver → hasImpairments → Impairments <br />
    * `Driver SubClassOf hasImpairments min 0 Impairments` <br />
        A driver may have impairments.
    * `Driver SubClassOf hasImpairments only Impairments` <br />
        All drivers can have impairments, and if they do, those impairments must be instances of the Impairments class.

3. DrivingHistory → hasTrafficViolation → TrafficViolation <br />
    * `DrivingHistory SubClassOf hasTrafficViolation min 0 TrafficViolation` <br />
        A driving history may have TrafficViolation.
    * `DrivingHistory SubClassOf hasTrafficViolation only TrafficViolation` <br />
        A DrivingHistory can have TrafficViolation, and if they do, those trafficViolations must be instances of TrafficViolation.

4. DrivingHistory → hasDrivingExperience → DrivingExperience <br />
    * `DrivingHistory SubClassOf hasDrivingExperience some DrivingExperience` <br />
        A driving history must include at least one driving experience.
    * `DrivingHistory SubClassOf hasDrivingExperience only DrivingExperience` <br />
        A DrivingHistory can have DrivingExperience, and if they do, those DrivingExperience must be instance of DrivingExperience.

5. TrafficViolation → licenseSuspension → xsd <br />
    * `TrafficViolation SubClassOf licenseSuspension only xsd:string` <br />
        A traffic violation may result in a license suspension, and it has to be recorded as a string.
    * `TrafficViolation SubClassOf licenseSuspension exactly 1 xsd:string` <br />
        A traffic violation can have exactly one associated license suspension.

6. TrafficViolation → violationType → xsd <br />
    * `TrafficViolation SubClassOf violationType only xsd:string` <br />
        A traffic violation may result in a violationType, and it has to be recorded as a string.
    * `TrafficViolation SubClassOf violationType exactly 1 xsd:string` <br />
        Each traffic violation must have exactly one type.

7. TrafficViolation → violationDate → TemporalExtent <br />
    * `TrafficViolation SubClassOf violationDate some TemporalExtent` <br />
        Every traffic violation is associated with a temporal extent.
    * `TrafficViolation SubClassOf violationDate only TemporalExtent` <br />
        Every TrafficViolation is restricted to having only TemporalExtent classified as instances of the TemporalExtent class.

8. DrivingExperience → totalYearsOfDriving → TemporalExtent <br />
    * `DrivingExperience SubClassOf totalYearsOfDriving some TemporalExtent` <br />
        A driving experience must include total years of driving.
    * `DrivingExperience SubClassOf violationDate only TemporalExtent` <br />
        Every DrivingExperience is restricted to having only TemporalExtent classified as instances of the TemporalExtent class.

9. DrivingExperience → experienceLevel → ExperienceLevel <br />
    * `DrivingExperience SubClassOf experienceLevel some ExperienceLevel` <br />
        Every driving experience must have at least one experience level.
    * `DrivingExperience SubClassOf experienceLevel only ExperienceLevel` <br />
        Every DrivingExperience is restricted to having only experienceLevel classified as instances of the ExperienceLevel class.

10. Driver → hasLicenseStatus → xsd <br />
    * `Driver SubClassOf hasLicenseStatus exactly 1 xsd:string` <br />
        Each driver must have exactly one license status.
    * `Driver SubClassOf hasLicenseStatus only xsd:string` <br />
        Every Driver can have licenseStatus, if they do, it must be xsd:string.


## EMS

![EMS](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/EMS/EMS.png)


### Axioms

1. EmergencyMedicalService → hasNotificationTime → TemporalExtent <br />
    * `EmergencyMedicalService SubClassOf hasNotificationTime some TemporalExtent` <br />
        Every emergency medical service must have at least one notification time.  
    * `EmergencyMedicalService SubClassOf hasNotificationTime max 1 TemporalExtent` <br />
        Every emergency medical service must have at max one notification time.
    * `EmergencyMedicalService SubClassOf hasNotificationTime only TemporalExtent` <br />
        Every emergency medical service can have notification time, only if its instance of TemporalExtent.  

2. EmergencyMedicalService → hasArrivalTimeToCrash → TemporalExtent <br />
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash some TemporalExtent` <br />
        Every emergency medical service must have at least one arrival time to the crash site.  
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash max 1 TemporalExtent` <br />
        Every emergency medical service must have at max one arrival time to the crash site.
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash only TemporalExtent` <br />
        Every emergency medical service can have ArrivalTimeToCrash, only if its instance of TemporalExtent.

3. EmergencyMedicalService → hasArrivalTimeToHospital → TemporalExtent <br />
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital some TemporalExtent` <br />
        Every emergency medical service must have at least one arrival time to the hospital.  
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital max 1 TemporalExtent` <br />
        Every emergency medical service must have at max one arrival time to the hospital.
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital only TemporalExtent` <br />
        Every emergency medical service can have arrivalTimeToHospital, only if its instance of TemporalExtent.

## Impairment
![Impairment](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/Impairment/Impairment.png)

### Axioms

1. Impairments → impairmentsAsString → xsd <br />
    * `Impairments SubClassOf impairmentsAsString exactly 1 xsd:string` <br />
        Each impairment can have exactly one associated string description.  

2. SubstanceImpairments → Impairments <br />
    * `SubstanceImpairments SubClassOf Impairments` <br />
        Every SubstanceImpairments are Impairments.

3. Distraction → Impairments <br />
    * `Distraction SubClassOf Impairments` <br />
        Every Distractions are Impairment.

## Person

![image](https://github.com/user-attachments/assets/47d87a0a-8f75-4560-a253-9c1f6bd8aec7)

### Axioms

1. Person → hasGender → xsd <br />
    * `Person SubClassOf hasGender exactly 1 xsd:string` <br />
        A person can have exactly one associated gender.  
    * `Person SubClassOf hasGender only xsd:string` <br />
        Every Person can have relation hasGender, if it does it has to be of type string.

2. Person → hasAge → xsd <br />
    * `Person SubClassOf hasAge exactly 1 xsd:integer` <br />
        A person can have exactly one associated age.  
    * `Person SubClassOf hasAge only xsd:integer` <br />
        Every Person can have relation hasAge, if it does it has to be of type integer.  
    
3. Person → performsPersonInCrash → PersonInCrash <br />
    * `Person SubClassOf performsPersonInCrash some PersonInCrash` <br />
        Every person must perform at least one PersonInCrash in the context of a crash.
    * `Person SubClassOf performsPersonInCrash only PersonInCrash` <br />
        Every Person can have performsPersonInCrash,if they do, it must be instance of class PersonInCrash.

4. Crash → providesPersonInCrash → PersonInCrash <br />
    * `Crash SubClassOf providesPersonInCrash some PersonInCrash` <br />
        Every crash must provide at least one PersonInCrash role.
    * `Crash SubClassOf providesPersonInCrash only PersonInCrash` <br />
        Every Crash can have providesPersonInCrash,if they do, it must be instance of class PersonInCrash.

5. PersonInCrash → hasInjurySeverity → InjurySeverity <br />
    * `PersonInCrash SubClassOf hasInjurySeverity some InjurySeverity` <br />
        Every person in a crash must have at least one associated injury severity.
    * `PersonInCrash SubClassOf hasInjurySeverity only InjurySeverity` <br />
        Every person in a crash can have injury severity, if it does, it must be instance of class InjurySeverity.

6. PersonInCrash → isFatal → Fatality <br />
    * `PersonInCrash SubClassOf isFatal some Fatality` <br />
        Every person in a crash who is fatal must have an associated Fatality record.
    * `PersonInCrash SubClassOf isFatal only Fatality` <br />
        Every person in a crash who is fatal must be instance of class Fatality.

7. Fatality → hasLagTime → TemporalExtent <br />
    * `Fatality SubClassOf hasLagTime exactly 1 TemporalExtent` <br />
        Every fatality must have exactly one associated TemporalExtent for the lag time, representing the time between the crash and the fatality.
    * `Fatality SubClassOf hasLagTime only TemporalExtent` <br />
        Every fatality may have lag Time, if it does, it must be instance of TemporalExtent.

8. NonOccupant → PersonInCrash  <br />
    * `NonOccupant SubClassOf PersonInCrash` <br />
        Every NonOccupant is PersonInCrash.

9. NonOccupant → locationDuringCrash → xsd <br />
    * `NonOccupant SubClassOf locationDuringCrash exactly 1 xsd:string` <br />
        Every non-occupant must have exactly one associated location during the crash.
    * `NonOccupant SubClassOf locationDuringCrash only xsd:string` <br />
        Every non-occupant may have location during the crash, if it does, it must be of type string.

10. Pedestrian → NonOccupant <br />
    * `Pedestrian SubClassOf NonOccupant` <br />
        Every Pedestrain is NonOccupant.

11. Cyclist → NonOccupant <br />
    * `Cyclist SubClassOf NonOccupant` <br />
        Every Cyclist is NonOccupant.

12. Occupant → PersonInCrash <br />
    * `Occupant SubClassOf PersonInCrash` <br />
        Every Occupant is PersonInCrash.

13. Occupant → seatPosition → xsd <br />
    * `Occupant SubClassOf seatPosition exactly 1 xsd:string` <br />
        Every occupant must have exactly one associated seat position.
    * `Occupant SubClassOf seatPosition only xsd:string` <br />
        Every occupant may have seat position, if it does it must be of type string.

14. Occupant → safetyRestraintUsed → xsd <br />
    * `Occupant SubClassOf safetyRestraintUsed exactly 1 xsd:string` <br />
        Every occupant must have exactly one associated safety restraint used.
    * `Occupant SubClassOf safetyRestraintUsed only xsd:string` <br />
        Every occupant may have safety restraint used, if it does, it must be of type string.

15. Occupant → hasAirbagDeployed → xsd <br />
    * `Occupant SubClassOf hasAirbagDeployed exactly 1 xsd:boolean` <br />
        Every occupant must have exactly one associated boolean value indicating whether an airbag was deployed.
    * `Occupant SubClassOf hasAirbagDeployed only xsd:boolean` <br />
        Every occupant may have airbagDeployed, if they do, it must be of type boolean.

16. Occupant → hasEjectionStatus → xsd <br />
    * `Occupant SubClassOf hasEjectionStatus exactly 1 xsd:string` <br />
        Every occupant must have exactly one associated ejecetion status.
    * `Occupant SubClassOf hasAirbagDeployed only xsd:boolean` <br />
        Every occupant may have ejection status, if they do, it must be of type string.

17. Driver → Occupant <br />
    * `Driver SubClassOf Occupant` <br />
        Every Driver is Occupant.

18. Passenger → Occupant <br />
    * `Passenger SubClassOf Occupant` <br />
        Every Passenger is Occupant.

## Time

![Time](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/Time/Time.png)

### Axioms

1. PointInTime → TemporalExtent <br />
    * `PointInTime SubClassOf TemporalExtent` <br />
        Every PointInTime is a specific instance of TemporalExtent, implying that all PointInTime instances are part of the broader TemporalExtent class.
   
2. TimeInterval → TemporalExtent <br />
    * `TimeInterval SubClassOf TemporalExtent` <br />
        Every TimeInterval is a subclass of TemporalExtent, representing a span or interval of time within the broader temporal framework.

3. PointInTime → hasTimeOfTheDay → TimeOfDay <br />
    * `PointInTime SubClassOf hasTimeOfTheDay only TimeOfDay` <br />
        The range of the hasTimeOfTheDay property must belong to the class TimeOfDay.
    * `PointInTime SubClassOf hasTimeOfTheDay some TimeOfDay` <br />
        Every PointInTime must have at least one associated TimeOfDay.

4. PointInTime → hasDayOfTheWeek → DayOfTheWeek <br />
    * `PointInTime SubClassOf hasDayOfTheWeek only DayOfTheWeek` <br />
        The range of the hasDayOfTheWeek property must belong to the class DayOfTheWeek.
    * `PointInTime SubClassOf hasDayOfTheWeek exactly 1 DayOfTheWeek` <br />
        Every PointInTime must have at max one associated DayOfTheWeek.

5. PointInTime → hasSeason → Season <br />
    * `PointInTime SubClassOf hasSeason only Season` <br />
        The range of the hasSeason property must belong to the class Season.
    * `PointInTime SubClassOf hasSeason exactly 1 Season` <br />
        Every PointInTime must have at least one associated Season.

6. PointInTime → pointInTimeAsDateTime → xsd <br />
    * `PointInTime SubClassOf pointInTimeAsDateTime exactly 1 xsd:dateTime` <br />
        Every PointInTime must have exactly one associated pointInTimeAsDateTime as type xsd:datetime.
    * `PointInTime SubClassOf pointInTimeAsDateTime only xsd:dateTime` <br />
        Every PointInTime may have pointInTimeAsDateTime,if they do they must be type as xsd:datetime.

7. TimeInterval → startsAt → PointInTime <br />
    * `TimeInterval SubClassOf startsAt only PointInTime` <br />
        The range of the startsAt property must belong to the class PointInTime.
    * `TimeInterval SubClassOf startsAt exactly 1 PointInTime` <br />
        Every TimeInterval must start at a single specific PointInTime.

8. TimeInterval → endsAt → PointInTime <br />
    * `TimeInterval SubClassOf endsAt only PointInTime` <br />
        The range of the endsAt property must belong to the class PointInTime.
    * `TimeInterval SubClassOf endsAt exactly 1 PointInTime` <br />
        Every TimeInterval must end at a single specific PointInTime.

## Crash

![image](https://github.com/user-attachments/assets/1e6d8bfd-3ee3-4f5c-a9e5-17053fa76e4c)



### Axioms

1. Crash → hasTemporalExtent → TemporalExtent <br />
    * `Crash SubClassOf hasTemporalExtent only TemporalExtent` <br />
        The range of the property hasTemporalExtent must belong to the class TemporalExtent.
    * `Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent` <br />
        Every Crash must have exactly one associated temporal extent.

2. Crash → occurredAt → Location <br />
    * `Crash SubClassOf occurredAt only Location` <br />
        The range of the property occurredAt must belong to the class Location.
    * `Crash SubClassOf occurredAt exactly 1 Location` <br />
        Every Crash must occur at exactly one location.

3. Location → hasWorkZoneName → WorkZoneName <br />
    * `Location SubClassOf hasWorkZoneName only WorkZoneName` <br />
        The range of the property hasWorkZoneName must belong to the class WorkZoneName.
    * `Location SubClassOf hasWorkZoneName some WorkZoneName` <br />
        Every Location must have at least one WorkZoneName.

4. Location → hasWeatherCondition → WeatherCondition  
    * `Location SubClassOf hasWeatherCondition only WeatherCondition` <br />
        The weather condition of any Location must be of type WeatherCondition.

    * `Location SubClassOf hasWeatherCondition some WeatherCondition` <br />
        Every Location must have at least one WeatherCondition.

5. Location → hasLightingCondition → LightingCondition  
    * `Location SubClassOf hasLightingCondition only LightingCondition` <br />
        The Lighting condition of any Location must be of type LightingCondition.

    * `Location SubClassOf hasLightingCondition some LightingCondition` <br />
        Every Location must have at least one LightingCondition.  

6. Location → hasIntersectionName → IntersectionName <br />
    * `Location SubClassOf hasIntersectionName only IntersectionName` <br />
        The range of the property hasIntersectionName must belong to the class IntersectionName.
    * `Location SubClassOf hasIntersection exactly 1 Intersection` <br />
        Every Location must have exactly one IntersectionName.

7. Crash → hasTotalFatalities → xsd <br />
    * `Crash SubClassOf hasTotalFatalities only xsd:integer` <br />
        The range of the property hasTotalFatalities must be an integer.
    * `Crash SubClassOf hasTotalFatalities min 0 xsd:integer` <br />
        Every Crash may have associated integer value representing total fatalities.
      
8. Crash → hasTotalParticipants → xsd <br />
    * `Crash SubClassOf hasTotalParticipants only xsd:integer` <br />
        The range of the property hasTotalParticipants must be an integer.
    * `Crash SubClassOf hasTotalFatalities min 0 xsd:integer` <br />
        Every Crash may have associated integer value representing total number of participants.

9. Crash → hasTotalVehicles → xsd <br />
    * `Crash SubClassOf hasTotalVehicles only xsd:integer` <br />
        The range of the property hasTotalVehicles must be an integer.
    * `Crash SubClassOf hasTotalVehicles min 0 xsd:integer` <br />
        Every Crash may have associated integer value representing total number of vehicles.

10. Crash → hasParticipant → Participant <br />
    * `Crash SubClassOf hasParticipant only Participant` <br />
        The range of the property hasParticipant must belong to the class Participant.
    * `Crash SubClassOf hasParticipant some Participant` <br />
        Every Crash must have at least one associated Participant.

11. Participant Subclass Relationships <br />
    * Person → Participant <br />
        * `Person SubClassOf Participant` <br />
            Every Person is a subclass of Participant.
    * Vehicle → Participant <br />
        * `Vehicle SubClassOf Participant` <br />
            Every Vehicle is a subclass of Participant.
    * EMS → Participant <br />
        * `EMS SubClassOf Participant` <br />
            Every EMS (Emergency Medical Service) is a subclass of Participant.

## Location

![Location](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/location/Location.png)

### Axioms

1. Location → hasWorkZone → WorkZone <br />
    * `Location SubClassOf hasWorkZone only WorkZone` <br />
        The range of the property hasWorkZone must belong to the class WorkZone.
    * `Location SubClassOf hasWorkZone some WorkZone` <br />
        Every Location must have at least one WorkZone.

2. Location → hasIntersection → Intersection <br />
    * `Location SubClassOf hasIntersection only Intersection` <br />
        The range of the property hasIntersection must belong to the class Intersection.
    * `Location SubClassOf hasIntersection exactly 1 Intersection` <br />
        Every Location must have exactly one Intersection.

3. Location → hasCoordinates → Coordinates <br />
    * `Location SubClassOf hasCoordinates only Coordinates` <br />
        The range of the property hasCoordinates must belong to the class Coordinates.
    * `Location SubClassOf hasCoordinates exactly 1 Coordinates` <br />
        Every Location must have exactly one set of Coordinates.

4. Coordinates → hasLatitude → xsd <br />
    * `Coordinates SubClassOf hasLatitude only xsd:float` <br />
        The range of the property hasLatitude must be a float value.
    * `Coordinates SubClassOf hasLatitude some xsd:float` <br />
        Every Coordinates must have at least one Latitude.

5. Coordinates → hasLongitude → xsd <br />
    * `Coordinates SubClassOf hasLongitude only xsd:float` <br />
        The range of the property hasLongitude must be a float value.
    * `Coordinates SubClassOf hasLongitude some xsd:float` <br />
        Every Coordinates must have atleast one Longitude.

6. Location → hasState → State <br />
    * `Location SubClassOf hasState only State` <br />
        The range of the property hasState must belong to the class State.
    * `Location SubClassOf hasState some State` <br />
        Every Location must have at least one State.

7. State → hasStateName → xsd <br />
    * `State SubClassOf hasStateName only xsd:string` <br />
        The range of the property hasStateName must be a string value.
    * `State SubClassOf hasStateName exactly 1 xsd:string` <br />
        Every State must have exactly one StateName.

8. State → hasCity → City <br />
    * `State SubClassOf hasCity only City` <br />
        The range of the property `hasCity` must belong to the class City.
    * `State SubClassOf hasCity some City` <br />
        Every State must have at least one City.

9. City → hasCityName → xsd <br />
    * `City SubClassOf hasCityName only xsd:string` <br />
        The range of the property hasCityName must be a string value.
    * `City SubClassOf hasCityName exactly 1 xsd:string` <br />
        Every City must have exactly one CityName.

10. City → hasZipCode → xsd <br />
    * `City SubClassOf hasZipCode some xsd:string` <br />
        Every City must have at least one associated ZipCode.
    * `City SubClassOf hasZipCode only xsd:string` <br />
        Every City may have associated ZipCode, if it does, it must be of type xsd:string.

11. City → hasCounty → County <br />
    * `City SubClassOf hasCounty some County` <br />
        Every City must be associated with at least one County.
    * `City SubClassOf hasCounty only County` <br />
        Every City may be associated with County, if it does, it must be instance of class County.

12. County → hasCountyName → xsd <br />
    * `County SubClassOf hasCountyName exactly 1 xsd:string` <br />
        Every County must have exactly one CountyName.
    * `County SubClassOf hasCountyName only xsd:string` <br />
        Every County may have CountyName, if it does, it must be of type xsd:string.

13. County → hasStreet → Street <br />
    * `County SubClassOf hasStreet some Street` <br />
        Every County must have at least one Street.
    * `County SubClassOf hasStreet only Street` <br />
        Every County may have Street, if it does, it must be instance of class Street.

14. Street → hasStreetName → xsd <br />
    * `Street SubClassOf hasStreetName exactly 1 xsd:string` <br />
        Every Street must have exactly one StreetName.
    * `Street SubClassOf hasStreetName only xsd:string` <br />
        Every Street may have StreetName, if it does, it must be of type xsd:string.

15. County → hasZipCode → xsd <br />
    * `County SubClassOf hasZipCode only xsd:string` <br />
        The range of the property hasZipCode must be a string value.
    * `County SubClassOf hasZipCode some xsd:string` <br />
        Every County must have at least one associated ZipCode.

## SocioEconomic Condition
![SocioEconomic Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/socioeconomic_Factors/socioEconomicCondition.png)

### Axioms

1. Location → hasSocioEconomicCondition → SocioEconomicCondition <br />  
    * `Location SubClassOf hasSocioEconomicCondition only SocioEconomicCondition` <br /> 
        The socioeconomic condition of any location must be of type SocioEconomicCondition.
    * `Location SubClassOf hasSocioEconomicCondition some SocioEconomicCondition` <br /> 
         Location must have at least one socioeconomic condition.

2. SocioEconomicCondition → hasTemporalExtent → TemporalExtent <br /> 
    * `SocioEconomicCondition SubClassOf hasTemporalExtent only TemporalExtent` <br /> 
        The temporal extent of any SocioEconomicCondition must be TemporalExtent.
    * `SocioEconomicCondition SubClassOf hasTemporalExtent some TemporalExtent` <br /> 
        Every SocioEconomicCondition must have at least one temporal extent.

3.  IncomeHouseHoldMedian → SocioEconomicCondition <br /> 
    * `IncomeHouseHoldMedium SubClassOf SocioEconomicCondition` <br />
        Every IncomeHouseHoldMedium is SocioEconomicCondition

4. IncomeHouseHoldMedian → incomeHouseholdMedianAsDecimal → xsd <br /> 
    * `IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal only xsd:decimal` <br /> 
        Every IncomeHouseholdMedian can only have incomeHouseHoldMediumAsString values of type xsd:decimal
    * `IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal some xsd:decimal` <br /> 
        Every IncomeHouseholdMedian must have atleast incomeHouseholdMedianAsDecimal values of type xsd:decimal
    

5. EmploymentRate → SocioEconomicCondition 
    * `EmploymentRate SubClassOf SocioEconomicCondition` <br />
        Every EmploymentRate is SocioEconomicCondition

6. EmploymentRate → employmentRateAsDecimal → xsd  
    * `EmploymentRate SubClassOf employmentRateAsDecimal only xsd:decimal`  
        Every EmploymentRate can only have employmentRateAsString values of type xsd:decimal.
    * `EmploymentRate SubClassOf employmentRateAsDecimal some xsd:decimal`  
        Every EmploymentRate must have employmentRateAsString values of type xsd:decimal.

7.  PopulationDensity → SocioEconomicCondition   
    * `PopulationDensity SubClassOf SocioEconomicCondition` <br />
    Every PopulationDensity is SocioEconomicCondition

8. PopulationDensity → populationDensityAsDecimal → xsd  
    * `PopulationDensity SubClassOf populationDensityAsDecimal only xsd:decimal`  
        Every PopulationDensity can only have populationDensityAsString values of type xsd:string.
    * `PopulationDensity SubClassOf populationDensityAsDecimal some xsd:decimal`  
        Every PopulationDensity must have populationDensityAsString values of type xsd:string.

9.  EducationLevel → SocioEconomicCondition  
    * `EducationLevel SubClassOf SocioEconomicCondition` <br />
    Every EducationLevel is SocioEconomicCondition

## Vehicle

![Vehicle](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/vehicle/Vehicle.png)

### Axioms

1. Vehicle → hasVehicleType → xsd  
    * `hasVehicleType some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleType is classified as a Vehicle.
    * `Vehicle SubClassOf hasVehicleType Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleType, represented as a string
    * `Vehicle SubClassOf hasVehicleType only xsd:string` <br />
        Every Vehicle may have VehicleType,and it should be represented as a string

2. Vehicle → hasVehicleModel → xsd  
    * `hasVehicleModel some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleModel is classified as a Vehicle.
    * `Vehicle SubClassOf hasVehicleModel Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleModel, represented as a string
    * `Vehicle SubClassOf hasVehicleModel only xsd:string` <br />
        Every Vehicle may have VehicleModel,and it should be represented as a string

3. Vehicle → hasVehicleMake → xsd  
    * `hasVehicleMake some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleMake is classified as a Vehicle.
    * `Vehicle SubClassOf hasVehicleMake Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleMake, represented as a string
    * `Vehicle SubClassOf hasVehicleMake only xsd:string` <br />
        Every Vehicle may have VehicleMake,nad it should be represented as a string

4. Vehicle → hasVehicleManufacturingYear → xsd  
    * `hasVehicleManufacturingYear some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleManufacturingYear is classified as a Vehicle.
    * `Vehicle SubClassOf hasVehicleManufacturingYear Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleManufacturingYear, represented as a string
    * `Vehicle SubClassOf hasVehicleManufacturingYear only xsd:string` <br />
        Every Vehicle may have VehicleManufacturingYear,and it should be represented as a string

5. Vehicle → hasWeight → Weight  
    * `OWL:Thing SubClassOf hasWeight only Weight` <br />
        Everything that has a weight is restricted to having only weights classified as instances of the Weight class.
    * `Vehicle SubClassOf hasWeight exactly 1 Weight` <br />
        Every Vehicle must have exactly one weight.

6. Weight → rangeFrom → xsd  
    * `Weight SubClassOf rangeFrom only xsd:integer` <br />
        Every Weight can only have rangeFrom values of type xsd:integer.  
    * `Weight SubClassOf rangeFrom exactly 1 xsd:integer`  
        Every weight must have exactly one starting range value as an integer.

7. Weight → rangeTo → xsd  
    * `Weight SubClassOf rangeTo only xsd:integer` <br />
        Every Weight can only have rangeTo values of type xsd:integer.  
    * `Weight SubClassOf rangeTo exactly 1 xsd:integer`  
        Every weight must have exactly one ending range value as an integer.

8. Vehicle → performsVehicleInAccident → VehicleInAccident  
    * `VehicleInAccident SubClassOf Vehicle` <br />
        Every VehicleInAccident is Vehicle
    * `PerformsVehicleInAccident some VehicleInAccident SubClassOf Vehicle` <br />
        Anything that performs a role in a vehicle accident is a type of vehicle.
    * `Vehicle SubClassOf PerformsVehicleInAccident some VehicleInAccident` <br />
        Every vehicle performs at least one role in a vehicle accident.
    * `VehicleInAccident SubClassOf PerformsVehicleInAccident- some Vehicle` <br />
        Every vehicle involved in an accident is the object of a role performed by some vehicle.

9. Crash → providesVehicleInAccident → VehicleInAccident
    * `Crash SubClassOf providesVehicleInAccident some VehicleInAccident` <br />
        Every crash must provide at least one VehicleInAccident role.

10. VehicleInAccident → hasSpeed → xsd  
    * `VehicleInAccident SubClassOf hasSpeed only xsd:integer` <br />
        Every VehicleInAccident can only have speed of type xsd:integer
    
    * `VehicleInAccident SubClassOf hasSpeed min 0 VehicleInAccident` <br />
        Every VehicleInAccident may have Speed of type xsd:integer.

11. VehicleInAccident → hasMileage → xsd  
    * `VehicleInAccident SubClassOf hasMileage only xsd:float` <br />
        Every VehicleInAccident can only have Mileage of type xsd:float

    * `hasMileage some xsd:integer SubClassOf VehicleInAccident` <br />
        Anything that hasMileage is classified as a VehicleInAccident

    * `VehicleInAccident SubClassOf hasMileage exactly 1 xsd:float` <br />
        VehicleInAccident can have exactly one mileage value as a float.

12. VehicleInAccident → involvedInHitAndRun → xsd  
    * `VehicleInAccident SubClassOf involvedInHitAndRun only xsd:Boolean` <br />
        vehicleInAccident involved in hit-and-run must be represented as a boolean value

    * `involvedInHitAndRun some xsd:Boolean SubClassOf VehicleInAccident` <br />
        Anything associated with a hit-and-run boolean value is classified as a vehicleInAccident

13. VehicleInAccident → hasTemporalExtent → TemporalExtent  
    * `VehicleInAccident SubClassOf hasTemporalExtent only TemporalExtent` <br />
        The temporal extent (time period) of any vehicle involved in an accident must be TemporalExtent.

    * `VehicleInAccident SubClassOf hasTemporalExtent some TemporalExtent` <br />
        Every vehicle involved in an accident must have at least one temporal extent.

## Weather

![Weather](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/weather/WeatherCondition.png)

### Axioms

1. Location → hasWeatherCondition → WeatherCondition  
    * `Location SubClassOf hasWeatherCondition only WeatherCondition` <br />
        The weather condition of any Location must be of type WeatherCondition.

    * `Location SubClassOf hasWeatherCondition some WeatherCondition` <br />
        Every Location must have at least one WeatherCondition.  

2. WeatherCondition → hasTemperature → Temperature  
    * `WeatherCondition SubClassOf hasTemperature only Temperature` <br />
        The Temperature of every WeatherCondition must be of type Temperature.  

    * `WeatherCondition SubClassOf hasTemperature some Temperature` <br />
        Every WeatherCondition must have at least one Temperature.  

3. WeatherCondition → hasPercipitation → Percipitation  
    * `WeatherCondition SubClassOf hasPrecipitation only Percipitation` <br />
        The Precipitation of every WeatherCondition must be of type Precipitation.  

    * `WeatherCondition SubClassOf hasPercipitation Exactly 1 Percipitation` <br />
        Every weather condition must have exactly one precipitation value associated with it

4. WeatherCondition → hasTemporalExtent → TemporalExtent  
    * `WeatherCondition SubClassOf hasTemporalExtent only TemporalExtent` <br />
        The TemporalExtent of every WeatherCondition must be of type TemporalExtent.  

    * `WeatherCondition SubClassOf hasTemporalExtent some TemporalExtent` <br />
        Every WeatherCondition must have at least one TemporalExtent.  

5. WeatherCondition → weatherConditionAsString → xsd  
    * `WeatherCondition SubClassOf weatherConditionAsString only xsd:string` <br />
        Every WeatherCondition can only have weatherConditionAsString values of type xsd:string. 

    * `WeatherCondition SubClassOf weatherConditionAsString exactly 1 xsd:string` <br />
        Every WeatherCondition must have exactly one string representing its description.  

6. Temperature → inCelsius → xsd  
    * `Temperature SubClassOf inCelsius only xsd:decimal` <br />
        The temperature in Celsius must always be represented as a decimal value.  

    * `Temperature SubClassOf inCelsius exactly 1 xsd:decimal` <br />
        Every Temperature must have exactly one value in Celsius.  

7. Temperature → inFahrenheit → xsd  
    * `Temperature SubClassOf inFahrenheit only xsd:decimal` <br />
        The temperature inFarenheit must always be represented as a decimal value.  

    * `Temperature SubClassOf inFahrenheit exactly 1 xsd:decimal` <br />
        Every Temperature must have exactly one value in Fahrenheit.  
