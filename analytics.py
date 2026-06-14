import streamlit as st

def render_stats_ui(history_list):
    st.write("SEARCH HISTORY ANALYTICS")

    if len(history_list) == 0:
        st.write("No data available")
        return
    
    total_keywords = len(history_list)

    longest_keywords = history_list[0]

    for i in history_list:
        if len(i) > len(longest_keywords):
            longest_keywords = i

    st.write(f"Total keywords: {total_keywords}")
    st.write(f"Longest keyword: `{longest_keywords}` ({len(longest_keywords)} character)")