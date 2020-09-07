const goBtn = document.getElementById('goBtn');
const linksContainer = document.getElementById('linksContainer');

const url = "<input type ='url'></input>"

goBtn.addEventListener('click', ()=>{
    if(linksContainer.style.visibility == 'hidden'){
        addUrlinp();
    }else{alert("Refresh the page to change no of classes.")}

})

function addUrlinp(){
    const noClass = document.getElementById('noClasses').value;
    if(noClass>0){ 
    for(i = 0; i<noClass; i++){
        var id = 'url' + String(i)
        links = document.getElementById('links');
        const inp = document.createElement('input');
        inp.setAttribute('id', id);
        inp.setAttribute('type', 'url');
        inp.setAttribute('class','url');
        inp.setAttribute('placeholder', 'Enter Url Here')
        links.appendChild(inp);
        linksContainer.style.visibility = 'visible';
    }}else alert("No of Classes can't be zero");
}