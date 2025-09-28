import streamlit as st

st.set_page_config(page_title="PROGRAMMER'S CALC", layout="centered")

st.title("🔢PROGRAMMER'S CALC")

# Layout: two columns (input left, dropdown right)
col1, col2 = st.columns([1, 1])

with col1:
c_from = st.selectbox(                  #left column
        "Convert From:",
        ["Bin", "Oct", "Dec", "Hex"],   #select the base to conver FROM
        placeholder="convert from"
    )

with col2:
    base = st.selectbox(                #right dropdown menu
        "Convert To:",                   # base to convert TO       
        ["Bin", "Oct", "Dec", "Hex"],
        placeholder="convert to"
    )

# Map bases to numbers
base_map = {"Bin": 2, "Oct": 8, "Dec": 10, "Hex": 16}   #assign str values integers

st.markdown("---")  # separator line            #a separator line...like <hr>

num = st.text_input("Enter a number:")          #streamlit requests for user input...type=number...nani hajui number😂

#nested if loop to check which bases the useer chose....and to convert the value
if num:
    try:
        # Convert input to decimal
        decimal_num = int(num, base_map[c_from])

        if c_from == base:  #cant convert from BIN to BIN
            st.warning("⚠️ You selected the same base for conversion.")
        else:
            # Show result based on target base
            st.subheader("✨ Conversion Result")

            if base == "Dec":
                st.write(f"**Decimal:** {decimal_num}")
            elif base == "Bin":
                st.write(f"**Binary:** {bin(decimal_num)[2:]}")
            elif base == "Oct":
                st.write(f"**Octal:** {oct(decimal_num)[2:]}")
            elif base == "Hex":
                st.write(f"**Hexadecimal:** {hex(decimal_num)[2:].upper()}")

    except ValueError:
        st.error("⚠️ Invalid number for the selected base. Please check your input.")
