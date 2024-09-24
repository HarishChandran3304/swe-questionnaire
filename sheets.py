import gspread
import csv
import streamlit as st


# Streamlit setup
credentials = {
    "type": st.secrets["type"],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"],
    "universe_domain": st.secrets["universe_domain"]
}
gc = gspread.service_account_from_dict(credentials)


# Local setup
# gc = gspread.service_account(filename="credentials.json")


sh = gc.open("SWE Test")
worksheet = sh.sheet1


def get_all_rows():
    return worksheet.get_all_values()

def import_csv():
    rows = get_all_rows()
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows) 

def insert_row(row):
    worksheet.append_row(row)


if __name__ == "__main__":
    import_csv()