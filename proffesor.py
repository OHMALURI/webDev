import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
 
def get_data(dept, prof_type, assoc_prof_type, assist_prof_type, lect_type):
    url = requests.get (f'https://www.{dept}.ruet.ac.bd/teacher_list').text
    soup = BeautifulSoup(url, 'lxml')
    teachers = soup.find_all('tr')[1:]
    #print(teachers)
    name_en = []
    designation = []
    phone_no = []
    email = []
    departments = []
    for teacher in teachers:
        name = teacher.find_all('td')[1].text.strip()
        desig = teacher.find_all('td')[3].text.strip()
        phone = teacher.find_all('td')[6].text.strip()
        mail = teacher.find_all('td')[5].text.strip()
        department = teacher.find_all('td')[4].text.strip()
        if (desig == "Professor" and prof_type) or (desig == "Associate Professor" and assoc_prof_type) or (desig == "Assistant Professor" and assist_prof_type) or (desig == "Lecturer" and lect_type):
            name_en.append(name)
            designation.append(desig)
            phone_no.append(phone)
            email.append(mail)
            departments.append(department)
    data = pd.DataFrame({'Name': name_en, 'Designation': designation, 'Phone': phone_no, 'Email': email, 'Department': departments})
    return data
 
 
def main():
    st.title("RUET Teacher's Information")
    #department selection
    depts = ["EEE", "CSE", "CHEM", "MATH", "PHY"]
    dept = st.sidebar.selectbox("Select Department", depts).lower()
    #Adding designation filter using checkbox
    prof = st.sidebar.checkbox("Professor", value=True)
    assoc_prof = st.sidebar.checkbox("Associate Professor")
    assist_prof = st.sidebar.checkbox("Assistant Professor")
    lect = st.sidebar.checkbox("Lecturer")
 
    data = get_data(dept, prof, assoc_prof, assist_prof, lect)
    st.dataframe(data)
 
#constructor
 
if __name__ == '__main__':
    main()