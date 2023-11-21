const fruitsData = [
    { "name": "Apple", "description": "A sweet and crisp fruit often red or green in color." },
    { "name": "Banana", "description": "A yellow fruit with a soft and creamy texture." },
    { "name": "Grapes", "description": "Small, round, and usually purple or green in color, often used to make wine." },
    { "name": "Mango", "description": "A tropical fruit with a sweet and fragrant taste." },
    { "name": "Orange", "description": "A citrus fruit known for its juicy and tangy flavor." },
    { "name": "Strawberry", "description": "A red, juicy fruit with tiny seeds on the surface." },
    { "name": "Watermelon", "description": "A large, green fruit with sweet, red or pink flesh and black seeds." }
]

function getResultsContainer() {
    return document.getElementById('search-results');
}

function resetResultsContainer() {
    const resultsContainer = getResultsContainer();
    resultsContainer.innerHTML = '';
}

function addSearchResultToResultsContainer(resultInnerHtml) {
    const resultsContainer = getResultsContainer();
    const resultItem = document.createElement('div');
    resultItem.classList.add('search-result-item');
    resultItem.innerHTML = resultInnerHtml;
    resultsContainer.appendChild(resultItem);
}

function showNoResultsMessage() {
    addSearchResultToResultsContainer('No results found.');
}

function updateUrlWithSearchParameter(keywords) {
    const url = new URL(window.location.href);
    url.searchParams.set('search', keywords);
    window.history.pushState({}, '', url);
}

function getNormalizedSearchInput() {
    const keywords = document.getElementById('search-input').value
    return keywords.toLowerCase();
}

async function searchController() {
    resetResultsContainer();
    const keywords = getNormalizedSearchInput();
    updateUrlWithSearchParameter(keywords);
    if (keywords === 'fruits') {
        if (fruitsData.length === 0) {
            showNoResultsMessage();
        } else {
            fruitsData.forEach(fruit => {
                addSearchResultToResultsContainer(`<strong>${fruit.name}</strong>: ${fruit.description}`);
            });
        }
    } else {
        showNoResultsMessage();
    }
}

document.getElementById('search-form').addEventListener('submit', function (event) {
    event.preventDefault();
    searchController();
});
