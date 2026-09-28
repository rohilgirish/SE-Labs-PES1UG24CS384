# Software Engineering Lab 1: Requirements Engineering & UML Use-Case Modelling

- SRN: PES1UG24CS384
- Scenario No: 16
- Project Title: Remote Patient Vitals Alert & Monitoring App
- Primary Domain: Healthcare & Telemedicine
- Target Actors: Remote Patient, On-Call Caregiver

## Lab Contents

- `PES1UG24CS384_LAB01.pdf` - Complete Lab 1 submission document containing Requirements Table, UML Use-Case Model details, embedded diagram, and Use-Case Flow Specification.
- `requirements.md` - Complete Requirements Table with exactly 5 functional requirements and 2 non-functional requirements.
- `use-case-flow.md` - One-page Use-Case Flow Specification for the core use case Receive Critical Alert & Acknowledge Alert.
- `use-case-diagram.png` - Rendered UML Use-Case Diagram for the Remote Patient Vitals Alert & Monitoring System.

## Traceability Summary

| Requirement ID | Mapped Use Case(s) |
| --- | --- |
| FR-001 | Transmit Vital Telemetry, Evaluate Vital Thresholds & Detect Breach |
| FR-002 | Evaluate Vital Thresholds & Detect Breach, Receive Critical Alert |
| FR-003 | Receive Critical Alert, Acknowledge Alert, Authenticate User |
| FR-004 | Acknowledge Alert, Escalate to Backup Caregiver |
| FR-005 | Configure Clinical Thresholds, Authenticate User |
| NFR-001 | Cross-cutting — Transmit Vital Telemetry, Evaluate Vital Thresholds & Detect Breach (ingestion throughput & uptime) |
| NFR-002 | Cross-cutting — Authenticate User, View Live Vitals Dashboard, Receive Critical Alert (encryption, HIPAA-equivalent compliance, secure auth) |
