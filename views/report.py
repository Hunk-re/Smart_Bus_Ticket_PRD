"""Menu 7 - Generate Booking Report."""

import streamlit as st
from helpers import money


def page_report():
    st.header("Booking Report")

    bookings = st.session_state["bookings"]

    total_bookings = len(bookings)
    confirmed_count = 0
    cancelled_count = 0
    seats_reserved = 0
    confirmed_revenue = 0
    fully_booked_routes = 0
    route_rows = []

    # Count the booking statuses
    for booking in bookings:
        if booking["status"] == "Confirmed":
            confirmed_count = confirmed_count + 1
        else:
            cancelled_count = cancelled_count + 1

    # Nested loops: outer loop = routes, inner loop = confirmed bookings of that route
    for route in st.session_state["routes"]:
        route_seats = 0
        route_revenue = 0

        for booking in bookings:
            if booking["route_id"] == route["route_id"] and booking["status"] == "Confirmed":
                route_seats = route_seats + booking["seats"]
                route_revenue = route_revenue + booking["total_fare"]

        seats_reserved = seats_reserved + route_seats
        confirmed_revenue = confirmed_revenue + route_revenue

        if route["available_seats"] == 0:
            fully_booked_routes = fully_booked_routes + 1

        route_rows.append({
            "Route": route["route_id"],
            "Journey": route["departure_city"] + " -> " + route["destination_city"],
            "Seats Reserved": route_seats,
            "Confirmed Revenue": money(route_revenue),
        })

    st.write("**Total bookings created:** " + str(total_bookings))
    st.write("**Confirmed bookings:** " + str(confirmed_count))
    st.write("**Cancelled bookings:** " + str(cancelled_count))
    st.write("**Seats currently reserved:** " + str(seats_reserved))
    st.write("**Confirmed revenue:** " + money(confirmed_revenue))
    st.write("**Fully booked routes:** " + str(fully_booked_routes))

    st.subheader("Confirmed bookings by route")
    st.table(route_rows)
