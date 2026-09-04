import os

# 1. New HTML
new_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BIGBROSTUDIO | Custom Pet Portraits</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <!-- PayPal SDK -->
    <script src="https://www.paypal.com/sdk/js?client-id=AT9bM0e8mHh6d_x830mU_YVvF4WcR-y47iL5XQnXZuF9Q2oJ2TzP6xGz6dE9Xp8M0e8mHh6d_x830mU_Y&currency=USD"></script>
</head>
<body>

    <!-- Header -->
    <header class="site-header">
        <div class="container header-container">
            <div class="logo">
                <span class="logo-text">BIGBROSTUDIO</span>
            </div>
            <nav class="main-nav">
                <a href="#how-it-works">How it Works</a>
                <a href="#reviews">Reviews</a>
                <a href="#order" class="btn-primary-small">Start Order</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container hero-container">
            <div class="hero-text">
                <div class="rating-badge">★★★★★ Over 10,000 Pets Transformed</div>
                <h1>Turn Your Pet into a Masterpiece</h1>
                <p>Upload a photo of your dog or cat, and our digital artisans will transform it into a stunning royal portrait, Disney-style cartoon, or classic watercolor.</p>
                <a href="#order" class="btn-primary-large">Create Your Portrait</a>
            </div>
            <div class="hero-visual">
                <img src="https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80" alt="Pet Portrait Example" class="hero-img">
                <div class="floating-badge">👑 Royal Renaissance</div>
            </div>
        </div>
    </section>

    <!-- How It Works -->
    <section id="how-it-works" class="how-it-works">
        <div class="container">
            <h2>How It Works</h2>
            <div class="steps-grid">
                <div class="step-card">
                    <div class="step-icon">📸</div>
                    <h3>1. Upload Photo</h3>
                    <p>Snap a cute photo of your pet from your phone and upload it securely.</p>
                </div>
                <div class="step-card">
                    <div class="step-icon">🎨</div>
                    <h3>2. Choose Style</h3>
                    <p>Pick from Royal, Cartoon, or Watercolor. Our AI artisans do the rest.</p>
                </div>
                <div class="step-card">
                    <div class="step-icon">💌</div>
                    <h3>3. Receive Art</h3>
                    <p>Get your high-res digital file via email in 24-48 hours. Ready to print!</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Order Section (The Wizard) -->
    <section id="order" class="order-section">
        <div class="container">
            <div class="order-box" id="upload-wizard">
                
                <!-- Wizard Progress -->
                <div class="wizard-progress">
                    <div class="step active" data-step="1">1. Photo</div>
                    <div class="step" data-step="2">2. Style</div>
                    <div class="step" data-step="3">3. Cart</div>
                    <div class="step" data-step="4">4. Pay</div>
                </div>

                <!-- STEP 1: UPLOAD -->
                <div class="wizard-step active" id="step-1">
                    <h2>Upload Your Pet's Photo</h2>
                    <p class="subtitle">Drop a clear photo of your pet here or click to browse.</p>
                    
                    <div class="drop-zone" id="drop-zone">
                        <div class="drop-icon">☁️</div>
                        <p>Drag & Drop your photo here</p>
                        <p class="or">or</p>
                        <button id="browse-btn" class="btn-secondary">Browse Files</button>
                        <input type="file" id="file-input" accept="image/jpeg, image/png, image/webp" style="display: none;">
                    </div>
                    
                    <div class="guidelines">
                        <h4>📸 Photo Guidelines</h4>
                        <div class="guide-grid">
                            <div class="guide-good">
                                <h5>✅ What works best:</h5>
                                <ul>
                                    <li>Clear, well-lit photos</li>
                                    <li>Pet's face is fully visible</li>
                                    <li>Taken at eye level</li>
                                </ul>
                            </div>
                            <div class="guide-bad">
                                <h5>❌ What to avoid:</h5>
                                <ul>
                                    <li>Blurry or dark photos</li>
                                    <li>Ears or head cut off</li>
                                    <li>Pet is too far away</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- STEP 2: EDIT & STYLE -->
                <div class="wizard-step" id="step-2">
                    <h2>Choose Your Art Style</h2>
                    
                    <div class="preview-container">
                        <img id="image-preview" src="" alt="Preview">
                    </div>

                    <div class="style-grid">
                        <label class="style-card">
                            <input type="radio" name="art_style" value="Royal Renaissance" checked>
                            <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=300&q=80" alt="Royal">
                            <div class="style-name">Royal</div>
                        </label>
                        <label class="style-card">
                            <input type="radio" name="art_style" value="Disney Cartoon">
                            <img src="https://images.unsplash.com/photo-1517849845537-4d257902454a?auto=format&fit=crop&w=300&q=80" alt="Cartoon">
                            <div class="style-name">Cartoon</div>
                        </label>
                        <label class="style-card">
                            <input type="radio" name="art_style" value="Classic Watercolor">
                            <img src="https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80" alt="Watercolor">
                            <div class="style-name">Watercolor</div>
                        </label>
                    </div>
                    
                    <div class="wizard-actions">
                        <button class="btn-outline prev-step">Back</button>
                        <button class="btn-primary next-step">Save & Next</button>
                    </div>
                </div>

                <!-- STEP 3: CART -->
                <div class="wizard-step" id="step-3">
                    <h2>Review Your Order</h2>
                    <div class="cart-container">
                        <table class="cart-table">
                            <thead>
                                <tr>
                                    <th>Item</th>
                                    <th>Price</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody id="cart-table-body">
                                <!-- JS inserts rows -->
                            </tbody>
                        </table>
                        <div class="cart-summary">
                            <div class="cart-total-row">
                                <span>Total:</span>
                                <span id="cart-total">$0.00</span>
                            </div>
                        </div>
                    </div>
                    <div class="wizard-actions">
                        <button class="btn-outline" onclick="document.getElementById('file-input').click()">Add Another Pet</button>
                        <button class="btn-primary next-step">Checkout</button>
                    </div>
                </div>

                <!-- STEP 4: PAYPAL -->
                <div class="wizard-step" id="step-4">
                    <h2>Secure Payment</h2>
                    <p class="subtitle">You are paying for a custom digital pet portrait service.</p>
                    
                    <div class="payment-container">
                        <div id="paypal-button-container"></div>
                    </div>
                    
                    <div class="wizard-actions">
                        <button class="btn-outline prev-step">Back to Cart</button>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Reviews Section -->
    <section id="reviews" class="reviews-section">
        <div class="container">
            <h2>Happy Pet Owners</h2>
            <div id="reviews-grid" class="reviews-grid">
                <!-- JS inserts reviews here -->
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <p>&copy; 2026 BIGBROSTUDIO. All rights reserved.</p>
            <div class="footer-links">
                <a href="terms.html">Terms of Service</a>
                <a href="privacy.html">Privacy Policy</a>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script src="i18n.js"></script>
</body>
</html>
"""

# 2. New CSS
new_css = """
:root {
    --bg-color: #FAFAFA;
    --text-main: #2D3436;
    --text-light: #636E72;
    --primary: #FF9F43;
    --primary-hover: #F39C12;
    --surface: #FFFFFF;
    --border: #DFE6E9;
    --font-main: 'Nunito', sans-serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-main); background: var(--bg-color); color: var(--text-main); line-height: 1.6; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

/* Buttons */
.btn-primary-large { display: inline-block; background: var(--primary); color: #fff; padding: 18px 40px; font-size: 1.2rem; font-weight: 800; border-radius: 50px; text-decoration: none; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 10px 20px rgba(255, 159, 67, 0.3); transition: all 0.3s; border: none; cursor: pointer; }
.btn-primary-large:hover { transform: translateY(-3px); box-shadow: 0 15px 25px rgba(255, 159, 67, 0.4); background: var(--primary-hover); }
.btn-primary-small { display: inline-block; background: var(--primary); color: #fff; padding: 10px 24px; font-weight: 800; border-radius: 30px; text-decoration: none; transition: all 0.3s; }
.btn-primary-small:hover { background: var(--primary-hover); transform: translateY(-2px); }
.btn-primary { background: var(--primary); color: white; border: none; padding: 14px 30px; font-size: 1rem; font-weight: 800; border-radius: 30px; cursor: pointer; transition: 0.3s; text-transform: uppercase; }
.btn-primary:hover { background: var(--primary-hover); transform: translateY(-2px); }
.btn-secondary { background: var(--text-main); color: white; border: none; padding: 12px 24px; font-weight: 700; border-radius: 30px; cursor: pointer; }
.btn-outline { background: transparent; border: 2px solid var(--border); color: var(--text-main); padding: 12px 24px; font-weight: 700; border-radius: 30px; cursor: pointer; }

/* Header */
.site-header { background: var(--surface); padding: 20px 0; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; }
.header-container { display: flex; justify-content: space-between; align-items: center; }
.logo-text { font-size: 1.8rem; font-weight: 900; letter-spacing: -1px; color: var(--text-main); }
.main-nav { display: flex; gap: 20px; align-items: center; }
.main-nav a { text-decoration: none; color: var(--text-main); font-weight: 700; }

/* Hero */
.hero { padding: 60px 0; }
.hero-container { display: flex; align-items: center; gap: 40px; flex-wrap: wrap; }
.hero-text { flex: 1; min-width: 300px; }
.rating-badge { color: var(--primary); font-weight: 800; margin-bottom: 15px; font-size: 1.1rem; }
.hero h1 { font-size: 4rem; font-weight: 900; line-height: 1.1; margin-bottom: 20px; }
.hero p { font-size: 1.2rem; color: var(--text-light); margin-bottom: 30px; }
.hero-visual { flex: 1; min-width: 300px; position: relative; text-align: center; }
.hero-img { width: 100%; max-width: 500px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); transform: rotate(2deg); }
.floating-badge { position: absolute; bottom: -20px; left: 10%; background: #fff; padding: 15px 25px; border-radius: 30px; font-weight: 800; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }

/* How it works */
.how-it-works { background: var(--surface); padding: 80px 0; text-align: center; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.how-it-works h2 { font-size: 2.5rem; font-weight: 900; margin-bottom: 50px; }
.steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; }
.step-card { padding: 20px; }
.step-icon { font-size: 3rem; margin-bottom: 20px; }
.step-card h3 { font-size: 1.5rem; font-weight: 800; margin-bottom: 10px; }
.step-card p { color: var(--text-light); }

/* Order Section */
.order-section { padding: 80px 0; background: #F4F6F8; }
.order-box { background: var(--surface); max-width: 800px; margin: 0 auto; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); padding: 40px; }

/* Wizard */
.wizard-progress { display: flex; justify-content: space-between; margin-bottom: 40px; border-bottom: 2px solid var(--border); padding-bottom: 20px; }
.wizard-progress .step { font-weight: 700; color: var(--text-light); opacity: 0.5; }
.wizard-progress .step.active { color: var(--primary); opacity: 1; }

.wizard-step { display: none; text-align: center; }
.wizard-step.active { display: block; animation: fadeIn 0.4s; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

.wizard-step h2 { font-size: 2rem; font-weight: 900; margin-bottom: 10px; }
.subtitle { color: var(--text-light); margin-bottom: 30px; }

/* Drop Zone */
.drop-zone { border: 3px dashed var(--border); padding: 50px 20px; border-radius: 20px; background: #FAFAFA; cursor: pointer; transition: 0.3s; margin-bottom: 30px; }
.drop-zone:hover { border-color: var(--primary); background: #FFF5EA; }
.drop-icon { font-size: 3rem; margin-bottom: 10px; }
.drop-zone p { font-weight: 700; margin-bottom: 15px; }

/* Guidelines */
.guide-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; text-align: left; background: #F8F9FA; padding: 20px; border-radius: 15px; margin-top: 20px; }
.guide-good h5 { color: #27AE60; font-size: 1.1rem; margin-bottom: 10px; }
.guide-bad h5 { color: #E74C3C; font-size: 1.1rem; margin-bottom: 10px; }
.guide-grid ul { list-style: none; color: var(--text-light); font-size: 0.95rem; }
.guide-grid li { margin-bottom: 8px; }

/* Styles Grid */
.style-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }
.style-card { display: block; cursor: pointer; border: 3px solid transparent; border-radius: 15px; padding: 10px; transition: 0.3s; position: relative; }
.style-card img { width: 100%; border-radius: 10px; aspect-ratio: 1/1; object-fit: cover; }
.style-card input { display: none; }
.style-name { font-weight: 800; margin-top: 10px; font-size: 1.2rem; }
.style-card:has(input:checked) { border-color: var(--primary); box-shadow: 0 10px 20px rgba(255, 159, 67, 0.2); transform: translateY(-5px); }
.style-card:has(input:checked)::after { content: '✓'; position: absolute; top: 20px; right: 20px; background: var(--primary); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; }

.preview-container { margin-bottom: 30px; }
.preview-container img { max-width: 100%; max-height: 400px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }

.wizard-actions { display: flex; justify-content: space-between; margin-top: 40px; border-top: 1px solid var(--border); padding-top: 20px; }

/* Cart */
.cart-table { width: 100%; text-align: left; border-collapse: collapse; margin-bottom: 20px; }
.cart-table th { border-bottom: 2px solid var(--border); padding: 15px 10px; color: var(--text-light); }
.cart-table td { border-bottom: 1px solid var(--border); padding: 15px 10px; vertical-align: middle; }
.remove-btn { background: #FFEAA7; color: #D63031; border: none; width: 30px; height: 30px; border-radius: 50%; cursor: pointer; font-weight: bold; }
.cart-total-row { font-size: 1.5rem; font-weight: 900; text-align: right; padding: 20px 10px; color: var(--primary); }

/* Reviews */
.reviews-section { padding: 80px 0; background: var(--surface); text-align: center; }
.reviews-section h2 { font-size: 2.5rem; font-weight: 900; margin-bottom: 50px; }
.reviews-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.review-card { text-align: left; padding: 30px; background: #F8F9FA; border-radius: 20px; }
.review-stars-wrapper { color: var(--primary); font-size: 1.2rem; margin-bottom: 15px; }

/* Footer */
.site-footer { background: var(--text-main); color: white; padding: 40px 0; text-align: center; }
.footer-links { margin-top: 20px; display: flex; justify-content: center; gap: 20px; }
.footer-links a { color: #B2BEC3; text-decoration: none; }

@media (max-width: 768px) {
    .hero h1 { font-size: 2.5rem; }
    .hero-container { flex-direction: column; text-align: center; }
    .hero-text { padding-right: 0; }
    .guide-grid { grid-template-columns: 1fr; }
    .floating-badge { display: none; }
}
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

