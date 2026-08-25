# Software Engineering Lab 1: Requirements Engineering & UML Use-Case Modelling

- SRN: PES1UG24CS384
- Scenario No: 16
- Project Title: Remote Patient Vitals Alert & Monitoring App
- Primary Domain: Healthcare & Telemedicine
- Target Actors: Remote Patient, On-Call Caregiver

## Repository Contents

- `PES1UG24CS384_LAB01.docx` - Complete Lab 1 report document containing Requirements Table, UML Use-Case Model details, and Use-Case Flow Specification.
- `README.md` - Repository overview and requirements traceability matrix.
- `use-case-diagram.png` - Rendered UML Use-Case Diagram for the Remote Patient Vitals Alert & Monitoring System.
- `use-case-diagram.puml` - Reproducible PlantUML source code for the use-case diagram.

## Traceability Summary

| Requirement ID | Mapped Use Case(s) |
| --- | --- |
| FR-001 | Transmit Vital Telemetry, Evaluate Vital Thresholds & Detect Breach, Receive Critical Alert |
| FR-002 | Transmit Vital Telemetry, View Live Vitals Dashboard, Authenticate User |
| FR-003 | Receive Critical Alert, Acknowledge Alert, Authenticate User |
| FR-004 | Configure Clinical Thresholds, Authenticate User |
| FR-005 | Acknowledge Alert, Escalate to Backup Caregiver |
| NFR-001 | Cross-cutting requirement for telemetry ingestion throughput, scalability, and 99.99% uptime |
| NFR-002 | Cross-cutting requirement for end-to-end encryption, HIPAA compliance, and secure user authentication |
