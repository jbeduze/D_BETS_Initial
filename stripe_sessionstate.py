import streamlit as st
import stripe

def session_state_initial():
    if "stripe_line_items" not in st.session_state:
        st.session_state.stripe_stripe_line_items = [{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}]
    if "stripe_mode" not in st.session_state:
        st.session_state.stripe_mode = "payment"
    if "stripe_ui_mode" not in st.session_state:
        st.session_state.stripe_ui_mode = "hosted"
    if "stripe_successurl" not in st.session_state:
        st.session_state.stripe_stripe_successurl = "https://reimagined-space-journey-pj74pv5j79p2r65v-8503.app.github.dev?session_id={CHECKOUT_SESSION_ID}"
    if "stripe_cancelurl" not in st.session_state:
        st.session_state.stripe_cancelurl = "https://reimagined-space-journey-pj74pv5j79p2r65v-8503.app.github.dev/"
    if "stripe_session_id" not in st.session_state:
        st.session_state.stripe_session_id = None
    if "stripe_payment_status" not in st.session_state:
        st.session_state.stripe_stripe_line_items = None
    if "stripe_customer_email" not in st.session_state:
        st.session_state.stripe_customer_email = None
    if "stripe_payment_intent" not in st.session_state:
        st.session_state.stripe_payment_intent = None
    if "stripe_customer_address_state" not in st.session_state:
        st.session_state.stripe_customer_address_state = None
    if "stripe_customer_address_zip" not in st.session_state:
        st.session_state.stripe_customer_address_zip = None
    if "stripe_customer_name" not in st.session_state:
        st.session_state.stripe_customer_name = None
    if "stripe_session_url" not in st.session_state:
        st.session_state.stripe_session_url = None
    if "stripe_session" not in st.session_state:
        st.session_state.stripe_session = None
    if "stripe_updated_session" not in st.session_state:
        st.session_state.stripe_updated_session = None

def update_sessionstate_checkout_creation(varCheckoutSessionId, varCheckoutSessionURL):
    st.session_state.stripe_session_url = varCheckoutSessionURL
    st.session_state.stripe_session_id = varCheckoutSessionId