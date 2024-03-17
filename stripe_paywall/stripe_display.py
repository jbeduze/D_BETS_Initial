import streamlit as st
import stripe

from stripe_paywall import stripe_functions as sf

def get_checkout_button():
    checkout_button = st.link_button(
        label="Checkout",
        url=st.session_state.stripe_session_url,
        type="primary",
        use_container_width=True
    )

def get_checkout_proceed_button():
    proceed_button = st.button(
        label="Proceed to checkout",
        key="button1",
        type="primary",
        use_container_width=True
    )
    if proceed_button:
        st.divider()
        checkout_session = sf.create_checkout_session()
        get_checkout_button()

# def get_checkout_container():
#     checkout_container = st.container(border=True)
#     with checkout_container:
#         tabExisting, tabNew = st.tabs(tabs=["Existing User", "New User"])
#         with tabExisting:
#             st.markdown("Yo")
#         with tabNew:
#             get_checkout_proceed_button()