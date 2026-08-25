# Use-Case Flow Specification

**Document Type:** 1-Page Core Use-Case Specification  
**Course:** Software Engineering Lab (PES University - Dept. of CSE)  
**Problem Statement #16:** Remote Patient Vitals Alert & Monitoring App  
**Student SRN:** `PES1UG24CS384`  

---

### Use Case: UC-03 - Process Critical Vital Breach & Escalate Caregiver Alert

- **Primary Actor(s):** Remote Patient, On-Call Caregiver
- **Secondary Actor(s):** IoT Vital Sensor Device, Tier-2 Emergency Response Matrix
- **Stakeholders & Interests:**
  - *Remote Patient:* Expects immediate emergency response during critical physiological decompensation.
  - *On-Call Caregiver:* Needs instant, high-priority notifications with patient vitals and room context to execute rapid triage.
  - *Clinical Administration / Doctor:* Demands guaranteed alert delivery, zero telemetry loss, and non-repudiable audit logs.

---

### Preconditions
1. The remote patient is registered in the system with active IoT vitals sensors paired and calibrated.
2. Patient-specific baseline thresholds (e.g., $\text{HR} \in [50, 110]\text{ bpm}$, $\text{SpO}_2 \ge 92\%$, $\text{Systolic BP} \le 140\text{ mmHg}$) are loaded into the evaluation pipeline.
3. The caregiver matrix has an assigned primary On-Call Caregiver and active Tier-2 backup contacts.

---

### Postconditions
- **Success Postcondition:** The critical breach is acknowledged by the caregiver, triage state is updated to `IN_PROGRESS`, repeating sirens are silenced, and all event timestamps are stored in the audit log.
- **Escalation Postcondition:** If unacknowledged within 60 seconds, the alert automatically escalates to the Tier-2 emergency matrix with full audit logging.

---

### Main Success Scenario (MSS):
1. The **IoT Vital Sensor Device** transmits a continuous telemetry packet containing abnormal vitals (e.g., $\text{SpO}_2 = 86\%$, $\text{HR} = 148\text{ BPM}$).
2. System ingests telemetry data, decrypts payload, and executes `<<include>> UC-04: Evaluate Clinical Thresholds`.
3. System confirms that readings breach configured baseline thresholds and flags priority status as `CRITICAL_ANOMALY` within **2 seconds**.
4. System constructs an emergency alert payload containing patient ID, room location, live vitals snapshot, and timestamp.
5. System dispatches a high-priority audible push notification and SMS alert to the assigned **On-Call Caregiver**.
6. **On-Call Caregiver** receives the alert, views the patient's real-time telemetry dashboard, and taps **"Acknowledge & Triage"**.
7. System updates alert status to `ACKNOWLEDGED`, silences repeating audible alarms, and displays a notification on the patient interface that caregiver assistance is active.
8. System logs caregiver ID, response time, and vital telemetry snapshot into the clinical audit repository.
9. **Use case ends successfully.**

---

### Alternate Flows:

#### 5a. Primary Caregiver Timeout (Unacknowledged Alert)
- **5a1.** Upon dispatching the emergency alert (Step 5), the system initiates an automated **60-second countdown timer**.
- **5a2.** The 60-second timer expires without receiving an acknowledgment from the primary On-Call Caregiver.
- **5a3.** System flags the primary caregiver as `UNRESPONSIVE`, logs a timeout event in the audit trail, and triggers `<<extend>> UC-07: Escalate to Tier-2 Caregiver Matrix`.
- **5a4.** System broadcasts simultaneous emergency alerts to Tier-2 backup medical staff and hospital rapid response dispatchers.
- **5a5.** A Tier-2 emergency responder acknowledges the alert; system assigns triage to Tier-2 responder and proceeds to Step 7.

#### 5b. Sensor Telemetry Disconnection During Active Breach
- **5b1.** If sensor connectivity drops during an active critical breach event, the system locks the last valid abnormal vitals snapshot.
- **5b2.** System appends a `SENSOR_OFFLINE_WARNING` banner to the caregiver alert payload and continues high-priority escalation.
- **5b3.** Upon sensor reconnection, the live stream resumes and updates the triage screen automatically.
