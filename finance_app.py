import streamlit as st
import anthropic

lient = anthropic.Anthropic(api_key="YOUR_KEY_PLACEHOLDER")

# Page configuration
st.set_page_config(
    page_title="AI Finance Assistant",
    page_icon="💰",
    layout="centered"
)

# Title and description
st.title("💰 AI Finance Assistant")
st.markdown("**Your personal AI powered accounting and finance expert!**")
st.divider()

# System prompt
system_prompt = """You are an expert financial assistant and accountant.
You help clients with:
- Invoice and billing questions
- Tax calculations and advice
- Budget planning and expense tracking
- Financial reporting
- Accounting best practices
Always give clear, professional financial advice.
Keep answers short and easy to understand."""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

# Chat input
user_input = st.chat_input("Ask me anything about finance...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Add to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                system=system_prompt,
                messages=st.session_state.messages
            )
            answer = response.content[0].text
            st.write(answer)

    # Save response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })