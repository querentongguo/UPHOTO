import re

with open('index.html', 'r') as f:
    content = f.read()

# Wrap guidelines and upload area in a flex container
old_html = """<div class="guidelines-grid">
<div class="guideline-card good">"""

new_html = """<div class="step-1-layout">
<div class="upload-area" id="drop-zone">
<div class="upload-icon" data-i18n="index_div_32">☁️</div>
<p data-i18n="upload_drag">Drag &amp; Drop your photo here</p>
<span data-i18n="upload_or">or</span><br/>
<button class="cta-button" data-i18n="upload_browse" id="browse-btn">Browse Files</button>
<input accept="image/*" hidden="" id="file-input" type="file"/>
</div>
<div class="guidelines-grid">
<div class="guideline-card good">"""

content = content.replace(old_html, new_html)

# Remove the old upload area since we moved it above
upload_area_regex = r'</div>\n<div class="upload-area" id="drop-zone">.*?type="file"/>\n</div>'
content = re.sub(upload_area_regex, "</div>\n</div>", content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

