const accessKey='x7jA2tA6pjc1G8cfvAtqOG225NkYvTZR2KYPt0ifKZE';
const searchform=document.querySelector('form');
const searhcInput=document.querySelector('.search-input');
const imagesContainer=document.querySelector('.images-container');
const loadMoreBtn=document.querySelector('.loadMoreBtn');

let page=1;
//function to fetch images from api
const fetchImages=async (query,pageNo)=>{  //asynchronous func runs side by side with other code
    //console.log(query);
    try{
    
    if(pageNo===1)
        {
            imagesContainer.innerHTML='';
        }
    

    const url=`https://api.unsplash.com/search/photos/?query=${query}&per_page=28&page=${pageNo}&client_id=${accessKey}`;

    const response= await fetch(url);
    console.log(response);
    const data= await response.json();
    console.table(data);

    if(data.results.length>0){
        
            data.results.forEach(photo => {
                console.table(photo.urls);
                //image element (image specific)
                const imageElement=document.createElement('div');
                imageElement.innerHTML=`<img src="${photo.urls.regular}"/>`;
                imageElement.classList.add('imageDiv');
                
                //image overlay
                const overLayElement=document.createElement('div');
                overLayElement.classList.add('overlay');
        
                //image overlayText
                const overlayText=document.createElement('h3');
                overlayText.innerText=`${photo.alt_description}`;
        
                //append
                imagesContainer.appendChild(imageElement);
                imageElement.appendChild(overLayElement);
                overLayElement.appendChild(overlayText);
        
                if(data.total_pages===pageNo)
                    {
                        loadMoreBtn.style.display="none";
                    }
                else
                {
                    loadMoreBtn.style.display="block";
                }
            });
        }  
    else{
        imagesContainer.innerHTML=`<h2>No Images Found !!</h2>`;
        loadMoreBtn.style.display="none";
    }  
    
    }
    catch(error){
        imagesContainer.innerHTML=`<h2>Failed to catch Images..Please try again later</h2>`;
    }
    
}

//adding event listener to search form


    searchform.addEventListener('submit',(e)=>{
    e.preventDefault(); //prevent auto submission
    //console.log(searhcInput.value); 

    const inpText=searhcInput.value.trim();

    if(inpText!='')
        {
            page=1;
            fetchImages(inpText,page);
        }
    else
    {
        imagesContainer.innerHTML=`<h2>Please enter a search query</h2>`

        if(loadMoreBtn.style.display==="block")
            {
                loadMoreBtn.style.display=none;
            }
    }
})

//adding event listener to load more btn

loadMoreBtn.addEventListener('click',()=>{
    fetchImages(searhcInput.value.trim(),++page)
})
