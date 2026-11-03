# My Contribution – Busfy Project

**Contributor:** Mohamad W. M. Alhaddad  
**GitHub:** `ilotekk`

## Overview

I worked on the project's application setup, IETT API communication, user configuration interface, and integration of the monitoring workflow. I also maintained the repository and integrated changes from other team members.

## 1. IETT API Integration (`api/iett_client.py`, `api/wsdl_cleaner.py`)

- Implemented the connection to IETT SOAP services using the `zeep` library and managed reusable API clients.
- Added request handling with retries and error handling.
- Implemented hourly API request tracking and rate-limit checks.
- Added functions for retrieving live bus positions, stop data, line data, and service announcements.
- Added WSDL-related support for connecting to the required services.

## 2. User Configuration Interface (`setup_app.py`)

- Developed a Streamlit interface for setting up bus commute routes.
- Added searchable stop selection, bus line selection, commute days and hours, walking-time settings, and notification preferences.
- Implemented coordinate parsing and Turkish-text normalization to support stop searches.
- Added options to save, view, and delete routes using a JSON profile.
- Included notification topic configuration and a test notification button.

## 3. Main Application and Monitoring (`main.py`)

- Implemented loading and saving of user profiles and monitoring state.
- Connected route scheduling, live IETT data requests, bus validation, event detection, and notification formatting into the monitoring cycle.
- Added handling for approaching, arrived, leave-now, and disruption events.
- Integrated duplicate-notification checks and state updates.
- Added a repeating monitoring loop with basic error handling.

## 4. Configuration and Project Integration

- Set up shared configuration values, file paths, distance thresholds, and API request limits in `config.py`.
- Worked on project dependencies, setup files, and sample route/stop/line data used by the application.
- Integrated and adjusted code across modules to connect separately developed components.
- Maintained the main GitHub repository and incorporated team contributions.

## Summary

My main contribution was building the application setup and external-data connections, providing the user configuration interface, and integrating the monitoring and notification workflow. Other team members contributed their own specialized modules, which were incorporated into the overall application.

