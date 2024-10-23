# Key Notions

## Classes

### Accident:

**Rationale**: An accident forms the central event that connects the other entities and attributes of the information - vehicles, drivers, pedestrians, etc, and weather, road conditions, location, fatalities. As a matter of fact the core, majority, focus of the data pertains to it and many a relationship emanates from it.

**Connected Pattern**: Event (from MODL) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/event
from MODL best fits the event pattern, as it allows taking into consideration an accident as an event involving entities in spatio-temporal terms.

**Source Data-sets:** Accident Table (Processed Data from FARs)

### Driver:

**Rationale:** In the analysis of road accidents, identification of the driver entity is made by characteristics like age, sex, driving history, impairments, distractions, and violations. The identified characteristics develop an important part in gaining insight into the behaviour of drivers and the areas where their actions affect the outcomes of an accident.

**Connected Pattern**:
Agent-role (from MODL) https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/agent-role/agent-role-pattern.pdf

**Source Datasets:** Driver Information Table (processed data from FARs), Traffic Violations Table (processed data from FARs)

### Vehicles:

**Rationale**: Vehicle attribute data such as make, model, year of manufacture and type are critical for proper identification of the vehicle. Other factors such as condition, defects, speed and parked/ work zone become very important in determining how the vehicle contributed to or was involved with the accident. These attributes provide insight into potential causes associated with vehicle performance and associated situations.
Related Pattern:
 CS-MODL Car (from CS-MODL) https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Car.ttl
provenance-pattern from MODL https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/provenance/provenance-pattern.pdf
identifier-pattern from MODL https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/identifier

**Source Dataset:** Vehicles Table (processed data from FARs)

### Location:

**Rationale:** In traffic accidents, the geographical location in which the traffic accident has happened, for example, city or county or state, provides crucial information regarding accident patterns and contextualizes the data using environmental factors or population factors. This binds the spatial with accident data for enabling queries and analysis that are spatial in nature in the knowledge graph.

**Connected Pattern:**
CS-MODL Area (from CS-MODL) https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Area.ttl
CS-MODL City (from CS-MODL) https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/City.ttl

**Source Datasets:** Accidents Table (processed data from FARs), `https://simplemaps.com/data/us-cities`.

### Weather Condition:

**Rationale**: Weather conditions are one of the most important factors for road accidents as they directly impact the condition for driving, such as visibility, and control. Since weather conditions vary over space and time, addressing the spatial and temporal dimensions of weather conditions with respect to accidents is important in the analysis of accident patterns.

**Connected Pattern**: **Spatiotemporal Extent Pattern** (MODL Library) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/spatiotemporal-extent

**Source Dataset**: Weather Conditions Table (preprocessed data from FARs), **Accidents Table**(preprocessed data from FARs)

### Road Condition:

**Rationale**: Road conditions may be observed and measured considering a set of attributes of the condition such as: road surface - wet, dry; road defects - potholes; lighting - well lit, dark. These are critical factors contributing to the safety of the roads and the chance of accidents.

**Connected Pattern**: **MODL Observation** (MODL Library) https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation

**Source Dataset**: Road Conditions Table (processed data from FARs)