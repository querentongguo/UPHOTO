with open('script.js', 'r') as f:
    content = f.read()

import re
# 1. Remove the old PayPal Integration block entirely
paypal_block_regex = r"// PayPal Integration with Backend.*?}\n\n?}\);\n?$"
content = re.sub(paypal_block_regex, "});\n", content, flags=re.DOTALL)

# 2. Inject the function definition right before the final `});`
paypal_func = """
    let paypalRendered = false;
    function renderPayPal() {
        if (typeof paypal !== 'undefined' && !paypalRendered) {
            document.getElementById('paypal-button-container-wizard').innerHTML = '<p class="paypal-placeholder" data-i18n="index_p_3">' + (window.t ? window.t("index_p_3") : 'PayPal integration ready') + '</p>';
            paypal.Buttons({
                createOrder: function(data, actions) {
                    const emailInput = document.getElementById('customer-email');
                    if (!emailInput.value || !emailInput.value.includes('@')) {
                        document.getElementById('email-error').style.display = 'block';
                        alert(window.t ? window.t("error_email_required") : "Email required");
                        throw new Error("Invalid email");
                    }
                    document.getElementById('email-error').style.display = 'none';
                    
                    if (cartItems.length === 0) {
                        alert(window.t ? window.t("error_cart_empty") : "Cart empty");
                        throw new Error("Empty cart");
                    }

                    let subtotalUSD = 0;
                    cartItems.forEach(item => { subtotalUSD += getBasePrice(item.tier); });
                    let discountPercent = 0;
                    if (cartItems.length === 2) discountPercent = 0.20;
                    else if (cartItems.length === 3) discountPercent = 0.40;
                    else if (cartItems.length >= 4) discountPercent = 0.50;
                    const finalTotalUSD = subtotalUSD - (subtotalUSD * discountPercent);

                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: finalTotalUSD.toFixed(2)
                            },
                            description: `UPHOTO Restoration Service (${cartItems.length} photos)`
                        }]
                    });
                },
                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        const transactionId = details.id;
                        
                        document.getElementById('upload-wizard').style.display = 'none';
                        cartItems = [];
                        renderCart();
                        
                        alert(`✅ Payment Successful!\\n\\nYour Transaction ID is: ${transactionId}\\n\\nSince this is a secure checkout, please EMAIL your photos to orders@uphoto-studio.com and include your Transaction ID in the email subject.\\n\\nWe will begin restoration immediately upon receiving your email.`);
                    });
                },
                onError: function(err) {
                    console.error("PayPal Error:", err);
                }
            }).render('#paypal-button-container-wizard');
            paypalRendered = true;
        }
    }
"""
content = re.sub(r"\}\);\s*$", paypal_func + "\n});\n", content)

# 3. Modify updateWizardView to call renderPayPal()
old_view = """    function updateWizardView() {
        document.querySelectorAll('.wizard-step').forEach(step => step.classList.remove('active'));
        document.querySelectorAll('.wizard-progress .step').forEach(indicator => indicator.classList.remove('active'));
        
        document.getElementById(`step-${currentStep}`).classList.add('active');
        for(let i=1; i<=currentStep; i++) {
            document.querySelector(`.wizard-progress .step[data-step="${i}"]`)?.classList.add('active');
        }
        
        if (currentStep === 2) {
            renderThumbnailsBar();
        } else if (currentStep === 3) {
            if(cropper && currentEditIndex >= 0) {
                // Save cropped state before leaving step 2
                cartItems[currentEditIndex].notes = document.getElementById('user-notes').value;
            }
            renderCart();
        }
    }"""

new_view = """    function updateWizardView() {
        document.querySelectorAll('.wizard-step').forEach(step => step.classList.remove('active'));
        document.querySelectorAll('.wizard-progress .step').forEach(indicator => indicator.classList.remove('active'));
        
        document.getElementById(`step-${currentStep}`).classList.add('active');
        for(let i=1; i<=currentStep; i++) {
            document.querySelector(`.wizard-progress .step[data-step="${i}"]`)?.classList.add('active');
        }
        
        if (currentStep === 2) {
            renderThumbnailsBar();
        } else if (currentStep === 3) {
            if(cropper && currentEditIndex >= 0) {
                // Save cropped state before leaving step 2
                cartItems[currentEditIndex].notes = document.getElementById('user-notes').value;
            }
            renderCart();
        } else if (currentStep === 4) {
            renderPayPal();
        }
    }"""

content = content.replace(old_view, new_view)

with open('script.js', 'w') as f:
    f.write(content)
