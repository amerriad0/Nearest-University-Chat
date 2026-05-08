import streamlit as st

st.set_page_config(page_title="Nearest University Chat")

st.title("Nearest University Chat") 
st.write("Write your city ")

universities = {
    "nablus": "An-Najah National University",
    "tulkarm": "Palestine Technical University - Kadoorie",
    "ramallah": "Birzeit University",
    "jenin": "Arab American University",
    "hebron": "Hebron University",
    "bethlehem": "Bethlehem University",
    "qalqilya": "Palestine Technical University - Kadoorie",
    "jericho": "Al-Quds University",
    "jerusalem": "Al-Quds University"
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("ASK")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    text = user_input.lower()
    found_cities = []

    for city in universities:
        if city in text:
            found_cities.append(city)

    if found_cities:
        replies = []

        for city in found_cities:
            reply_line = f"The nearest university to {city.title()} is {universities[city]}."
            replies.append(reply_line)

        reply = "\n\n".join(replies)
    else:
        reply = "I can't find your city"

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.write(reply)