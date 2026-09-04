import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Google Fonts
fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
"""
html = html.replace('<head>', '<head>\n' + fonts)

# Revamp Hero Section
new_hero = """
        <div class="hero" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; max-width: 1200px; margin: 40px auto; padding: 0 20px; text-align: left;">
            <div class="hero-content" style="flex: 1; min-width: 300px; padding-right: 40px;">
                <h1 data-i18n="hero_h1" style="font-size: 3.5rem; font-weight: 900; line-height: 1.1; margin-bottom: 20px; color: var(--text-color);">Turn Your Pet into a Masterpiece</h1>
                <p data-i18n="hero_p" style="font-size: 1.2rem; color: #555; margin-bottom: 30px; line-height: 1.6;">Upload a photo of your dog or cat, and our digital artisans will transform it into a stunning royal portrait, Disney-style cartoon, or classic watercolor.</p>
                <div class="hero-buttons">
                    <button class="cta-button" onclick="document.getElementById('upload-wizard').scrollIntoView({behavior: 'smooth'})" data-i18n="hero_cta" style="font-size: 1.2rem; padding: 15px 40px; border-radius: 50px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 10px 20px rgba(255, 179, 71, 0.4);">Create Your Pet Portrait</button>
                </div>
                <div style="margin-top: 20px; display: flex; align-items: center; gap: 10px; font-weight: 700; color: #333;">
                    <div style="color: #FFB347; font-size: 1.2rem;">★★★★★</div>
                    <span>Over 10,000 Happy Pets</span>
                </div>
            </div>
            <div class="hero-image" style="flex: 1; min-width: 300px; text-align: center; position: relative;">
                <!-- Placeholder for dynamic before/after or cool product image -->
                <img src="https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80" alt="Pet Portrait Example" style="width: 100%; max-width: 500px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); transform: rotate(2deg);">
                <div style="position: absolute; bottom: -20px; left: 10%; background: white; padding: 15px 25px; border-radius: 30px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); font-weight: 800; color: #333; display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">👑</span> Royal Renaissance
                </div>
            </div>
        </div>
        
        <!-- How it works section -->
        <div class="how-it-works" style="background: #FFF; padding: 60px 20px; text-align: center; margin-top: 40px; border-top: 2px dashed #eee;">
            <h2 style="font-size: 2.5rem; font-weight: 900; margin-bottom: 40px; color: var(--text-color);">How It Works</h2>
            <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; max-width: 1000px; margin: 0 auto;">
                <div style="flex: 1; min-width: 250px;">
                    <div style="font-size: 3rem; margin-bottom: 15px;">📸</div>
                    <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">1. Upload Photo</h3>
                    <p style="color: #666; line-height: 1.5;">Snap a cute photo of your pet from your phone and upload it securely.</p>
                </div>
                <div style="flex: 1; min-width: 250px;">
                    <div style="font-size: 3rem; margin-bottom: 15px;">🎨</div>
                    <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">2. Choose Style</h3>
                    <p style="color: #666; line-height: 1.5;">Pick from Royal, Cartoon, or Watercolor. Our AI artisans do the rest.</p>
                </div>
                <div style="flex: 1; min-width: 250px;">
                    <div style="font-size: 3rem; margin-bottom: 15px;">💌</div>
                    <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">3. Receive Art</h3>
                    <p style="color: #666; line-height: 1.5;">Get your high-res digital file via email in 24-48 hours. Ready to print!</p>
                </div>
            </div>
        </div>
"""
html = re.sub(r'<div class="hero">.*?</div>', new_hero, html, flags=re.DOTALL)

# Revamp Style Selector in Step 2
new_styles = """
        <div class="style-selector-container" style="margin-top: 30px; text-align: center; background: #f9f9f9; padding: 20px; border-radius: 15px;">
            <h3 style="margin-bottom: 20px; color: var(--text-color); font-weight: 800; font-size: 1.5rem;">Select Your Pet's New Identity</h3>
            <div class="style-options" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; justify-content: center;">
                
                <label class="style-card modern-card">
                    <input type="radio" name="art_style" value="Royal Renaissance" checked style="display:none;">
                    <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=300&q=80" alt="Royal" style="width: 100%; border-radius: 10px; margin-bottom: 10px; aspect-ratio: 1/1; object-fit: cover;">
                    <div style="font-weight: 800; font-size: 1.1rem; color: #333;">Royal</div>
                    <div style="font-size: 0.9rem; color: #777;">Renaissance Classic</div>
                </label>

                <label class="style-card modern-card">
                    <input type="radio" name="art_style" value="Disney Cartoon" style="display:none;">
                    <img src="https://images.unsplash.com/photo-1517849845537-4d257902454a?auto=format&fit=crop&w=300&q=80" alt="Cartoon" style="width: 100%; border-radius: 10px; margin-bottom: 10px; aspect-ratio: 1/1; object-fit: cover;">
                    <div style="font-weight: 800; font-size: 1.1rem; color: #333;">Cartoon</div>
                    <div style="font-size: 0.9rem; color: #777;">Disney Inspired</div>
                </label>

                <label class="style-card modern-card">
                    <input type="radio" name="art_style" value="Classic Watercolor" style="display:none;">
                    <img src="https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80" alt="Watercolor" style="width: 100%; border-radius: 10px; margin-bottom: 10px; aspect-ratio: 1/1; object-fit: cover;">
                    <div style="font-weight: 800; font-size: 1.1rem; color: #333;">Watercolor</div>
                    <div style="font-size: 0.9rem; color: #777;">Elegant Splash</div>
                </label>

            </div>
            <style>
                .modern-card { cursor: pointer; border: 3px solid transparent; border-radius: 15px; padding: 10px; background: #fff; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
                .modern-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
                .modern-card:has(input:checked) { border-color: var(--primary-color) !important; box-shadow: 0 0 0 2px var(--primary-color), 0 10px 25px rgba(255, 179, 71, 0.3) !important; transform: translateY(-5px); }
            </style>
        </div>
"""
html = re.sub(r'<div class="style-selector-container".*?</div>\s*</div>\s*<style>.*?</style>\s*</div>', new_styles, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Overhaul styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_theme_vars = """
:root {
    --bg-color: #FAFAFA;
    --text-color: #2D3436;
    --text-muted: #636E72;
    --primary-color: #FF9F43;
    --primary-hover: #F39C12;
    --border-color: #DFE6E9;
    --card-bg: #FFFFFF;
    --accent-color: #FF9F43;
    --header-bg: #FFFFFF;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Nunito', sans-serif;
}

nav {
    background: var(--header-bg);
    border-bottom: 1px solid var(--border-color);
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}

.logo-text {
    font-weight: 900;
    color: #2D3436;
    letter-spacing: -1px;
    font-size: 1.8rem;
}

.upload-wizard {
    background: var(--card-bg);
    border: none;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    border-radius: 24px;
}

.wizard-progress .step.active .step-icon {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.step-btn, .cta-button, .add-btn, .next-step, .prev-step {
    background: var(--primary-color);
    color: white;
    border: none;
    border-radius: 50px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 4px 15px rgba(255, 159, 67, 0.3);
    transition: all 0.3s ease;
}

.step-btn:hover, .cta-button:hover, .next-step:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 159, 67, 0.4);
}

.prev-step {
    background: #DFE6E9;
    color: #2D3436;
    box-shadow: none;
}
.prev-step:hover {
    background: #B2BEC3;
}

.drop-zone {
    border: 3px dashed var(--border-color);
    background: #F8F9FA;
    border-radius: 20px;
    transition: all 0.3s ease;
}
.drop-zone:hover {
    border-color: var(--primary-color);
    background: #FFF5EA;
}

.image-preview-container {
    border: none;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-radius: 20px;
    overflow: hidden;
}

.review-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    box-shadow: 0 5px 15px rgba(0,0,0,0.02);
    border-radius: 16px;
}

.review-stars {
    color: #FF9F43;
}

footer {
    background: #2D3436;
    color: #FFF;
    border-top: none;
}
"""

css = re.sub(r':root\s*\{.*?(?=body\s*\{)', new_theme_vars, css, flags=re.DOTALL)
# The above regex might be tricky, let's just prepend the new theme and let CSS cascade handle the overrides, 
# or completely replace the root and body.
