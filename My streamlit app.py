import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="😊",
    layout="wide",
)


st.header("College Events")
st.subheader("Upcoming Events")
st.write("Here are some upcoming college events that you might be interested in attending. Stay tuned for more updates!")
st.text("College Fest - Date: 15th March 2023, Location: College Grounds")
st.caption("Join us for a day filled with fun activities, food stalls, and live performances. Don't miss out on the excitement!")
st.markdown("**Guest Lecture - Date: 20th March 2023, Location: Auditorium**")

st.divider()
st.header("Event Registration")

name = st.text_input("Enter your name:")
st.write("Hello, {name}!")
message = st.text_area("Enter your message:")
age = st.number_input("Enter your age:", min_value=1, max_value=60, value=18)
gender = st.radio("Select your gender:", ("Male", "Female", "Other"))
city = st.selectbox(
    "Select your city:",
    ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix"),
)
skills = st.multiselect(
    "Select your skills:",
    ["Python", "Data Analysis", "Machine Learning", "Web Development"],
)
experience = st.slider("Select your years of experience:", 0, 10, 1)
is_student = st.checkbox("Are you a student?")
dob = st.date_input("Select your date of birth:")
meeting_time = st.time_input("Select your preferred meeting time:")
color = st.color_picker("Pick your favorite color:", "#00f900")
uploaded_file = st.file_uploader("Upload your resume:", type=["pdf", "docx"])
type_of_event = st.selectbox(
    "Select the type of event you are interested in:",
    ["Workshop", "Seminar", "Conference", "Networking Event"],
)
picture = st.camera_input("Take a picture:")
audio = st.file_uploader("Upload an audio file:", type=["mp3", "wav"])
feedback = st.text_area("Provide your feedback:")

if st.button("Register"):
    st.success(
        f"Thank you for registering, {name}! We have received your message: "
        f"'{message}'."
    )

st.divider()
st.header("Event Schedule")

try:
    df = pd.read_csv("event_schedule.csv", parse_dates=["Date"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Events", len(df))

    with col2:
        st.metric("Upcoming Events", len(df[df["Date"] > pd.Timestamp.now()]))

    with col3:
        st.metric("Past Events", len(df[df["Date"] < pd.Timestamp.now()]))

except FileNotFoundError:
    st.warning("event_schedule.csv was not found. Add it to the app directory to show event metrics.")
except KeyError:
    st.warning("event_schedule.csv must contain a 'Date' column.")

st.divider()
st.header("Event Information")

tab1, tab2, tab3, tab4 = st.tabs(["Student", "Faculty", "Alumni", "Events"])

with tab1:
    st.write("Student information")

with tab2:
    st.write("Faculty information")

with tab3:
    st.write("Alumni information")

with tab4:
    st.write("Event details")
    st.header(" 7 Event Countdown")
     with st.expander("Click to see the countdown to the next event")
        st.divider()

     st.header("8. Event Feedback")
     st.success("Thank you for attending the event! Please provide your feedback below.")
     st.info("Your feedback is valuable to us and will help us improve future events.")
        st.warning("Please be honest and constructive in your feedback. We appreciate your input!")
        st.error("If you have any issues or concerns, please contact the event organizers directly.")
        if st.button("Show Exeption"):
            st.ballons()
            st.divider()
