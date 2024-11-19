Module: Driver Condition Schema
 
•	hasDrivingHistory some owl:Thing SubClassOf Driver
If something has a driving history, it must be a driver.
•	Driver SubClassOf hasDrivingHistory only DrivingHistory
The range of the relationship hasDrivingHistory must be DrivingHistory.
•	Driver SubClassOf hasDrivingHistory some DrivingHistory
Every driver must have a driving history.
•	hasImpairments some owl:Thing SubClassOf Driver
If something has impairments, it must be a driver.
•	Driver SubClassOf hasImpairments only Impairments
The range of the relationship hasImpairments must be Impairments.
•	Driver SubClassOf hasImpairments some Impairments
A driver may have impairments.
•	hasTrafficViolation some owl:Thing SubClassOf DrivingHistory
If something has traffic violations, it must belong to a driving history.
•	DrivingHistory SubClassOf hasTrafficViolation only TrafficViolation
The range of the relationship hasTrafficViolation must be TrafficViolation.
•	DrivingHistory SubClassOf hasTrafficViolation some TrafficViolation
A driving history may include at least one traffic violation.
 
•	hasDrivingExperience some owl:Thing SubClassOf DrivingHistory
If something has driving experience, it must belong to a driving history.
•	DrivingHistory SubClassOf hasDrivingExperience only DrivingExperience
The range of the relationship hasDrivingExperience must be DrivingExperience.
•	DrivingHistory SubClassOf hasDrivingExperience some DrivingExperience
A driving history must include at least one driving experience.
•	TrafficViolation SubClassOf licenseSuspension some xsd:string
A traffic violation may result in a license suspension. If there is a suspension, it is captured as a string.
•	TrafficViolation SubClassOf licenseSuspension max 1 xsd:string
A traffic violation can have at most one associated license suspension, ensuring no ambiguity.
•	TrafficViolation SubClassOf violationType max 1 xsd:string
A traffic violation has at most one type.
•	TrafficViolation SubClassOf violationType exactly 1 xsd:string
Each traffic violation must have exactly one type.
•	TrafficViolation SubClassOf violationDate some TemporalExtent
Every traffic violation is associated with a date (temporal extent).
•	DrivingExperience SubClassOf totalYearsOfDriving some TemporalExtent
A driving experience must include total years of driving.
•	DrivingExperience SubClassOf experienceLevel only ExperienceLevel
The range of the relationship experienceLevel must be one of the predefined experience levels (novice, intermediate, experienced).
•	DrivingExperience SubClassOf experienceLevel some ExperienceLevel
Every driving experience must have at least one experience level.
•	Driver SubClassOf hasLicenseStatus max 1 xsd:string
A driver has at most one license status.
•	Driver SubClassOf hasLicenseStatus exactly 1 xsd:string
Each driver must have exactly one license status.

![image](https://github.com/user-attachments/assets/d637cd73-0816-4524-8c0a-e905b0c758a8)
