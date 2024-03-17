import streamlit as st
import stripe
from stripe_paywall import stripe_sessionstate as ss

def create_checkout_session_dev():
    session = stripe.checkout.Session.create(
        api_key = st.secrets.stripe_api_key_test,
        line_items=[{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}],
        mode="payment",
        ui_mode="hosted",
        success_url="https://fuzzy-engine-4j74jjrvj9j92qqr7.github.dev?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="https://fuzzy-engine-4j74jjrvj9j92qqr7.github.dev/"
    )
    
    st.session_state.stripe_session = session
    ss.update_sessionstate_checkout_creation(varCheckoutSessionId=session.id, varCheckoutSessionURL=session.url)
    print(session)
    return session

def create_checkout_session():
    session = stripe.checkout.Session.create(
        api_key = st.secrets.stripe_api_key_test,
        line_items=[{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}],
        mode="payment",
        ui_mode="hosted",
        success_url="https://testpayfg.streamlit.app?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="https://testpayfg.streamlit.app"
    )
    
    st.session_state.stripe_session = session
    ss.update_sessionstate_checkout_creation(varCheckoutSessionId=session.id, varCheckoutSessionURL=session.url)
    print(session)
    return session


def retrieve_checkout_session1(varCheckoutSessionId):
    updated_session = stripe.checkout.Session.retrieve(
        api_key=st.secrets.stripe_api_key_test,
        id=varCheckoutSessionId
    )

    st.session_state.stripe_updated_session = updated_session
    st.session_state.stripe_customer_email = updated_session.customer_email
    st.session_state.stripe_payment_intent = updated_session.payment_intent
    st.session_state.stripe_payment_status = updated_session.payment_intent
    st.session_state.stripe_customer_name = updated_session.customer_details.name
    st.session_state.stripe_customer_address_state = updated_session.customer_details.address.state
    st.session_state.stripe_customer_address_zip = updated_session.customer_details.address.postal_code
    data = {
        "email": updated_session.customer_email,
        "payment_status": updated_session.payment_status,
        "payment_intent": updated_session.payment_intent,
        "name": updated_session.customer_details.name,
        "postalcode": updated_session.customer_details.address.postal_code,
        "state": updated_session.customer_details.address.state
    }
    print(updated_session)
    return updated_session

def get_query_params():
    query_params = st.query_params.get(
        "session_id",
        None
    )
    
    print(query_params)
    return query_params

def retrieve_checkout_session2(varSessionId):
    updated_session = stripe.checkout.Session.retrieve(
        api_key=st.secrets.stripe_api_key_test,
        id=varSessionId
    )
    #print(get_query_params())
    print(updated_session)
    st.session_state.stripe_updated_session = updated_session
    st.session_state.stripe_customer_email = updated_session.customer_email
    st.session_state.stripe_payment_intent = updated_session.payment_intent
    st.session_state.stripe_payment_status = updated_session.payment_intent
    st.session_state.stripe_customer_name = updated_session.customer_details.name
    st.session_state.stripe_customer_address_state = updated_session.customer_details.address.state
    st.session_state.stripe_customer_address_zip = updated_session.customer_details.address.postal_code
    data = {
        "email": updated_session.customer_email,
        "payment_status": updated_session.payment_status,
        "payment_intent": updated_session.payment_intent,
        "name": updated_session.customer_details.name,
        "postalcode": updated_session.customer_details.address.postal_code,
        "state": updated_session.customer_details.address.state
    }
    return updated_session
    