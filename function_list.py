import streamlit as st

def scorecard(title, value):
    return f"""
        <div style="
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            width: 150px;
            margin: auto;
        ">
            <p style="font-size: 18px; margin: 0; color: gray;">{title}</p>
            <p style="font-size: 40px; font-weight: bold; color: black; margin: 0;">{value}</p>
        </div>
    """