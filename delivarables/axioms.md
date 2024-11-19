# Road Crashes Ontology

![Road Crashes all together](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/allTogether/allTogether.png)

## Driver Condition

### Axioms

1. Driver SubClassOf hasLicenseStatus only xsd:string
   The scoped range of hasLicenseStatus, scoped by Driver, is an xsd:string

2. Driver SubClassOf hasLicenseStatus exactly 1 xsd:string
   Every Driver has exactly 1 License Status.

3. Driver SubClassOf hasImpairments only Impairments
   The scoped range of hasImpairments, scoped by Driver, is Impairments

4. Driver SubClassOf hasDrivingHistory exactly 1 DrivingHistory
   Every Driver has exactly 1 Driving History.

5. DrivingHistory SubClassOf TrafficViolation min 0
   Every DrivingHistory has at minimum 0 Traffic Violations.

6. TrafficViolation SubClassOf violationType only xsd:string
   The scoped range of violationType, scoped by TrafficViolation, is an xsd:string

7. TrafficViolation SubClassOf violationType exactly 1 xsd:string
   Every TrafficViolation has exactly 1 Violation Type.

8. TrafficViolation SubClassOf violationDate only TemporalExtent
   The scoped range of violationDate, scoped by TrafficViolation, is TemporalExtent

9. TrafficViolation SubClassOf violationDate exactly 1 TemporalExtent
   Every TrafficViolation has exactly 1 Violation Date.

10. TrafficViolation SubClassOf licenseSuspension only xsd:string
    The scoped range of licenseSuspension, scoped by TrafficViolation, is an xsd:string

11. DrivingHistory SubClassOf DrivingExperience exactly 1
    Every DrivingHistory has exactly 1 DrivingExperience.

12. DrivingExperience SubClassOf totalYearsOfDriving only TemporalExtent
    The scoped range of totalYearsOfDriving, scoped by DrivingExperience, is TemporalExtent

13. DrivingExperience SubClassOf totalYearsOfDriving exactly 1 TemporalExtent
    Every DrivingExperience has exactly 1 Total Years of Driving.

14. DrivingExperience SubClassOf experienceLevel only ExperienceLevel
    The scoped range of experienceLevel, scoped by DrivingExperience, is ExperienceLevel

15. DrivingExperience SubClassOf experienceLevel exactly 1 ExperienceLevel
    Every DrivingExperience has exactly 1 Experience Level.

16. ExperienceLevel SubClassOf {novice, intermediate, experienced}
    Experience Level can only be one of: novice, intermediate, or experienced.






## EMS

### Axioms

1. EmergencyMedicalService SubClassOf hasArrivalTimeToCrash only TemporalExtent
   The scoped range of hasArrivalTimeToCrash, scoped by EmergencyMedicalService, is TemporalExtent

2. EmergencyMedicalService SubClassOf hasArrivalTimeToCrash exactly 1 TemporalExtent
   Every EmergencyMedicalService has exactly 1 Arrival Time To Crash.

3. EmergencyMedicalService SubClassOf hasArrivalTimeToHospital only TemporalExtent
   The scoped range of hasArrivalTimeToHospital, scoped by EmergencyMedicalService, is TemporalExtent

4. EmergencyMedicalService SubClassOf hasArrivalTimeToHospital exactly 1 TemporalExtent
   Every EmergencyMedicalService has exactly 1 Arrival Time To Hospital.

5. EmergencyMedicalService SubClassOf hasNotificationTime only TemporalExtent
   The scoped range of hasNotificationTime, scoped by EmergencyMedicalService, is TemporalExtent

6. EmergencyMedicalService SubClassOf hasNotificationTime exactly 1 TemporalExtent
   Every EmergencyMedicalService has exactly 1 Notification Time.



## Person

### Axioms

1. Person SubClassOf hasRace only xsd:string
   The scoped range of hasRace, scoped by Person, is an xsd:string

2. Person SubClassOf hasAge only xsd:integer
   The scoped range of hasAge, scoped by Person, is an xsd:integer

3. Person SubClassOf hasGender only xsd:string
   The scoped range of hasGender, scoped by Person, is an xsd:string

4. Person SubClassOf performsRole exactly 1 PersonInCrash
   Every Person performs exactly 1 PersonInCrash role.

5. Crash SubClassOf providesRole min 1 PersonInCrash
   Every Crash provides at least 1 PersonInCrash role.

6. PersonInCrash SubClassOf hasInjurySeverity only InjurySeverity
   The scoped range of hasInjurySeverity, scoped by PersonInCrash, is InjurySeverity

7. PersonInCrash SubClassOf hasInjurySeverity exactly 1 InjurySeverity
   Every PersonInCrash has exactly 1 InjurySeverity.

8. InjurySeverity SubClassOf {noInjury, suspectedSeriousInjury, possibleInjury, suspectedMinorInjury, FatalInjury, diedPriorToCrash, injuredSeverityUnknown}
   InjurySeverity can only be one of the enumerated values.

9. PersonInCrash SubClassOf isFatal only Fatality
   The scoped range of isFatal, scoped by PersonInCrash, is Fatality

10. Fatality SubClassOf hasLagTime only TemporalExtent
    The scoped range of hasLagTime, scoped by Fatality, is TemporalExtent

11. Fatality SubClassOf fatalityAsBoolean only xsd:Boolean
    The scoped range of fatalityAsBoolean, scoped by Fatality, is an xsd:Boolean

12. NonOccupant SubClassOf PersonInCrash
    Every NonOccupant is a PersonInCrash.

13. NonOccupant SubClassOf hasImpairment only Impairments
    The scoped range of hasImpairment, scoped by NonOccupant, is Impairments

14. NonOccupant SubClassOf locationDuringCrash only xsd:string
    The scoped range of locationDuringCrash, scoped by NonOccupant, is an xsd:string

15. Pedestrian SubClassOf NonOccupant
    Every Pedestrian is a NonOccupant.

16. Cyclist SubClassOf NonOccupant
    Every Cyclist is a NonOccupant.

17. Occupant SubClassOf PersonInCrash
    Every Occupant is a PersonInCrash.

18. Occupant SubClassOf hasAirbagDeployed only xsd:boolean
    The scoped range of hasAirbagDeployed, scoped by Occupant, is an xsd:boolean

19. Occupant SubClassOf safetyRestraintUsed only xsd:string
    The scoped range of safetyRestraintUsed, scoped by Occupant, is an xsd:string

20. Occupant SubClassOf seatPosition only xsd:string
    The scoped range of seatPosition, scoped by Occupant, is an xsd:string

21. Driver SubClassOf Occupant
    Every Driver is an Occupant.

22. Passenger SubClassOf Occupant
    Every Passenger is an Occupant.


## Time

### Axioms

1. PointInTime SubClassOf TemporalExtent
   Every PointInTime is a TemporalExtent.

2. TimeInterval SubClassOf TemporalExtent
   Every TimeInterval is a TemporalExtent.

3. TimeInterval SubClassOf startsAt only PointInTime
   The scoped range of startsAt, scoped by TimeInterval, is PointInTime

4. TimeInterval SubClassOf startsAt exactly 1 PointInTime
   Every TimeInterval has exactly 1 start PointInTime.

5. TimeInterval SubClassOf endsAt only PointInTime
   The scoped range of endsAt, scoped by TimeInterval, is PointInTime

6. TimeInterval SubClassOf endsAt exactly 1 PointInTime
   Every TimeInterval has exactly 1 end PointInTime.

7. PointInTime SubClassOf hasValue only xsd:datetime
   The scoped range of hasValue, scoped by PointInTime, is an xsd:datetime

8. PointInTime SubClassOf hasValue exactly 1 xsd:datetime
   Every PointInTime has exactly 1 datetime value.

9. PointInTime SubClassOf hasTimeOfTheDay only TimeOfDay
   The scoped range of hasTimeOfTheDay, scoped by PointInTime, is TimeOfDay

10. TimeOfDay SubClassOf {dusk, morning, afternoon, evening, dawn}
    TimeOfDay can only be one of: dusk, morning, afternoon, evening, or dawn.

11. PointInTime SubClassOf hasSeason only Season
    The scoped range of hasSeason, scoped by PointInTime, is Season

12. Season SubClassOf {spring, summer, fall, winter}
    Season can only be one of: spring, summer, fall, or winter.

13. PointInTime SubClassOf hasDayOfTheWeek only DayOfTheWeek
    The scoped range of hasDayOfTheWeek, scoped by PointInTime, is DayOfTheWeek

14. DayOfTheWeek SubClassOf {sunday, monday, tuesday, wednesday, thursday, friday, saturday}
    DayOfTheWeek can only be one of: sunday, monday, tuesday, wednesday, thursday, friday, or saturday.

15. PointInTime SubClassOf hasTimeOfTheDay exactly 1 TimeOfDay
    Every PointInTime has exactly 1 TimeOfDay.

16. PointInTime SubClassOf hasSeason exactly 1 Season
    Every PointInTime has exactly 1 Season.

17. PointInTime SubClassOf hasDayOfTheWeek exactly 1 DayOfTheWeek
    Every PointInTime has exactly 1 DayOfTheWeek.

## Crash

### Axioms

1. Crash SubClassOf hasMannerOfCollision only MannerOfCollision
   The scoped range of hasMannerOfCollision, scoped by Crash, is MannerOfCollision

2. Crash SubClassOf hasMannerOfCollision exactly 1 MannerOfCollision
   Every Crash has exactly 1 MannerOfCollision.

3. Crash SubClassOf hasTemporalExtent only TemporalExtent
   The scoped range of hasTemporalExtent, scoped by Crash, is TemporalExtent

4. Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent
   Every Crash has exactly 1 TemporalExtent.

5. Crash SubClassOf OccuredAt only Location
   The scoped range of OccuredAt, scoped by Crash, is Location

6. Crash SubClassOf OccuredAt exactly 1 Location
   Every Crash occurs at exactly 1 Location.

7. Crash SubClassOf hasTotalFatalities only xsd:integer
   The scoped range of hasTotalFatalities, scoped by Crash, is an xsd:integer

8. Crash SubClassOf hasTotalFatalities exactly 1 xsd:integer
   Every Crash has exactly 1 TotalFatalities count.

9. Crash SubClassOf hasParticipant min 1 Participant
   Every Crash has at minimum 1 Participant.

10. Participant SubClassOf {Person, Vehicle, EMS}
    A Participant can only be one of: Person, Vehicle, or EMS.

11. Person SubClassOf Participant
    Every Person is a Participant.

12. Vehicle SubClassOf Participant
    Every Vehicle is a Participant.

13. EMS SubClassOf Participant
    Every EMS is a Participant.

## Location

### Axioms

1. Location SubClassOf hasWorkZone only WorkZone
   The scoped range of hasWorkZone, scoped by Location, is WorkZone

2. WorkZone SubClassOf {None, Construction, Maintenance, Utility, "Work Zone, Type Unknown"}
   WorkZone can only be one of: None, Construction, Maintenance, Utility, or Work Zone, Type Unknown.

3. Location SubClassOf hasIntersection only Intersection
   The scoped range of hasIntersection, scoped by Location, is Intersection

4. Intersection SubClassOf {"Not an Intersection", "Four-Way Intersection", "T-Intersection", "Y-Intersection", "Roundabout", "Five-Point, or More", "L-Intersection", "Other Intersection Type"}
   Intersection can only be one of the enumerated types.

5. Location SubClassOf hasCoordinates only Coordinates
   The scoped range of hasCoordinates, scoped by Location, is Coordinates

6. Coordinates SubClassOf hasLatitude only xsd:float
   The scoped range of hasLatitude, scoped by Coordinates, is an xsd:float

7. Coordinates SubClassOf hasLongitude only xsd:float
   The scoped range of hasLongitude, scoped by Coordinates, is an xsd:float

8. Location SubClassOf hasState exactly 1 State
   Every Location has exactly 1 State.

9. State SubClassOf hasStateName only xsd:string
   The scoped range of hasStateName, scoped by State, is an xsd:string

10. State SubClassOf hasCity some City
    Every State has some City.

11. City SubClassOf hasCityName only xsd:string
    The scoped range of hasCityName, scoped by City, is an xsd:string

12. City SubClassOf hasZipCode only xsd:string
    The scoped range of hasZipCode, scoped by City, is an xsd:string

13. City SubClassOf hasCounty exactly 1 County
    Every City has exactly 1 County.

14. County SubClassOf hasCountyName only xsd:string
    The scoped range of hasCountyName, scoped by County, is an xsd:string

15. County SubClassOf hasZipCode only xsd:string
    The scoped range of hasZipCode, scoped by County, is an xsd:string

16. County SubClassOf hasStreet some Street
    Every County has some Street.

17. Street SubClassOf hasStreetName only xsd:string
    The scoped range of hasStreetName, scoped by Street, is an xsd:string

18. Location SubClassOf hasCoordinates exactly 1 Coordinates
    Every Location has exactly 1 Coordinates.

19. Coordinates SubClassOf hasLatitude exactly 1 xsd:float
    Every Coordinates has exactly 1 Latitude.

20. Coordinates SubClassOf hasLongitude exactly 1 xsd:float
    Every Coordinates has exactly 1 Longitude.

21. State SubClassOf hasStateName exactly 1 xsd:string
    Every State has exactly 1 State Name.

22. City SubClassOf hasCityName exactly 1 xsd:string
    Every City has exactly 1 City Name.

23. County SubClassOf hasCountyName exactly 1 xsd:string
    Every County has exactly 1 County Name.

24. Street SubClassOf hasStreetName exactly 1 xsd:string
    Every Street has exactly 1 Street Name.


## Vehicle

![Vehicle](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/vehicle/Vehicle.png)

### Axioms

1. VehicleInAccident SubClassOf Vehicle
    Every VehicleInAccident is Vehicle

2. PerformsRole some VehicleInAccident SubClassOf Vehicle
    Anything that performs a role in a vehicle accident is a type of vehicle.

3. Vehicle SubClassOf PerformsRole some VehicleInAccident
    Every vehicle performs at least one role in a vehicle accident.

4. VehicleInAccident SubClassOf PerformsRole-.some Vehicle
    Every vehicle involved in an accident is the object of a role performed by some vehicle.

5. Vehicle SubClassOf hasWeight Exactly 1 Weight
    Every vehicle has exactly one weight associated with it.

6. Vehicle SubClassOf hasWeight only Weight
    The weight of every vehicle must be of type Weight.

7. Vehicle SubClassOf hasWeight some Weight
    Every vehicle must have at least one weight specified.

8. Owl.Thing SubClassOf hasWeight exactly 1 Weight
    Everything in the ontology must have exactly one weight.

9. VehicleInAccident SubClassOf hasTemporalExtent only TemporalExtent
    The temporal extent (time period) of any vehicle involved in an accident must be TemporalExtent.

10. VehicleInAccident SubClassOf hasTemporalExtent some TemporalExtent
    Every vehicle involved in an accident must have at least one temporal extent.

11. providesRole some VehicleInAccident SubClassOf Crash
    Anything that provides a role involving a VehicleInAccident is classified as a crash.

12. Crash SubClassOf providesRole min 1 VehicleInAccident
   Every Crash provides at least 1 VehicleInAccident role.

13. Crash SubClassOf providesRole some VehicleInAccident
    Every crash must provide at least one VehicleInAccident role.

14. OWL.Thing SubClassOf hasSpeed only xsd:integer
    Everything in the ontology can only have speed of type xsd:integer

15. hasSpeed some xsd:integer SubClassOf VehicleInAccident
    Anything that hasSpeed is classified as a VehicleInAccident.

16. OWL.Thing SubClassOf hasMileage only xsd:float
    Everything in the ontology can only hasMileage of type xsd:float

17. hasMileage some xsd:integer SubClassOf VehicleInAccident
    Anything that hasMileage is classified as a VehicleInAccident

18. VehicleInAccident SubClassOf involvedInHitAndRun only xsd:Boolean
    vehicleInAccident involved in hit-and-run must be represented as a boolean value

19. involvedInHitAndRun some xsd:Boolean SubClassOf VehicleInAccident
    Anything associated with a hit-and-run boolean value is classified as a vehicleInAccident

20. Vehicle SubClassOf hasVehicleType only xsd:string
    The Vehicletype of every Vehicle must be represented as a string.

21. hasVehicleType some xsd:string SubClassOf Vehicle
    Anything that has a VehicleType is classified as a Vehicle.

22. Vehicle SubClassOf hasVehicleType Exactly 1 xsd:string
    Every Vehicle must have exactly one VehicleType, represented as a string

24. hasVehicleMake some xsd:string SubClassOf Vehicle
    Anything that has a VehicleMake is classified as a Vehicle.

25. Vehicle SubClassOf hasVehicleMake Exactly 1 xsd:string
    Every Vehicle must have exactly one VehicleMake, represented as a string.

26. hasVehicleModel some xsd:string SubClassOf Vehicle
    Anything that has a VehicleModel is classified as a Vehicle.

27. Vehicle SubClassOf hasVehicleModel Exactly 1 xsd:string
    Every Vehicle must have exactly one VehicleModel, represented as a string.

28. hasVehicleManufacturingYear some xsd:string SubClassOf Vehicle
    Anything that has a VehicleManufacturingYear is classified as a Vehicle.

29. Vehicle SubClassOf hasVehicleManufacturingYear Exactly 1 xsd:string
    Every Vehicle must have exactly one VehicleManufacturingYear, represented as a string.

30. OWL.Thing SubClassOf rangeFrom only xsd:integer
    Everything in the ontology can only have rangeFrom values of type xsd:integer.

31. OWL.Thing SubClassOf rangeTo only xsd:integer
    Everything in the ontology can only have rangeTo values of type xsd:integer.


## Impairment
![Impairment](https://github.com/korrapati-SaiSree/cs7810-group2/tree/main/delivarables/scehmaDiagrams_Final/Impairment)

### Axioms

1. SubstanceImairments SubClassOf Impairments
    Every SubstanceImairments is SubstanceImairments

2. SubstanceImairments SubClassOf {"Test Not Given", "Tested, No Drugs Found/Negative", "Not Reported", "Narcotic Analgesics", "Depressants", "Hallucinogens", "Cannabinoids", "Stimulants", "Dissociative Anesthetics", "Anabolic Steroids ", "Inhalants","Non-Psychoactive/Other Drugs","Non-Psychoactive/Other Drugs", "Other Drug (Specify:)", "Tested for Drugs, Drugs Found, Type Unknown/Positive", "Tested for Drugs, Results Unknown",
}
   SubstanceImairments can only be one of the enumerated types.

3. Distraction SubClassOf Impairments
    Every SubstanceImairments is SubstanceImairments

4. Distraction SubClassOf {"Not Distracted", "By Other Occupant(s)", "By a Moving Object in Vehicle", "While Talking or Listening to Mobile Phone", "While Adjusting Audio or Climate Controls", "While Using Other Component/Controls Integral to Vehicle", "While Using or Reaching for Device/Object Brought Into Vehicle", "Distracted by Outside Person, Object or Event", "Eating or Drinking", "Smoking Related", "No Driver Present/Unknown if Driver Present","Distraction/Inattention", "Other Mobile Phone Related ", "Distraction/Careless", "Careless/Inattentive", "Lost in Thought/Daydreaming", "Other Distraction","Distraction (Distracted), Details Unknown", "Inattention (Inattentive), Details Unknown ",
}
   Distraction can only be one of the enumerated types.

## SocioEconomic Condition
![SocioEconomic Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/socioeconomic_Factors/socioEconomicCondition.png)

### Axioms

1. Location SubClassOf hasSocioEconomicCondition only SocioEconomicCondition
    The socioeconomic condition of any location must be of type SocioEconomicCondition.

2. IncomeHouseHoldMedium SubClassOf SocioEconomicCondition
    Every IncomeHouseHoldMedium is SocioEconomicCondition

3. OWL.Things SubClassOf incomeHouseHoldMediumAsString only xsd:string
    Everything in the ontology can only have incomeHouseHoldMediumAsString values of type xsd:string.

4. EmploymentRate SubClassOf SocioEconomicCondition
    Every EmploymentRate is SocioEconomicCondition

5. OWL.Things SubClassOf employmentRateAsString only xsd:string
    Everything in the ontology can only have employmentRateAsString values of type xsd:string.

6. PopulationDensity SubClassOf SocioEconomicCondition
    Every PopulationDensity is SocioEconomicCondition

7. OWL.Things SubClassOf populationDensityAsString only xsd:string
    Everything in the ontology can only have populationDensityAsString values of type xsd:string.

8. EducationLevel SubClassOf SocioEconomicCondition
    Every EducationLevel is SocioEconomicCondition

9. EducationLevel SubClassOf {"Less than high school graduate", "High school graduate", "Some college or associate's degree", "Bachelor's degree or higher"}
   EducationLevel can only be one of the enumerated types.


## Weather

### Axioms

1. Location SubClassOf hasWeatherCondition only Weather Condition
    The weather condition of any Location must be of type WeatherCondition.

2. OWL.Things SubClassOf weatherConditionAsString only xsd:string
    Everything in the ontology can only have weatherConditionAsString values of type xsd:string.

3. WeatherCondition SubClassOf hasPrecipitation Exactly 1 Precipitation
    Every weather condition must have exactly one precipitation value associated with it

4. WeatherCondition SubClassOf hasTemperature only Temperature
    The Temperature of every WeatherCondition must be of type Temperature.

5. WeatherCondition SubClassOf hasTemperature some Temperature
    Every WeatherCondition must have at least one Temperature specified.

6. Temperature SubClassOf inCelcius only xsd:decimal
    The temperature in Celsius must always be represented as a decimal value.

7. Temperature SubClassOf inFarenheit only xsd:decimal
    The temperature inFarenheit must always be represented as a decimal value.
