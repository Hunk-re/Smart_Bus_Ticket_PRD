"""Menu 2 - Search for a Route."""

import streamlit as st
from helpers import show_route_line


def page_search_route():
    st.header("Search for a Route")
    term = st.text_input("Search by route ID or city")

    if st.button("Search"):
        term = term.strip().lower()
        if term == "":
            st.warning("Please type a route ID or a city name.")
            return

        matches = []

        # First look for an exact route ID (a route ID is unique, so stop at once)
        for route in st.session_state["routes"]:
            if route["route_id"].lower() == term:
                matches.append(route)
                break
        else:
            # No route ID matched, so look for cities (can match many routes)
            for route in st.session_state["routes"]:
                if (route["departure_city"].lower() == term
                        or route["destination_city"].lower() == term):
                    matches.append(route)

        if len(matches) == 0:
            st.warning("No matching routes found.")
        else:
            for route in matches:
                show_route_line(route)
