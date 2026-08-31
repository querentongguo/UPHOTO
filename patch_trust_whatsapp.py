import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add Trust Badges under paypal-wrapper
trust_badges = """<div class="paypal-wrapper" id="paypal-button-container-wizard">
<!-- PayPal buttons will render here -->
<p class="paypal-placeholder" data-i18n="index_p_3">PayPal integration ready for API keys.</p>
</div>
<div class="trust-badges" style="text-align: center; margin-top: 15px; padding-bottom: 10px;">
    <div style="font-size: 0.85rem; color: #a1a1aa; margin-bottom: 10px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
        <span>🔒 <span data-i18n="trust_ssl">SSL Secure Checkout</span></span>
        <span>🛡️ <span data-i18n="trust_guarantee">100% Satisfaction Guarantee</span></span>
    </div>
    <div style="display: flex; justify-content: center; gap: 8px; opacity: 0.8;">
        <!-- Card Icons using simple CSS/Emojis or SVGs -->
        <span style="background: #fff; padding: 2px 6px; border-radius: 4px; color: #1434CB; font-weight: bold; font-size: 0.8rem; font-family: sans-serif;">VISA</span>
        <span style="background: #fff; padding: 2px 6px; border-radius: 4px; color: #EB001B; font-weight: bold; font-size: 0.8rem; font-family: sans-serif;">MasterCard</span>
        <span style="background: #fff; padding: 2px 6px; border-radius: 4px; color: #003087; font-weight: bold; font-size: 0.8rem; font-family: sans-serif;">PayPal</span>
    </div>
</div>"""

content = re.sub(
    r'<div class="paypal-wrapper" id="paypal-button-container-wizard">.*?</div>',
    trust_badges,
    content,
    flags=re.DOTALL
)

# 2. Add WhatsApp floating button before </body>
whatsapp_btn = """
<!-- WhatsApp Floating Button -->
<a href="https://wa.me/1234567890" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 32 32" width="32" height="32"><path d="M16.05 2.5A13.45 13.45 0 0 0 2.6 15.95c0 2.38.63 4.7 1.8 6.74L2 29.5l6.98-2.32a13.43 13.43 0 0 0 7.07 2.01h.01a13.45 13.45 0 0 0 13.44-13.44A13.45 13.45 0 0 0 16.05 2.5zm0 24.64a11.19 11.19 0 0 1-5.7-1.56l-.41-.24-4.24 1.41 1.13-4.13-.27-.42A11.16 11.16 0 0 1 4.86 15.95a11.2 11.2 0 0 1 11.2-11.2 11.2 11.2 0 0 1 11.19 11.2 11.2 11.2 0 0 1-11.2 11.19zm6.15-8.4c-.34-.17-2-.99-2.31-1.1s-.54-.17-.76.17-.87 1.1-.1 1.33c-.2.23-.46.34-.84.15a9.23 9.23 0 0 1-2.73-1.68 10.2 10.2 0 0 1-1.89-2.36c-.17-.3-.02-.46.15-.63.15-.15.34-.39.5-.59.17-.2.23-.33.34-.56.11-.23.05-.43-.03-.59-.1-.17-.77-1.84-1.05-2.52-.27-.66-.55-.57-.76-.58-.2-.01-.43-.01-.66-.01s-.6.08-.91.42c-.31.33-1.2 1.17-1.2 2.85s1.23 3.3 1.4 3.53c.17.23 2.41 3.68 5.84 5.16 2.37.99 3.26 1.07 4.38.9.91-.14 2-.82 2.28-1.61.28-.79.28-1.47.2-1.61-.11-.18-.4-.28-.73-.45z" fill="#fff"></path></svg>
</a>

<style>
.whatsapp-float {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #25d366;
    color: #fff;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 10px rgba(37, 211, 102, 0.4);
    z-index: 1000;
    transition: transform 0.3s ease;
}
.whatsapp-float:hover {
    transform: scale(1.1);
}
</style>
"""

content = content.replace('</body>', whatsapp_btn + '\n</body>')

with open('index.html', 'w') as f:
    f.write(content)
