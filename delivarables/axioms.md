# Road Crashes Ontology

![image](https://github.com/user-attachments/assets/8f0dfebb-c632-4451-a281-a0e7c32b2156)

## Module: Driver Condition Schema
 ![image](https://github.com/user-attachments/assets/da6e9d93-7b22-4b86-bbb9-625886d4990e)


     hasDrivingHistory some owl:Thing SubClassOf Driver
     If something has a driving history, it must be a driver.
     
     Driver SubClassOf hasDrivingHistory only DrivingHistory
     The range of the relationship hasDrivingHistory must be DrivingHistory.
     
     Driver SubClassOf hasDrivingHistory some DrivingHistory
     Every driver must have a driving history.
 

hasImpairments some owl:Thing SubClassOf Driver

If something has impairments, it must be a driver.

Driver SubClassOf hasImpairments only Impairments

The range of the relationship hasImpairments must be Impairments.

Driver SubClassOf hasImpairments some Impairments

A driver may have impairments.
 

hasTrafficViolation some owl:Thing SubClassOf DrivingHistory

If something has traffic violations, it must belong to a driving history.

DrivingHistory SubClassOf hasTrafficViolation only TrafficViolation

The range of the relationship hasTrafficViolation must be TrafficViolation.

DrivingHistory SubClassOf hasTrafficViolation some TrafficViolation

A driving history may include at least one traffic violation.
 

hasDrivingExperience some owl:Thing SubClassOf DrivingHistory

If something has driving experience, it must belong to a driving history.

DrivingHistory SubClassOf hasDrivingExperience only DrivingExperience

The range of the relationship hasDrivingExperience must be DrivingExperience.

DrivingHistory SubClassOf hasDrivingExperience some DrivingExperience

A driving history must include at least one driving experience.
 

TrafficViolation SubClassOf licenseSuspension some xsd:string

A traffic violation may result in a license suspension. If there is a suspension, it is captured as a string.

TrafficViolation SubClassOf licenseSuspension max 1 xsd:string

A traffic violation can have at most one associated license suspension, ensuring no ambiguity.
 

TrafficViolation SubClassOf violationType max 1 xsd:string

A traffic violation has at most one type.

TrafficViolation SubClassOf violationType exactly 1 xsd:string

Each traffic violation must have exactly one type.
 

TrafficViolation SubClassOf violationDate some TemporalExtent

Every traffic violation is associated with a date (temporal extent).
 

DrivingExperience SubClassOf totalYearsOfDriving some TemporalExtent

A driving experience must include total years of driving.
 

DrivingExperience SubClassOf experienceLevel only ExperienceLevel

The range of the relationship experienceLevel must be one of the predefined experience levels (novice, intermediate, experienced).

DrivingExperience SubClassOf experienceLevel some ExperienceLevel

Every driving experience must have at least one experience level.
 

Driver SubClassOf hasLicenseStatus max 1 xsd:string

A driver has at most one license status.

Driver SubClassOf hasLicenseStatus exactly 1 xsd:string

Each driver must have exactly one license status.


Module: Emergency Medical Service Schema
 

hasNotificationTime some owl:Thing SubClassOf EmergencyMedicalService

If an entity has a notification time, it must be an emergency medical service.

EmergencyMedicalService SubClassOf hasNotificationTime only TemporalExtent

The range of the property hasNotificationTime must be a temporal extent.

EmergencyMedicalService SubClassOf hasNotificationTime exactly 1 TemporalExtent

Every emergency medical service must have exactly one notification time.
 

hasArrivalTimeToCrash some owl:Thing SubClassOf EmergencyMedicalService

If an entity has an arrival time to crash, it must be an emergency medical service.

EmergencyMedicalService SubClassOf hasArrivalTimeToCrash only TemporalExtent

The range of the property hasArrivalTimeToCrash must be a temporal extent.

EmergencyMedicalService SubClassOf hasArrivalTimeToCrash exactly 1 TemporalExtent

Every emergency medical service must have exactly one arrival time to the crash site.
 

hasArrivalTimeToHospital some owl:Thing SubClassOf EmergencyMedicalService

If an entity has an arrival time to hospital, it must be an emergency medical service.

EmergencyMedicalService SubClassOf hasArrivalTimeToHospital only TemporalExtent

The range of the property hasArrivalTimeToHospital must be a temporal extent.

EmergencyMedicalService SubClassOf hasArrivalTimeToHospital exactly 1 TemporalExtent

Every emergency medical service must have exactly one arrival time to the hospital.
Module: Impairments Schema
 
 

Impairments SubClassOf impairmentsAsString max 1 xsd:string

Each impairment can have at most one associated string description.

Impairments SubClassOf impairmentsAsString exactly 1 xsd:string

Every impairment must have exactly one associated string description.
 

substanceImpairments SubClassOf Impairments

All substance impairments are a type of impairment.

Impairments SubClassOf substanceImpairments only substanceImpairments

The range of the substanceImpairments property must belong to the substanceImpairments class.

Impairments SubClassOf substanceImpairments some substanceImpairments

Every impairment may involve at least one substance impairment.
 

distraction SubClassOf Impairments

All distractions are a type of impairment.

Impairments SubClassOf distraction only distraction

The range of the distraction property must belong to the distraction class.

Impairments SubClassOf distraction some distraction

Every impairment may involve at least one distraction.

Module: Person Schema
 
 

Person SubClassOf hasRace max 1 xsd:string

A person can have at most one associated race.

Person SubClassOf hasRace exactly 1 xsd:string

Every person must have exactly one associated race.
 

Person SubClassOf hasGender max 1 xsd:string

A person can have at most one associated gender.

Person SubClassOf hasGender exactly 1 xsd:string

Every person must have exactly one associated gender.
 

Person SubClassOf hasAge max 1 xsd:integer

A person can have at most one associated age.

Person SubClassOf hasAge exactly 1 xsd:integer

Every person must have exactly one associated age.
 

Person SubClassOf performsRole only PersonInCrash

The range of the property performsRole must belong to the class PersonInCrash.

Person SubClassOf performsRole some PersonInCrash

Every person must perform at least one role in the context of a crash.
 

providesRole some owl:Thing SubClassOf PersonInCrash

If something has a providesRole property, it must belong to PersonInCrash.

PersonInCrash SubClassOf providesRole only Crash

The range of the property providesRole must belong to the class Crash.

PersonInCrash SubClassOf providesRole some Crash

Every person in a crash must provide at least one role in the context of a crash.
 

PersonInCrash SubClassOf hasInjurySeverity only InjurySeverity

The range of the property hasInjurySeverity must belong to the InjurySeverity class.

PersonInCrash SubClassOf hasInjurySeverity some InjurySeverity

Every person in a crash must have at least one associated injury severity.
 

PersonInCrash SubClassOf isFatal only Fatality

The range of the isFatal property must belong to the class Fatality.

PersonInCrash SubClassOf isFatal some Fatality

Every person in a crash who is fatal must have an associated Fatality record.
 

Fatality SubClassOf isFatal exactly 1 xsd:boolean

A fatality must have exactly one associated boolean value indicating if it is fatal.
 

Fatality SubClassOf hasLagTime only TemporalExtent

The range of the property hasLagTime must belong to the class TemporalExtent.

Fatality SubClassOf hasLagTime some TemporalExtent

Every fatality must have at least one associated TemporalExtent for the lag time, representing the time between the crash and the fatality.


PersonInCrash SubClassOf isNonOccupant only NonOccupant

The range of the isNonOccupant property must belong to the class NonOccupant.

PersonInCrash SubClassOf isNonOccupant some NonOccupant

Every person in a crash who is a non-occupant must be associated with at least one NonOccupant record.
 

PersonInCrash SubClassOf isOccupant only Occupant

The range of the isOccupant property must belong to the class Occupant.

PersonInCrash SubClassOf isOccupant some Occupant

Every person in a crash who is an occupant must be associated with at least one Occupant record.
 

NonOccupant SubClassOf locationDuringCrash max 1 xsd:string

A non-occupant can have at most one associated location during the crash.

NonOccupant SubClassOf locationDuringCrash exactly 1 xsd:string

Every non-occupant must have exactly one associated location during the crash.
 

NonOccupant SubClassOf hasImpairment only Impairments

The range of the property hasImpairment must belong to the class Impairments.

NonOccupant SubClassOf hasImpairment some Impairments

Every non-occupant must have at least one associated impairment.
 

NonOccupant SubClassOf isPedestrian only Pedestrian

The range of the property isPedestrian must belong to the class Pedestrian.

NonOccupant SubClassOf isPedestrian some Pedestrian

Every non-occupant who is a pedestrian must have an associated record in the class Pedestrian.
 

NonOccupant SubClassOf isCyclist only Cyclist

The range of the property isCyclist must belong to the class Cyclist.


NonOccupant SubClassOf isCyclist some Cyclist

Every non-occupant who is a cyclist must have an associated record in the class Cyclist.
 

Occupant SubClassOf seatPosition max 1 xsd:string

An occupant can have at most one associated seat position.

Occupant SubClassOf seatPosition exactly 1 xsd:string

Every occupant must have exactly one associated seat position.
 

Occupant SubClassOf safetyRestraintUsed max 1 xsd:string

An occupant can have at most one associated safety restraint used.

Occupant SubClassOf safetyRestraintUsed exactly 1 xsd:string

Every occupant must have exactly one associated safety restraint used.
 

Occupant SubClassOf hasAirbagDeployed max 1 xsd:boolean

An occupant can have at most one associated boolean value indicating whether an airbag was deployed.

Occupant SubClassOf hasAirbagDeployed exactly 1 xsd:boolean

Every occupant must have exactly one associated boolean value indicating whether an airbag was deployed.
 

Occupant SubClassOf isDriver only Driver

The range of the property isDriver must belong to the class Driver.

Occupant SubClassOf isDriver some Driver

Every occupant who is a driver must have an associated record in the class Driver.
 

Occupant SubClassOf isPassenger only Passenger

The range of the property isPassenger must belong to the class Passenger.

Occupant SubClassOf isPassenger some Passenger

Every occupant who is a passenger must have an associated record in the class Passenger.
 

PersonInCrash SubClassOf someTemporalAspect only TemporalExtent

The range of the relationship between PersonInCrash and its temporal aspects must belong to the class TemporalExtent.

PersonInCrash SubClassOf someTemporalAspect some TemporalExtent

Every PersonInCrash must have at least one associated TemporalExtent, representing some time-related information about their crash involvement.
Module: Time Schema
 
 

PointInTime SubClassOf TemporalExtent

Every PointInTime is a specific instance of TemporalExtent, implying that all PointInTime instances are part of the broader TemporalExtent class.
 

TimeInterval SubClassOf TemporalExtent

Every TimeInterval is a subclass of TemporalExtent, representing a span or interval of time within the broader temporal framework.
 

PointInTime SubClassOf hasTimeOfTheDay only TimeOfDay

The range of the hasTimeOfTheDay property must belong to the class TimeOfDay.

PointInTime SubClassOf hasTimeOfTheDay some TimeOfDay

Every PointInTime must have at least one associated TimeOfDay.
 

PointInTime SubClassOf hasDayOfTheWeek only DayOfTheWeek

The range of the hasDayOfTheWeek property must belong to the class DayOfTheWeek.

PointInTime SubClassOf hasDayOfTheWeek some DayOfTheWeek

Every PointInTime must have at least one associated DayOfTheWeek.
 

PointInTime SubClassOf hasSeason only Season

The range of the hasSeason property must belong to the class Season.

PointInTime SubClassOf hasSeason some Season

Every PointInTime must have at least one associated Season.
 

PointInTime SubClassOf hasValue max 1 xsd:datetime

A PointInTime can have at most one associated xsd:datetime value.

PointInTime SubClassOf hasValue exactly 1 xsd:datetime

Every PointInTime must have exactly one associated xsd:datetime value.
 

TimeInterval SubClassOf startsAt only PointInTime

The range of the startsAt property must belong to the class PointInTime.

TimeInterval SubClassOf startsAt some PointInTime

Every TimeInterval must start at a specific PointInTime.
 

TimeInterval SubClassOf endsAt only PointInTime

The range of the endsAt property must belong to the class PointInTime.

TimeInterval SubClassOf endsAt some PointInTime

Every TimeInterval must end at a specific PointInTime.
 
Crash
 

hasMannerOfCollision some owl:Thing SubClassOf Crash

If an entity has a manner of collision, it must be a Crash.

Crash SubClassOf hasMannerOfCollision only MannerOfCollision

The range of the property hasMannerOfCollision must be a MannerOfCollision.

Crash SubClassOf hasMannerOfCollision exactly 1 MannerOfCollision

Every Crash must have exactly one manner of collision.
 

hasTemporalExtent some owl:Thing SubClassOf Crash

If an entity has a temporal extent, it must be a Crash.

Crash SubClassOf hasTemporalExtent only TemporalExtent

The range of the property hasTemporalExtent must be a TemporalExtent.

Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent

Every Crash must have exactly one temporal extent.
 

occurredAt some owl:Thing SubClassOf Crash

If an entity occurred at a location, it must be a Crash.

Crash SubClassOf occurredAt only Location

The range of the property occurredAt must be a Location.

Crash SubClassOf occurredAt exactly 1 Location

Every Crash must occur at exactly one location.
 

hasTotalFatalities some owl:Thing SubClassOf Crash

If an entity has total fatalities, it must be a Crash.

Crash SubClassOf hasTotalFatalities only xsd:integer

The range of the property hasTotalFatalities must be an integer value.

Crash SubClassOf hasTotalFatalities exactly 1 xsd:integer

Every Crash must have exactly one integer value representing total fatalities.
 

hasParticipant some owl:Thing SubClassOf Crash

If an entity has participants, it must be a Crash.

Crash SubClassOf hasParticipant only Participant

The range of the property hasParticipant must be a Participant.

Crash SubClassOf hasParticipant min 0 Participant

A Crash may have zero or more Participants.
 

Person SubClassOf Participant

Every Person is a subclass of Participant.



Vehicle SubClassOf Participant

Every Vehicle is a subclass of Participant.

EMS SubClassOf Participant

Every EMS (Emergency Medical Service) is a subclass of Participant.
Location
 
1. Location → hasWorkZone → WorkZone
•	Axiom 3: Global Domain
Manchester Syntax:
hasWorkZone some owl:Thing SubClassOf Location
Natural Language Description:
If an entity has a work zone, it must be a Location.
•	Axiom 5: Global Range
Manchester Syntax:
Location SubClassOf hasWorkZone only WorkZone
Natural Language Description:
The range of the property hasWorkZone must be a WorkZone.
•	Axiom 7: Existential Restriction
Manchester Syntax:
Location SubClassOf hasWorkZone some WorkZone
Natural Language Description:
Every Location must have at least one WorkZone.
 
2. Location → hasIntersection → Intersection
•	Axiom 3: Global Domain
Manchester Syntax:
hasIntersection some owl:Thing SubClassOf Location
Natural Language Description:
If an entity has an intersection, it must be a Location.
•	Axiom 5: Global Range
Manchester Syntax:
Location SubClassOf hasIntersection only Intersection
Natural Language Description:
The range of the property hasIntersection must be an Intersection.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Location SubClassOf hasIntersection exactly 1 Intersection
Natural Language Description:
Every Location must have exactly one intersection type.
 
3. Location → hasCoordinates → Coordinates
•	Axiom 3: Global Domain
Manchester Syntax:
hasCoordinates some owl:Thing SubClassOf Location
Natural Language Description:
If an entity has coordinates, it must be a Location.
•	Axiom 5: Global Range
Manchester Syntax:
Location SubClassOf hasCoordinates only Coordinates
Natural Language Description:
The range of the property hasCoordinates must be Coordinates.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Location SubClassOf hasCoordinates exactly 1 Coordinates
Natural Language Description:
Every Location must have exactly one set of coordinates.
 
4. Coordinates → hasLatitude → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasLatitude some owl:Thing SubClassOf Coordinates
Natural Language Description:
If an entity has a latitude, it must be a set of Coordinates.
•	Axiom 5: Global Range
Manchester Syntax:
Coordinates SubClassOf hasLatitude only xsd:float
Natural Language Description:
The range of the property hasLatitude must be a float value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Coordinates SubClassOf hasLatitude exactly 1 xsd:float
Natural Language Description:
Every set of Coordinates must have exactly one latitude value.
 
5. Coordinates → hasLongitude → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasLongitude some owl:Thing SubClassOf Coordinates
Natural Language Description:
If an entity has a longitude, it must be a set of Coordinates.
•	Axiom 5: Global Range
Manchester Syntax:
Coordinates SubClassOf hasLongitude only xsd:float
Natural Language Description:
The range of the property hasLongitude must be a float value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Coordinates SubClassOf hasLongitude exactly 1 xsd:float
Natural Language Description:
Every set of Coordinates must have exactly one longitude value.
 
6. Location → hasState → State
•	Axiom 3: Global Domain
Manchester Syntax:
hasState some owl:Thing SubClassOf Location
Natural Language Description:
If an entity has a state, it must be a Location.
•	Axiom 5: Global Range
Manchester Syntax:
Location SubClassOf hasState only State
Natural Language Description:
The range of the property hasState must be a State.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Location SubClassOf hasState exactly 1 State
Natural Language Description:
Every Location must have exactly one state.
 
7. State → hasStateName → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasStateName some owl:Thing SubClassOf State
Natural Language Description:
If an entity has a state name, it must be a State.
•	Axiom 5: Global Range
Manchester Syntax:
State SubClassOf hasStateName only xsd:string
Natural Language Description:
The range of the property hasStateName must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
State SubClassOf hasStateName exactly 1 xsd:string
Natural Language Description:
Every State must have exactly one state name.
 
8. State → hasCity → City
•	Axiom 3: Global Domain
Manchester Syntax:
hasCity some owl:Thing SubClassOf State
Natural Language Description:
If an entity has a city, it must be a State.
•	Axiom 5: Global Range
Manchester Syntax:
State SubClassOf hasCity only City
Natural Language Description:
The range of the property hasCity must be a City.
•	Axiom 7: Existential Restriction
Manchester Syntax:
State SubClassOf hasCity some City
Natural Language Description:
Every State must have at least one City.
 
9. City → hasCityName → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasCityName some owl:Thing SubClassOf City
Natural Language Description:
If an entity has a city name, it must be a City.
•	Axiom 5: Global Range
Manchester Syntax:
City SubClassOf hasCityName only xsd:string
Natural Language Description:
The range of the property hasCityName must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
City SubClassOf hasCityName exactly 1 xsd:string
Natural Language Description:
Every City must have exactly one city name.
 
10. City → hasZipCode → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasZipCode some owl:Thing SubClassOf City
Natural Language Description:
If an entity has a zip code, it must be a City.
•	Axiom 5: Global Range
Manchester Syntax:
City SubClassOf hasZipCode only xsd:string
Natural Language Description:
The range of the property hasZipCode must be a string value.
•	Axiom 7: Existential Restriction
Manchester Syntax:
City SubClassOf hasZipCode some xsd:string
Natural Language Description:
Every City must have at least one zip code.
 
City → hasCounty → County
•	Axiom 3: Global Domain
Manchester Syntax:
hasCounty some owl:Thing SubClassOf City
Natural Language Description:
If an entity has a county, it must be a City.
•	Axiom 5: Global Range
Manchester Syntax:
City SubClassOf hasCounty only County
Natural Language Description:
The range of the property hasCounty must be a County.
•	Axiom 7: Existential Restriction
Manchester Syntax:
City SubClassOf hasCounty some County
Natural Language Description:
Every City must be associated with at least one County.
11. County → hasCountyName → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasCountyName some owl:Thing SubClassOf County
Natural Language Description:
If an entity has a county name, it must be a County.
•	Axiom 5: Global Range
Manchester Syntax:
County SubClassOf hasCountyName only xsd:string
Natural Language Description:
The range of the property hasCountyName must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
County SubClassOf hasCountyName exactly 1 xsd:string
Natural Language Description:
Every County must have exactly one county name.
 
12. County → hasZipCode → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasZipCode some owl:Thing SubClassOf County
Natural Language Description:
If an entity has a zip code, it must be a County.
•	Axiom 5: Global Range
Manchester Syntax:
County SubClassOf hasZipCode only xsd:string
Natural Language Description:
The range of the property hasZipCode must be a string value.
•	Axiom 7: Existential Restriction
Manchester Syntax:
County SubClassOf hasZipCode some xsd:string
Natural Language Description:
Every County must have at least one zip code.
 
13. County → hasStreet → Street
•	Axiom 3: Global Domain
Manchester Syntax:
hasStreet some owl:Thing SubClassOf County
Natural Language Description:
If an entity has a street, it must be a County.
•	Axiom 5: Global Range
Manchester Syntax:
County SubClassOf hasStreet only Street
Natural Language Description:
The range of the property hasStreet must be a Street.
•	Axiom 7: Existential Restriction
Manchester Syntax:
County SubClassOf hasStreet some Street
Natural Language Description:
Every County must have at least one Street.
 
14. Street → hasStreetName → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasStreetName some owl:Thing SubClassOf Street
Natural Language Description:
If an entity has a street name, it must be a Street.
•	Axiom 5: Global Range
Manchester Syntax:
Street SubClassOf hasStreetName only xsd:string
Natural Language Description:
The range of the property hasStreetName must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Street SubClassOf hasStreetName exactly 1 xsd:string
Natural Language Description:
Every Street must have exactly one street name.
Socioeconomic Factors
 
1. Location → hasSocioEconomicCondition → SocioEconomicCondition
•	Axiom 3: Global Domain
Manchester Syntax:
hasSocioEconomicCondition some owl:Thing SubClassOf Location
Natural Language Description:
If an entity has a socio-economic condition, it must be a Location.
•	Axiom 5: Global Range
Manchester Syntax:
Location SubClassOf hasSocioEconomicCondition only SocioEconomicCondition
Natural Language Description:
The range of the property hasSocioEconomicCondition must be a SocioEconomicCondition.
•	Axiom 7: Existential Restriction
Manchester Syntax:
Location SubClassOf hasSocioEconomicCondition some SocioEconomicCondition
Natural Language Description:
Every Location must have at least one SocioEconomicCondition.
 
2. SocioEconomicCondition → hasTemporalExtent → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasTemporalExtent some owl:Thing SubClassOf SocioEconomicCondition
Natural Language Description:
If an entity has a temporal extent, it must be a SocioEconomicCondition.
•	Axiom 5: Global Range
Manchester Syntax:
SocioEconomicCondition SubClassOf hasTemporalExtent only TemporalExtent
Natural Language Description:
The range of the property hasTemporalExtent must be a TemporalExtent.
•	Axiom 7: Existential Restriction
Manchester Syntax:
SocioEconomicCondition SubClassOf hasTemporalExtent some TemporalExtent
Natural Language Description:
Every SocioEconomicCondition must be associated with at least one TemporalExtent.
 
3. SocioEconomicCondition → hasIncomeHouseholdMedian → IncomeHouseholdMedian
•	Axiom 3: Global Domain
Manchester Syntax:
hasIncomeHouseholdMedian some owl:Thing SubClassOf SocioEconomicCondition
Natural Language Description:
If an entity has a median household income, it must be a SocioEconomicCondition.
•	Axiom 5: Global Range
Manchester Syntax:
SocioEconomicCondition SubClassOf hasIncomeHouseholdMedian only IncomeHouseholdMedian
Natural Language Description:
The range of the property hasIncomeHouseholdMedian must be an IncomeHouseholdMedian.
•	Axiom 7: Existential Restriction
Manchester Syntax:
SocioEconomicCondition SubClassOf hasIncomeHouseholdMedian some IncomeHouseholdMedian
Natural Language Description:
Every SocioEconomicCondition must have at least one IncomeHouseholdMedian.
 
4. IncomeHouseholdMedian → incomeHouseholdMedianAsDecimal → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
incomeHouseholdMedianAsDecimal some owl:Thing SubClassOf IncomeHouseholdMedian
Natural Language Description:
If an entity has a median household income as a decimal, it must be an IncomeHouseholdMedian.
•	Axiom 5: Global Range
Manchester Syntax:
IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal only xsd:decimal
Natural Language Description:
The range of the property incomeHouseholdMedianAsDecimal must be a decimal value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal exactly 1 xsd:decimal
Natural Language Description:
Every IncomeHouseholdMedian must have exactly one decimal value representing its median household income.
 
5. SocioEconomicCondition → hasEmploymentRate → EmploymentRate
•	Axiom 3: Global Domain
Manchester Syntax:
hasEmploymentRate some owl:Thing SubClassOf SocioEconomicCondition
Natural Language Description:
If an entity has an employment rate, it must be a SocioEconomicCondition.
•	Axiom 5: Global Range
Manchester Syntax:
SocioEconomicCondition SubClassOf hasEmploymentRate only EmploymentRate
Natural Language Description:
The range of the property hasEmploymentRate must be an EmploymentRate.
•	Axiom 7: Existential Restriction
Manchester Syntax:
SocioEconomicCondition SubClassOf hasEmploymentRate some EmploymentRate
Natural Language Description:
Every SocioEconomicCondition must have at least one EmploymentRate.
 
6. EmploymentRate → employmentRateAsDecimal → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
employmentRateAsDecimal some owl:Thing SubClassOf EmploymentRate
Natural Language Description:
If an entity has an employment rate as a decimal, it must be an EmploymentRate.
•	Axiom 5: Global Range
Manchester Syntax:
EmploymentRate SubClassOf employmentRateAsDecimal only xsd:decimal
Natural Language Description:
The range of the property employmentRateAsDecimal must be a decimal value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
EmploymentRate SubClassOf employmentRateAsDecimal exactly 1 xsd:decimal
Natural Language Description:
Every EmploymentRate must have exactly one decimal value representing its employment rate.
 
7. SocioEconomicCondition → hasPopulationDensity → PopulationDensity
•	Axiom 3: Global Domain
Manchester Syntax:
hasPopulationDensity some owl:Thing SubClassOf SocioEconomicCondition
Natural Language Description:
If an entity has a population density, it must be a SocioEconomicCondition.
•	Axiom 5: Global Range
Manchester Syntax:
SocioEconomicCondition SubClassOf hasPopulationDensity only PopulationDensity
Natural Language Description:
The range of the property hasPopulationDensity must be a PopulationDensity.
•	Axiom 7: Existential Restriction
Manchester Syntax:
SocioEconomicCondition SubClassOf hasPopulationDensity some PopulationDensity
Natural Language Description:
Every SocioEconomicCondition must have at least one PopulationDensity.
 
8. PopulationDensity → populationDensityAsDecimal → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
populationDensityAsDecimal some owl:Thing SubClassOf PopulationDensity
Natural Language Description:
If an entity has a population density as a decimal, it must be a PopulationDensity.
•	Axiom 5: Global Range
Manchester Syntax:
PopulationDensity SubClassOf populationDensityAsDecimal only xsd:decimal
Natural Language Description:
The range of the property populationDensityAsDecimal must be a decimal value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
PopulationDensity SubClassOf populationDensityAsDecimal exactly 1 xsd:decimal
Natural Language Description:
Every PopulationDensity must have exactly one decimal value representing its population density.
 
9. SocioEconomicCondition → hasEducationLevel → EducationLevel
•	Axiom 3: Global Domain
Manchester Syntax:
hasEducationLevel some owl:Thing SubClassOf SocioEconomicCondition
Natural Language Description:
If an entity has an education level, it must be a SocioEconomicCondition.
•	Axiom 5: Global Range
Manchester Syntax:
SocioEconomicCondition SubClassOf hasEducationLevel only EducationLevel
Natural Language Description:
The range of the property hasEducationLevel must be an EducationLevel.
•	Axiom 7: Existential Restriction
Manchester Syntax:
SocioEconomicCondition SubClassOf hasEducationLevel some EducationLevel
Natural Language Description:
Every SocioEconomicCondition must have at least one EducationLevel.

Vehicle
 
1. Vehicle → hasVehicleType → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasVehicleType some owl:Thing SubClassOf Vehicle
Natural Language Description:
If an entity has a vehicle type, it must be a Vehicle.
•	Axiom 5: Global Range
Manchester Syntax:
Vehicle SubClassOf hasVehicleType only xsd:string
Natural Language Description:
The range of the property hasVehicleType must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Vehicle SubClassOf hasVehicleType exactly 1 xsd:string
Natural Language Description:
Every Vehicle must have exactly one vehicle type.
 
2. Vehicle → hasVehicleModel → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasVehicleModel some owl:Thing SubClassOf Vehicle
Natural Language Description:
If an entity has a vehicle model, it must be a Vehicle.
•	Axiom 5: Global Range
Manchester Syntax:
Vehicle SubClassOf hasVehicleModel only xsd:string
Natural Language Description:
The range of the property hasVehicleModel must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Vehicle SubClassOf hasVehicleModel exactly 1 xsd:string
Natural Language Description:
Every Vehicle must have exactly one vehicle model.
 
3. Vehicle → hasVehicleMake → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasVehicleMake some owl:Thing SubClassOf Vehicle
Natural Language Description:
If an entity has a vehicle make, it must be a Vehicle.
•	Axiom 5: Global Range
Manchester Syntax:
Vehicle SubClassOf hasVehicleMake only xsd:string
Natural Language Description:
The range of the property hasVehicleMake must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Vehicle SubClassOf hasVehicleMake exactly 1 xsd:string
Natural Language Description:
Every Vehicle must have exactly one vehicle make.
 
4. Vehicle → hasVehicleManufacturingYear → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasVehicleManufacturingYear some owl:Thing SubClassOf Vehicle
Natural Language Description:
If an entity has a manufacturing year, it must be a Vehicle.
•	Axiom 5: Global Range
Manchester Syntax:
Vehicle SubClassOf hasVehicleManufacturingYear only xsd:integer
Natural Language Description:
The range of the property hasVehicleManufacturingYear must be an integer value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Vehicle SubClassOf hasVehicleManufacturingYear exactly 1 xsd:integer
Natural Language Description:
Every Vehicle must have exactly one manufacturing year.
 
5. Vehicle → hasWeight → Weight
•	Axiom 3: Global Domain
Manchester Syntax:
hasWeight some owl:Thing SubClassOf Vehicle
Natural Language Description:
If an entity has a weight, it must be a Vehicle.
•	Axiom 5: Global Range
Manchester Syntax:
Vehicle SubClassOf hasWeight only Weight
Natural Language Description:
The range of the property hasWeight must be a Weight.
•	Axiom 7: Existential Restriction
Manchester Syntax:
Vehicle SubClassOf hasWeight some Weight
Natural Language Description:
Every Vehicle must have at least one Weight.
 
6. Weight → rangeFrom → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
rangeFrom some owl:Thing SubClassOf Weight
Natural Language Description:
If an entity has a weight range starting value, it must be a Weight.
•	Axiom 5: Global Range
Manchester Syntax:
Weight SubClassOf rangeFrom only xsd:integer
Natural Language Description:
The range of the property rangeFrom must be an integer value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Weight SubClassOf rangeFrom exactly 1 xsd:integer
Natural Language Description:
Every Weight must have exactly one starting value for the weight range.
 
7. Weight → rangeTo → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
rangeTo some owl:Thing SubClassOf Weight
Natural Language Description:
If an entity has a weight range ending value, it must be a Weight.
•	Axiom 5: Global Range
Manchester Syntax:
Weight SubClassOf rangeTo only xsd:integer
Natural Language Description:
The range of the property rangeTo must be an integer value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Weight SubClassOf rangeTo exactly 1 xsd:integer
Natural Language Description:
Every Weight must have exactly one ending value for the weight range.
 
8. VehicleInAccident → performsRole → Vehicle
•	Axiom 3: Global Domain
Manchester Syntax:
performsRole some owl:Thing SubClassOf VehicleInAccident
Natural Language Description:
If an entity performs a role, it must be a VehicleInAccident.
•	Axiom 5: Global Range
Manchester Syntax:
VehicleInAccident SubClassOf performsRole only Vehicle
Natural Language Description:
The range of the property performsRole must be a Vehicle.
 
9. VehicleInAccident → providesRole → Crash
•	Axiom 3: Global Domain
Manchester Syntax:
providesRole some owl:Thing SubClassOf VehicleInAccident
Natural Language Description:
If an entity provides a role, it must be a VehicleInAccident.
•	Axiom 5: Global Range
Manchester Syntax:
VehicleInAccident SubClassOf providesRole only Crash
Natural Language Description:
The range of the property providesRole must be a Crash.
 
10. VehicleInAccident → hasSpeed → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasSpeed some owl:Thing SubClassOf VehicleInAccident
Natural Language Description:
If an entity has a speed, it must be a VehicleInAccident.
•	Axiom 5: Global Range
Manchester Syntax:
VehicleInAccident SubClassOf hasSpeed only xsd:integer
Natural Language Description:
The range of the property hasSpeed must be an integer value.
 
11. VehicleInAccident → hasMileage → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasMileage some owl:Thing SubClassOf VehicleInAccident
Natural Language Description:
If an entity has mileage, it must be a VehicleInAccident.
•	Axiom 5: Global Range
Manchester Syntax:
VehicleInAccident SubClassOf hasMileage only xsd:float
Natural Language Description:
The range of the property hasMileage must be a float value.
 
12. VehicleInAccident → involvedInHitAndRun → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
involvedInHitAndRun some owl:Thing SubClassOf VehicleInAccident
Natural Language Description:
If an entity is involved in a hit-and-run, it must be a VehicleInAccident.
•	Axiom 5: Global Range
Manchester Syntax:
VehicleInAccident SubClassOf involvedInHitAndRun only xsd:boolean
Natural Language Description:
The range of the property involvedInHitAndRun must be a boolean value.
 
13. VehicleInAccident → hasTemporalExtent → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasTemporalExtent some owl:Thing SubClassOf VehicleInAccident
Natural Language Description:
If an entity has a temporal extent, it must be a VehicleInAccident.
•	Axiom 5: Global Range
Manchester Syntax:
VehicleInAccident SubClassOf hasTemporalExtent only TemporalExtent
Natural Language Description:
The range of the property hasTemporalExtent must be a TemporalExtent.
Weather Condition
 
1. Location → hasWeatherCondition → WeatherCondition
•	Axiom 3: Global Domain
Manchester Syntax:
hasWeatherCondition some owl:Thing SubClassOf Location
Natural Language Description:
If an entity has a weather condition, it must be a Location.
•	Axiom 5: Global Range
Manchester Syntax:
Location SubClassOf hasWeatherCondition only WeatherCondition
Natural Language Description:
The range of the property hasWeatherCondition must be a WeatherCondition.
•	Axiom 7: Existential Restriction
Manchester Syntax:
Location SubClassOf hasWeatherCondition some WeatherCondition
Natural Language Description:
Every Location must have at least one WeatherCondition.
 
2. WeatherCondition → hasTemperature → Temperature
•	Axiom 3: Global Domain
Manchester Syntax:
hasTemperature some owl:Thing SubClassOf WeatherCondition
Natural Language Description:
If an entity has a temperature, it must be a WeatherCondition.
•	Axiom 5: Global Range
Manchester Syntax:
WeatherCondition SubClassOf hasTemperature only Temperature
Natural Language Description:
The range of the property hasTemperature must be a Temperature.
•	Axiom 7: Existential Restriction
Manchester Syntax:
WeatherCondition SubClassOf hasTemperature some Temperature
Natural Language Description:
Every WeatherCondition must have at least one Temperature.
 
3. WeatherCondition → hasPrecipitation → Precipitation
•	Axiom 3: Global Domain
Manchester Syntax:
hasPrecipitation some owl:Thing SubClassOf WeatherCondition
Natural Language Description:
If an entity has precipitation, it must be a WeatherCondition.
•	Axiom 5: Global Range
Manchester Syntax:
WeatherCondition SubClassOf hasPrecipitation only Precipitation
Natural Language Description:
The range of the property hasPrecipitation must be a Precipitation.
•	Axiom 17: Structural Tautology
Manchester Syntax:
WeatherCondition SubClassOf hasPrecipitation min 0 Precipitation
Natural Language Description:
A WeatherCondition may have zero or more Precipitation instances.
 
4. WeatherCondition → hasTemporalExtent → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasTemporalExtent some owl:Thing SubClassOf WeatherCondition
Natural Language Description:
If an entity has a temporal extent, it must be a WeatherCondition.
•	Axiom 5: Global Range
Manchester Syntax:
WeatherCondition SubClassOf hasTemporalExtent only TemporalExtent
Natural Language Description:
The range of the property hasTemporalExtent must be a TemporalExtent.
•	Axiom 7: Existential Restriction
Manchester Syntax:
WeatherCondition SubClassOf hasTemporalExtent some TemporalExtent
Natural Language Description:
Every WeatherCondition must have at least one TemporalExtent.
 
5. WeatherCondition → weatherConditionAsString → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
weatherConditionAsString some owl:Thing SubClassOf WeatherCondition
Natural Language Description:
If an entity has a weather condition as a string, it must be a WeatherCondition.
•	Axiom 5: Global Range
Manchester Syntax:
WeatherCondition SubClassOf weatherConditionAsString only xsd:string
Natural Language Description:
The range of the property weatherConditionAsString must be a string value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
WeatherCondition SubClassOf weatherConditionAsString exactly 1 xsd:string
Natural Language Description:
Every WeatherCondition must have exactly one string representing its description.
 
6. Temperature → inCelsius → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
inCelsius some owl:Thing SubClassOf Temperature
Natural Language Description:
If an entity has a temperature in Celsius, it must be a Temperature.
•	Axiom 5: Global Range
Manchester Syntax:
Temperature SubClassOf inCelsius only xsd:decimal
Natural Language Description:
The range of the property inCelsius must be a decimal value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Temperature SubClassOf inCelsius exactly 1 xsd:decimal
Natural Language Description:
Every Temperature must have exactly one value in Celsius.
 
7. Temperature → inFahrenheit → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
inFahrenheit some owl:Thing SubClassOf Temperature
Natural Language Description:
If an entity has a temperature in Fahrenheit, it must be a Temperature.
•	Axiom 5: Global Range
Manchester Syntax:
Temperature SubClassOf inFahrenheit only xsd:decimal
Natural Language Description:
The range of the property inFahrenheit must be a decimal value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Temperature SubClassOf inFahrenheit exactly 1 xsd:decimal
Natural Language Description:
Every Temperature must have exactly one value in Fahrenheit.

![image](https://github.com/user-attachments/assets/ec72c5ef-a426-4310-bda4-45f1b646afcd)

