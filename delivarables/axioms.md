# Road Crashes Ontology

![Road Crashes all together](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/allTogether/allTogether.png)

## Driver Condition

![Driver Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/DriverCondition/DriverCondition.png)


### Axioms

1. Driver → hasDrivingHistory → DrivingHistory <br />
    * `Driver SubClassOf hasDrivingHistory some DrivingHistory` <br />
        Every driver must have at least one associated driving history.

2. Driver → hasImpairments → Impairments <br />
    * `Driver SubClassOf hasImpairments min 0 Impairments` <br />
        A driver may have impairments.

3. DrivingHistory → hasTrafficViolation → TrafficViolation <br />
    * `DrivingHistory SubClassOf hasTrafficViolation min 0 TrafficViolation` <br />
        A driving history may have TrafficViolation.

4. DrivingHistory → hasDrivingExperience → DrivingExperience <br />
    * `DrivingHistory SubClassOf hasDrivingExperience some DrivingExperience` <br />
        A driving history must include at least one driving experience.

5. TrafficViolation → licenseSuspension → xsd <br />
    * `TrafficViolation SubClassOf licenseSuspension some xsd:string` <br />
        A traffic violation may result in a license suspension, recorded as a string.
    * `TrafficViolation SubClassOf licenseSuspension max 1 xsd:string` <br />
        A traffic violation can have at most one associated license suspension.

6. TrafficViolation → violationType → xsd <br />
    * `TrafficViolation SubClassOf violationType exactly 1 xsd:string` <br />
        Each traffic violation must have exactly one type.

7. TrafficViolation → violationDate → TemporalExtent <br />
    * `TrafficViolation SubClassOf violationDate some TemporalExtent` <br />
        Every traffic violation is associated with a temporal extent.

8. DrivingExperience → totalYearsOfDriving → TemporalExtent <br />
    * `DrivingExperience SubClassOf totalYearsOfDriving some TemporalExtent` <br />
        A driving experience must include total years of driving.

9. DrivingExperience → experienceLevel → ExperienceLevel <br />
    * `DrivingExperience SubClassOf experienceLevel some ExperienceLevel` <br />
        Every driving experience must have at least one experience level.

10. Driver → hasLicenseStatus → xsd <br />
    * `Driver SubClassOf hasLicenseStatus exactly 1 xsd:string` <br />
        Each driver must have exactly one license status.


## EMS

![EMS](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/EMS/EMS.png)


### Axioms

1. EmergencyMedicalService → hasNotificationTime → TemporalExtent <br />
    * `EmergencyMedicalService SubClassOf hasNotificationTime some TemporalExtent` <br />
        Every emergency medical service must have at least one notification time.  
    * `EmergencyMedicalService SubClassOf hasNotificationTime max 1 TemporalExtent` <br />
        Every emergency medical service must have at max one notification time.

2. EmergencyMedicalService → hasArrivalTimeToCrash → TemporalExtent <br />
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash some TemporalExtent` <br />
        Every emergency medical service must have at least one arrival time to the crash site.  
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash max 1 TemporalExtent` <br />
        Every emergency medical service must have at max one arrival time to the crash site.

3. EmergencyMedicalService → hasArrivalTimeToHospital → TemporalExtent <br />
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital some TemporalExtent` <br />
        Every emergency medical service must have at least one arrival time to the hospital.  
    * `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital max 1 TemporalExtent` <br />
        Every emergency medical service must have at max one arrival time to the hospital.

## Impairment
![Impairment](https://github.com/korrapati-SaiSree/cs7810-group2/tree/main/delivarables/scehmaDiagrams_Final/Impairment)

### Axioms

1. Impairments → impairmentsAsString → xsd <br />
    * `Impairments SubClassOf impairmentsAsString max 1 xsd:string` <br />
        Each impairment can have at most one associated string description.  
    * `Impairments SubClassOf impairmentsAsString some xsd:string` <br />
        Every impairment must have atleast one associated string description.

2. SubstanceImpairments → Impairments <br />
    * `SubstanceImpairments SubClassOf Impairments` <br />
        Every SubstanceImpairments are Impairments.

3. Distraction → Impairments <br />
    * `Distraction SubClassOf Impairments` <br />
        Every Distractions are Impairment.

## Person

![Person](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/Person/Person.png)

### Axioms

1. Person → hasRace → xsd <br />
    * `Person SubClassOf hasRace max 1 xsd:string` <br />
        A person can have at most one associated race.  
    * `Person SubClassOf hasRace some xsd:string` <br />
        Every person must have atleast one associated race.

2. Person → hasGender → xsd <br />
    * `Person SubClassOf hasGender max 1 xsd:string` <br />
        A person can have at most one associated gender.  
    * `Person SubClassOf hasGender some xsd:string` <br />
        Every person must have atleast one associated gender.

3. Person → hasAge → xsd <br />
    * `Person SubClassOf hasAge max 1 xsd:integer` <br />
        A person can have at most one associated age.  
    * `Person SubClassOf hasAge some xsd:integer` <br />
        Every person must have atleast one associated age.

4. Person → performsRole → PersonInCrash <br />
    * `Person SubClassOf performsRole some PersonInCrash` <br />
        Every person must perform at least one role in the context of a crash.

5. Crash → providesRole → PersonInCrash <br />
    * `Crash SubClassOf providesRole some PersonInCrash` <br />
        Every crash must provide at least one PersonInCrash role.

6. PersonInCrash → hasInjurySeverity → InjurySeverity <br />
    * `PersonInCrash SubClassOf hasInjurySeverity some InjurySeverity` <br />
        Every person in a crash must have at least one associated injury severity.

7. PersonInCrash → isFatal → Fatality <br />
    * `PersonInCrash SubClassOf isFatal some Fatality` <br />
        Every person in a crash who is fatal must have an associated Fatality record.

8. Fatality → fatalityAsBoolean → xsd <br />
    * `Fatality SubClassOf fatalityAsBoolean some xsd:boolean` <br />
        A fatality must have atleast one associated boolean value indicating whether it is fatal.
    * `Fatality SubClassOf fatalityAsBoolean max 1 xsd:boolean` <br />
        A fatality must have at max one associated boolean value indicating whether it is fatal.

9. Fatality → hasLagTime → TemporalExtent <br />
    * `Fatality SubClassOf hasLagTime some TemporalExtent` <br />
        Every fatality must have at least one associated TemporalExtent for the lag time, representing the time between the crash and the fatality.
    * `Fatality SubClassOf hasLagTime max 1 TemporalExtent` <br />
        Every fatality must have at most one associated TemporalExtent for the lag time, representing the time between the crash and the fatality.

10. NonOccupant → PersonInCrash  <br />
    * `NonOccupant SubClassOf PersonInCrash` <br />
        Every NonOccupant is PersonInCrash.

11. NonOccupant → hasImpairment → Impairments <br />
    * `NonOccupant SubClassOf hasImpairment min 0 Impairments` <br />
        Every non-occupant may have impairment.

12. NonOccupant → locationDuringCrash → xsd <br />
    * `NonOccupant SubClassOf locationDuringCrash exactly 1 xsd:string` <br />
        Every non-occupant must have exactly one associated location during the crash.

13. Pedestrian → NonOccupant <br />
    * `Pedestrian SubClassOf NonOccupant` <br />
        Every Pedestrain is NonOccupant.

14. Cyclist → NonOccupant <br />
    * `Cyclist SubClassOf NonOccupant` <br />
        Every Cyclist is NonOccupant.

15. Occupant → PersonInCrash <br />
    * `Occupant SubClassOf PersonInCrash` <br />
        Every Occupant is PersonInCrash.

16. Occupant → seatPosition → xsd <br />
    * `Occupant SubClassOf seatPosition exactly 1 xsd:string` <br />
        Every occupant must have exactly one associated seat position.

17. Occupant → safetyRestraintUsed → xsd <br />
    * `Occupant SubClassOf safetyRestraintUsed exactly 1 xsd:string` <br />
        Every occupant must have exactly one associated safety restraint used.

18. Occupant → hasAirbagDeployed → xsd <br />
    * `Occupant SubClassOf hasAirbagDeployed exactly 1 xsd:boolean` <br />
        Every occupant must have exactly one associated boolean value indicating whether an airbag was deployed.

19. Driver → Occupant <br />
    * `Driver SubClassOf Occupant` <br />
        Every Driver is Occupant.

20. Passenger → Occupant <br />
    * `Passenger SubClassOf Occupant` <br />
        Every Passenger is Occupant.

21. PersonInCrash → hasTemporalExtent → TemporalExtent <br />
    * `PersonInCrash SubClassOf hasTemporalExtent some TemporalExtent` <br />
        Every PersonInCrash must have at least one associated TemporalExtent, representing some time-related information about their crash involvement.
    * `PersonInCrash SubClassOf hasTemporalExtent max 1 TemporalExtent` <br />
        Every PersonInCrash must have at most one associated TemporalExtent, representing some time-related information about their crash involvement.


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
    * `PointInTime SubClassOf hasDayOfTheWeek some DayOfTheWeek` <br />
        Every PointInTime must have at least one associated DayOfTheWeek.

5. PointInTime → hasSeason → Season <br />
    * `PointInTime SubClassOf hasSeason only Season` <br />
        The range of the hasSeason property must belong to the class Season.
    * `PointInTime SubClassOf hasSeason some Season` <br />
        Every PointInTime must have at least one associated Season.

6. PointInTime → hasValue → xsd <br />
    * `PointInTime SubClassOf hasValue max 1 xsd:datetime` <br />
        A PointInTime can have at most one associated `xsd:datetime` value.
    * `PointInTime SubClassOf hasValue exactly 1 xsd:datetime` <br />
        Every PointInTime must have exactly one associated `xsd:datetime` value.

7. TimeInterval → startsAt → PointInTime <br />
    * `TimeInterval SubClassOf startsAt only PointInTime` <br />
        The range of the startsAt property must belong to the class PointInTime.
    * `TimeInterval SubClassOf startsAt some PointInTime` <br />
        Every TimeInterval must start at a specific PointInTime.

8. TimeInterval → endsAt → PointInTime <br />
    * `TimeInterval SubClassOf endsAt only PointInTime` <br />
        The range of the endsAt property must belong to the class PointInTime.
    * `TimeInterval SubClassOf endsAt some PointInTime` <br />
        Every TimeInterval must end at a specific PointInTime.

## Crash

![Crash](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/crash/Crash.png)


### Axioms

1. Crash → hasMannerOfCollision → MannerOfCollision <br />
    * `Crash SubClassOf hasMannerOfCollision only MannerOfCollision` <br />
        The range of the property hasMannerOfCollision must belong to the class MannerOfCollision.
    * `Crash SubClassOf hasMannerOfCollision exactly 1 MannerOfCollision` <br />
        Every Crash must have exactly one associated manner of collision.

2. Crash → hasTemporalExtent → TemporalExtent <br />
    * `Crash SubClassOf hasTemporalExtent only TemporalExtent` <br />
        The range of the property hasTemporalExtent must belong to the class TemporalExtent.
    * `Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent` <br />
        Every Crash must have exactly one associated temporal extent.

3. Crash → occurredAt → Location <br />
    * `Crash SubClassOf occurredAt only Location` <br />
        The range of the property occurredAt must belong to the class Location.
    * `Crash SubClassOf occurredAt exactly 1 Location` <br />
        Every Crash must occur at exactly one location.

4. Crash → hasTotalFatalities → xsd <br />
    * `Crash SubClassOf hasTotalFatalities only xsd:integer` <br />
        The range of the property hasTotalFatalities must be an integer.
    * `Crash SubClassOf hasTotalFatalities exactly 1 xsd:integer` <br />
        Every Crash must have exactly one associated integer value representing total fatalities.

5. Crash → hasParticipant → Participant <br />
    * `Crash SubClassOf hasParticipant only Participant` <br />
        The range of the property hasParticipant must belong to the class Participant.
    * `Crash SubClassOf hasParticipant some Participant` <br />
        Every Crash must have at least one associated Participant.

6. Participant Subclass Relationships <br />
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
    * `Coordinates SubClassOf hasLatitude exactly 1 xsd:float` <br />
        Every Coordinates must have exactly one Latitude.

5. Coordinates → hasLongitude → xsd <br />
    * `Coordinates SubClassOf hasLongitude only xsd:float` <br />
        The range of the property hasLongitude must be a float value.
    * `Coordinates SubClassOf hasLongitude exactly 1 xsd:float` <br />
        Every Coordinates must have exactly one Longitude.

6. Location → hasState → State <br />
    * `Location SubClassOf hasState only State` <br />
        The range of the property hasState must belong to the class State.
    * `Location SubClassOf hasState exactly 1 State` <br />
        Every Location must have exactly one State.

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

11. City → hasCounty → County <br />
    * `City SubClassOf hasCounty some County` <br />
        Every City must be associated with at least one County.

12. County → hasCountyName → xsd <br />
    * `County SubClassOf hasCountyName exactly 1 xsd:string` <br />
        Every County must have exactly one CountyName.

13. County → hasStreet → Street <br />
    * `County SubClassOf hasStreet some Street` <br />
        Every County must have at least one Street.

14. Street → hasStreetName → xsd <br />
    * `Street SubClassOf hasStreetName exactly 1 xsd:string` <br />
        Every Street must have exactly one StreetName.

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

2. SocioEconomicCondition → hasTemporalExtent → TemporalExtent <br /> 
    * `SocioEconomicCondition SubClassOf hasTemporalExtent only TemporalExtent` <br /> 
        The temporal extent of any SocioEconomicCondition must be TemporalExtent.
    * `SocioEconomicCondition SubClassOf hasTemporalExtent some TemporalExtent` <br /> 
        Every SocioEconomicCondition must have at least one temporal extent.

3.  IncomeHouseholdMedian → SocioEconomicCondition <br /> 
    * `IncomeHouseHoldMedium SubClassOf SocioEconomicCondition` <br />
        Every IncomeHouseHoldMedium is SocioEconomicCondition

4. IncomeHouseholdMedian → incomeHouseholdMedianAsDecimal → xsd <br /> 
    * `IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal only xsd:decimal` <br /> 
        Every IncomeHouseholdMedian can only have incomeHouseHoldMediumAsString values of type xsd:string

5. EmploymentRate → SocioEconomicCondition 
    * `EmploymentRate SubClassOf SocioEconomicCondition` <br />
        Every EmploymentRate is SocioEconomicCondition

6. EmploymentRate → employmentRateAsDecimal → xsd  
    * `EmploymentRate SubClassOf employmentRateAsDecimal only xsd:decimal`  
        Every EmploymentRate can only have employmentRateAsString values of type xsd:string.

7.  PopulationDensity → SocioEconomicCondition   
    * `PopulationDensity SubClassOf SocioEconomicCondition` <br />
    Every PopulationDensity is SocioEconomicCondition

8. PopulationDensity → populationDensityAsDecimal → xsd  
    * `PopulationDensity SubClassOf populationDensityAsDecimal only xsd:decimal`  
        Every PopulationDensity can only have populationDensityAsString values of type xsd:string.

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

2. Vehicle → hasVehicleModel → xsd  
    * `hasVehicleModel some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleModel is classified as a Vehicle.

    * `Vehicle SubClassOf hasVehicleModel Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleModel, represented as a string

3. Vehicle → hasVehicleMake → xsd  
    * `hasVehicleMake some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleMake is classified as a Vehicle.

    * `Vehicle SubClassOf hasVehicleMake Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleMake, represented as a string

4. Vehicle → hasVehicleManufacturingYear → xsd  
    * `hasVehicleManufacturingYear some xsd:string SubClassOf Vehicle` <br />
        Anything that has a VehicleManufacturingYear is classified as a Vehicle.

    * `Vehicle SubClassOf hasVehicleManufacturingYear Exactly 1 xsd:string` <br />
        Every Vehicle must have exactly one VehicleManufacturingYear, represented as a string

5. Vehicle → hasWeight → Weight  
    * `Vehicle SubClassOf hasWeight only Weight` <br />
        The weight of every vehicle must be of type Weight.

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

8. Vehicle → performsRole → VehicleInAccident  
    * `VehicleInAccident SubClassOf Vehicle` <br />
        Every VehicleInAccident is Vehicle

    * `PerformsRole some VehicleInAccident SubClassOf Vehicle` <br />
        Anything that performs a role in a vehicle accident is a type of vehicle.

    * `Vehicle SubClassOf PerformsRole some VehicleInAccident` <br />
        Every vehicle performs at least one role in a vehicle accident.
    
    * `VehicleInAccident SubClassOf PerformsRole- some Vehicle` <br />
        Every vehicle involved in an accident is the object of a role performed by some vehicle.

9. Crash → providesRole → VehicleInAccident
    * `Crash SubClassOf providesRole some VehicleInAccident` <br />
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

3. WeatherCondition → hasPrecipitation → Precipitation  
    * `WeatherCondition SubClassOf hasPrecipitation only Precipitation` <br />
        The Precipitation of every WeatherCondition must be of type Precipitation.  

    * `WeatherCondition SubClassOf hasPrecipitation Exactly 1 Precipitation` <br />
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
