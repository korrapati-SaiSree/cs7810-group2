# Key Notions

## Classes

### Accident:

**Rationale**: An accident is the core event that connects to the other entities (vehicles, drivers, pedestrians, etc ) and attributes (weather, road conditions, location, fatalities). It is the main focus in the dataset, and many relationship stems out from it.

**Connected Pattern**: Event (from MODL) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/event
the event pattern from MODL fits the most, as it allows to treat an accident as an event that involves entities and takes place in specific time and location (spatio-temporal).

**Source Datasets:** Accident Table (processed data from FARs)

### Driver:

**Rationale**: Understanding the driver entity, including attributes such as age, sex, driving history, impairments, distractions, and violations, is essential for identifying and analyzing the causes and contributing factors of road accidents. These characteristics provide crucial insights into driver behavior and their impact on accident outcomes.

**Connected Pattern**:
Agent-role (from MODL) https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/agent-role/agent-role-pattern.pdf

**Source Datasets:** Driver Information Table (processed data from FARs), Traffic Violations Table (processed data from FARs)

### Vehicles:

**Rationale**: Information on vehicle attributes such as make, model, year of manufacture, and type is crucial for accurate vehicle identification. Additionally, factors like vehicle maneuver, condition, defects, speed, and parked/work zone status are critical for understanding the role of the vehicle in contributing to or being involved in an accident. These attributes help uncover potential causes related to vehicle performance and situational dynamics.

**Connected Pattern:**
CS-MODL Car (from CS-MODL) https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Car.ttl
provenance-pattern (from MODL) https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/provenance/provenance-pattern.pdf
identifier-pattern (from MODL) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier

**Source Dataset:** Vehicles Table (processed data from FARs)

### Location:

**Rationale:** In the context of road accidents, the geographic location where accidents occur (such as the city, county, or state) is crucial for analyzing accident patterns and contextualizing the data with environmental or population-based factors. This notion ties spatial information to accident data, enabling spatial queries and analyses in the knowledge graph.

**Connected Pattern:**
CS-MODL Area (from CS-MODL) https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Area.ttl
CS-MODL City (from CS-MODL) https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/City.ttl

**Source Datasets:** Accidents Table (processed data from FARs), `https://simplemaps.com/data/us-cities`.

### Weather Condition:

**Rationale**: Weather conditions are a critical factor in road accidents, as they directly affect driving conditions (e.g., visibility, traction, and control). Since weather conditions change over time and are location-specific, capturing both the spatial (where) and temporal (when) aspects of weather in relation to accidents is essential for analyzing crash patterns.

**Connected Pattern**: **Spatiotemporal Extent Pattern** (MODL Library) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/spatiotemporal-extent

**Source Dataset**: Weather Conditions Table (processed data from FARs), **Accidents Table**(processed data from FARs)

### Road Condition:

**Rationale**: Road conditions can be observed and measured through various attributes like the road surface (e.g., wet, dry), road defects (e.g., potholes), and lighting (e.g., well-lit, dark). These are key factors that contribute to road safety and accident likelihood.

**Connected Pattern**: **MODL Observation** (MODL Library) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation

**Source Dataset**: Road Conditions Table (processed data from FARs)
