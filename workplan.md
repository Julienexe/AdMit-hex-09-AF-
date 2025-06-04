# 📚 Django Backend App Structure for School Admin Portal

This project is structured into 7 modular Django apps, each responsible for a distinct feature set based on the provided system flowchart.

---

## 1. 🧩 admit

**Responsibilities:**
- Admin authentication and login (School Admin Login)
- User roles and permissions (e.g., admin, reviewer)
- Session and token management
- Dashboard entry point (`School Dashboard`)
- Display high-level links and recent activities
- Home view aggregating application statistics and alerts

---

## 2. 📈 analytics

**Responsibilities:**
- Application Trends and Reports module (`Analytics & Reports`)
- Statistical breakdowns:
  - Gender Distribution
  - Geographic Distribution
  - Grade Level Demand
  - Application Success Rates
  - Peak Application Periods
- Generates visual reports and exports (PDF/CSV)
- Summary statistics used on the dashboard overview

---

## 3. 📬 applications

**Responsibilities:**
- Application submission and management (`Application Management Center`)
- List, filter, and search applications by status
- Review interface for individual applications
- Application decision workflow:
  - Accept → Generate Admission Letter
  - Reject → Send Rejection Notice
  - Need Info → Request Additional Info
- Application statistics overview (Received, Accepted, Rejected, Pending)
- Alert system for new applications
- Handles integration with `students` and `finance` apps after decisions

---

## 4. 🏫 schools

**Responsibilities:**
- Manage school profile and public-facing info (`School Profile Management`)
- Editable sections:
  - Contact Details & Location
  - Website & Social Media
  - School Photos / Gallery
  - Programs Offered
  - Application Periods (start/end dates)
- Admin UI for updating and previewing school info

---

## 5. 💰 finance

**Responsibilities:**
- Financial Management module for application-related payments
- Application Fee Tracking:
  - Received Payments
  - Outstanding Balances
- Payment Status Monitor:
  - Confirmed Payments
  - Failed Transactions
- Revenue analytics dashboard (total revenue, monthly summary)
- Links with `applications` for fee verification
- Integration with third-party payment gateways (configured via `config`)

---

## 6. ⚙️ management

**Responsibilities:**
- System Configuration Panel (`System Configuration`)
- Modules:
  - User Account Settings (change password, profile)
  - Notification Preferences (email/SMS settings)
  - Admission Criteria Setup:
    - Minimum Grade Requirements
    - Required Documents List
    - Application Deadlines
  - Payment Gateway Configuration:
    - Set Application Fees
    - Payment Methods (Mobile Money, Cards)
  - Interface Customization:
    - Theme & Color Settings
    - Layout Preferences
  - Help & Support Access

---

## 7. 👩‍🎓 students

**Responsibilities:**
- Student profile data and relationship with applications
- Profile review sections:
  - Academic Records
  - Personal Information
  - Uploaded Application Documents
  - Parent/Guardian Details
- Dashboard updates after admission or rejection
- Tracks communication history with the student
- Links with `applications` to retrieve profile for review

---

## 📦 Future Improvements

- Split `admit` into `users` and `dashboard` if complexity increases
- Add `communication` app for notification templates and logs
- Add `audit` or `logs` app to track admin actions and system changes

---
