# Road Crashes Ontology

![Road Crashes all together](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/allTogether/allTogether.png)

## Driver Condition

![Driver Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/DriverCondition/DriverCondition.png)


### Axioms

* `Driver SubClassOf hasLicenseStatus only xsd:string` <br />
   The scoped range of hasLicenseStatus, scoped by Driver, is an xsd:string

* `Driver SubClassOf hasLicenseStatus exactly 1 xsd:string` <br />
   Every Driver has exactly 1 License Status.

* `Driver SubClassOf hasImpairments only Impairments` <br />
   The scoped range of hasImpairments, scoped by Driver, is Impairments

* `Driver SubClassOf hasDrivingHistory exactly 1 DrivingHistory` <br />
   Every Driver has exactly 1 Driving History.

* `DrivingHistory SubClassOf TrafficViolation min 0` <br />
   Every DrivingHistory has at minimum 0 Traffic Violations.

* `TrafficViolation SubClassOf violationType only xsd:string` <br />
   The scoped range of violationType, scoped by TrafficViolation, is an xsd:string

* `TrafficViolation SubClassOf violationType exactly 1 xsd:string` <br />
   Every TrafficViolation has exactly 1 Violation Type.

* `TrafficViolation SubClassOf violationDate only TemporalExtent` <br />
   The scoped range of violationDate, scoped by TrafficViolation, is TemporalExtent

* `TrafficViolation SubClassOf violationDate exactly 1 TemporalExtent` <br />
   Every TrafficViolation has exactly 1 Violation Date.

* `TrafficViolation SubClassOf licenseSuspension only xsd:string` <br />
    The scoped range of licenseSuspension, scoped by TrafficViolation, is an xsd:string

* `DrivingHistory SubClassOf DrivingExperience exactly 1` <br />
    Every DrivingHistory has exactly 1 DrivingExperience.

* `DrivingExperience SubClassOf totalYearsOfDriving only TemporalExtent` <br />
    The scoped range of totalYearsOfDriving, scoped by DrivingExperience, is TemporalExtent

* `DrivingExperience SubClassOf totalYearsOfDriving exactly 1 TemporalExtent` <br />
    Every DrivingExperience has exactly 1 Total Years of Driving.

* `DrivingExperience SubClassOf experienceLevel only ExperienceLevel` <br />
    The scoped range of experienceLevel, scoped by DrivingExperience, is ExperienceLevel

* `DrivingExperience SubClassOf experienceLevel exactly 1 ExperienceLevel` <br />
    Every DrivingExperience has exactly 1 Experience Level.

* `ExperienceLevel SubClassOf {novice, intermediate, experienced}` <br />
    Experience Level can only be one of: novice, intermediate, or experienced.






## EMS

![EMS](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/EMS/EMS.png)


### Axioms

* `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash only TemporalExtent` <br />
   The scoped range of hasArrivalTimeToCrash, scoped by EmergencyMedicalService, is TemporalExtent

* `EmergencyMedicalService SubClassOf hasArrivalTimeToCrash exactly 1 TemporalExtent` <br />
   Every EmergencyMedicalService has exactly 1 Arrival Time To Crash.

* `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital only TemporalExtent` <br />
   The scoped range of hasArrivalTimeToHospital, scoped by EmergencyMedicalService, is TemporalExtent

* `EmergencyMedicalService SubClassOf hasArrivalTimeToHospital exactly 1 TemporalExtent` <br />
   Every EmergencyMedicalService has exactly 1 Arrival Time To Hospital.

* `EmergencyMedicalService SubClassOf hasNotificationTime only TemporalExtent` <br />
   The scoped range of hasNotificationTime, scoped by EmergencyMedicalService, is TemporalExtent

* `EmergencyMedicalService SubClassOf hasNotificationTime exactly 1 TemporalExtent` <br />
   Every EmergencyMedicalService has exactly 1 Notification Time.



## Person

![Person](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/Person/Person.png)


### Axioms

* `Person SubClassOf hasRace only xsd:string` <br />
   The scoped range of hasRace, scoped by Person, is an xsd:string

* `Person SubClassOf hasAge only xsd:integer` <br />
   The scoped range of hasAge, scoped by Person, is an xsd:integer

* `Person SubClassOf hasGender only xsd:string` <br />
   The scoped range of hasGender, scoped by Person, is an xsd:string

* `Person SubClassOf performsRole exactly 1 PersonInCrash` <br />
   Every Person performs exactly 1 PersonInCrash role.

* `Crash SubClassOf providesRole min 1 PersonInCrash` <br />
   Every Crash provides at least 1 PersonInCrash role.

* `PersonInCrash SubClassOf hasInjurySeverity only InjurySeverity` <br />
   The scoped range of hasInjurySeverity, scoped by PersonInCrash, is InjurySeverity

* `PersonInCrash SubClassOf hasInjurySeverity exactly 1 InjurySeverity` <br />
   Every PersonInCrash has exactly 1 InjurySeverity.

* `InjurySeverity SubClassOf {noInjury, suspectedSeriousInjury, possibleInjury, suspectedMinorInjury, FatalInjury, diedPriorToCrash, injuredSeverityUnknown}` <br />
   InjurySeverity can only be one of the enumerated values.

* `PersonInCrash SubClassOf isFatal only Fatality` <br />
   The scoped range of isFatal, scoped by PersonInCrash, is Fatality

* `Fatality SubClassOf hasLagTime only TemporalExtent` <br />
    The scoped range of hasLagTime, scoped by Fatality, is TemporalExtent

* `Fatality SubClassOf fatalityAsBoolean only xsd:Boolean` <br />
    The scoped range of fatalityAsBoolean, scoped by Fatality, is an xsd:Boolean

* `NonOccupant SubClassOf PersonInCrash` <br />
    Every NonOccupant is a PersonInCrash.

* `NonOccupant SubClassOf hasImpairment only Impairments` <br />
    The scoped range of hasImpairment, scoped by NonOccupant, is Impairments

* `NonOccupant SubClassOf locationDuringCrash only xsd:string` <br />
    The scoped range of locationDuringCrash, scoped by NonOccupant, is an xsd:string

* `Pedestrian SubClassOf NonOccupant` <br />
    Every Pedestrian is a NonOccupant.

* `Cyclist SubClassOf NonOccupant` <br />
    Every Cyclist is a NonOccupant.

* `Occupant SubClassOf PersonInCrash` <br />
    Every Occupant is a PersonInCrash.

* `Occupant SubClassOf hasAirbagDeployed only xsd:boolean` <br />
    The scoped range of hasAirbagDeployed, scoped by Occupant, is an xsd:boolean

* `Occupant SubClassOf safetyRestraintUsed only xsd:string` <br />
    The scoped range of safetyRestraintUsed, scoped by Occupant, is an xsd:string

* `Occupant SubClassOf seatPosition only xsd:string` <br />
    The scoped range of seatPosition, scoped by Occupant, is an xsd:string

* `Driver SubClassOf Occupant` <br />
    Every Driver is an Occupant.

* `Passenger SubClassOf Occupant` <br />
    Every Passenger is an Occupant.


## Time

![Time](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/Time/Time.png)


### Axioms

* `PointInTime SubClassOf TemporalExtent` <br />
   Every PointInTime is a TemporalExtent.

* `TimeInterval SubClassOf TemporalExtent` <br />
   Every TimeInterval is a TemporalExtent.

* `TimeInterval SubClassOf startsAt only PointInTime` <br />
   The scoped range of startsAt, scoped by TimeInterval, is PointInTime

* `TimeInterval SubClassOf startsAt exactly 1 PointInTime` <br />
   Every TimeInterval has exactly 1 start PointInTime.

* `TimeInterval SubClassOf endsAt only PointInTime` <br /> 
   The scoped range of endsAt, scoped by TimeInterval, is PointInTime

* `TimeInterval SubClassOf endsAt exactly 1 PointInTime` <br />
   Every TimeInterval has exactly 1 end PointInTime.

* `PointInTime SubClassOf hasValue only xsd:datetime` <br />
   The scoped range of hasValue, scoped by PointInTime, is an xsd:datetime

* `PointInTime SubClassOf hasValue exactly 1 xsd:datetime` <br />
   Every PointInTime has exactly 1 datetime value.

* `PointInTime SubClassOf hasTimeOfTheDay only TimeOfDay` <br />
   The scoped range of hasTimeOfTheDay, scoped by PointInTime, is TimeOfDay

* `TimeOfDay SubClassOf {dusk, morning, afternoon, evening, dawn}` <br />
    TimeOfDay can only be one of: dusk, morning, afternoon, evening, or dawn.

* `PointInTime SubClassOf hasSeason only Season` <br />
    The scoped range of hasSeason, scoped by PointInTime, is Season

* `Season SubClassOf {spring, summer, fall, winter}` <br />
    Season can only be one of: spring, summer, fall, or winter.

* `PointInTime SubClassOf hasDayOfTheWeek only DayOfTheWeek` <br />
    The scoped range of hasDayOfTheWeek, scoped by PointInTime, is DayOfTheWeek

* `DayOfTheWeek SubClassOf {sunday, monday, tuesday, wednesday, thursday, friday, saturday}` <br />
    DayOfTheWeek can only be one of: sunday, monday, tuesday, wednesday, thursday, friday, or saturday.

* `PointInTime SubClassOf hasTimeOfTheDay exactly 1 TimeOfDay` <br />
    Every PointInTime has exactly 1 TimeOfDay.

* `PointInTime SubClassOf hasSeason exactly 1 Season` <br />
    Every PointInTime has exactly 1 Season.

* `PointInTime SubClassOf hasDayOfTheWeek exactly 1 DayOfTheWeek` <br />
    Every PointInTime has exactly 1 DayOfTheWeek.

## Crash

![Crash](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/crash/Crash.png)


### Axioms

* `Crash SubClassOf hasMannerOfCollision only MannerOfCollision` <br />
   The scoped range of hasMannerOfCollision, scoped by Crash, is MannerOfCollision

* `Crash SubClassOf hasMannerOfCollision exactly 1 MannerOfCollision` <br />
   Every Crash has exactly 1 MannerOfCollision.

* `Crash SubClassOf hasTemporalExtent only TemporalExtent` <br />
   The scoped range of hasTemporalExtent, scoped by Crash, is TemporalExtent

* `Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent` <br />
   Every Crash has exactly 1 TemporalExtent.

* `Crash SubClassOf OccuredAt only Location` <br />
   The scoped range of OccuredAt, scoped by Crash, is Location

* `Crash SubClassOf OccuredAt exactly 1 Location` <br />
   Every Crash occurs at exactly 1 Location.

* `Crash SubClassOf hasTotalFatalities only xsd:integer` <br />
   The scoped range of hasTotalFatalities, scoped by Crash, is an xsd:integer

* `Crash SubClassOf hasTotalFatalities exactly 1 xsd:integer` <br />
   Every Crash has exactly 1 TotalFatalities count.

* `Crash SubClassOf hasParticipant min 1 Participant` <br />
   Every Crash has at minimum 1 Participant.

* `Participant SubClassOf {Person, Vehicle, EMS}` <br />
    A Participant can only be one of: Person, Vehicle, or EMS.

* `Person SubClassOf Participant` <br />
    Every Person is a Participant.

* `Vehicle SubClassOf Participant` <br />
    Every Vehicle is a Participant. 

* `EMS SubClassOf Participant` <br />
    Every EMS is a Participant.

## Location

![Location](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/location/Location.png)

### Axioms

* `Location SubClassOf hasWorkZone only WorkZone` <br />
   The scoped range of hasWorkZone, scoped by Location, is WorkZone

* `WorkZone SubClassOf {None, Construction, Maintenance, Utility, "Work Zone, Type Unknown"}` <br />
   WorkZone can only be one of: None, Construction, Maintenance, Utility, or Work Zone, Type Unknown.

* `Location SubClassOf hasIntersection only Intersection` <br />
   The scoped range of hasIntersection, scoped by Location, is Intersection

* `Intersection SubClassOf {"Not an Intersection", "Four-Way Intersection", "T-Intersection", "Y-Intersection", "Roundabout", "Five-Point, or More", "L-Intersection", "Other Intersection Type"}` <br />
   Intersection can only be one of the enumerated types.

* `Location SubClassOf hasCoordinates only Coordinates` <br />
   The scoped range of hasCoordinates, scoped by Location, is Coordinates

* `Coordinates SubClassOf hasLatitude only xsd:float` <br />
   The scoped range of hasLatitude, scoped by Coordinates, is an xsd:float

* `Coordinates SubClassOf hasLongitude only xsd:float` <br />
   The scoped range of hasLongitude, scoped by Coordinates, is an xsd:float

* `Location SubClassOf hasState exactly 1 State` <br />
   Every Location has exactly 1 State.

* `State SubClassOf hasStateName only xsd:string` <br />
   The scoped range of hasStateName, scoped by State, is an xsd:string

* `State SubClassOf hasCity some City` <br />
    Every State has some City.

* `City SubClassOf hasCityName only xsd:string` <br />
    The scoped range of hasCityName, scoped by City, is an xsd:string

* `City SubClassOf hasZipCode only xsd:string` <br />
    The scoped range of hasZipCode, scoped by City, is an xsd:string

* `City SubClassOf hasCounty exactly 1 County` <br />
    Every City has exactly 1 County.

* `County SubClassOf hasCountyName only xsd:string` <br />
    The scoped range of hasCountyName, scoped by County, is an xsd:string

* `County SubClassOf hasZipCode only xsd:string` <br />
    The scoped range of hasZipCode, scoped by County, is an xsd:string

* `County SubClassOf hasStreet some Street` <br />
    Every County has some Street.

* `Street SubClassOf hasStreetName only xsd:string` <br />
    The scoped range of hasStreetName, scoped by Street, is an xsd:string

* `Location SubClassOf hasCoordinates exactly 1 Coordinates` <br />
    Every Location has exactly 1 Coordinates.

* `Coordinates SubClassOf hasLatitude exactly 1 xsd:float` <br />
    Every Coordinates has exactly 1 Latitude.

* `Coordinates SubClassOf hasLongitude exactly 1 xsd:float` <br />
    Every Coordinates has exactly 1 Longitude.

* `State SubClassOf hasStateName exactly 1 xsd:string` <br />
    Every State has exactly 1 State Name.

* `City SubClassOf hasCityName exactly 1 xsd:string` <br />
    Every City has exactly 1 City Name.

* `County SubClassOf hasCountyName exactly 1 xsd:string` <br />
    Every County has exactly 1 County Name.

* `Street SubClassOf hasStreetName exactly 1 xsd:string` <br />
    Every Street has exactly 1 Street Name.


## Vehicle

![Vehicle](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/vehicle/Vehicle.png)

### Axioms

* `VehicleInAccident SubClassOf Vehicle` <br />
    Every VehicleInAccident is Vehicle

* `PerformsRole some VehicleInAccident SubClassOf Vehicle` <br />
    Anything that performs a role in a vehicle accident is a type of vehicle.

* `Vehicle SubClassOf PerformsRole some VehicleInAccident` <br />
    Every vehicle performs at least one role in a vehicle accident.

* `VehicleInAccident SubClassOf PerformsRole-.some Vehicle` <br />
    Every vehicle involved in an accident is the object of a role performed by some vehicle.

* `Vehicle SubClassOf hasWeight Exactly 1 Weight` <br />
    Every vehicle has exactly one weight associated with it.

* `Vehicle SubClassOf hasWeight only Weight` <br />
    The weight of every vehicle must be of type Weight.

* `Vehicle SubClassOf hasWeight some Weight` <br />
    Every vehicle must have at least one weight specified.

* `Owl.Thing SubClassOf hasWeight exactly 1 Weight` <br />
    Everything in the ontology must have exactly one weight.

* `VehicleInAccident SubClassOf hasTemporalExtent only TemporalExtent` <br />
    The temporal extent (time period) of any vehicle involved in an accident must be TemporalExtent.

* `VehicleInAccident SubClassOf hasTemporalExtent some TemporalExtent` <br />
    Every vehicle involved in an accident must have at least one temporal extent.

* `providesRole some VehicleInAccident SubClassOf Crash` <br />
    Anything that provides a role involving a VehicleInAccident is classified as a crash.

* `Crash SubClassOf providesRole min 1 VehicleInAccident` <br />
    Every Crash provides at least 1 VehicleInAccident role.

* `Crash SubClassOf providesRole some VehicleInAccident` <br />
    Every crash must provide at least one VehicleInAccident role.

* `OWL.Thing SubClassOf hasSpeed only xsd:integer` <br />
    Everything in the ontology can only have speed of type xsd:integer

* `hasSpeed some xsd:integer SubClassOf VehicleInAccident` <br />
    Anything that hasSpeed is classified as a VehicleInAccident.

* `OWL.Thing SubClassOf hasMileage only xsd:float` <br />
    Everything in the ontology can only hasMileage of type xsd:float

* `hasMileage some xsd:integer SubClassOf VehicleInAccident` <br />
    Anything that hasMileage is classified as a VehicleInAccident

* `VehicleInAccident SubClassOf involvedInHitAndRun only xsd:Boolean` <br />
    vehicleInAccident involved in hit-and-run must be represented as a boolean value

* `involvedInHitAndRun some xsd:Boolean SubClassOf VehicleInAccident` <br />
    Anything associated with a hit-and-run boolean value is classified as a vehicleInAccident

* `Vehicle SubClassOf hasVehicleType only xsd:string` <br />
    The Vehicletype of every Vehicle must be represented as a string.

* `hasVehicleType some xsd:string SubClassOf Vehicle` <br />
    Anything that has a VehicleType is classified as a Vehicle.

* `Vehicle SubClassOf hasVehicleType Exactly 1 xsd:string` <br />
    Every Vehicle must have exactly one VehicleType, represented as a string

* `hasVehicleMake some xsd:string SubClassOf Vehicle` <br />
    Anything that has a VehicleMake is classified as a Vehicle.

* `Vehicle SubClassOf hasVehicleMake Exactly 1 xsd:string` <br />
    Every Vehicle must have exactly one VehicleMake, represented as a string.

* `hasVehicleModel some xsd:string SubClassOf Vehicle` <br />
    Anything that has a VehicleModel is classified as a Vehicle.

* `Vehicle SubClassOf hasVehicleModel Exactly 1 xsd:string` <br />
    Every Vehicle must have exactly one VehicleModel, represented as a string.

* `hasVehicleManufacturingYear some xsd:string SubClassOf Vehicle` <br />
    Anything that has a VehicleManufacturingYear is classified as a Vehicle.

* `Vehicle SubClassOf hasVehicleManufacturingYear Exactly 1 xsd:string` <br />
    Every Vehicle must have exactly one VehicleManufacturingYear, represented as a string.

* `OWL.Thing SubClassOf rangeFrom only xsd:integer` <br />
    Everything in the ontology can only have rangeFrom values of type xsd:integer.

* `OWL.Thing SubClassOf rangeTo only xsd:integer` <br />
    Everything in the ontology can only have rangeTo values of type xsd:integer.


## Impairment
![Impairment](https://github.com/korrapati-SaiSree/cs7810-group2/tree/main/delivarables/scehmaDiagrams_Final/Impairment)

### Axioms

* `SubstanceImairments SubClassOf Impairments` <br />
    Every SubstanceImairments is SubstanceImairments

* `SubstanceImairments SubClassOf {"Test Not Given", "Tested, No Drugs Found/Negative", "Not Reported", "Narcotic Analgesics", "Depressants", "Hallucinogens", "Cannabinoids", "Stimulants", "Dissociative Anesthetics", "Anabolic Steroids ", "Inhalants","Non-Psychoactive/Other Drugs","Non-Psychoactive/Other Drugs", "Other Drug (Specify:)", "Tested for Drugs, Drugs Found, Type Unknown/Positive", "Tested for Drugs, Results Unknown"}` <br />
   SubstanceImairments can only be one of the enumerated types.

* `Distraction SubClassOf Impairments` <br />
    Every SubstanceImairments is SubstanceImairments

* `Distraction SubClassOf {"Not Distracted", "By Other Occupant(s)", "By a Moving Object in Vehicle", "While Talking or Listening to Mobile Phone", "While Adjusting Audio or Climate Controls", "While Using Other Component/Controls Integral to Vehicle", "While Using or Reaching for Device/Object Brought Into Vehicle", "Distracted by Outside Person, Object or Event", "Eating or Drinking", "Smoking Related", "No Driver Present/Unknown if Driver Present","Distraction/Inattention", "Other Mobile Phone Related ", "Distraction/Careless", "Careless/Inattentive", "Lost in Thought/Daydreaming", "Other Distraction","Distraction (Distracted), Details Unknown", "Inattention (Inattentive), Details Unknown "}` <br />
   Distraction can only be one of the enumerated types.

## SocioEconomic Condition
![SocioEconomic Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/socioeconomic_Factors/socioEconomicCondition.png)

### Axioms

* `Location SubClassOf hasSocioEconomicCondition only SocioEconomicCondition` <br />
    The socioeconomic condition of any location must be of type SocioEconomicCondition.

* `IncomeHouseHoldMedium SubClassOf SocioEconomicCondition` <br />
    Every IncomeHouseHoldMedium is SocioEconomicCondition

* `OWL.Things SubClassOf incomeHouseHoldMediumAsString only xsd:string` <br />
    Everything in the ontology can only have incomeHouseHoldMediumAsString values of type xsd:string.

* `EmploymentRate SubClassOf SocioEconomicCondition` <br />
    Every EmploymentRate is SocioEconomicCondition

* `OWL.Things SubClassOf employmentRateAsString only xsd:string` <br />
    Everything in the ontology can only have employmentRateAsString values of type xsd:string.

* `PopulationDensity SubClassOf SocioEconomicCondition` <br />
    Every PopulationDensity is SocioEconomicCondition

* `OWL.Things SubClassOf populationDensityAsString only xsd:string` <br />
    Everything in the ontology can only have populationDensityAsString values of type xsd:string.

* `EducationLevel SubClassOf SocioEconomicCondition` <br />
    Every EducationLevel is SocioEconomicCondition

* `EducationLevel SubClassOf {"Less than high school graduate", "High school graduate", "Some college or associate's degree", "Bachelor's degree or higher"}` <br />
   EducationLevel can only be one of the enumerated types.


## Weather

![Weather](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/weather/WeatherCondition.png)

### Axioms

* `Location SubClassOf hasWeatherCondition only Weather Condition` <br />
    The weather condition of any Location must be of type WeatherCondition.

* `OWL.Things SubClassOf weatherConditionAsString only xsd:string` <br />
    Everything in the ontology can only have weatherConditionAsString values of type xsd:string.

* `WeatherCondition SubClassOf hasPrecipitation Exactly 1 Precipitation` <br />
    Every weather condition must have exactly one precipitation value associated with it

* `WeatherCondition SubClassOf hasTemperature only Temperature` <br />
    The Temperature of every WeatherCondition must be of type Temperature.

* `WeatherCondition SubClassOf hasTemperature some Temperature` <br />
    Every WeatherCondition must have at least one Temperature specified.

* `Temperature SubClassOf inCelcius only xsd:decimal` <br />
    The temperature in Celsius must always be represented as a decimal value.

* `Temperature SubClassOf inFarenheit only xsd:decimal` <br />
    The temperature inFarenheit must always be represented as a decimal value.
