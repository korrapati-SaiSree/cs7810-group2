# Key Notions
* Crash

  * Rationale: The Crash Event is the focal point of the entire knowledge graph. Every piece of data—whether it's about driver behavior, vehicle condition, or road infrastructure—ultimately ties back to the crash event. Modeling a crash event allows us to ask critical questions like "What caused this crash?", "Where and when did it happen?", and "Who was involved?". Understanding each crash as a distinct event with its own unique set of contributing factors is essential to uncover patterns in road accidents, identify high-risk conditions, and develop preventive measures.

  * Connected Pattern: Event Pattern from MODL. This pattern is highly suitable for representing any discrete occurrence, such as a road crash, that involves participants (drivers, vehicles), a location, and a time.
  * Pattern Source: https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/event

  * Data Source: Fatality Analysis Reporting System (FARS)

* Driver

  * Rationale: Driver Condition captures the state of the driver at the time of the crash, including factors like distraction, fatigue, alcohol or drug influence, and overall experience. Drivers are often the most critical factor in accidents, and the knowledge graph needs to model how different states of driver impairment or distraction influence the likelihood and severity of crashes. The relationship between driver condition and environmental factors (like weather or road infrastructure) can reveal new insights into high-risk scenarios that traditional analyses may overlook.

    * Connected Pattern: AgentRole Pattern from MODL. This pattern models the different roles that agents (e.g., drivers) play in events, such as being a distracted driver in a crash event.
        
    * Data Source: Fatality Analysis Reporting System (FARS)

* Vehicle

  * Rationale: Vehicle Condition encompasses the mechanical state of the vehicle, such as the quality of its brakes, tires, and safety features (like airbags or ABS). A well-maintained vehicle can reduce crash severity, while poorly maintained vehicles are more prone to malfunctions that could lead to a crash. In this knowledge graph, capturing vehicle conditions provides insights into how different types of vehicle defects—combined with other factors like road or weather conditions—contribute to accidents. It’s essential to model these conditions dynamically, as vehicle conditions change over time and can vary significantly from one crash event to another.

  * Connected Pattern: ObjectFeature Pattern from CS-MODL. This pattern effectively models changing features of physical objects, such as vehicles, over time.

  * Data Source: Fatality Analysis Reporting System (FARS)

* Location

  * Rationale: Geographic Location is crucial for understanding where crashes occur. By linking crash events to specific locations, we can analyze regional accident patterns, assess the impact of urban versus rural roads, and identify accident-prone zones. This helps local authorities prioritize infrastructure improvements and safety interventions. Geographic location also interacts with other factors, such as socioeconomic conditions, traffic density, and weather patterns, to provide a complete picture of crash risks.

  * Connected Pattern: Place Pattern from GeoSPARQL. This pattern allows the representation of spatial entities and their properties, such as coordinates and geographic classification.

  * Data Source: Fatality Analysis Reporting System (FARS)

* Socioeconomic Factors

  * Rationale: Socioeconomic Factors such as income level, education, and infrastructure investment in a region have a direct impact on road safety. Poorer regions may have older, less safe vehicles and poorly maintained roads, leading to higher accident rates. Understanding the socioeconomic context of crashes helps policymakers target investments and interventions to reduce disparities in road safety across different regions.

  * Connected Pattern: Agent with Provenance Pattern from MODL. This pattern captures the socioeconomic characteristics of regions and their influence on crash events.

  * Data Source: Census Data

* EMS (Emergency Medical Service)

  * Rationale: The time from crash reporting to on-scene arrival and transportation to treatment facilities significantly affects the survival result. Capturing the EMS-related data in the graph will allow us to examine the impact of response delays or inefficiencies on fatality rates, providing important information for improving emergency response systems.
 
  * Connected Pattern: Process Pattern from MODL. This pattern captures temporal and procedural details of EMS interventions.
 
  * Data Source: Fatality Analysis Reporting System (FARS)

* Impairments

  * Rationale: Road crashes are largely caused by driver impairments like weariness, drug or alcohol usage, and distractions. By capturing these variables, the knowledge graph can show relationships between particular impairments and the chance of a crash, supporting focused awareness campaigns and the implementation of policies.
 
  * Connected Pattern: AgentRole Pattern from MODL. This pattern models the impaired driver’s role in crash scenarios.
 
  * Data Source: Fatality Analysis Reporting System (FARS)
 
* Person

  * Rationale: A critical part of any crash data includes the persons involved in a collision: drivers, passengers, and pedestrians. Modeling of person-specific data-such as age, gender, and degree of injury-allows analysis of how demographic characteristics affect collision outcomes and hazards.

  * Connected Pattern: Agent Pattern. This pattern represents individuals and their roles in crash events.
 
  * Data Source: Fatality Analysis Reporting System (FARS)
 
* Time

  * Rationale: Temporal parameters, such as time of day, season, and day of the week, significantly affect the probability of an accident. The modeling of temporal patterns enables targeted preventive actions to be implemented and helps discover tendencies such as crash peak hours or heightened hazards under particular weather conditions.

  * Connected Pattern: Time Interval Pattern from OWL-Time ontology. This pattern models temporal intervals associated with events.
 
  * Data Source: Fatality Analysis Reporting System (FARS)




