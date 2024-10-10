# Key Notions
* Crash Event
        * Rationale: The Crash Event is the focal point of the entire knowledge graph. Every piece of data—whether it's about driver behavior, vehicle condition, or road infrastructure—ultimately ties back to the crash event. Modeling a crash event allows us to ask critical questions like "What caused this crash?", "Where and when did it happen?", and "Who was involved?". Understanding each crash as a distinct event with its own unique set of contributing factors is essential to uncover patterns in road accidents, identify high-risk conditions, and develop preventive measures.
        * Connected Pattern: Event Pattern from MODL. This pattern is highly suitable for representing any discrete occurrence, such as a road crash, that involves participants (drivers, vehicles), a location, and a time.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Driver Condition
        * Rationale: Driver Condition captures the state of the driver at the time of the crash, including factors like distraction, fatigue, alcohol or drug influence, and overall experience. Drivers are often the most critical factor in accidents, and the knowledge graph needs to model how different states of driver impairment or distraction influence the likelihood and severity of crashes. The relationship between driver condition and environmental factors (like weather or road infrastructure) can reveal new insights into high-risk scenarios that traditional analyses may overlook.
        * Connected Pattern: AgentRole Pattern from MODL. This pattern models the different roles that agents (e.g., drivers) play in events, such as being a distracted driver in a crash event.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Vehicle Condition
        * Rationale: Vehicle Condition encompasses the mechanical state of the vehicle, such as the quality of its brakes, tires, and safety features (like airbags or ABS). A well-maintained vehicle can reduce crash severity, while poorly maintained vehicles are more prone to malfunctions that could lead to a crash. In this knowledge graph, capturing vehicle conditions provides insights into how different types of vehicle defects—combined with other factors like road or weather conditions—contribute to accidents. It’s essential to model these conditions dynamically, as vehicle conditions change over time and can vary significantly from one crash event to another.
        * Connected Pattern: ObjectFeature Pattern from CS-MODL. This pattern effectively models changing features of physical objects, such as vehicles, over time.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Road Infrastructure
        * Rationale: Poor or outdated Road Infrastructure—such as bad road surfaces, unclear signage, or inadequate lighting—can increase the likelihood of accidents. This notion captures the physical aspects of the road and how they interact with other factors like driver behavior and weather conditions. Roads with higher pothole density, sharp curves, or poor lighting are more prone to accidents, especially during adverse weather. Modeling road infrastructure is crucial for identifying regions that need maintenance or infrastructure investment to reduce crashes.
        * Connected Pattern: PhysicalObject with Provenance from MODL. This pattern allows us to model infrastructure as physical objects with attributes that change over time, such as road maintenance status.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Weather Conditions
        * Rationale: Weather plays a significant role in road safety, influencing visibility, road slipperiness, and driver reaction times. Weather Conditions such as rain, snow, fog, or clear skies interact with both road and driver conditions to create crash risks. For instance, fog reduces visibility, making even minor distractions more dangerous, while rain can cause slippery surfaces, especially if the road is poorly maintained. Modeling weather as a dynamic factor in crash events helps identify patterns where specific weather conditions exacerbate risks.
        * Connected Pattern: Situation Pattern from MODL. This pattern models the influence of external situations, such as weather, on events like crashes.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Crash Severity
        * Rationale: Crash Severity captures the impact of the crash in terms of damage and injuries, ranging from minor property damage to fatalities. This notion is key to understanding which combinations of factors (e.g., speeding during fog, worn-out tires on icy roads) lead to more severe crashes. By modeling crash severity, we can predict high-risk conditions and prioritize interventions. Furthermore, understanding severity helps insurance companies and policymakers craft better strategies for accident prevention and response.
        * Connected Pattern: Quality Pattern from DUL (DOLCE+DnS Ultralite). This pattern is useful for capturing attributes like severity, which are essential qualities of a crash event.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Geographic Location
        * Rationale: Geographic Location is crucial for understanding where crashes occur. By linking crash events to specific locations, we can analyze regional accident patterns, assess the impact of urban versus rural roads, and identify accident-prone zones. This helps local authorities prioritize infrastructure improvements and safety interventions. Geographic location also interacts with other factors, such as socioeconomic conditions, traffic density, and weather patterns, to provide a complete picture of crash risks.
        * Connected Pattern: Place Pattern from GeoSPARQL. This pattern allows the representation of spatial entities and their properties, such as coordinates and geographic classification.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Traffic and Road Usage
        * Rationale: Traffic and Road Usage represents the flow and behavior of vehicles on the road, including factors like traffic volume, speed, and whether the road is congested or under construction. Heavy traffic during rush hour, for example, creates more opportunities for accidents, especially in poorly maintained or high-risk areas. Modeling road usage helps to correlate traffic density and road capacity with accident frequency and severity.
        * Connected Pattern: Observation Pattern from SOSA (Sensor, Observation, Sample, and Actuator). This pattern models traffic data as observable phenomena that impact crash likelihood.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Driver Experience
        * Rationale: Driver Experience factors like the number of years a person has been driving, their past infractions, and their familiarity with the vehicle are all critical to understanding accident risk. Less experienced drivers or those with a history of reckless driving are more likely to be involved in accidents. Capturing this notion allows us to explore how experience interacts with other conditions, like road type or weather, to either exacerbate or mitigate crash risks.
        * Connected Pattern: AgentRole Pattern from MODL. This pattern models the experience and qualifications of an agent (driver) in the context of a crash event.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Socioeconomic Factors
        * Rationale: Socioeconomic Factors such as income level, education, and infrastructure investment in a region have a direct impact on road safety. Poorer regions may have older, less safe vehicles and poorly maintained roads, leading to higher accident rates. Understanding the socioeconomic context of crashes helps policymakers target investments and interventions to reduce disparities in road safety across different regions.
        * Connected Pattern: Agent with Provenance Pattern from MODL. This pattern captures the socioeconomic characteristics of regions and their influence on crash events.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Temporal Patterns
        * Rationale: Time plays a critical role in accident occurrence. Temporal Patterns help us understand when crashes are most likely to happen (e.g., during rush hour, at night, or on weekends). By modeling temporal patterns, we can uncover trends in accident frequency based on time of day, season, or holidays, and use these insights to implement time-specific preventive measures, such as increased patrols during high-traffic periods or poor weather.
        * Connected Pattern: Time Interval Pattern from OWL-Time ontology. This pattern models temporal intervals to capture specific times, days, or seasons related to crashes.
        * Data Source: Fatality Analysis Reporting System (FARS)
* Animal Crossings
        * Rationale: Animal Crossings are a significant factor in rural and suburban crashes. By modeling where and when animals (e.g., deer, elk) frequently cross roads, and whether there are proper warning signs in place, we can predict and prevent animal-related accidents. This is particularly important for regions with high wildlife populations.
        * Connected Pattern: Event Pattern from MODL for modeling crossing incidents as distinct events, similar to crash events.
        * Data Source: Fatality Analysis Reporting System (FARS)
