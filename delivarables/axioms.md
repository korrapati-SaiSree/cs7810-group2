# Road Crashes Ontology

![image](https://github.com/user-attachments/assets/8f0dfebb-c632-4451-a281-a0e7c32b2156)

## Module: Driver Condition Schema
 ![image](https://github.com/user-attachments/assets/da6e9d93-7b22-4b86-bbb9-625886d4990e)


     hasDrivingHistory some owl:Thing SubClassOf Driver
     If something has a driving history, it must be a driver  
     
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
    
    
## Module: Emergency Medical Service Schema

![EMS (1)](https://github.com/user-attachments/assets/5d3b316f-25a9-43c5-abd1-267ad666bb28)

     
    
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
    
 ## Module: Impairments Schema
     
 ![Impairment (1)](https://github.com/user-attachments/assets/ec5cfd68-fe68-435f-a614-b846c3bdedc6)

    
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
 
 
hasWorkZone some owl:Thing SubClassOf Location

If an entity has a work zone, it must be a Location.

Location SubClassOf hasWorkZone only WorkZone

The range of the property hasWorkZone must be a WorkZone.

Location SubClassOf hasWorkZone some WorkZone

Every Location must have at least one WorkZone.
 

hasIntersection some owl:Thing SubClassOf Location

If an entity has an intersection, it must be a Location.

Location SubClassOf hasIntersection only Intersection

The range of the property hasIntersection must be an Intersection.

Location SubClassOf hasIntersection exactly 1 Intersection

Every Location must have exactly one intersection type.
 

hasCoordinates some owl:Thing SubClassOf Location

If an entity has coordinates, it must be a Location.

Location SubClassOf hasCoordinates only Coordinates

The range of the property hasCoordinates must be Coordinates.

Location SubClassOf hasCoordinates exactly 1 Coordinates

Every Location must have exactly one set of coordinates.
 

hasLatitude some owl:Thing SubClassOf Coordinates

If an entity has a latitude, it must be a set of Coordinates.

Coordinates SubClassOf hasLatitude only xsd:float

The range of the property hasLatitude must be a float value.

Coordinates SubClassOf hasLatitude exactly 1 xsd:float

Every set of Coordinates must have exactly one latitude value.
 

hasLongitude some owl:Thing SubClassOf Coordinates

If an entity has a longitude, it must be a set of Coordinates.

Coordinates SubClassOf hasLongitude only xsd:float

The range of the property hasLongitude must be a float value.

Coordinates SubClassOf hasLongitude exactly 1 xsd:float

Every set of Coordinates must have exactly one longitude value.
 

hasState some owl:Thing SubClassOf Location

If an entity has a state, it must be a Location.

Location SubClassOf hasState only State

The range of the property hasState must be a State.

Location SubClassOf hasState exactly 1 State

Every Location must have exactly one state.
 

hasStateName some owl:Thing SubClassOf State

If an entity has a state name, it must be a State.

State SubClassOf hasStateName only xsd:string

The range of the property hasStateName must be a string value.

State SubClassOf hasStateName exactly 1 xsd:string

Every State must have exactly one state name.
 

hasCity some owl:Thing SubClassOf State

If an entity has a city, it must be a State.

State SubClassOf hasCity only City

The range of the property hasCity must be a City.

State SubClassOf hasCity some City

Every State must have at least one City.
 

hasCityName some owl:Thing SubClassOf City

If an entity has a city name, it must be a City.


City SubClassOf hasCityName only xsd:string

The range of the property hasCityName must be a string value.

City SubClassOf hasCityName exactly 1 xsd:string

Every City must have exactly one city name.
 

hasZipCode some owl:Thing SubClassOf City

If an entity has a zip code, it must be a City.

City SubClassOf hasZipCode only xsd:string

The range of the property hasZipCode must be a string value.

City SubClassOf hasZipCode some xsd:string

Every City must have at least one zip code.
 

hasCounty some owl:Thing SubClassOf City

If an entity has a county, it must be a City.

City SubClassOf hasCounty only County

The range of the property hasCounty must be a County.

City SubClassOf hasCounty some County

Every City must be associated with at least one County.

hasCountyName some owl:Thing SubClassOf County

If an entity has a county name, it must be a County.

County SubClassOf hasCountyName only xsd:string

The range of the property hasCountyName must be a string value.

County SubClassOf hasCountyName exactly 1 xsd:string

Every County must have exactly one county name.
 

hasZipCode some owl:Thing SubClassOf County

If an entity has a zip code, it must be a County.

County SubClassOf hasZipCode only xsd:string

The range of the property hasZipCode must be a string value.

County SubClassOf hasZipCode some xsd:string

Every County must have at least one zip code.
 

hasStreet some owl:Thing SubClassOf County

If an entity has a street, it must be a County.

County SubClassOf hasStreet only Street

The range of the property hasStreet must be a Street.

County SubClassOf hasStreet some Street

Every County must have at least one Street.
 

hasStreetName some owl:Thing SubClassOf Street

If an entity has a street name, it must be a Street.

Street SubClassOf hasStreetName only xsd:string

The range of the property hasStreetName must be a string value.

Street SubClassOf hasStreetName exactly 1 xsd:string

Every Street must have exactly one street name.
Socioeconomic Factors
 

hasSocioEconomicCondition some owl:Thing SubClassOf Location

If an entity has a socio-economic condition, it must be a Location.

Location SubClassOf hasSocioEconomicCondition only SocioEconomicCondition

The range of the property hasSocioEconomicCondition must be a SocioEconomicCondition.

Location SubClassOf hasSocioEconomicCondition some SocioEconomicCondition

Every Location must have at least one SocioEconomicCondition.
 

hasTemporalExtent some owl:Thing SubClassOf SocioEconomicCondition

If an entity has a temporal extent, it must be a SocioEconomicCondition.

SocioEconomicCondition SubClassOf hasTemporalExtent only TemporalExtent

The range of the property hasTemporalExtent must be a TemporalExtent.

SocioEconomicCondition SubClassOf hasTemporalExtent some TemporalExtent

Every SocioEconomicCondition must be associated with at least one TemporalExtent.
 

hasIncomeHouseholdMedian some owl:Thing SubClassOf SocioEconomicCondition

If an entity has a median household income, it must be a SocioEconomicCondition.

SocioEconomicCondition SubClassOf hasIncomeHouseholdMedian only IncomeHouseholdMedian

The range of the property hasIncomeHouseholdMedian must be an IncomeHouseholdMedian.

SocioEconomicCondition SubClassOf hasIncomeHouseholdMedian some IncomeHouseholdMedian

Every SocioEconomicCondition must have at least one IncomeHouseholdMedian.
 

incomeHouseholdMedianAsDecimal some owl:Thing SubClassOf IncomeHouseholdMedian

If an entity has a median household income as a decimal, it must be an IncomeHouseholdMedian.

IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal only xsd:decimal

The range of the property incomeHouseholdMedianAsDecimal must be a decimal value.

IncomeHouseholdMedian SubClassOf incomeHouseholdMedianAsDecimal exactly 1 xsd:decimal

Every IncomeHouseholdMedian must have exactly one decimal value representing its median household income.
 

hasEmploymentRate some owl:Thing SubClassOf SocioEconomicCondition

If an entity has an employment rate, it must be a SocioEconomicCondition.

SocioEconomicCondition SubClassOf hasEmploymentRate only EmploymentRate

The range of the property hasEmploymentRate must be an EmploymentRate.

SocioEconomicCondition SubClassOf hasEmploymentRate some EmploymentRate

Every SocioEconomicCondition must have at least one EmploymentRate.
 

employmentRateAsDecimal some owl:Thing SubClassOf EmploymentRate

If an entity has an employment rate as a decimal, it must be an EmploymentRate.

EmploymentRate SubClassOf employmentRateAsDecimal only xsd:decimal

The range of the property employmentRateAsDecimal must be a decimal value.

EmploymentRate SubClassOf employmentRateAsDecimal exactly 1 xsd:decimal

Every EmploymentRate must have exactly one decimal value representing its employment rate.
 

hasPopulationDensity some owl:Thing SubClassOf SocioEconomicCondition

If an entity has a population density, it must be a SocioEconomicCondition.

SocioEconomicCondition SubClassOf hasPopulationDensity only PopulationDensity

The range of the property hasPopulationDensity must be a PopulationDensity.

SocioEconomicCondition SubClassOf hasPopulationDensity some PopulationDensity

Every SocioEconomicCondition must have at least one PopulationDensity.
 

populationDensityAsDecimal some owl:Thing SubClassOf PopulationDensity

If an entity has a population density as a decimal, it must be a PopulationDensity.

PopulationDensity SubClassOf populationDensityAsDecimal only xsd:decimal

The range of the property populationDensityAsDecimal must be a decimal value.

PopulationDensity SubClassOf populationDensityAsDecimal exactly 1 xsd:decimal

Every PopulationDensity must have exactly one decimal value representing its population density.
 

hasEducationLevel some owl:Thing SubClassOf SocioEconomicCondition

If an entity has an education level, it must be a SocioEconomicCondition.

SocioEconomicCondition SubClassOf hasEducationLevel only EducationLevel

The range of the property hasEducationLevel must be an EducationLevel.

SocioEconomicCondition SubClassOf hasEducationLevel some EducationLevel

Every SocioEconomicCondition must have at least one EducationLevel.

Vehicle
 


hasVehicleType some owl:Thing SubClassOf Vehicle

If an entity has a vehicle type, it must be a Vehicle.

Vehicle SubClassOf hasVehicleType only xsd:string

The range of the property hasVehicleType must be a string value.

Vehicle SubClassOf hasVehicleType exactly 1 xsd:string

Every Vehicle must have exactly one vehicle type.
 

hasVehicleModel some owl:Thing SubClassOf Vehicle

If an entity has a vehicle model, it must be a Vehicle.

Vehicle SubClassOf hasVehicleModel only xsd:string

The range of the property hasVehicleModel must be a string value.

Vehicle SubClassOf hasVehicleModel exactly 1 xsd:string

Every Vehicle must have exactly one vehicle model.
 

hasVehicleMake some owl:Thing SubClassOf Vehicle

If an entity has a vehicle make, it must be a Vehicle.

Vehicle SubClassOf hasVehicleMake only xsd:string

The range of the property hasVehicleMake must be a string value.

Vehicle SubClassOf hasVehicleMake exactly 1 xsd:string

Every Vehicle must have exactly one vehicle make.
 

hasVehicleManufacturingYear some owl:Thing SubClassOf Vehicle

If an entity has a manufacturing year, it must be a Vehicle.

Vehicle SubClassOf hasVehicleManufacturingYear only xsd:integer

The range of the property hasVehicleManufacturingYear must be an integer value.

Vehicle SubClassOf hasVehicleManufacturingYear exactly 1 xsd:integer

Every Vehicle must have exactly one manufacturing year.
 

hasWeight some owl:Thing SubClassOf Vehicle

If an entity has a weight, it must be a Vehicle.

Vehicle SubClassOf hasWeight only Weight

The range of the property hasWeight must be a Weight.

Vehicle SubClassOf hasWeight some Weight

Every Vehicle must have at least one Weight.
 

rangeFrom some owl:Thing SubClassOf Weight

If an entity has a weight range starting value, it must be a Weight.

Weight SubClassOf rangeFrom only xsd:integer

The range of the property rangeFrom must be an integer value.

Weight SubClassOf rangeFrom exactly 1 xsd:integer

Every Weight must have exactly one starting value for the weight range.
 

rangeTo some owl:Thing SubClassOf Weight

If an entity has a weight range ending value, it must be a Weight.

Weight SubClassOf rangeTo only xsd:integer

The range of the property rangeTo must be an integer value.

Weight SubClassOf rangeTo exactly 1 xsd:integer

Every Weight must have exactly one ending value for the weight range.
 

performsRole some owl:Thing SubClassOf VehicleInAccident

If an entity performs a role, it must be a VehicleInAccident.

VehicleInAccident SubClassOf performsRole only Vehicle

The range of the property performsRole must be a Vehicle.
 

providesRole some owl:Thing SubClassOf VehicleInAccident

If an entity provides a role, it must be a VehicleInAccident.

VehicleInAccident SubClassOf providesRole only Crash

The range of the property providesRole must be a Crash.
 

hasSpeed some owl:Thing SubClassOf VehicleInAccident

If an entity has a speed, it must be a VehicleInAccident.

VehicleInAccident SubClassOf hasSpeed only xsd:integer

The range of the property hasSpeed must be an integer value.
 

hasMileage some owl:Thing SubClassOf VehicleInAccident

If an entity has mileage, it must be a VehicleInAccident.

VehicleInAccident SubClassOf hasMileage only xsd:float

The range of the property hasMileage must be a float value.
 

involvedInHitAndRun some owl:Thing SubClassOf VehicleInAccident

If an entity is involved in a hit-and-run, it must be a VehicleInAccident.

VehicleInAccident SubClassOf involvedInHitAndRun only xsd:boolean

The range of the property involvedInHitAndRun must be a boolean value.
 

hasTemporalExtent some owl:Thing SubClassOf VehicleInAccident

If an entity has a temporal extent, it must be a VehicleInAccident.

VehicleInAccident SubClassOf hasTemporalExtent only TemporalExtent

The range of the property hasTemporalExtent must be a TemporalExtent.
Weather Condition
 

hasWeatherCondition some owl:Thing SubClassOf Location

If an entity has a weather condition, it must be a Location.

Location SubClassOf hasWeatherCondition only WeatherCondition

The range of the property hasWeatherCondition must be a WeatherCondition.

Location SubClassOf hasWeatherCondition some WeatherCondition

Every Location must have at least one WeatherCondition.
 

hasTemperature some owl:Thing SubClassOf WeatherCondition

If an entity has a temperature, it must be a WeatherCondition.

WeatherCondition SubClassOf hasTemperature only Temperature

The range of the property hasTemperature must be a Temperature.

WeatherCondition SubClassOf hasTemperature some Temperature

Every WeatherCondition must have at least one Temperature.
 

hasPrecipitation some owl:Thing SubClassOf WeatherCondition

If an entity has precipitation, it must be a WeatherCondition.

WeatherCondition SubClassOf hasPrecipitation only Precipitation

The range of the property hasPrecipitation must be a Precipitation.

WeatherCondition SubClassOf hasPrecipitation min 0 Precipitation

A WeatherCondition may have zero or more Precipitation instances.
 

hasTemporalExtent some owl:Thing SubClassOf WeatherCondition

If an entity has a temporal extent, it must be a WeatherCondition.

WeatherCondition SubClassOf hasTemporalExtent only TemporalExtent

The range of the property hasTemporalExtent must be a TemporalExtent.

WeatherCondition SubClassOf hasTemporalExtent some TemporalExtent

Every WeatherCondition must have at least one TemporalExtent.
 

weatherConditionAsString some owl:Thing SubClassOf WeatherCondition

If an entity has a weather condition as a string, it must be a WeatherCondition.

WeatherCondition SubClassOf weatherConditionAsString only xsd:string

The range of the property weatherConditionAsString must be a string value.

WeatherCondition SubClassOf weatherConditionAsString exactly 1 xsd:string

Every WeatherCondition must have exactly one string representing its description.
 

inCelsius some owl:Thing SubClassOf Temperature

If an entity has a temperature in Celsius, it must be a Temperature.

Temperature SubClassOf inCelsius only xsd:decimal

The range of the property inCelsius must be a decimal value.

Temperature SubClassOf inCelsius exactly 1 xsd:decimal

Every Temperature must have exactly one value in Celsius.
 

inFahrenheit some owl:Thing SubClassOf Temperature

If an entity has a temperature in Fahrenheit, it must be a Temperature.


Temperature SubClassOf inFahrenheit only xsd:decimal

The range of the property inFahrenheit must be a decimal value.

Temperature SubClassOf inFahrenheit exactly 1 xsd:decimal

Every Temperature must have exactly one value in Fahrenheit.



