console.log("ReviewCred Content Script v2.2.0 Loaded!");
console.log(window.location.href);

type rev = {
    title: string;
    body: string;
    rating: string;
}

const extractedReviews: rev[] = [];

function injectStyles() {
    if (document.getElementById('review-cred-styles')) return;

    const styleEl = document.createElement('style');
    styleEl.id = 'review-cred-styles';
    styleEl.textContent = `
      .review-cred-badge-container {
        position: relative;
        display: block !important;
        margin-bottom: 10px !important;
        margin-top: 6px !important;
        z-index: 9 !important;
        clear: both !important;
      }
      
      .review-cred-badge {
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
        background: #ffffff !important;
        border: 1.5px solid #E5E7EB !important;
        border-radius: 9999px !important;
        padding: 6px 14px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: help !important;
        user-select: none !important;
      }

      .review-cred-badge:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04) !important;
      }

      .review-cred-indicator {
        width: 8px !important;
        height: 8px !important;
        border-radius: 50% !important;
        position: relative !important;
        display: inline-block !important;
      }

      .review-cred-indicator::after {
        content: '' !important;
        position: absolute !important;
        top: -3px !important;
        left: -3px !important;
        right: -3px !important;
        bottom: -3px !important;
        border-radius: 50% !important;
        border: 2px solid currentColor !important;
        opacity: 0.45 !important;
        animation: review-cred-ping 2s cubic-bezier(0, 0, 0.2, 1) infinite !important;
      }

      @keyframes review-cred-ping {
        75%, 100% {
          transform: scale(2.2) !important;
          opacity: 0 !important;
        }
      }

      /* Score-specific styles */
      .review-cred-score-high .review-cred-badge {
        border-color: #10B981 !important;
        background: #F0FDF4 !important;
      }
      .review-cred-score-high .review-cred-indicator {
        background-color: #10B981 !important;
        color: #10B981 !important;
      }
      .review-cred-score-high .review-cred-value {
        color: #065F46 !important;
      }
      .review-cred-score-high .review-cred-label {
        color: #047857 !important;
      }

      .review-cred-score-medium .review-cred-badge {
        border-color: #F59E0B !important;
        background: #FFFBEB !important;
      }
      .review-cred-score-medium .review-cred-indicator {
        background-color: #F59E0B !important;
        color: #F59E0B !important;
      }
      .review-cred-score-medium .review-cred-value {
        color: #92400E !important;
      }
      .review-cred-score-medium .review-cred-label {
        color: #B45309 !important;
      }

      .review-cred-score-low .review-cred-badge {
        border-color: #EF4444 !important;
        background: #FEF2F2 !important;
      }
      .review-cred-score-low .review-cred-indicator {
        background-color: #EF4444 !important;
        color: #EF4444 !important;
      }
      .review-cred-score-low .review-cred-value {
        color: #991B1B !important;
      }
      .review-cred-score-low .review-cred-label {
        color: #B91C1C !important;
      }

      .review-cred-label {
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
      }

      .review-cred-value {
        font-size: 13px !important;
        font-weight: 800 !important;
      }

      /* Tooltip styles */
      .review-cred-tooltip {
        visibility: hidden !important;
        opacity: 0 !important;
        position: absolute !important;
        bottom: 110% !important;
        left: 50% !important;
        transform: translateX(-50%) translateY(4px) !important;
        background: rgba(17, 24, 39, 0.96) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        color: #ffffff !important;
        padding: 14px !important;
        border-radius: 12px !important;
        width: 220px !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        font-size: 12px !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.15), 0 10px 10px -5px rgba(0, 0, 0, 0.1) !important;
        z-index: 10 !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        pointer-events: none !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
      }

      .review-cred-tooltip::after {
        content: '' !important;
        position: absolute !important;
        top: 100% !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        border-width: 6px !important;
        border-style: solid !important;
        border-color: rgba(17, 24, 39, 0.96) transparent transparent transparent !important;
      }

      .review-cred-badge-container:hover .review-cred-tooltip {
        visibility: visible !important;
        opacity: 1 !important;
        transform: translateX(-50%) translateY(0) !important;
      }

      .review-cred-tooltip-title {
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.15) !important;
        padding-bottom: 6px !important;
        margin-bottom: 8px !important;
        color: #38BDF8 !important;
        font-size: 10px !important;
      }

      .review-cred-tooltip-row {
        display: flex !important;
        justify-content: space-between !important;
        margin-bottom: 6px !important;
      }

      .review-cred-tooltip-row:last-child {
        margin-bottom: 0 !important;
      }

      .review-cred-tooltip-row span {
        color: #9CA3AF !important;
        font-size: 11px !important;
      }

      .review-cred-tooltip-row strong {
        color: #F3F4F6 !important;
        font-weight: 600 !important;
      }

      .review-cred-score-high .status-value {
        color: #34D399 !important;
      }
      .review-cred-score-medium .status-value {
        color: #FBBF24 !important;
      }
      .review-cred-score-low .status-value {
        color: #F87171 !important;
      }
    `;
    
    const target = document.head || document.documentElement;
    if (target) {
        target.appendChild(styleEl);
    }
}

function findReviews(): Element[] {
    const list: Element[] = [];
    const selectors = [
        '[data-hook="review"]',
        '.a-section.review',
        'div[id^="customer_review-"]',
        '.review'
    ];
    selectors.forEach(sel => {
        document.querySelectorAll(sel).forEach(el => {
            if (!list.includes(el)) {
                list.push(el);
            }
        });
    });
    return list;
}

function extractTitle(review: Element): string {
    const titleSpan = review.querySelector('[data-hook="review-title"] span') ||
                      review.querySelector('.review-title-content span') ||
                      review.querySelector('[data-hook="reviewTitle"]') ||
                      review.querySelector('.review-title');
    return titleSpan?.textContent?.trim() ?? "";
}

function extractBody(review: Element): string {
    const bodySpan = review.querySelector('[data-hook="review-body"] span') ||
                     review.querySelector('[data-hook="review-body"]') ||
                     review.querySelector('[data-hook="reviewText"]') ||
                     review.querySelector('.review-text-content span') ||
                     review.querySelector('.review-text-content') ||
                     review.querySelector('.reviewRichContentContainer');
    return bodySpan?.textContent?.trim() ?? "";
}

function extractRating(review: Element): string {
    const ratingEl = review.querySelector('[data-hook="review-star-rating"]') ||
                     review.querySelector('.review-rating') ||
                     review.querySelector('[data-hook="cmps-review-star-rating"]') ||
                     review.querySelector('.a-icon-star');
    return ratingEl?.textContent?.trim() ?? "";
}

function getDummyScore(text: string) {
    let hash = 0;
    const cleanText = text || "";
    for (let i = 0; i < cleanText.length; i++) {
        hash = cleanText.charCodeAt(i) + ((hash << 5) - hash);
    }
    const score = 55 + (Math.abs(hash) % 41); // score between 55 and 95
    
    // Deterministic metrics based on hash
    const sentiment = 60 + (Math.abs(hash >> 2) % 36);
    const profile = 50 + (Math.abs(hash >> 4) % 46);
    const pattern = 65 + (Math.abs(hash >> 6) % 31);
    
    return { score, sentiment, profile, pattern };
}

function injectDummyScore(review: Element, bodyText: string) {
    try {
        const bodyEl = review.querySelector('[data-hook="review-body"]') || 
                       review.querySelector('[data-hook="reviewText"]') ||
                       review.querySelector('.review-text-content') ||
                       review.querySelector('.reviewRichContentContainer');
        if (!bodyEl) return;

        // Check if we already injected it
        if (review.querySelector('.review-cred-badge-container')) return;

        const { score, sentiment, profile, pattern } = getDummyScore(bodyText);

        let scoreClass = 'review-cred-score-low';
        let statusText = 'Low Trust';
        if (score >= 80) {
            scoreClass = 'review-cred-score-high';
            statusText = 'Verified';
        } else if (score >= 65) {
            scoreClass = 'review-cred-score-medium';
            statusText = 'Caution';
        }

        // 1. Create and inject the beautiful badge above the review text
        const badgeContainer = document.createElement('div');
        badgeContainer.className = `review-cred-badge-container ${scoreClass}`;
        badgeContainer.innerHTML = `
          <div class="review-cred-badge">
            <span class="review-cred-indicator"></span>
            <span class="review-cred-label">ReviewCred Score</span>
            <span class="review-cred-value">${score}%</span>
          </div>
          <div class="review-cred-tooltip">
            <div class="review-cred-tooltip-title">Credibility Analysis</div>
            <div class="review-cred-tooltip-row">
              <span>Overall Status:</span>
              <strong class="status-value">${statusText}</strong>
            </div>
            <div class="review-cred-tooltip-row">
              <span>Sentiment Consistency:</span>
              <strong>${sentiment}%</strong>
            </div>
            <div class="review-cred-tooltip-row">
              <span>Profile Trustworthiness:</span>
              <strong>${profile}%</strong>
            </div>
            <div class="review-cred-tooltip-row">
              <span>Writing Pattern:</span>
              <strong>${pattern}%</strong>
            </div>
          </div>
        `;

        if (bodyEl.parentNode) {
            bodyEl.parentNode.insertBefore(badgeContainer, bodyEl);
        } else {
            bodyEl.insertBefore(badgeContainer, bodyEl.firstChild);
        }



    } catch (err) {
        console.error("ReviewCred: Error injecting score badge", err);
    }
}

function processReviews() {
    try {
        injectStyles();
        
        const reviews = findReviews();
        const newlyProcessed: rev[] = [];
        
        reviews.forEach((review) => {
            // If already processed, skip
            if (review.getAttribute('data-reviewcred-processed') === 'true') return;
            
            const title = extractTitle(review);
            const body = extractBody(review);
            const rating = extractRating(review);

            const reviewData = {
                title,
                rating,
                body,
            };

            extractedReviews.push(reviewData);
            newlyProcessed.push(reviewData);

            injectDummyScore(review, body);
            review.setAttribute('data-reviewcred-processed', 'true');
        });

        if (newlyProcessed.length > 0) {
            console.log("ReviewCred: Processed new reviews:", newlyProcessed);
            console.log("ReviewCred: Accumulated reviews:", extractedReviews);
        }
    } catch (err) {
        console.error("ReviewCred: Error processing reviews", err);
    }
}

function init() {
    // Run initially
    processReviews();

    // Watch for dynamic/lazy-loaded reviews
    const observer = new MutationObserver(() => {
        processReviews();
    });
    const targetNode = document.body || document.documentElement;
    if (targetNode) {
        observer.observe(targetNode, { childList: true, subtree: true });
    }

    // Fallback interval polling to guarantee updates
    setInterval(processReviews, 1000);
}

// Support early run or deferred run
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
} else {
    init();
}