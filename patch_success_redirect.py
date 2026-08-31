import re

with open('script.js', 'r') as f:
    content = f.read()

old_approve = """                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        const transactionId = details.id;
                        
                        document.getElementById('upload-wizard').style.display = 'none';
                        cartItems = [];
                        renderCart();
                        
                        alert(`✅ Payment Successful!\\n\\nYour Transaction ID is: ${transactionId}\\n\\nSince this is a secure checkout, please EMAIL your photos to orders@uphoto-studio.com and include your Transaction ID in the email subject.\\n\\nWe will begin restoration immediately upon receiving your email.`);
                    });
                },"""

new_approve = """                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        const transactionId = details.id;
                        
                        // Clear cart
                        cartItems = [];
                        localStorage.removeItem('uphoto_cart');
                        
                        // Redirect to success page with transaction ID
                        window.location.href = "success.html?txid=" + transactionId;
                    });
                },"""

content = content.replace(old_approve, new_approve)

with open('script.js', 'w') as f:
    f.write(content)
