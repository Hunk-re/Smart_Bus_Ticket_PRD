"""Menu 5 - Cancel a Booking."""

import streamlit as st
from helpers import find_route


def page_cancel_booking():
    st.header("Cancel a Booking")
    booking_id = st.text_input("Enter booking ID to cancel (for example B1001)")

    if not st.button("Cancel Booking"):
        return

    booking_id = booking_id.strip().upper()
    if booking_id == "":
        st.warning("Please enter a booking ID.")
        return

    for booking in st.session_state["bookings"]:
        if booking["booking_id"] == booking_id:
            if booking["status"] == "Confirmed":
                # Change the status and give the seats back, as one operation
                route = find_route(booking["route_id"])
                route["available_seats"] = route["available_seats"] + booking["seats"]
                booking["status"] = "Cancelled"

                st.success("Booking " + booking_id + " has been cancelled.")
                st.write("Seats restored: " + str(booking["seats"]))
                st.write("Route " + route["route_id"] + " available seats: "
                         + str(route["available_seats"]))
            else:
                st.error("Booking " + booking_id + " is already cancelled.")
            break
    else:
        st.error("Booking ID " + booking_id + " was not found.")
