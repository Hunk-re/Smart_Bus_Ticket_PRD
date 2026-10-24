"""Menu 4 - View My Bookings."""

import streamlit as st
from helpers import find_route, money


def page_view_bookings():
    st.header("My Bookings")

    if len(st.session_state["bookings"]) == 0:
        st.info("No bookings found.")
        return

    rows = []
    for number, booking in enumerate(st.session_state["bookings"], start=1):
        route = find_route(booking["route_id"])
        rows.append({
            "No.": number,
            "Booking ID": booking["booking_id"],
            "Passenger": booking["passenger_name"],
            "Route": booking["route_id"] + " ("
                     + route["departure_city"] + " -> "
                     + route["destination_city"] + ")",
            "Seats": booking["seats"],
            "Total Fare": money(booking["total_fare"]),
            "Status": booking["status"],
        })
    st.table(rows)
