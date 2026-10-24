"""Menu 1 - View Available Routes."""

import streamlit as st
from helpers import build_route_rows


def page_view_routes():
    st.header("Available Bus Routes")
    only_available = st.checkbox("Show only routes with seats available")

    rows = build_route_rows(only_available)
    if len(rows) == 0:
        st.info("No routes to show.")
    else:
        st.table(rows)
