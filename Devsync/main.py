import streamlit as st

st.set_page_config(
    page_title="DevSync",
    layout="wide"
)

st.sidebar.title(" DevSync")
st.sidebar.markdown("Collaborative Issue Tracker")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", [
    " Dashboard",
    " Raise Issue",
    " All Issues"
])

if page == " Dashboard":
    from app.pages import dashboard
    dashboard.show()

elif page == " Raise Issue":
    from app.pages import raise_issue
    raise_issue.show()

elif page == " All Issues":
    from app.pages import all_issues
    all_issues.show()
