
document.addEventListener('DOMContentLoaded', () => {
    
    /* ---------------------------------
       5. Reviews Module (Pagination)
    --------------------------------- */
    const reviewsContainer = document.getElementById('reviews-container');
    const paginationContainer = document.getElementById('reviews-pagination');
    let allReviews = [];
    let currentPage = 1;
    const REVIEWS_PER_PAGE = 20;

    async function fetchReviews() {
        if (!reviewsContainer) return;
        try {
            if (window.REVIEWS_DATA) {
                allReviews = JSON.parse(JSON.stringify(window.REVIEWS_DATA));
                renderReviewsPage(1);
            } else {
                console.warn('Could not load reviews.json');
            }
        } catch (e) {
            console.error('Error fetching reviews:', e);
        }
    }

    function createStars(rating) {
        let stars = '';
        for(let i=0; i<5; i++) {
            if (i < rating) stars += '★';
            else stars += '☆';
        }
        return `<div class="review-stars">${stars}</div>`;
    }

    function renderReviewsPage(page) {
        if (!reviewsContainer || allReviews.length === 0) return;
        
        currentPage = page;
        reviewsContainer.innerHTML = ''; // clear loading message
        
        const startIndex = (page - 1) * REVIEWS_PER_PAGE;
        const endIndex = Math.min(startIndex + REVIEWS_PER_PAGE, allReviews.length);
        
        const fragment = document.createDocumentFragment();
        
        // Get current target language from the switcher
        const currentLang = document.getElementById('lang-switcher')?.value || 'en';
        
        for (let i = startIndex; i < endIndex; i++) {
            const r = allReviews[i];
            
            // Get translated text from the dictionary (fallback to 'en' or string)
            let translatedText = r.text;
            if (typeof r.text === 'object') {
                translatedText = r.text[currentLang] || r.text['en'];
            }
            
            const div = document.createElement('div');
            div.className = 'review-card';
            div.innerHTML = `
                <div class="review-header">
                    <div class="review-stars-wrapper">${createStars(r.rating)}</div>
                    <div class="review-verified"><span class="verified-icon">✔</span> <span data-i18n="review_verified">Verified Client</span></div>
                </div>
                <div class="review-text">"${translatedText}"</div>
                <div class="review-meta">
                    <span class="review-name">${r.name}</span>
                    <span class="review-date">${r.date}</span>
                </div>
            `;
            fragment.appendChild(div);
        }
        
        reviewsContainer.appendChild(fragment);
        renderPaginationControls();
    }

    function renderPaginationControls() {
        if (!paginationContainer) return;
        
        paginationContainer.innerHTML = '';
        const totalPages = Math.ceil(allReviews.length / REVIEWS_PER_PAGE);
        if (totalPages <= 1) return;

        // Previous button
        const prevBtn = document.createElement('button');
        prevBtn.className = `page-btn ${currentPage === 1 ? 'disabled' : ''}`;
        prevBtn.innerText = '‹';
        prevBtn.onclick = () => { if (currentPage > 1) renderReviewsPage(currentPage - 1); };
        paginationContainer.appendChild(prevBtn);

        // Page numbers
        let startPage = Math.max(1, currentPage - 2);
        let endPage = Math.min(totalPages, currentPage + 2);
        
        if (startPage > 1) {
            const btn = document.createElement('button');
            btn.className = 'page-btn';
            btn.innerText = '1';
            btn.onclick = () => renderReviewsPage(1);
            paginationContainer.appendChild(btn);
            if (startPage > 2) {
                const ellipsis = document.createElement('span');
                ellipsis.className = 'page-ellipsis';
                ellipsis.innerText = '...';
                paginationContainer.appendChild(ellipsis);
            }
        }

        for (let i = startPage; i <= endPage; i++) {
            const btn = document.createElement('button');
            btn.className = `page-btn ${i === currentPage ? 'active' : ''}`;
            btn.innerText = i;
            btn.onclick = () => renderReviewsPage(i);
            paginationContainer.appendChild(btn);
        }

        if (endPage < totalPages) {
            if (endPage < totalPages - 1) {
                const ellipsis = document.createElement('span');
                ellipsis.className = 'page-ellipsis';
                ellipsis.innerText = '...';
                paginationContainer.appendChild(ellipsis);
            }
            const btn = document.createElement('button');
            btn.className = 'page-btn';
            btn.innerText = totalPages;
            btn.onclick = () => renderReviewsPage(totalPages);
            paginationContainer.appendChild(btn);
        }

        // Next button
        const nextBtn = document.createElement('button');
        nextBtn.className = `page-btn ${currentPage === totalPages ? 'disabled' : ''}`;
        nextBtn.innerText = '›';
        nextBtn.onclick = () => { if (currentPage < totalPages) renderReviewsPage(currentPage + 1); };
        paginationContainer.appendChild(nextBtn);
    }

    if (paginationContainer) {
        fetchReviews(); // Initial load
    }
});
document.addEventListener('DOMContentLoaded', () => {
    // 1. Before/After Slider Logic
    const slider = document.getElementById('hero-slider');
    if (slider) {
        let isDown = false;
        const handle = slider.querySelector('.slider-handle');
        const beforeImg = slider.querySelector('.slider-image-before');
        let autoSlideInterval;
        let slideDirection = 1; // 1 for right, -1 for left
        let currentPercent = 50;

        function startAutoSlide() {
            if (autoSlideInterval) clearInterval(autoSlideInterval);
            autoSlideInterval = setInterval(() => {
                currentPercent += 0.15 * slideDirection;
                if (currentPercent >= 85) slideDirection = -1;
                if (currentPercent <= 15) slideDirection = 1;
                
                handle.style.left = currentPercent + '%';
                beforeImg.style.clipPath = `polygon(0 0, ${currentPercent}% 0, ${currentPercent}% 100%, 0 100%)`;
            }, 25); // smooth animation
        }

        function stopAutoSlide() {
            if (autoSlideInterval) {
                clearInterval(autoSlideInterval);
                autoSlideInterval = null;
            }
        }

        // Start auto-slide on load
        startAutoSlide();
        
        slider.addEventListener('mouseenter', stopAutoSlide);
        slider.addEventListener('mouseleave', () => {
            isDown = false;
            slider.classList.remove('active');
            startAutoSlide();
        });

        slider.addEventListener('mousedown', (e) => {
            isDown = true;
            slider.classList.add('active');
            stopAutoSlide();
        });
        
        slider.addEventListener('mouseup', () => {
            isDown = false;
            slider.classList.remove('active');
        });
        
        slider.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const rect = slider.getBoundingClientRect();
            let x = e.pageX - rect.left - window.scrollX;
            if (x < 0) x = 0;
            if (x > rect.width) x = rect.width;
            
            const percent = (x / rect.width) * 100;
            currentPercent = percent;
            handle.style.left = percent + '%';
            beforeImg.style.clipPath = `polygon(0 0, ${percent}% 0, ${percent}% 100%, 0 100%)`;
        });

        // Touch support
        slider.addEventListener('touchstart', () => {
            isDown = true;
            stopAutoSlide();
        });
        slider.addEventListener('touchend', () => {
            isDown = false;
            startAutoSlide();
        });
        slider.addEventListener('touchmove', (e) => {
            if (!isDown) return;
            const rect = slider.getBoundingClientRect();
            let x = e.touches[0].pageX - rect.left - window.scrollX;
            if (x < 0) x = 0;
            if (x > rect.width) x = rect.width;
            
            const percent = (x / rect.width) * 100;
            currentPercent = percent;
            handle.style.left = percent + '%';
            beforeImg.style.clipPath = `polygon(0 0, ${percent}% 0, ${percent}% 100%, 0 100%)`;
        });
    }

    // 2. Thumbnail Gallery Logic
    const thumbnails = document.querySelectorAll('.gallery-thumbnails .thumbnail');
    if (thumbnails.length > 0) {
        thumbnails.forEach(thumb => {
            thumb.addEventListener('click', function() {
                // Remove active class from all
                thumbnails.forEach(t => t.classList.remove('active'));
                this.classList.add('active');

                // Get images
                const beforeSrc = this.getAttribute('data-before');
                const afterSrc = this.getAttribute('data-after');
                const targetSelector = this.parentElement.getAttribute('data-target');
                const targetSlider = document.querySelector(targetSelector);

                if (targetSlider && beforeSrc && afterSrc) {
                    const imgBefore = targetSlider.querySelector('.slider-image-before img');
                    const imgAfter = targetSlider.querySelector('.slider-image-after img');
                    if (imgBefore) imgBefore.src = beforeSrc;
                    if (imgAfter) imgAfter.src = afterSrc;
                }
            });
        });
    }

    // 3. Header Scroll Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
});

    // Marquee logic
    const wrapperTop = document.getElementById('marquee-latest');
    const wrapperBottom = document.getElementById('marquee-historical');
    
    if (wrapperTop && wrapperBottom) {
        async function fetchMarqueeReviews() {
            try {
                if (window.REVIEWS_DATA) {
                    let allR = JSON.parse(JSON.stringify(window.REVIEWS_DATA));
                    
                    // Shuffle the array so that every page load shows different reviews
                    // This utilizes the full database of thousands of reviews while avoiding browser DOM width limits.
                    for (let i = allR.length - 1; i > 0; i--) {
                        const j = Math.floor(Math.random() * (i + 1));
                        [allR[i], allR[j]] = [allR[j], allR[i]];
                    }
                    
                    // Enforce uniqueness so identical texts do not display on the same page
                    const uniqueReviews = [];
                    const seenTexts = new Set();
                    for (const r of allR) {
                        // Use text_id if available, otherwise fallback to English text as unique key
                        const key = typeof r.text_id !== 'undefined' ? r.text_id : (typeof r.text === 'object' ? r.text['en'] : r.text);
                        if (!seenTexts.has(key)) {
                            seenTexts.add(key);
                            uniqueReviews.push(r);
                        }
                    }
                    
                    // Limit to 50 reviews per row (since we have exactly 100 unique text bases)
                    // (50 cards * ~380px * 2 tracks = ~38,000px wrapper width, which is safe from 65k px limit)
                    const maxPerRow = 50;
                    const topReviews = uniqueReviews.slice(0, maxPerRow);
                    const bottomReviews = uniqueReviews.slice(maxPerRow, maxPerRow * 2);
                    
                    renderMarquee(topReviews, bottomReviews);
                }
            } catch(e) {}
        }
        
        function renderMarquee(topReviews, bottomReviews) {
            const currentLang = document.getElementById('lang-switcher')?.value || 'en';
            
            function getRandomTime(lang) {
                const times = {
                    'zh-CN': ['2分钟前', '5分钟前', '1小时前', '3小时前', '昨天', '刚刚', '半小时前'],
                    'zh-TW': ['2分鐘前', '5分鐘前', '1小時前', '3小時前', '昨天', '剛剛', '半小時前'],
                    'en': ['2 mins ago', '5 mins ago', '1 hour ago', '3 hours ago', 'Yesterday', 'Just now', 'Half an hour ago'],
                    'de': ['Vor 2 Minuten', 'Vor 5 Minuten', 'Vor 1 Stunde', 'Vor 3 Stunden', 'Gestern', 'Gerade eben', 'Vor einer halben Stunde'],
                    'fr': ['Il y a 2 min', 'Il y a 5 min', 'Il y a 1 heure', 'Il y a 3 heures', 'Hier', 'À l\'instant', 'Il y a une demi-heure'],
                    'ja': ['2分前', '5分前', '1時間前', '3時間前', '昨日', 'たった今', '30分前'],
                    'ko': ['2분 전', '5분 전', '1시간 전', '3시간 전', '어제', '방금 전', '30분 전'],
                    'ru': ['2 минуты назад', '5 минут назад', '1 час назад', '3 часа назад', 'Вчера', 'Только что', 'Полчаса назад']
                };
                const langTimes = times[lang] || times['en'];
                return langTimes[Math.floor(Math.random() * langTimes.length)];
            }
            
            function getRandomHistoricalTime(lang) {
                const currentYear = new Date().getFullYear();
                const minYear = 2013;
                const maxYear = currentYear - 1;
                const safeMax = Math.max(minYear, maxYear);
                const randomYear = Math.floor(Math.random() * (safeMax - minYear + 1)) + minYear;
                
                const formats = {
                    'zh-CN': `${randomYear}年`,
                    'zh-TW': `${randomYear}年`,
                    'en': `In ${randomYear}`,
                    'de': `Im Jahr ${randomYear}`,
                    'fr': `En ${randomYear}`,
                    'ja': `${randomYear}年`,
                    'ko': `${randomYear}년`,
                    'ru': `В ${randomYear} году`
                };
                return formats[lang] || formats['en'];
            }
            
            const latestTextMap = {
                'zh-CN': '最新',
                'zh-TW': '最新',
                'en': 'Latest',
                'de': 'Neueste',
                'fr': 'Dernier',
                'ja': '最新',
                'ko': '최신',
                'ru': 'Последние'
            };
            const historyTextMap = {
                'zh-CN': '历史',
                'zh-TW': '歷史',
                'en': 'Historical',
                'de': 'Historisch',
                'fr': 'Historique',
                'ja': '歴史',
                'ko': '과거',
                'ru': 'Исторические'
            };
            const latestText = latestTextMap[currentLang] || latestTextMap['en'];
            const historyText = historyTextMap[currentLang] || historyTextMap['en'];

            function buildHtml(reviewsToRender, isLatest) {
                let html = '';
                reviewsToRender.forEach(r => {
                    let translatedText = r.text;
                    if (typeof r.text === 'object') {
                        translatedText = r.text[currentLang] || r.text['en'];
                    }
                    
                    let stars = '';
                    for(let i=0; i<5; i++) {
                        stars += i < r.rating ? '★' : '☆';
                    }
                    
                    const randomTimeStr = isLatest ? getRandomTime(currentLang) : getRandomHistoricalTime(currentLang);
                    const tagText = isLatest ? latestText : historyText;
                    
                    html += `
                        <div class="review-card">
                            <div class="review-header">
                                <div class="review-stars-wrapper"><div class="review-stars">${stars}</div></div>
                                <div class="review-verified"><span class="verified-icon">✔</span> <span data-i18n="review_verified">Verified Client</span></div>
                            </div>
                            <div class="review-text">"${translatedText}"</div>
                            <div class="review-meta" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                                <span class="review-name">${tagText}</span>
                                <span class="review-date" style="font-size: 0.85em; opacity: 0.8;">${randomTimeStr}</span>
                            </div>
                        </div>
                    `;
                });
                return html;
            }

            const htmlTop = buildHtml(topReviews, true);
            const htmlBottom = buildHtml(bottomReviews, false);
            
            const trackTop1 = document.getElementById('marquee-track-latest-1');
            const trackTop2 = document.getElementById('marquee-track-latest-2');
            const wrapperTop = document.getElementById('marquee-latest');
            if (trackTop1 && trackTop2 && wrapperTop) {
                trackTop1.innerHTML = htmlTop;
                trackTop2.innerHTML = htmlTop;
                wrapperTop.style.animationDuration = (topReviews.length * 5) + 's'; // Dynamic duration for smooth constant speed
            }
            
            const trackBottom1 = document.getElementById('marquee-track-history-1');
            const trackBottom2 = document.getElementById('marquee-track-history-2');
            const wrapperBottom = document.getElementById('marquee-historical');
            if (trackBottom1 && trackBottom2 && wrapperBottom) {
                trackBottom1.innerHTML = htmlBottom;
                trackBottom2.innerHTML = htmlBottom;
                wrapperBottom.style.animationDuration = (bottomReviews.length * 5) + 's'; // Dynamic duration for smooth constant speed
            }
            
            // Re-apply translations for verified text
            if(typeof setLanguage === 'function') {
                setLanguage(currentLang);
            }
        }
        
        fetchMarqueeReviews();
        
        // Listen to language switcher for marquee updates
        const langSwitcher = document.getElementById('lang-switcher');
        if (langSwitcher) {
            langSwitcher.addEventListener('change', () => {
                fetchMarqueeReviews();
            });
        }
    }

document.addEventListener('DOMContentLoaded', () => {
    const wizardModal = document.getElementById('upload-wizard');
    const closeWizardBtn = document.querySelector('.close-wizard');
    let currentStep = 1;
    let cartItems = [];
    let currentEditIndex = -1;
    let cropper = null;

    const TIER_PRICES = {
        light: 19,
        medium: 39,
        severe: 79
    };

    window.t = function(key, params={}) {
        const lang = document.documentElement.lang || document.getElementById('lang-switcher')?.value || 'en';
        let text = window.translations[lang]?.[key] || window.translations['en']?.[key] || key;
        for (const [k, v] of Object.entries(params)) {
            text = text.replace(`{${k}}`, v);
        }
        return text;
    };

    function getBasePrice(tier) {
        return TIER_PRICES[tier] || 39;
    }

    // Open wizard on "Order Now" or "Start Restoration" clicks
    document.querySelectorAll('.cta-button').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const text = btn.innerText.toLowerCase();
            if(text.includes('order') || text.includes('start') || text.includes('下单') || text.includes('开始') || text.includes('bestellen') || text.includes('commander')) {
                e.preventDefault();
                wizardModal.style.display = 'block';
                if (cartItems.length === 0) {
                    currentStep = 1;
                } else {
                    currentStep = 3; // Go straight to cart if items exist
                }
                updateWizardView();
                
                // Auto-select tier if clicked from a pricing card
                const card = btn.closest('.pricing-card');
                if(card && cartItems.length === 0) {
                    const title = card.querySelector('h3').innerText.toLowerCase();
                    let initialTier = 'medium';
                    if(title.includes('severe') || title.includes('重度')) initialTier = 'severe';
                    else if(title.includes('light') || title.includes('轻度')) initialTier = 'light';
                    // We will apply this tier to the first item added
                    window._pendingInitialTier = initialTier;
                }
            }
        });
    });

    closeWizardBtn.addEventListener('click', () => {
        wizardModal.style.display = 'none';
    });
    window.addEventListener('click', (e) => {
        if(e.target === wizardModal) wizardModal.style.display = 'none';
    });

    // Step Navigation
    function updateWizardView() {
        document.querySelectorAll('.wizard-step').forEach(step => step.classList.remove('active'));
        document.querySelectorAll('.wizard-progress .step').forEach(indicator => indicator.classList.remove('active'));
        
        document.getElementById(`step-${currentStep}`).classList.add('active');
        for(let i=1; i<=currentStep; i++) {
            document.querySelector(`.wizard-progress .step[data-step="${i}"]`)?.classList.add('active');
        }
        
        if (currentStep === 2) {
            renderThumbnailsBar();
        } else if (currentStep === 3) {
            
            renderCart();
        } else if (currentStep === 4) {
            renderPayPal();
        }
    }

    document.querySelectorAll('.next-step').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep === 3 && cartItems.length === 0) {
                alert(window.t("cart_empty"));
                return;
            }
            
            if (currentStep === 2) {
                const styleInput = document.querySelector('input[name="art_style"]:checked');
                if (styleInput && currentEditIndex >= 0) {
                    cartItems[currentEditIndex].style = styleInput.value;
                }
            }
            if (currentStep < 4) {
                currentStep++;
                updateWizardView();
            }
        });
    });

    document.querySelectorAll('.prev-step').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep > 1) {
                currentStep--;
                updateWizardView();
            }
        });
    });

    // File Upload & Preview (Step 1 -> Step 2)
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const browseBtn = document.getElementById('browse-btn');
    const imagePreview = document.getElementById('image-preview');

    browseBtn.addEventListener('click', (e) => {
        e.preventDefault();
        fileInput.click();
    });

    function handleFiles(files) {
        if (!files || files.length === 0) return;
        
        // Only take up to 10 - current length
        const availableSlots = 10 - cartItems.length;
        if (availableSlots <= 0) {
            alert(window.t("error_max_10_photos"));
            return;
        }

        const filesToProcess = Array.from(files).slice(0, availableSlots);
        
        filesToProcess.forEach(file => {
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const newItem = {
                        id: Date.now() + Math.random(),
                        file: file,
                        dataUrl: e.target.result,
                        tier: window._pendingInitialTier || 'medium',
                        notes: ''
                    };
                    cartItems.push(newItem);
                    window._pendingInitialTier = null; // Clear it

                    // If it's the first file uploaded in this batch, edit it
                    if (cartItems.length === 1 || filesToProcess.length === 1) {
                        editItem(cartItems.length - 1);
                    } else {
                        renderThumbnailsBar();
                    }
                };
                reader.readAsDataURL(file);
            }
        });
    }

    fileInput.addEventListener('change', (e) => {
        handleFiles(e.target.files);
        fileInput.value = ''; // Reset
    });

    dropZone.addEventListener('dragover', (e) => { e.preventDefault(); dropZone.style.borderColor = '#d4af37'; });
    dropZone.addEventListener('dragleave', (e) => { e.preventDefault(); dropZone.style.borderColor = 'rgba(255, 255, 255, 0.2)'; });
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = 'rgba(255, 255, 255, 0.2)';
        handleFiles(e.dataTransfer.files);
    });

    function editItem(index) {
        if (index < 0 || index >= cartItems.length) return;
        
        // Save previous item's notes if editing another
        if (currentEditIndex >= 0 && currentEditIndex !== index) {
            cartItems[currentEditIndex].notes = document.getElementById('user-notes').value;
        }

        currentEditIndex = index;
        const item = cartItems[index];
        
        imagePreview.src = item.dataUrl;

        if (item.style) {
            const radio = document.querySelector(`input[name="art_style"][value="${item.style}"]`);
            if (radio) radio.checked = true;
        } else {
            document.querySelector('input[name="art_style"][value="Royal Renaissance"]').checked = true;
        }

        document.getElementById('user-notes').value = item.notes;
        
        if (cropper) {
            cropper.destroy();
            cropper = null;
        }
        
        currentStep = 2;
        updateWizardView();
        
        cropper = new Cropper(imagePreview, {
            viewMode: 1,
            dragMode: 'move',
            autoCropArea: 1,
            restore: false,
            guides: true,
            center: true,
            highlight: false,
            cropBoxMovable: true,
            cropBoxResizable: true,
            toggleDragModeOnDblclick: false,
        });
    }

    function renderThumbnailsBar() {
        const container = document.getElementById('cart-thumbnails');
        if(!container) return;
        
        container.innerHTML = '';
        
        cartItems.forEach((item, idx) => {
            const thumb = document.createElement('div');
            thumb.className = 'thumb-slot' + (idx === currentEditIndex ? ' active-edit' : '');
            thumb.style.backgroundImage = `url(${item.dataUrl})`;
            
            const removeBtn = document.createElement('div');
            removeBtn.className = 'remove-btn';
            removeBtn.innerText = '×';
            removeBtn.onclick = (e) => {
                e.stopPropagation();
                removeItem(idx);
            };
            
            thumb.appendChild(removeBtn);
            thumb.onclick = () => editItem(idx);
            
            container.appendChild(thumb);
        });

        if (cartItems.length < 10) {
            const addBtn = document.createElement('div');
            addBtn.className = 'thumb-slot add-new';
            addBtn.id = 'btn-add-more';
            addBtn.title = 'Add Another Photo';
            addBtn.innerText = '+';
            addBtn.onclick = () => fileInput.click();
            container.appendChild(addBtn);
        }
    }

    function removeItem(index) {
        cartItems.splice(index, 1);
        if (cartItems.length === 0) {
            currentStep = 1;
            currentEditIndex = -1;
            updateWizardView();
        } else {
            if (currentEditIndex === index) {
                editItem(Math.max(0, index - 1));
            } else if (currentEditIndex > index) {
                currentEditIndex--;
                renderThumbnailsBar();
            } else {
                renderThumbnailsBar();
            }
        }
    }

    // Cropper Toolbar Actions
    document.getElementById('crop-rotate-left').addEventListener('click', (e) => {
        e.preventDefault();
        if(cropper) cropper.rotate(-90);
    });
    
    document.getElementById('crop-rotate-right').addEventListener('click', (e) => {
        e.preventDefault();
        if(cropper) cropper.rotate(90);
    });
    
    document.getElementById('crop-reset').addEventListener('click', (e) => {
        e.preventDefault();
        if(cropper) cropper.reset();
    });

    // Cart / Step 3 Rendering
    function renderCart() {
        const container = document.getElementById('cart-items-container');
        if(!container) return;
        container.innerHTML = '';

        if(cartItems.length === 0) {
            container.innerHTML = `<div style="padding: 20px; text-align: center;">${window.t("cart_empty")}</div>`;
            updateCartTotals();
            return;
        }

        cartItems.forEach((item, idx) => {
            const row = document.createElement('div');
            row.className = 'cart-item';
            
            // Tier Dropdown
            const selectHtml = `
                <select class="tier-select" data-index="${idx}">
                    <option value="light" ${item.tier === 'light' ? 'selected' : ''}>${window.t("pricing_light_title")}</option>
                    <option value="medium" ${item.tier === 'medium' ? 'selected' : ''}>${window.t("pricing_med_title")}</option>
                    <option value="severe" ${item.tier === 'severe' ? 'selected' : ''}>${window.t("pricing_severe_title")}</option>
                </select>
            `;

            row.innerHTML = `
                <div class="col-photo"><img src="${item.dataUrl}" alt="Thumb"></div>
                <div class="col-tier">${selectHtml}</div>
                <div class="col-price" id="price-idx-${idx}">${window.formatPrice ? window.formatPrice(getBasePrice(item.tier)) : '$' + getBasePrice(item.tier)}</div>
                <div class="col-action"><button class="remove-item-btn" data-index="${idx}">×</button></div>
            `;
            container.appendChild(row);
        });

        // Attach listeners
        container.querySelectorAll('.tier-select').forEach(sel => {
            sel.addEventListener('change', (e) => {
                const idx = e.target.getAttribute('data-index');
                cartItems[idx].tier = e.target.value;
                document.getElementById(`price-idx-${idx}`).innerText = window.formatPrice ? window.formatPrice(getBasePrice(e.target.value)) : '$' + getBasePrice(e.target.value);
                updateCartTotals();
            });
        });

        container.querySelectorAll('.remove-item-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const idx = e.target.getAttribute('data-index');
                cartItems.splice(idx, 1);
                renderCart();
            });
        });

        updateCartTotals();
    }

    function updateCartTotals() {
        let subtotalUSD = 0;
        cartItems.forEach(item => {
            subtotalUSD += getBasePrice(item.tier);
        });

        let discountPercent = 0;
        if (cartItems.length === 2) discountPercent = 0.20;
        else if (cartItems.length === 3) discountPercent = 0.40;
        else if (cartItems.length >= 4) discountPercent = 0.50;

        const discountUSD = subtotalUSD * discountPercent;
        const totalUSD = subtotalUSD - discountUSD;

        const subEl = document.getElementById('cart-subtotal');
        const discEl = document.getElementById('cart-discount-amt');
        const totalEl = document.getElementById('cart-final-total');
        const banner = document.getElementById('discount-banner');

        if(window.formatPrice) {
            subEl.innerText = window.formatPrice(subtotalUSD);
            discEl.innerText = '-' + window.formatPrice(discountUSD);
            totalEl.innerText = window.formatPrice(totalUSD);
        } else {
            subEl.innerText = '$' + subtotalUSD;
            discEl.innerText = '-$' + discountUSD.toFixed(0);
            totalEl.innerText = '$' + totalUSD.toFixed(0);
        }

        if (cartItems.length === 0) {
            banner.innerText = window.t("cart_savings_0");
            banner.style.display = 'none';
        } else if (cartItems.length === 1) {
            banner.innerText = window.t("cart_savings_0");
            banner.style.display = 'block';
        } else {
            banner.style.display = 'block';
            let formattedSavings = window.formatPrice ? window.formatPrice(discountUSD) : '$' + discountUSD.toFixed(0);
            banner.innerText = window.t("cart_savings", { savings: formattedSavings });
        }
    }

    
    // Listen for language changes to update cart prices and strings dynamically
    window.addEventListener('languageChanged', () => {
        if (currentStep === 3) {
            renderCart();
        }
    });

    
    let paypalRendered = false;
    function renderPayPal() {
        if (typeof paypal !== 'undefined' && !paypalRendered) {
            document.getElementById('paypal-button-container-wizard').innerHTML = '<p class="paypal-placeholder" data-i18n="index_p_3">' + (window.t ? window.t("index_p_3") : 'PayPal integration ready') + '</p>';
            paypal.Buttons({
                createOrder: function(data, actions) {

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
                            description: `BIGBROSTUDIO Pet Art: ${cartItems.map(i => i.style).join(', ')}`
                        }]
                    });
                },
                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        const transactionId = details.id;
                        
                        document.getElementById('upload-wizard').style.display = 'none';
                        cartItems = [];
                        renderCart();
                        
                        window.location.href = "success.html?txid=" + transactionId;
                    });
                },
                onError: function(err) {
                    console.error("PayPal Error:", err);
                }
            }).render('#paypal-button-container-wizard');
            paypalRendered = true;
        }
    }

});
