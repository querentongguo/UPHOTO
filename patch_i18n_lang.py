import re

with open('i18n.js', 'r') as f:
    content = f.read()

old_init = """// Initialize language from localStorage or default to zh-CN
document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('uphoto_lang') || 'zh-CN';
    setLanguage(savedLang);"""

new_init = """// Initialize language from localStorage or auto-detect from browser
document.addEventListener('DOMContentLoaded', () => {
    let targetLang = localStorage.getItem('uphoto_lang');
    
    // Auto-detect browser language if not set manually
    if (!targetLang) {
        const browserLang = navigator.language || navigator.userLanguage; // e.g. "en-US", "zh-CN"
        
        // Map browser language to our supported languages
        if (browserLang.startsWith('zh')) {
            if (browserLang.includes('TW') || browserLang.includes('HK') || browserLang.includes('MO') || browserLang.includes('Hant')) {
                targetLang = 'zh-TW';
            } else {
                targetLang = 'zh-CN';
            }
        } else if (browserLang.startsWith('es')) {
            targetLang = 'es';
        } else if (browserLang.startsWith('ja')) {
            targetLang = 'ja';
        } else if (browserLang.startsWith('de')) {
            targetLang = 'de';
        } else if (browserLang.startsWith('fr')) {
            targetLang = 'fr';
        } else if (browserLang.startsWith('ko')) {
            targetLang = 'ko';
        } else if (browserLang.startsWith('ru')) {
            targetLang = 'ru';
        } else {
            // Default to English for all other countries/languages
            targetLang = 'en';
        }
        
        // Ensure the language exists in our translations, fallback to 'en'
        if (!window.translations[targetLang]) {
            targetLang = 'en';
        }
    }

    setLanguage(targetLang);"""

content = content.replace(old_init, new_init)

with open('i18n.js', 'w') as f:
    f.write(content)

