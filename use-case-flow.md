# Use-Case Flow Specification: Receive Critical Alert & Acknowledge Alert

- SRN: PES1UG24CS384
- Scenario No: 16
- Project Title: Remote Patient Vitals Alert & Monitoring App
- Primary Domain: Healthcare & Telemedicine
- Target Actors: Remote Patient, On-Call Caregiver, Backup Caregiver

---

## 1. Preconditions

- The Remote Patient is registered and actively paired with wearable biometric sensors streaming vital telemetry.
- Clinical baseline thresholds (Heart Rate, SpO2, Blood Pressure) are configured for the patient.
- The On-Call Caregiver and Backup Caregiver accounts are active and assigned in the caregiver matrix.

---

## 2. Postconditions

- The critical vital anomaly is acknowledged by the caregiver, and the alert state is updated to Acknowledged.
- The caregiver response timestamp and triage details are recorded in the clinical audit log.
- Repeating alarm sirens on the caregiver dashboard and patient device are silenced.
- If unacknowledged within the 60-second SLA, the alert is escalated to the Backup Caregiver.

---

## 3. Main Success Scenario

1. The Remote Patient sensors transmit vital telemetry containing abnormal physiological values (e.g., SpO2 = 86%, Heart Rate = 145 BPM).
2. The system executes Evaluate Vital Thresholds & Detect Breach and flags a critical threshold breach within 2 seconds.
3. The system generates a high-priority critical alert payload containing patient ID, room location, vital telemetry readings, and breach timestamp.
4. The system sends an urgent audible notification and push alert to the On-Call Caregiver (Receive Critical Alert).
5. The On-Call Caregiver opens the alert notification, which executes Authenticate User to verify caregiver session credentials.
6. The system displays the patient's live telemetry dashboard with real-time biometric trends.
7. The On-Call Caregiver reviews the vital breach and selects Acknowledge Alert.
8. The system updates the alert status to Acknowledged, silences active sirens, and logs the caregiver ID and acknowledgment timestamp into the clinical record.

---

## 4. Alternate Flow

### A1. Primary caregiver does not acknowledge alert within SLA

1. At Step 4, upon dispatching the alert to the primary On-Call Caregiver, the system starts an automated 60-second SLA countdown timer.
2. The 60-second timer elapses without receiving an acknowledgment from the primary On-Call Caregiver.
3. The system marks the primary caregiver as unresponsive and executes Escalate to Backup Caregiver (via extend relationship).
4. The system dispatches immediate high-priority alerts with full patient telemetry and timeout notice to the Backup Caregiver.
5. The Backup Caregiver authenticates, acknowledges the escalated alert, and initiates emergency clinical triage.
