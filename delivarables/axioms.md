# Road Crashes Onotlogy

![image](https://github.com/user-attachments/assets/5249a2f4-c027-42dd-88d6-5676e0cc8aba)

 
Module: Driver Condition Schema
 
1. Driver → hasDrivingHistory → DrivingHistory
•	Axiom 3: Global Domain
Manchester Syntax:
hasDrivingHistory some owl:Thing SubClassOf Driver
Natural Language Description:
If something has a driving history, it must be a driver.
•	Axiom 5: Global Range
Manchester Syntax:
Driver SubClassOf hasDrivingHistory only DrivingHistory
Natural Language Description:
The range of the relationship hasDrivingHistory must be DrivingHistory.
•	Axiom 7: Existential
Manchester Syntax:
Driver SubClassOf hasDrivingHistory some DrivingHistory
Natural Language Description:
Every driver must have a driving history.
 
2. Driver → hasImpairments → Impairments
•	Axiom 3: Global Domain
Manchester Syntax:
hasImpairments some owl:Thing SubClassOf Driver
Natural Language Description:
If something has impairments, it must be a driver.
•	Axiom 5: Global Range
Manchester Syntax:
Driver SubClassOf hasImpairments only Impairments
Natural Language Description:
The range of the relationship hasImpairments must be Impairments.
•	Axiom 7: Existential
Manchester Syntax:
Driver SubClassOf hasImpairments some Impairments
Natural Language Description:
A driver may have impairments.
 
3. DrivingHistory → hasTrafficViolation → TrafficViolation
•	Axiom 3: Global Domain
Manchester Syntax:
hasTrafficViolation some owl:Thing SubClassOf DrivingHistory
Natural Language Description:
If something has traffic violations, it must belong to a driving history.
•	Axiom 5: Global Range
Manchester Syntax:
DrivingHistory SubClassOf hasTrafficViolation only TrafficViolation
Natural Language Description:
The range of the relationship hasTrafficViolation must be TrafficViolation.
•	Axiom 7: Existential
Manchester Syntax:
DrivingHistory SubClassOf hasTrafficViolation some TrafficViolation
Natural Language Description:
A driving history may include at least one traffic violation.
 
4. DrivingHistory → hasDrivingExperience → DrivingExperience
•	Axiom 3: Global Domain
Manchester Syntax:
hasDrivingExperience some owl:Thing SubClassOf DrivingHistory
Natural Language Description:
If something has driving experience, it must belong to a driving history.
•	Axiom 5: Global Range
Manchester Syntax:
DrivingHistory SubClassOf hasDrivingExperience only DrivingExperience
Natural Language Description:
The range of the relationship hasDrivingExperience must be DrivingExperience.
•	Axiom 7: Existential
Manchester Syntax:
DrivingHistory SubClassOf hasDrivingExperience some DrivingExperience
Natural Language Description:
A driving history must include at least one driving experience.
 
5. TrafficViolation → licenseSuspension → xsd
•	Axiom 7: Existential
Manchester Syntax:
TrafficViolation SubClassOf licenseSuspension some xsd:string
Natural Language Description:
A traffic violation may result in a license suspension. If there is a suspension, it is captured as a string.
•	Axiom 10: Qualified Functionality
Manchester Syntax:
TrafficViolation SubClassOf licenseSuspension max 1 xsd:string
Natural Language Description:
A traffic violation can have at most one associated license suspension, ensuring no ambiguity.
 
6. TrafficViolation → violationType → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
TrafficViolation SubClassOf violationType max 1 xsd:string
Natural Language Description:
A traffic violation has at most one type.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
TrafficViolation SubClassOf violationType exactly 1 xsd:string
Natural Language Description:
Each traffic violation must have exactly one type.
 
7. TrafficViolation → violationDate → TemporalExtent
•	Axiom 7: Existential
Manchester Syntax:
TrafficViolation SubClassOf violationDate some TemporalExtent
Natural Language Description:
Every traffic violation is associated with a date (temporal extent).
 
8. DrivingExperience → totalYearsOfDriving → TemporalExtent
•	Axiom 7: Existential
Manchester Syntax:
DrivingExperience SubClassOf totalYearsOfDriving some TemporalExtent
Natural Language Description:
A driving experience must include total years of driving.
 
9. DrivingExperience → experienceLevel → ExperienceLevel
•	Axiom 5: Global Range
Manchester Syntax:
DrivingExperience SubClassOf experienceLevel only ExperienceLevel
Natural Language Description:
The range of the relationship experienceLevel must be one of the predefined experience levels (novice, intermediate, experienced).
•	Axiom 7: Existential
Manchester Syntax:
DrivingExperience SubClassOf experienceLevel some ExperienceLevel
Natural Language Description:
Every driving experience must have at least one experience level.
 
10. Driver → hasLicenseStatus → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Driver SubClassOf hasLicenseStatus max 1 xsd:string
Natural Language Description:
A driver has at most one license status.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Driver SubClassOf hasLicenseStatus exactly 1 xsd:string
Natural Language Description:
Each driver must have exactly one license status.


Module: Emergency Medical Service Schema
 
1. EmergencyMedicalService → hasNotificationTime → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasNotificationTime some owl:Thing SubClassOf EmergencyMedicalService
Natural Language Description:
If an entity has a notification time, it must be an emergency medical service.
•	Axiom 5: Global Range
Manchester Syntax:
EmergencyMedicalService SubClassOf hasNotificationTime only TemporalExtent
Natural Language Description:
The range of the property hasNotificationTime must be a temporal extent.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
EmergencyMedicalService SubClassOf hasNotificationTime exactly 1 TemporalExtent
Natural Language Description:
Every emergency medical service must have exactly one notification time.
 
2. EmergencyMedicalService → hasArrivalTimeToCrash → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasArrivalTimeToCrash some owl:Thing SubClassOf EmergencyMedicalService
Natural Language Description:
If an entity has an arrival time to crash, it must be an emergency medical service.
•	Axiom 5: Global Range
Manchester Syntax:
EmergencyMedicalService SubClassOf hasArrivalTimeToCrash only TemporalExtent
Natural Language Description:
The range of the property hasArrivalTimeToCrash must be a temporal extent.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
EmergencyMedicalService SubClassOf hasArrivalTimeToCrash exactly 1 TemporalExtent
Natural Language Description:
Every emergency medical service must have exactly one arrival time to the crash site.
 
3. EmergencyMedicalService → hasArrivalTimeToHospital → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasArrivalTimeToHospital some owl:Thing SubClassOf EmergencyMedicalService
Natural Language Description:
If an entity has an arrival time to hospital, it must be an emergency medical service.
•	Axiom 5: Global Range
Manchester Syntax:
EmergencyMedicalService SubClassOf hasArrivalTimeToHospital only TemporalExtent
Natural Language Description:
The range of the property hasArrivalTimeToHospital must be a temporal extent.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
EmergencyMedicalService SubClassOf hasArrivalTimeToHospital exactly 1 TemporalExtent
Natural Language Description:
Every emergency medical service must have exactly one arrival time to the hospital.
Module: Impairments Schema
 
 
Relationships and Axioms
1. Impairments → impairmentsAsString → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Impairments SubClassOf impairmentsAsString max 1 xsd:string
Natural Language Description:
Each impairment can have at most one associated string description.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Impairments SubClassOf impairmentsAsString exactly 1 xsd:string
Natural Language Description:
Every impairment must have exactly one associated string description.
 
2. Impairments → substanceImpairments
•	Axiom 1: Subclass
Manchester Syntax:
substanceImpairments SubClassOf Impairments
Natural Language Description:
All substance impairments are a type of impairment.
•	Axiom 5: Global Range
Manchester Syntax:
Impairments SubClassOf substanceImpairments only substanceImpairments
Natural Language Description:
The range of the substanceImpairments property must belong to the substanceImpairments class.
•	Axiom 7: Existential
Manchester Syntax:
Impairments SubClassOf substanceImpairments some substanceImpairments
Natural Language Description:
Every impairment may involve at least one substance impairment.
 
3. Impairments → distraction
•	Axiom 1: Subclass
Manchester Syntax:
distraction SubClassOf Impairments
Natural Language Description:
All distractions are a type of impairment.
•	Axiom 5: Global Range
Manchester Syntax:
Impairments SubClassOf distraction only distraction
Natural Language Description:
The range of the distraction property must belong to the distraction class.
•	Axiom 7: Existential
Manchester Syntax:
Impairments SubClassOf distraction some distraction
Natural Language Description:
Every impairment may involve at least one distraction.

Module: Person Schema
 
 
1. Person → hasRace → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Person SubClassOf hasRace max 1 xsd:string
Natural Language Description:
A person can have at most one associated race.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Person SubClassOf hasRace exactly 1 xsd:string
Natural Language Description:
Every person must have exactly one associated race.
 
2. Person → hasGender → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Person SubClassOf hasGender max 1 xsd:string
Natural Language Description:
A person can have at most one associated gender.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Person SubClassOf hasGender exactly 1 xsd:string
Natural Language Description:
Every person must have exactly one associated gender.
 
3. Person → hasAge → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Person SubClassOf hasAge max 1 xsd:integer
Natural Language Description:
A person can have at most one associated age.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Person SubClassOf hasAge exactly 1 xsd:integer
Natural Language Description:
Every person must have exactly one associated age.
 
4. Person → performsRole → PersonInCrash
•	Axiom 5: Global Range
Manchester Syntax:
Person SubClassOf performsRole only PersonInCrash
Natural Language Description:
The range of the property performsRole must belong to the class PersonInCrash.
•	Axiom 7: Existential
Manchester Syntax:
Person SubClassOf performsRole some PersonInCrash
Natural Language Description:
Every person must perform at least one role in the context of a crash.
 
5. PersonInCrash → providesRole → Crash
•	Axiom 3: Global Domain
Manchester Syntax:
providesRole some owl:Thing SubClassOf PersonInCrash
Natural Language Description:
If something has a providesRole property, it must belong to PersonInCrash.
•	Axiom 5: Global Range
Manchester Syntax:
PersonInCrash SubClassOf providesRole only Crash
Natural Language Description:
The range of the property providesRole must belong to the class Crash.
•	Axiom 7: Existential
Manchester Syntax:
PersonInCrash SubClassOf providesRole some Crash
Natural Language Description:
Every person in a crash must provide at least one role in the context of a crash.
 
6. PersonInCrash → hasInjurySeverity → InjurySeverity
•	Axiom 5: Global Range
Manchester Syntax:
PersonInCrash SubClassOf hasInjurySeverity only InjurySeverity
Natural Language Description:
The range of the property hasInjurySeverity must belong to the InjurySeverity class.
•	Axiom 7: Existential
Manchester Syntax:
PersonInCrash SubClassOf hasInjurySeverity some InjurySeverity
Natural Language Description:
Every person in a crash must have at least one associated injury severity.
 
8. PersonInCrash → isFatal → Fatality
•	Axiom 5: Global Range
Manchester Syntax:
PersonInCrash SubClassOf isFatal only Fatality
Natural Language Description:
The range of the isFatal property must belong to the class Fatality.
•	Axiom 7: Existential
Manchester Syntax:
PersonInCrash SubClassOf isFatal some Fatality
Natural Language Description:
Every person in a crash who is fatal must have an associated Fatality record.
 
9. Fatality → isFatal → Boolean
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Fatality SubClassOf isFatal exactly 1 xsd:boolean
Natural Language Description:
A fatality must have exactly one associated boolean value indicating if it is fatal.
 
Fatality → hasLagTime → TemporalExtent
11. Fatality → hasLagTime → TemporalExtent
•	Axiom 5: Global Range
Manchester Syntax:
Fatality SubClassOf hasLagTime only TemporalExtent
Natural Language Description:
The range of the property hasLagTime must belong to the class TemporalExtent.
•	Axiom 7: Existential
Manchester Syntax:
Fatality SubClassOf hasLagTime some TemporalExtent
Natural Language Description:
Every fatality must have at least one associated TemporalExtent for the lag time, representing the time between the crash and the fatality.

10. PersonInCrash → isNonOccupant → NonOccupant
•	Axiom 5: Global Range
Manchester Syntax:
PersonInCrash SubClassOf isNonOccupant only NonOccupant
Natural Language Description:
The range of the isNonOccupant property must belong to the class NonOccupant.
•	Axiom 7: Existential
Manchester Syntax:
PersonInCrash SubClassOf isNonOccupant some NonOccupant
Natural Language Description:
Every person in a crash who is a non-occupant must be associated with at least one NonOccupant record.
 
11. PersonInCrash → isOccupant → Occupant
•	Axiom 5: Global Range
Manchester Syntax:
PersonInCrash SubClassOf isOccupant only Occupant
Natural Language Description:
The range of the isOccupant property must belong to the class Occupant.
•	Axiom 7: Existential
Manchester Syntax:
PersonInCrash SubClassOf isOccupant some Occupant
Natural Language Description:
Every person in a crash who is an occupant must be associated with at least one Occupant record.
 
NonOccupant → locationDuringCrash → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
NonOccupant SubClassOf locationDuringCrash max 1 xsd:string
Natural Language Description:
A non-occupant can have at most one associated location during the crash.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
NonOccupant SubClassOf locationDuringCrash exactly 1 xsd:string
Natural Language Description:
Every non-occupant must have exactly one associated location during the crash.
 
2. NonOccupant → hasImpairment → Impairments
•	Axiom 5: Global Range
Manchester Syntax:
NonOccupant SubClassOf hasImpairment only Impairments
Natural Language Description:
The range of the property hasImpairment must belong to the class Impairments.
•	Axiom 7: Existential
Manchester Syntax:
NonOccupant SubClassOf hasImpairment some Impairments
Natural Language Description:
Every non-occupant must have at least one associated impairment.
 
3. NonOccupant → isPedestrian → Pedestrian
•	Axiom 5: Global Range
Manchester Syntax:
NonOccupant SubClassOf isPedestrian only Pedestrian
Natural Language Description:
The range of the property isPedestrian must belong to the class Pedestrian.
•	Axiom 7: Existential
Manchester Syntax:
NonOccupant SubClassOf isPedestrian some Pedestrian
Natural Language Description:
Every non-occupant who is a pedestrian must have an associated record in the class Pedestrian.
 
4. NonOccupant → isCyclist → Cyclist
•	Axiom 5: Global Range
Manchester Syntax:
NonOccupant SubClassOf isCyclist only Cyclist
Natural Language Description:
The range of the property isCyclist must belong to the class Cyclist.
•	Axiom 7: Existential
Manchester Syntax:
NonOccupant SubClassOf isCyclist some Cyclist
Natural Language Description:
Every non-occupant who is a cyclist must have an associated record in the class Cyclist.
 
Occupant
5. Occupant → seatPosition → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Occupant SubClassOf seatPosition max 1 xsd:string
Natural Language Description:
An occupant can have at most one associated seat position.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Occupant SubClassOf seatPosition exactly 1 xsd:string
Natural Language Description:
Every occupant must have exactly one associated seat position.
 
6. Occupant → safetyRestraintUsed → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Occupant SubClassOf safetyRestraintUsed max 1 xsd:string
Natural Language Description:
An occupant can have at most one associated safety restraint used.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Occupant SubClassOf safetyRestraintUsed exactly 1 xsd:string
Natural Language Description:
Every occupant must have exactly one associated safety restraint used.
 
7. Occupant → hasAirbagDeployed → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
Occupant SubClassOf hasAirbagDeployed max 1 xsd:boolean
Natural Language Description:
An occupant can have at most one associated boolean value indicating whether an airbag was deployed.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Occupant SubClassOf hasAirbagDeployed exactly 1 xsd:boolean
Natural Language Description:
Every occupant must have exactly one associated boolean value indicating whether an airbag was deployed.
 
8. Occupant → isDriver → Driver
•	Axiom 5: Global Range
Manchester Syntax:
Occupant SubClassOf isDriver only Driver
Natural Language Description:
The range of the property isDriver must belong to the class Driver.
•	Axiom 7: Existential
Manchester Syntax:
Occupant SubClassOf isDriver some Driver
Natural Language Description:
Every occupant who is a driver must have an associated record in the class Driver.
 
9. Occupant → isPassenger → Passenger
•	Axiom 5: Global Range
Manchester Syntax:
Occupant SubClassOf isPassenger only Passenger
Natural Language Description:
The range of the property isPassenger must belong to the class Passenger.
•	Axiom 7: Existential
Manchester Syntax:
Occupant SubClassOf isPassenger some Passenger
Natural Language Description:
Every occupant who is a passenger must have an associated record in the class Passenger.
 
PersonInCrash → TemporalExtent
10. PersonInCrash → TemporalExtent
•	Axiom 5: Global Range
Manchester Syntax:
PersonInCrash SubClassOf someTemporalAspect only TemporalExtent
Natural Language Description:
The range of the relationship between PersonInCrash and its temporal aspects must belong to the class TemporalExtent.
•	Axiom 7: Existential
Manchester Syntax:
PersonInCrash SubClassOf someTemporalAspect some TemporalExtent
Natural Language Description:
Every PersonInCrash must have at least one associated TemporalExtent, representing some time-related information about their crash involvement.
Module: Time Schema
 
 
1. PointInTime → TemporalExtent
•	Axiom 1: Subclass Relationship
Manchester Syntax:
PointInTime SubClassOf TemporalExtent
Natural Language Description:
Every PointInTime is a specific instance of TemporalExtent, implying that all PointInTime instances are part of the broader TemporalExtent class.
 
2. TimeInterval → TemporalExtent
•	Axiom 1: Subclass Relationship
Manchester Syntax:
TimeInterval SubClassOf TemporalExtent
Natural Language Description:
Every TimeInterval is a subclass of TemporalExtent, representing a span or interval of time within the broader temporal framework.
 
3. PointInTime → hasTimeOfTheDay → TimeOfDay
•	Axiom 5: Global Range
Manchester Syntax:
PointInTime SubClassOf hasTimeOfTheDay only TimeOfDay
Natural Language Description:
The range of the hasTimeOfTheDay property must belong to the class TimeOfDay.
•	Axiom 7: Existential
Manchester Syntax:
PointInTime SubClassOf hasTimeOfTheDay some TimeOfDay
Natural Language Description:
Every PointInTime must have at least one associated TimeOfDay.
 
4. PointInTime → hasDayOfTheWeek → DayOfTheWeek
•	Axiom 5: Global Range
Manchester Syntax:
PointInTime SubClassOf hasDayOfTheWeek only DayOfTheWeek
Natural Language Description:
The range of the hasDayOfTheWeek property must belong to the class DayOfTheWeek.
•	Axiom 7: Existential
Manchester Syntax:
PointInTime SubClassOf hasDayOfTheWeek some DayOfTheWeek
Natural Language Description:
Every PointInTime must have at least one associated DayOfTheWeek.
 
5. PointInTime → hasSeason → Season
•	Axiom 5: Global Range
Manchester Syntax:
PointInTime SubClassOf hasSeason only Season
Natural Language Description:
The range of the hasSeason property must belong to the class Season.
•	Axiom 7: Existential
Manchester Syntax:
PointInTime SubClassOf hasSeason some Season
Natural Language Description:
Every PointInTime must have at least one associated Season.
 
6. PointInTime → hasValue → xsd
•	Axiom 10: Qualified Functionality
Manchester Syntax:
PointInTime SubClassOf hasValue max 1 xsd:datetime
Natural Language Description:
A PointInTime can have at most one associated xsd:datetime value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
PointInTime SubClassOf hasValue exactly 1 xsd:datetime
Natural Language Description:
Every PointInTime must have exactly one associated xsd:datetime value.
 
7. TimeInterval → startsAt → PointInTime
•	Axiom 5: Global Range
Manchester Syntax:
TimeInterval SubClassOf startsAt only PointInTime
Natural Language Description:
The range of the startsAt property must belong to the class PointInTime.
•	Axiom 7: Existential
Manchester Syntax:
TimeInterval SubClassOf startsAt some PointInTime
Natural Language Description:
Every TimeInterval must start at a specific PointInTime.
 
8. TimeInterval → endsAt → PointInTime
•	Axiom 5: Global Range
Manchester Syntax:
TimeInterval SubClassOf endsAt only PointInTime
Natural Language Description:
The range of the endsAt property must belong to the class PointInTime.
•	Axiom 7: Existential
Manchester Syntax:
TimeInterval SubClassOf endsAt some PointInTime
Natural Language Description:
Every TimeInterval must end at a specific PointInTime.
 
Crash
 
1. Crash → hasMannerOfCollision → MannerOfCollision
•	Axiom 3: Global Domain
Manchester Syntax:
hasMannerOfCollision some owl:Thing SubClassOf Crash
Natural Language Description:
If an entity has a manner of collision, it must be a Crash.
•	Axiom 5: Global Range
Manchester Syntax:
Crash SubClassOf hasMannerOfCollision only MannerOfCollision
Natural Language Description:
The range of the property hasMannerOfCollision must be a MannerOfCollision.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Crash SubClassOf hasMannerOfCollision exactly 1 MannerOfCollision
Natural Language Description:
Every Crash must have exactly one manner of collision.
 
2. Crash → hasTemporalExtent → TemporalExtent
•	Axiom 3: Global Domain
Manchester Syntax:
hasTemporalExtent some owl:Thing SubClassOf Crash
Natural Language Description:
If an entity has a temporal extent, it must be a Crash.
•	Axiom 5: Global Range
Manchester Syntax:
Crash SubClassOf hasTemporalExtent only TemporalExtent
Natural Language Description:
The range of the property hasTemporalExtent must be a TemporalExtent.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Crash SubClassOf hasTemporalExtent exactly 1 TemporalExtent
Natural Language Description:
Every Crash must have exactly one temporal extent.
 
3. Crash → occurredAt → Location
•	Axiom 3: Global Domain
Manchester Syntax:
occurredAt some owl:Thing SubClassOf Crash
Natural Language Description:
If an entity occurred at a location, it must be a Crash.
•	Axiom 5: Global Range
Manchester Syntax:
Crash SubClassOf occurredAt only Location
Natural Language Description:
The range of the property occurredAt must be a Location.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Crash SubClassOf occurredAt exactly 1 Location
Natural Language Description:
Every Crash must occur at exactly one location.
 
4. Crash → hasTotalFatalities → xsd
•	Axiom 3: Global Domain
Manchester Syntax:
hasTotalFatalities some owl:Thing SubClassOf Crash
Natural Language Description:
If an entity has total fatalities, it must be a Crash.
•	Axiom 5: Global Range
Manchester Syntax:
Crash SubClassOf hasTotalFatalities only xsd:integer
Natural Language Description:
The range of the property hasTotalFatalities must be an integer value.
•	Axiom 12: Qualified Scoped Functionality
Manchester Syntax:
Crash SubClassOf hasTotalFatalities exactly 1 xsd:integer
Natural Language Description:
Every Crash must have exactly one integer value representing total fatalities.
 
5. Crash → hasParticipant → Participant
•	Axiom 3: Global Domain
Manchester Syntax:
hasParticipant some owl:Thing SubClassOf Crash
Natural Language Description:
If an entity has participants, it must be a Crash.
•	Axiom 5: Global Range
Manchester Syntax:
Crash SubClassOf hasParticipant only Participant
Natural Language Description:
The range of the property hasParticipant must be a Participant.
•	Axiom 17: Structural Tautology
Manchester Syntax:
Crash SubClassOf hasParticipant min 0 Participant
Natural Language Description:
A Crash may have zero or more Participants.
 
6. Participant Subclass Relationships
Participant → Person
•	Axiom 1: Subclass Relationship
Manchester Syntax:
Person SubClassOf Participant
Natural Language Description:
Every Person is a subclass of Participant.
Participant → Vehicle
•	Axiom 1: Subclass Relationship
Manchester Syntax:
Vehicle SubClassOf Participant
Natural Language Description:
Every Vehicle is a subclass of Participant.
Participant → EMS
•	Axiom 1: Subclass Relationship
Manchester Syntax:
EMS SubClassOf Participant
Natural Language Description:
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

![image](https://github.com/user-attachments/assets/c1ae88f7-2bef-42d5-a026-bbb907fdf9c4)



