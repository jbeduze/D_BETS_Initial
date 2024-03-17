import streamlit as st
from connections import connection_supabase as connSB

 
supabase_client = connSB.supabase_connection_initialize()
 
def login_success(varMessage: str, varUsername: str):
    success_message = st.success(body=varMessage, icon="✅")
    st.session_state.authenticated = True
    st.session_state.username = varUsername
 
def get_auth_data_json(varUsername, varCredential):
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    auth_data = {
        column_username: varUsername,
        column_credential: varCredential
    }
    return auth_data
 
def get_auth_select_string():
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    select_string = f"{column_username}, {column_credential}"
    return select_string
 
def get_error_message(varType,varError):
    if varType == "new":
        error_message = varError.message
    elif varType == "exist":
        error_message = varError
    else:
        error_message = "unknown"    
    error_icon = "⚠️"
    display_error = st.error(body=error_message, icon=error_icon)
   
def add_new_user(varUsername, varCredential):
    table_users = st.secrets.loginform.user_tablename
    data_new_user = get_auth_data_json(varUsername=varUsername, varCredential=varCredential)
    data, _ = (supabase_client.table(table_name=table_users).insert(json=data_new_user).execute())
    return data, _
 
def check_existing_user(varUsername, varCredential):
    table_users = st.secrets.loginform.user_tablename
    select_string = get_auth_select_string()
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    data, _ = (supabase_client.table(table_name=table_users).select(select_string).eq(column=column_username, value=varUsername).eq(column=column_credential, value=varCredential).execute())
    length_data = len(data[-1])
    return length_data
       
def formfield_username(varType):
    if varType=="new":
        field_label = st.secrets.loginform.create_username_label
        field_placeholder = st.secrets.loginform.create_username_placeholder
        field_help = st.secrets.loginform.create_username_help
    elif varType == "exist":
        field_label = st.secrets.loginform.login_username_label
        field_placeholder = st.secrets.loginform.login_username_placeholder
        field_help = st.secrets.loginform.login_username_help
    username_field = st.text_input(
        label=field_label,
        placeholder=field_placeholder,
        help=field_help,
        disabled=st.session_state.authenticated
    )
    return username_field
   
def formfield_credential(varType):
    if varType=="new":
        field_label = st.secrets.loginform.create_password_label
        field_placeholder = st.secrets.loginform.create_password_placeholder
        field_help = st.secrets.loginform.create_password_help
    elif varType == "exist":
        field_label = st.secrets.loginform.login_password_label
        field_placeholder = st.secrets.loginform.login_password_placeholder
        field_help = st.secrets.loginform.login_password_help
   
   
    credential_field = st.text_input(
        label=st.secrets.loginform.create_password_label,
        placeholder=st.secrets.loginform.create_password_placeholder,
        help=st.secrets.loginform.create_password_help,
        type="password",
        disabled=st.session_state.authenticated
    )
    return credential_field
 
def formbutton_submit():
    submit_formbutton = st.form_submit_button(
        label=st.secrets.loginform.create_submit_label,
        type="primary",
        disabled=st.session_state.authenticated
    )
    return submit_formbutton
 
def subform_create():
    subform_create = st.form(key="subform_create")
    with subform_create:
        subform_create_username = formfield_username(varType="new")
        subform_create_credential = formfield_credential(varType="new")
        subform_create_submit = formbutton_submit()
        if subform_create_submit:
            try:
                add_new_user(varUsername=subform_create_username, varCredential=subform_create_credential)
            except Exception as e:
                get_error_message(varError=e, varType="new")
            else:
                login_success(varMessage=st.secrets.loginform.create_success_message, varUsername=subform_create_username)
           
           
   
def subform_login():
    subform_login = st.form(key="subform_login")
    with subform_login:
        subform_login_username = formfield_username(varType="exist")
        subform_login_credential = formfield_credential(varType="exist")
        subform_login_submit = formbutton_submit()
        if subform_login_submit:
            user_check_length = check_existing_user(varUsername=subform_login_username, varCredential=subform_login_credential)
            if user_check_length > 0:
                login_success(varMessage=st.secrets.loginform.create_success_message, varUsername=subform_login_username)
            else:
                get_error_message(varType="exist", varError=st.secrets.loginform.login_error_message)
               
           
               
   
def get_login_expander():
    login_expander_label = st.secrets.loginform.title
    login_expander_expanded = not st.session_state.authenticated
    create_tab_title = st.secrets.loginform.create_title
    login_tab_title = st.secrets.loginform.login_title
    login_tabs = [create_tab_title, login_tab_title]
   
    login_expander = st.expander(
        label=login_expander_label,
        expanded=login_expander_expanded
    )
   
    with login_expander:
        create_tab, login_tab = st.tabs(tabs=login_tabs)
        with create_tab:
            subform_create()
        with login_tab:
            subform_login()
   
def get_form_login():
   
    login_form_container = st.container(border=True)
    with login_form_container:
        get_login_expander()
   