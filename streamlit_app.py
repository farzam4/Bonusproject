import streamlit as st

def calculate_percentage(obtained, total):
    if total == 0:
        raise ZeroDivisionError("Total marks cannot be zero")
    return (obtained / total) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# __________________ Starting with Streamlit __________________

st.set_page_config(page_title="Grade Calculator", page_icon="📊")

st.title("📊 Grade Calculator Application")
st.write("Description: This application calculates percentage and grade based on obtained marks.")
st.write("By Farzam Ahsan. ID: 2540045")

obtained_marks = st.number_input("Enter obtained marks:", min_value=0.0, format="%.2f")
total_marks = st.number_input("Enter total marks:", min_value=0.0, format="%.2f")

if st.button("Calculate Grade"):
    try:
        st.header("Result")
        percentage = calculate_percentage(obtained_marks, total_marks)
        grade = calculate_grade(percentage)

        st.success(f"Percentage: {percentage:.2f}%")
        st.success(f"Grade: {grade}")

    except ZeroDivisionError as error:
        st.error(error)
    except Exception:
        st.error("Invalid Input")
