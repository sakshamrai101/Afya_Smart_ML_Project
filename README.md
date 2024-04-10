# Afya Smart_ML Project

## Overview
The Afya Smart_ML Project is designed to optimize the e-consultation process for Primary Care Providers (PCPs) on the AfyaChat platform, leveraging GPT-3.5 Turbo for AI-driven insights. We streamline consultations, augment them for comprehensive submissions to specialists, and ensure compliance with best-practice guidelines.

## Getting Started
To begin using the Smart_ML application for enhancing e-consultations, just do:

**Running the Application:**
   - Start the server with `run.py`:
     ```sh
     python run.py
     ```
   - Access the application at `localhost` on your web browser.

## Features
- **User Authentication:** Secure login for PCPs with SQL-Lite database integration.
- **E-Consult File Handling:** Upload and analyze e-consult text files.
- **AI-Driven Workflow:** AI model scans for missing information, generates targeted questions, and offers evidence-based recommendations.
- **Real-Time Notifications:** Utilize Twilio service for immediate alerts.

## Components
- `app/`: Main application code including Flask routes and HTML templates.
- `static/`: CSS and JavaScript files for UI.
- `data/`: Data files used by the application.
- `tests/`: Unit tests for validating application functionality.



## Security
The application includes robust security features, such as secure data transmission and authentication, ensuring the confidentiality and integrity of e-consultation data.

## Feedback
Your feedback is valuable to us. Please submit any feedback or issues through the GitHub Issues section of this repository.
