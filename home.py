import streamlit as st
from streamlit.components.v1 import html, components
from stripe_paywall import stripe_display as sdisplay, stripe_functions as sfunction, stripe_sessionstate as ssession
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit_scrollable_textbox as sctbx
from streamlit_extras.stylable_container import stylable_container

#Font styling
with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
# Initialize session state variables if they don't exist
if 'terms_accepted' not in st.session_state:
    st.session_state['terms_accepted'] = False
if 'customer_status' not in st.session_state:
    st.session_state['customer_status'] = None  # 'new' or 'returning'

def read_markdown_file(termsandconditions):
    with open(termsandconditions, "r", encoding="utf-8") as file:
        return file.read()
markdown_content = read_markdown_file("termsandconditions.md")

with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")

with st.expander(
    "Daddy Bets: Terms and conditions",
    expanded=True
    ):
    st.markdown(markdown_content, unsafe_allow_html=True)
    # Accepting terms and conditions
    if st.button("Accept Terms and conditions", use_container_width=True) or st.session_state['terms_accepted']:
        st.session_state['terms_accepted'] = True  # Terms accepted
    # if st.session_state['terms_accepted']:
        st.success('You have accepted the terms and conditions')
        cols = st.columns(2)
        # Asking if the customer is new or returning
        if st.session_state['customer_status'] is None:
            if cols[0].button("Returning Customer"):
                st.session_state['customer_status'] = 'returning'
            elif cols[1].button("New Customer"):
                st.session_state['customer_status'] = 'new'

        # Handling returning customer
        if 'customer_status' in st.session_state and st.session_state['customer_status'] == 'returning':
            # Placeholder for the form
            placeholder = st.empty()
            
            # Preset login credentials
            actual_email = "email@example.com"
            actual_password = "password123"
            
            # Insert a form in the container
            with placeholder.form("login"):
                st.markdown("#### Enter your credentials")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")
            
            # Check if the form was submitted and the credentials match
            if submit:
                if email == actual_email and password == actual_password:
                    # Clear the form/container and display a success message
                    placeholder.empty()
                    st.success("Login successful")
                else:
                    # Display an error message if login fails
                    st.error("Login failed")
                
        # Handling new customer
        elif st.session_state['customer_status'] == 'new':
                    col = st.columns(2)
                    with col[1]:
                        st.write("A FLOWGENIUS product")
                    with col[0]:
                        ssession.session_state_initial()

                        queryp = sfunction.get_query_params()
                        if queryp is not None:
                            updated_session = sfunction.retrieve_checkout_session2(varSessionId = queryp)
                            name = updated_session.customer_details.name
                            form = st.form(key="supabase")
                            with form:
                                username = st.text_input(label="username", value=updated_session.customer_details.email, disabled=True)
                                credential = st.text_input(label="credential", type="password")
                                submit = st.form_submit_button(label="Submit", type="primary")
                                if submit:
                                    if credential is not None:
                                        st.success("Submit to supabase")
                                        st.rerun()
                                    else:
                                        st.error("no password")
                        else: 
                            sdisplay.get_checkout_proceed_button()
