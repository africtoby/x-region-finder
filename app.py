import streamlit as st
import requests
import json

# PAGE SETUP
st.set_page_config(page_title="X Region Finder", page_icon="🌍")
st.title("🌍 X (Twitter) User Region Finder")

# SIDEBAR: CREDENTIALS
st.sidebar.header("🔐 Step 1: Configuration")
st.sidebar.info("Paste your X cookies here.")
auth_token = st.sidebar.text_input("auth_token", type="password")
ct0 = st.sidebar.text_input("ct0", type="password")

# MAIN: SEARCH
st.header("Step 2: Search")
username = st.text_input("Enter X Username (No @):", placeholder="ElonMusk")

# LOGIC
def get_location(target_user, auth, ct0_token):
    url = "https://x.com/i/api/graphql/sLVLhk0bGj3MVFEKTdax1w/UserByScreenName"
    headers = {
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "x-csrf-token": ct0_token,
        "content-type": "application/json",
        "cookie": f"auth_token={auth}; ct0={ct0_token}"
    }
    variables = {"screen_name": target_user, "withSafetyModeUserFields": True}
    features = {"hidden_profile_likes_enabled": True, "responsive_web_graphql_exclude_directive_enabled": True, "verified_phone_label_enabled": False, "subscriptions_verification_info_is_identity_verified_enabled": True, "highlights_tweets_tab_ui_enabled": True, "creator_subscriptions_tweet_preview_api_enabled": True, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False, "responsive_web_graphql_timeline_navigation_enabled": True}
    
    try:
        resp = requests.get(url, headers=headers, params={"variables": json.dumps(variables), "features": json.dumps(features)})
        if resp.status_code == 200:
            data = resp.json()
            legacy = data.get("data", {}).get("user", {}).get("result", {}).get("legacy", {})
            return {"status": "success", "loc": legacy.get("location", "N/A"), "name": legacy.get("name", "Unknown")}
        return {"status": "error", "msg": f"Error {resp.status_code}"}
    except Exception as e:
        return {"status": "error", "msg": str(e)}

# BUTTON
if st.button("Find Location"):
    if not auth_token or not ct0:
        st.error("⚠️ Fill in the sidebar cookies first!")
    else:
        res = get_location(username, auth_token, ct0)
        if res['status'] == 'success':
            st.success(f"Found: {res['name']}")
            st.metric("Location", res['loc'])
        else:
            st.error(res['msg'])