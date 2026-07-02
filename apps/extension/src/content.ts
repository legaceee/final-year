console.log("Amazon review loaded");
console.log(window.location.href);

console.log(document.body.innerHTML.includes("review"));
const reviews = document.querySelectorAll('[data-hook="review"]');

type rev = {
    title: string;
    body: string;
    rating: string;
}

const extractedReviews: rev[] = [];

function extractTitle(review: Element): string {
    // 1. Try to find a span inside the review title (Amazon often nests it inside an anchor tag)
    const titleSpan = review.querySelector('[data-hook="review-title"] span');
    if (titleSpan && titleSpan.textContent?.trim()) {
        return titleSpan.textContent.trim();
    }
    
    // 2. Try the element with class review-title-content or similar
    const titleClassSpan = review.querySelector('.review-title-content span');
    if (titleClassSpan && titleClassSpan.textContent?.trim()) {
        return titleClassSpan.textContent.trim();
    }

    // 3. Try [data-hook="review-title"] directly, cloning to remove rating badges if they are nested inside
    const titleEl = review.querySelector('[data-hook="reviewTitle"]');
    if (titleEl) {
        const clone = titleEl.cloneNode(true) as HTMLElement;
        const ratingBadge = clone.querySelector('.review-rating, [data-hook="review-star-rating"], .a-icon-alt');
        if (ratingBadge) {
            ratingBadge.remove();
        }
        return clone.textContent?.trim() ?? "";
    }
    
    // 4. Try class .review-title directly
    const reviewTitleClass = review.querySelector('.review-title');
    if (reviewTitleClass) {
        const clone = reviewTitleClass.cloneNode(true) as HTMLElement;
        const ratingBadge = clone.querySelector('.review-rating, [data-hook="review-star-rating"], .a-icon-alt');
        if (ratingBadge) {
            ratingBadge.remove();
        }
        return clone.textContent?.trim() ?? "";
    }

    return "";
}

function extractBody(review: Element): string {
    // 1. Try data-hook="review-body"
    const bodyEl = review.querySelector('[data-hook="review-body"]');
    if (bodyEl) {
        const bodySpan = bodyEl.querySelector('span');
        if (bodySpan && bodySpan.textContent?.trim()) {
            return bodySpan.textContent.trim();
        }
        return bodyEl.textContent?.trim() ?? "";
    }

    // 2. Try class .review-text-content
    const textContentEl = review.querySelector('.review-text-content');
    if (textContentEl) {
        const span = textContentEl.querySelector('span');
        if (span && span.textContent?.trim()) {
            return span.textContent.trim();
        }
        return textContentEl.textContent?.trim() ?? "";
    }

    // 3. Try class .review-text
    const textEl = review.querySelector('.reviewRichContentContainer');
    if (textEl && textEl.textContent?.trim()) {
        return textEl.textContent.trim();
    }

    // 4. Try data-hook="review-text-container" (fallback to original)
    const originalBody = review.querySelector('[data-hook="reviewRichContentContainer"]');
    if (originalBody && originalBody.textContent?.trim()) {
        return originalBody.textContent.trim();
    }

    return "";
}

function extractRating(review: Element): string {
    // 1. Try data-hook="review-star-rating"
    const ratingEl = review.querySelector('[data-hook="review-star-rating"]');
    if (ratingEl && ratingEl.textContent?.trim()) {
        return ratingEl.textContent.trim();
    }

    // 2. Try class .review-rating
    const ratingClass = review.querySelector('.review-rating');
    if (ratingClass && ratingClass.textContent?.trim()) {
        return ratingClass.textContent.trim();
    }

    // 3. Try data-hook="cmps-review-star-rating"
    const cmpsRating = review.querySelector('[data-hook="cmps-review-star-rating"]');
    if (cmpsRating && cmpsRating.textContent?.trim()) {
        return cmpsRating.textContent.trim();
    }

    // 4. Try .a-icon-star
    const iconStar = review.querySelector('.a-icon-star');
    if (iconStar && iconStar.textContent?.trim()) {
        return iconStar.textContent.trim();
    }

    return "";
}

reviews.forEach((review) => {
    const title = extractTitle(review);
    const body = extractBody(review);
    const rating = extractRating(review);

    extractedReviews.push({
        title,
        rating,
        body,
    });
});

console.log(extractedReviews);