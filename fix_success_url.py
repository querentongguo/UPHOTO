with open('success.html', 'r') as f:
    content = f.read()

old_script = """        // Construct the Google Forms prefilled URL (User must replace YOUR_FORM_LINK and entry.123456)
        // Example: https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?usp=pp_url&entry.123456=
        const baseFormUrl = "https://forms.gle/YOUR_FORM_LINK"; 
        
        // For demonstration, we just append ?order=txid
        document.getElementById('upload-link').href = baseFormUrl + "?order_id=" + txid;"""

new_script = """        // Construct the Google Forms prefilled URL with the exact entry ID for Transaction ID
        const baseFormUrl = "https://docs.google.com/forms/d/e/1FAIpQLScVs6stu2MLP5juaZ4iOUlE8U2NyzKJWlCisrIC0m67vRyAFA/viewform?usp=pp_url";
        const txidEntry = "&entry.1191411884=" + encodeURIComponent(txid);
        
        document.getElementById('upload-link').href = baseFormUrl + txidEntry;"""

content = content.replace(old_script, new_script)

with open('success.html', 'w') as f:
    f.write(content)
