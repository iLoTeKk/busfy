# Contribution – Sara Mir

**Student ID:** 2309015086  
**GitHub:** xsarahy

## Files I worked on
- `schedule.py`
- `test_schedule.py`

## schedule.py – Scheduling and Time Management

This module is responsible for checking the current time and deciding which bus routes should be monitored.

- **`get_current_istanbul_time()`**: Gets the current date and time using the Istanbul timezone.
- **`is_in_commute_window(route, current_time)`**: Checks whether the current day and hour match the route's selected commuting schedule.
- **`has_any_active_route(profile, current_time)`**: Finds and returns all routes that are currently active.
- **`init_scheduler(cycle_callback)`**: Runs the monitoring cycle repeatedly with a 60-second interval.

## test_schedule.py – Testing

This file is used to test the scheduling functions and make sure they work correctly.

It helps check the scheduling logic and whether routes are selected according to their configured days and hours.

## How it fits in the project

The scheduling module makes sure Busfy only monitors buses during the user's selected commuting hours. This helps avoid unnecessary API requests and notifications outside those hours.