"""
This Module is responsible for formatting message for the user
"""


def format_approaching_message(bus: dict, route: dict, distance_m: float, eta_min: float) -> tuple[str, str, str]:
    name = route.get("name", "Bus")
    return (
        f"{name} is approaching",
        f"About {distance_m:.0f} m away (~{eta_min:.0f} min).",
        "default",
    )


def format_leave_now_message(bus: dict, route: dict, walk_min: int, eta_min: float) -> tuple[str, str, str]:
    name = route.get("name", "Bus")
    return (
        f"Leave now for {name}",
        f"Walk takes {walk_min} min, bus arrives in ~{eta_min:.0f} min.",
        "high",
    )


def format_arrived_message(bus: dict, route: dict) -> tuple[str, str, str]:
    name = route.get("name", "Bus")
    return (f"{name} has arrived", "Your bus is at the stop.", "urgent")


def format_disruption_message(announcement: dict, route: dict) -> tuple[str, str, str]:
    name = route.get("name", "Route")
    text = announcement.get("text") or announcement.get("message", "Service disruption.")
    return (f"Disruption on {name}", text, "high")
    pass