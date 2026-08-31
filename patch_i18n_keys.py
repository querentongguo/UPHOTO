import re

with open('i18n.js', 'r') as f:
    content = f.read()

en_keys = """        "success_a_3": "Return to Homepage",
        "trust_ssl": "SSL Secure Checkout",
        "trust_guarantee": "100% Satisfaction Guarantee",
        "payment_success_redirect": "Payment Successful! You will now be redirected to upload your high-resolution photos.",
"""
content = content.replace('"success_a_3": "Return to Homepage",', en_keys)

zh_keys = """        "success_a_3": "返回首页",
        "trust_ssl": "SSL 银行级加密支付",
        "trust_guarantee": "100% 满意度保证，修坏包赔",
        "payment_success_redirect": "支付成功！现在为您跳转到原图上传页面。",
"""
content = content.replace('"success_a_3": "返回首页",', zh_keys)

with open('i18n.js', 'w') as f:
    f.write(content)
