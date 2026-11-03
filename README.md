# Busfy

## Overview

Busfy is a Python project that helps people in Istanbul keep track of their buses. It uses live bus information from the IETT API and sends notifications through ntfy.

The user can select a bus line, choose a bus stop, and set their commuting hours. Busfy can send notifications when a bus is approaching, when it is time to leave, when the bus arrives, or when there is a service disruption.

## Setup

First, clone the repository:

```bash
git clone https://github.com/iLoTeKk/busfy.git
cd busfy
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

You also need the ntfy application on your phone to receive notifications. Subscribe to a topic and use the same topic name in Busfy.

## Usage and Example

To start the configuration page, run:

```bash
streamlit run setup_app.py
```

From the page, you can select your bus line and stop, set your commuting days and hours, and choose which notifications you want to receive.

After saving your route, open another terminal and run:

```bash
python main.py
```

The program will check your selected routes every 60 seconds and send notifications when needed.

**Example:**

A student takes bus 79E to university every weekday morning. They set their bus stop, choose 7:00–9:00 as their commuting time, and enter 6 minutes as their walking time.

Busfy monitors the bus and sends a notification when it is approaching or when the student should leave for the stop.