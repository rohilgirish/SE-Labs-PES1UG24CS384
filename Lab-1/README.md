# Software Engineering Lab 1: Requirements Engineering & UML Use-Case Modelling

- SRN: PES1UG24CS384
- Scenario No: 16
- Project Title: Remote Patient Vitals Alert & Monitoring App
- Primary Domain: Healthcare & Telemedicine
- Target Actors: Remote Patient, On-Call Caregiver

## 1. Requirements Table

Internal verification completed before finalization: exactly 5 functional requirements are listed as FR-001 to FR-005, exactly 2 non-functional requirements are listed as NFR-001 to NFR-002, no duplicate IDs are present, all six required columns are included, and the wording of FR-001 and NFR-001 preserves the supplied source intent.

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
| --- | --- | --- | --- | --- | --- |
| FR-001 | Functional | The system shall continuously evaluate ingested patient vitals against configured clinical thresholds and flag critical anomalies within 2 seconds. | High | Pass: High heart rate (>140 BPM), low SpO2 (<90%), or severe BP spike triggers immediate escalation alert within 2 seconds. Fail: Metric spike ignored or delayed > 5s. | Real-time anomaly detection is essential for post-operative patient safety to prevent acute cardiac and respiratory failure. |
| FR-002 | Functional | The system shall allow a Remote Patient and On-Call Caregiver to authenticate securely and view the live vitals dashboard displaying continuous SpO2, Heart Rate, and Blood Pressure streams. | High | Pass: Authenticated users can view real-time synchronized vitals telemetry updated every second. Fail: Unauthenticated user accesses vitals stream or dashboard fails to render telemetry. | Continuous vitals visibility allows both patient and caregiver to monitor physiological stability during post-operative recovery. |
| FR-003 | Functional | The system shall dispatch immediate critical alerts to the On-Call Caregiver upon detecting a vital threshold breach and record caregiver acknowledgment. | High | Pass: Critical alert notification reaches On-Call Caregiver within 3 seconds, and caregiver acknowledgment transitions alert state to acknowledged. Fail: Alert notification fails or acknowledgment is not recorded. | Immediate alert delivery and explicit acknowledgment ensure that medical caregivers are actively aware of life-threatening vital anomalies. |
| FR-004 | Functional | The system shall allow an On-Call Caregiver to configure and dynamically update clinical baseline thresholds for patient vitals. | High | Pass: Caregiver updates patient-specific vital limits, and the evaluation engine applies new limits within 10 seconds without restart. Fail: Threshold updates fail to persist or default global limits overwrite custom limits. | Individualized clinical thresholds are required to account for distinct surgical procedures and patient-specific baseline variations. |
| FR-005 | Functional | The system shall automatically escalate unacknowledged critical alerts to a Backup Caregiver if the primary On-Call Caregiver does not acknowledge within the configured SLA. | High | Pass: When primary caregiver fails to acknowledge within 60 seconds (SLA), the system dispatches escalation alert to Backup Caregiver with audit timestamp. Fail: Alert remains stuck on unacknowledged tier without timeout escalation. | Automated escalation prevents single-point-of-failure in clinical communication and guarantees secondary failover response. |
| NFR-001 | Non-Functional (Performance & Security) | The telemetry ingestion gateway shall support at least 500 concurrent continuous telemetry streams with 99.99% uptime. | High | Pass: Benchmarking tests confirm target latency (p99 < 500ms) and security standards under simulated peak load. Fail: Ingestion latency exceeds 1s or availability drops below 99.99%. | Telemedicine infrastructure must handle multi-patient telemetry in real time without dropping vitals packets during critical care windows. |
| NFR-002 | Non-Functional (Security & Data Integrity) | The system shall enforce end-to-end encryption for all protected health telemetry using TLS 1.3 in transit and AES-256 at rest with role-based access control. | High | Pass: All patient biometric data packets and database records are verified encrypted with zero plaintext exposure across logs and network traces. Fail: Plaintext biometric data exposed in transit or unauthorized access permitted. | HIPAA compliance and patient privacy protection are legally mandatory for remote healthcare monitoring systems. |

## 2. UML Use-Case Diagram

### Explicitly Mentioned Actors
- Remote Patient
- On-Call Caregiver
- Backup Caregiver (secondary actor)

### Explicitly Mentioned Use Cases
#### Primary Use Cases
- Transmit Vital Telemetry
- View Live Vitals Dashboard
- Receive Critical Alert
- Acknowledge Alert
- Configure Clinical Thresholds
- Escalate to Backup Caregiver

#### Secondary Use Cases
- Evaluate Vital Thresholds & Detect Breach
- Authenticate User

The secondary use cases support the primary telemetry and alert workflow. Authenticate User is mandatory included behavior during dashboard access and alert management, and Escalate to Backup Caregiver is conditional behavior executed when an alert is not acknowledged within the required SLA.

### Included & Extended Relationships
- Included relationships: View Live Vitals Dashboard includes Authenticate User; Receive Critical Alert includes Authenticate User; Configure Clinical Thresholds includes Authenticate User.
- Extended relationship: Escalate to Backup Caregiver extends Acknowledge Alert when no acknowledgement is received within SLA.

## 3. Use-Case Flow Specification - Receive Critical Alert & Acknowledge Alert

### 1. Preconditions
- The Remote Patient is registered and actively paired with wearable biometric sensors streaming vital telemetry.
- Clinical baseline thresholds (Heart Rate, SpO2, Blood Pressure) are configured for the patient.
- The On-Call Caregiver and Backup Caregiver accounts are active and assigned in the caregiver matrix.

### 2. Postconditions
- The critical vital anomaly is acknowledged by the caregiver, and the alert state is updated to Acknowledged.
- The caregiver response timestamp and triage details are recorded in the clinical audit log.
- Repeating alarm sirens on the caregiver dashboard and patient device are silenced.
- If unacknowledged within the 60-second SLA, the alert is escalated to the Backup Caregiver.

### 3. Main Success Scenario
1. The Remote Patient sensors transmit vital telemetry containing abnormal physiological values (e.g., SpO2 = 86%, Heart Rate = 145 BPM).
2. The system executes Evaluate Vital Thresholds & Detect Breach and flags a critical threshold breach within 2 seconds.
3. The system generates a high-priority critical alert payload containing patient ID, room location, vital telemetry readings, and breach timestamp.
4. The system sends an urgent audible notification and push alert to the On-Call Caregiver (Receive Critical Alert).
5. The On-Call Caregiver opens the alert notification, which executes Authenticate User to verify caregiver session credentials.
6. The system displays the patient's live telemetry dashboard with real-time biometric trends.
7. The On-Call Caregiver reviews the vital breach and selects Acknowledge Alert.
8. The system updates the alert status to Acknowledged, silences active sirens, and logs the caregiver ID and acknowledgment timestamp into the clinical record.

### 4. Alternate Flow
#### A1. Primary caregiver does not acknowledge alert within SLA
1. At Step 4, upon dispatching the alert to the primary On-Call Caregiver, the system starts an automated 60-second SLA countdown timer.
2. The 60-second timer elapses without receiving an acknowledgment from the primary On-Call Caregiver.
3. The system marks the primary caregiver as unresponsive and executes Escalate to Backup Caregiver (via extend relationship).
4. The system dispatches immediate high-priority alerts with full patient telemetry and timeout notice to the Backup Caregiver.
5. The Backup Caregiver authenticates, acknowledges the escalated alert, and initiates emergency clinical triage.
