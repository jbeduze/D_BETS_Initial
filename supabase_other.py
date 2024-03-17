


import streamlit as st
from supabase import Client, create_client
 
@st.cache_resource
def get_client_supabase():
    key = st.secrets.supabase.api_key
    url = st.secrets.supabase.url
    key_admin = st.secrets.supabase.api_key_admin
 
    client_supabase = Client(
        supabase_key=key,
        supabase_url=url
    )
 
    return client_supabase