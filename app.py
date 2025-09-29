import streamlit as st
import re
import streamlit.components.v1 as components

st.set_page_config(page_title="PROGRAMMER'S CALC", layout="centered")

# --- Inject PWA manifest & service worker ---
pwa_head = """
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#000000"/>
<script>
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("service-worker.js")
      .then(() => console.log("Service Worker Registered"));
  }
</script>
"""
components.html(pwa_head, height=0)

# --- App UI ---
st.title("🔢 PROGRAMMER'S CALC")

col1, col2 = st.columns([1, 1])

with col1:
    c_from = st.selectbox(
        "Convert From:",
        ["Bin", "Oct", "Dec", "Hex"],
        placeholder="convert from"
    )

with col2:
    base = st.selectbox(
        "Convert To:",
        ["Bin", "Oct", "Dec", "Hex"],
        placeholder="convert to"
    )

base_map = {"Bin": 2, "Oct": 8, "Dec": 10, "Hex": 16}

patterns = {
    "Bin": r"^[01]*$",
    "Oct": r"^[0-7]*$",
    "Dec": r"^[0-9]*$",
    "Hex": r"^[0-9A-Fa-f]*$"
}

st.markdown("---")

if c_from == "Hex":
    num = st.text_input(f"Enter a {c_from} number:", key="num_input")
else:
    num = st.number_input(f"Enter a {c_from} number:", key="num_input"  )
    num = str(int(num))

if num and not re.fullmatch(patterns[c_from], num):
    st.error(f"⚠️ Invalid input for {c_from}. Please enter only valid digits.")
    num = ""

if num:
    try:
        decimal_num = int(num, base_map[c_from])

        if c_from == base:
            st.warning("⚠️ You selected the same base for conversion.")
        else:
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
