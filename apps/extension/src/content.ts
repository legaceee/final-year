console.log("Amazon review loaded");
console.log(window.location.href);

console.log(document.body.innerHTML.includes("review"));
const reviews = document.querySelectorAll('[data-hook="review"]');
type rev={
    title:string,
    body:string,
    rating:string,
}
const extractedReviews:rev[] = [];

reviews.forEach((review) => {

    const title =
        review.querySelector('[data-hook="review-title"]')?.textContent?.trim() ?? "";

    const body =
        review.querySelector('[data-hook="review-body"]')?.textContent?.trim() ?? "";

    const rating =
        review.querySelector('[data-hook="review-star-rating"]')?.textContent?.trim() ?? "";

    extractedReviews.push({
        title,
        rating,
        body,
    });

});

console.log(extractedReviews);