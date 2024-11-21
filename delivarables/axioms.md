# Road Crashes Ontology

![Road Crashes all together](https://github.com/korrapati-SaiSree/cs7810-group2/blob/main/delivarables/scehmaDiagrams_Final/allTogether/allTogether.png)

## Driver Condition

![Driver Condition](https://github.com/korrapati-SaiSree/cs7810-group2/blob/axioms/delivarables/scehmaDiagrams_Final/DriverCondition/DriverCondition.png)


### Axioms

1. Driver → hasDrivingHistory → DrivingHistory <br />
   * `Driver SubClassOf hasDrivingHistory some DrivingHistory` <br />
     Every driver must have at least one associated driving history.

2. Driver → hasImpairments → Impairments <br />
   * `Driver SubClassOf hasImpairments some Impairments` <br />
     A driver may have impairments.

3. DrivingHistory → hasTrafficViolation → TrafficViolation <br />
   * `DrivingHistory SubClassOf hasTrafficViolation some TrafficViolation` <br />
     A driving history may include at least one traffic violation.

4. DrivingHistory → hasDrivingExperience → DrivingExperience <br />
   * `DrivingHistory SubClassOf hasDrivingExperience some DrivingExperience` <br />
     A driving history must include at least one driving experience.

5. TrafficViolation → licenseSuspension → xsd <br />
   * `TrafficViolation SubClassOf licenseSuspension some xsd:string` <br />
     A traffic violation may result in a license suspension, recorded as a string.
   * `TrafficViolation SubClassOf licenseSuspension max 1 xsd:string` <br />
     A traffic violation can have at most one associated license suspension.
