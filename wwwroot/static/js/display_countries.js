async function displayCounties(){
    responce = await fetch('/get_all_countries')
    data = await responce.json()
    console.log(data)
    countryListElement = document.getElementById('search-list-id')

    // displayCountryGuide(data)
    updateCountryValue(data, countryListElement)


    updateCountriesOnInput(data, countryListElement)
    
}


function updateCountriesOnInput(data, countryListElement){
    let myInput = document.getElementById('search');

    myInput.addEventListener('input', function(event) {
        let inputValue = myInput.value;
        let searchResult = data.filter(function(str) {
            return str.toLowerCase().startsWith(inputValue.toLowerCase());
            
        });
        updateCountryValue(searchResult, countryListElement)
    });
}


function updateCountryValue(data, countryListElement){
    countryListElement.innerHTML = ''

    data.forEach(country => {
        listItem = document.createElement('li')
        listItemLinkElement = document.createElement('a')
        listItemLinkElement.href = `country?name=${country}`
        listItemLinkElement.textContent = country

        listItem.appendChild(listItemLinkElement)
        countryListElement.appendChild(listItem)
    });
}

// function displayCountryGuide(data){
//     var markdownContentElement = document.getElementById('markdown-content');

//     fetch(`get_guide?guide_id=${data["guide_id"]}`)
//     .then(response => {
//         const clonedResponse = response.clone();
//         return Promise.all([response.text(), clonedResponse.text()]);
//     })
//     .then(([markdownHtml, clonedHtml]) => {
//         markdownContentElement.innerHTML = markdownHtml;
//     })
//     .catch(error => console.error('Error loading Markdown file:', error));
// }



displayCounties()





