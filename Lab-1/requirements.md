# Lab 1: Requirements Engineering & UML Use-Case Modelling

**Institution:** Department of Computer Science & Engineering, PES University  
**Course:** Software Engineering Lab (SE-Labs)  
**Problem Statement #16:** Remote Patient Vitals Alert & Monitoring App  
**Domain:** Healthcare & Telemedicine  
**Student SRN:** `PES1UG24CS384`  
**Target Stakeholders / Actors:** Remote Patient, On-Call Caregiver  

---

## 1. Problem Context & Overview

The **Remote Patient Vitals Alert & Monitoring App** provides an automated, continuous telemetry ingestion and clinical alert pipeline for post-operative patients recovering in home-care settings. Post-surgical patients are susceptible to rapid physiological deterioration such as acute hypoxia ($\text{SpO}_2 < 90\%$), tachycardia/bradycardia, and hypertensive crises. 

The system continuously streams biometric telemetry (`SpO2`, `Heart Rate`, `Blood Pressure`) from connected wearable IoT sensors, evaluates metrics against personalized clinical baseline thresholds within 2 seconds, and escalates emergency alerts through a multi-tier caregiver matrix.

---

## 2. Complete Requirements Table

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Functional | The system shall continuously evaluate ingested patient vitals against configured clinical thresholds and flag critical anomalies within 2 seconds. | **High** | **Pass:** High heart rate (>140 BPM), critical hypoxia (SpO2 < 90%), or severe BP spike triggers immediate escalation alert in $\le 2\text{s}$.<br>**Fail:** Metric spike ignored, dropped, or evaluation delayed > 5s. | Real-time anomaly detection is essential for post-operative patient safety to prevent acute cardiac/respiratory failure. *(Given Guideline)* |
| **FR-002** | Functional | The system shall allow authorized clinicians to configure and dynamically update patient-specific baseline vitals thresholds without requiring system downtime. | **High** | **Pass:** Clinician updates take effect in the live stream evaluation pipeline within 10 seconds.<br>**Fail:** Default global limits override patient customization or updates cause stream disruption. | Post-surgical recovery boundaries vary significantly by patient age, surgical history, and preexisting conditions. |
| **FR-003** | Functional | The system shall dispatch emergency alerts to the assigned primary On-Call Caregiver and automatically escalate to Tier-2 backup medical staff if unacknowledged within 60 seconds. | **High** | **Pass:** Push/SMS alert reaches primary caregiver within 3s; escalates to Tier-2 after 60s timeout if unacknowledged.<br>**Fail:** Alert remains unescalated on unacknowledged tier past 60s. | Prevents single-point-of-failure in human response; ensures critical patient alerts receive timely medical triage. |
| **FR-004** | Functional | The system shall provide an accessible, one-touch Emergency SOS Panic button on the Remote Patient interface that broadcasts an immediate distress alert with live location and vitals snapshot. | **High** | **Pass:** Single-tap SOS transmits urgent alert to caregiver and emergency matrix in $< 1\text{s}$ with GPS/room data.<br>**Fail:** SOS action fails, lags $> 2\text{s}$, or fails to attach location/vitals snapshot. | Allows patients experiencing acute symptoms (e.g., severe dizziness, acute chest pain) to manually trigger emergency help. |
| **FR-005** | Functional | The system shall persist timestamped historical vitals telemetry and provide automated graphical trend analytics and downloadable clinical summary reports (PDF/CSV) for daily doctor review. | **Medium** | **Pass:** 24-hour vitals summary report with trend graphs compiles and exports in $< 3\text{s}$ with zero data loss.<br>**Fail:** Telemetry data gaps exist, export takes $> 5\text{s}$, or timestamps are misaligned. | Enables attending physicians to track recovery progression, detect subtle hemodynamic degradation, and adjust post-op medications. |
| **NFR-001** | Nonfunctional | The telemetry ingestion gateway shall support at least 500 concurrent continuous telemetry streams with 99.99% uptime. | **High** | **Pass:** Benchmarking tests confirm target latency ($p99 < 500\text{ms}$) and security standards under simulated peak load (500 continuous streams).<br>**Fail:** Gateway crashes, drops packets $> 0.01\%$, or latency exceeds 1s under peak load. | Telemedicine infrastructure must handle multi-patient loads in real time without dropping telemetry packets during critical events. *(Given Guideline)* |
| **NFR-002** | Nonfunctional | The system shall enforce end-to-end encryption for all Protected Health Information (PHI) using TLS 1.3 in transit and AES-256 at rest, coupled with strict Role-Based Access Control (RBAC) and audit logging. | **High** | **Pass:** All network payloads and database records are verified encrypted (TLS 1.3 / AES-256), and unauthorized telemetry access attempts are blocked and logged with 100% audit integrity.<br>**Fail:** Plaintext PHI exposed in transit or logs. | Compliance with statutory healthcare regulations (HIPAA/GDPR) and patient privacy protection are mandatory for medical telemetry. |
