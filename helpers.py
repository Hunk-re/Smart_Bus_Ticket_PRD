import streamlit as st

def money(amount):
    """Format a number as rupees, e.g. 6000 -> 'Rs. 6,000'."""
    return "Rs. " + format(amount, ",")


def seat_status(route):
    """Return Available, Partially Booked or Fully Booked for a route."""
    if route["available_seats"] == 0:
        return "Fully Booked"
    elif route["available_seats"] == route["total_seats"]:
        return "Available"
    else:
        return "Partially Booked"


def find_route(route_id):
    """Return the route dictionary with this ID, or None if not found."""
    wanted = route_id.strip().upper()
    for route in st.session_state["routes"]:
        if route["route_id"] == wanted:
            return route
    return None


def make_booking_id():
    """Create a booking ID that is not already in the issued-ID set."""
    new_id = "B" + str(st.session_state["next_number"])
    while new_id in st.session_state["booking_ids"]:
        st.session_state["next_number"] = st.session_state["next_number"] + 1
        new_id = "B" + str(st.session_state["next_number"])
    st.session_state["next_number"] = st.session_state["next_number"] + 1
    return new_id


def build_route_rows(only_available):
    """Build a list of table rows describing the routes."""
    rows = []
    for number, route in enumerate(st.session_state["routes"], start=1):
        # Skip fully booked routes when the user asks for available-only
        if only_available and route["available_seats"] == 0:
            continue
        rows.append({
            "No.": number,
            "Route": route["route_id"],
            "Journey": route["departure_city"] + " -> " + route["destination_city"],
            "Depart": route["departure_time"],
            "Fare": money(route["ticket_price"]),
            "Seats": str(route["available_seats"]) + "/" + str(route["total_seats"]),
            "Status": seat_status(route),
        })
    return rows


def show_route_line(route):
    """Show one route as a single line of text (used by search)."""
    st.write(
        "**" + route["route_id"] + "** | "
        + route["departure_city"] + " -> " + route["destination_city"]
        + " | " + money(route["ticket_price"])
        + " | " + str(route["available_seats"]) + " seats available"
    )
