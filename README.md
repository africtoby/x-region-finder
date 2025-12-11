**X (Twitter) Region or Location Finder**


A robust, GUI-based tool to programmatically fetch User Region/Location data from X (formerly Twitter).



This tool connects directly to the internal GraphQL API (UserByScreenName) to retrieve accurate location data that is often hidden or unavailable via the standard public API.



&nbsp;Features



100% Accurate: Pulls data directly from X's internal backend.



Visual Interface: No coding required to run searches.



Secure: Runs locally on your machine. You input your own session cookies—no credentials are ever saved or shared.



Bypass Restrictions: Uses internal endpoints to get data not available on standard plans.



**Setup Guide for installation**


Step 1: Install Python

If you don't have Python installed:



Download it from python.org



CRITICAL: During installation, check the box that says "Add Python to PATH".



Step 2: Install the Tool

Download this repository (Click the green "Code" button -> "Download ZIP") and unzip it.



Open the folder.



Click the address bar at the top, type cmd, and press Enter.



In the terminal, paste this command and hit Enter:



Bash



pip install -r requirements.txt

Step 3: Run the App

In that same terminal, type:



Bash



streamlit run app.py


A browser window will open automatically with the tool.



**How to Get Your Cookies (Required)**



To use this tool, you need two "Keys" from your browser to prove you are a real user.



* Open x.com on your computer and log in.



* Right-click anywhere on the page and select Inspect (or press F12).



* Click on the Network tab at the top of the panel.



* In the "Filter" box (top left), type: UserByScreenName.



* Refresh the page. You will see a request appear in the list. Click it.



* Look at the Headers tab on the right. Scroll down to Request Headers.



* Find the line starting with cookie:. You need two values from inside that text:



* auth\_token: A long string of letters/numbers.



* ct0: Another long string (this is your CSRF token).



* Copy these two values and paste them into the app sidebar and you're done and ready to use this tool
