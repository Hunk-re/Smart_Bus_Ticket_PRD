"""Menu 8 - Route Schedule by departure city."""

import streamlit as st
from config import CITIES


def page_schedule():
    st.header("Route Schedule by Departure City")

    # Nested loops: outer loop = cities, inner loop = routes
    for city in CITIES:
        st.subheader(city)
        found_any = False

        for route in st.session_state["routes"]:
            if route["departure_city"] == city:
                st.write(route["route_id"] + " -> " + route["destination_city"]
                         + " | " + route["departure_time"])
                found_any = True

        if not found_any:
            st.write("No scheduled departures.")
