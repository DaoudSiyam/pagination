let apiURL = '/api/videos-list/';
let previousButton;
let nextButton;

function renderVideos(videosData) {
    const videosList = document.getElementById('action');
    videosList.innerHTML = '';

    for (const video of videosData) {
        const categoryHeading = document.createElement('h2');
        categoryHeading.textContent = video.category;
        videosList.appendChild(categoryHeading);
        
        const categoryVideosList = document.createElement('ul');
        const listItem = document.createElement('li');
        listItem.textContent = video.title;
        categoryVideosList.appendChild(listItem);
        videosList.appendChild(categoryVideosList);
    }
}

function renderPagination(pagination) {
    const paginationButtons = document.getElementById('pagination-buttons');
    paginationButtons.innerHTML = '';

    if (pagination.previous) {
        const prevButton = document.createElement('button');
        prevButton.textContent = 'Previous';
        prevButton.addEventListener("click", function(){
            apiURL = `${pagination.previous}`
            fetchVideos(apiURL)
        })
            
        paginationButtons.appendChild(prevButton);
    }
    paginationButtons.appendChild(document.createTextNode(`Page ${pagination.current_page} of ${pagination.total_pages}.`));

    if(pagination.next){
        const nextButton = document.createElement('button');
        nextButton.textContent = 'Next';
        nextButton.addEventListener("click", function(){
            apiURL = `${pagination.next}`
            fetchVideos(apiURL)
        })
        paginationButtons.appendChild(nextButton);
    }
    
}

function fetchVideos(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            renderVideos(data["results"]);
            renderPagination(data);
        })
        .catch(error => console.log('Error fetching videos:', error));
}

// Fetch initial data when the page loads
fetchVideos(`${apiURL}?page=1`);