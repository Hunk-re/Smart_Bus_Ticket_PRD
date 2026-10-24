"""Menu 6 - View Seat Availability."""

import streamlit as st
from helpers import seat_status


def page_seat_availability():
    st.header("Seat Availability")
    only_available = st.checkbox("Show only routes with seats remaining")

    rows = []
    for route in st.session_state["routes"]:
        if only_available and route["available_seats"] == 0:
            continue
        rows.append({
            "Route": route["route_id"],
            "Journey": route["departure_city"] + " -> " + route["destination_city"],
            "Available": route["available_seats"],
            "Capacity": route["total_seats"],
            "Status": seat_status(route),
        })

    if len(rows) == 0:
        st.info("No routes to show.")
    else:
        st.table(rows)
