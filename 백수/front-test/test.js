const container = document.getElementById('container');
const calander = document.getElementById('calander');
const movieRank = document.getElementById('movieRank');
const dateDiv = document.getElementById('date');
const yesterdayBtn = document.getElementById('yesterdayBtn');
const tomorrowBtn = document.getElementById('tomorrowBtn');
const modal = document.getElementById('modal');
const modalClose = document.getElementById('close');
const modalContent = document.getElementById('content');
const radioBtn = document.getElementsByName('nation');
const darkMode = document.getElementsByName('darkModeSwitch')[0];

const body = document.body;
let now = new Date();
let main_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=85ef7bd4e0f94ce78f0ba83e1cc343e7&targetDt=';

const getDate = (now) =>{
    now = new Date(Date.parse(now)-1000*60*60*24);

    let year = String(now.getFullYear());
    let month = String(now.getMonth()+1);
    let date = String(now.getDate());

    if(month.length === 1){
        month = "0"+ month;
    }
    if(date.length === 1){
        date = "0"+ date;
    }
    let day = year+month+date;
    dateDiv.innerHTML = day;
    
    return day
}

const changeDate = (plus)=>{
    if(plus){
        now = new Date(Date.parse(now)+1000*60*60*24);
    }else{
        now = new Date(Date.parse(now)-1000*60*60*24);
    }

    if(getDate(now) !== getDate(new Date())){
        tomorrowBtn.disabled = false;
    }else{
        tomorrowBtn.disabled = 'disabled';
    }
}

const getNation = () => {
    const radioBtn = document.getElementsByName('nation');
    let ret = '&repNationCd=';

    for(i=0;i<radioBtn.length;i++){
        if(radioBtn[i].checked){
            return ret+radioBtn[i].value;
        }
    }
}
const closeModal = () => {
    modal.classList.remove('show-modal');
    modalContent.innerHTML = '';
}

function DarkMode(){
    var mainLogo = document.getElementById('mainLogo');
    var chkbox = document.getElementsByName('darkModeSwitch')[0];
    var div  = document.getElementsByTagName('div');
    var button = document.getElementsByTagName('button');
    //console.log(chkbox);
    //console.log(mainLogo);
    if(chkbox.checked){
        //chkbox.checked = false;
        mainLogo.style.backgroundColor='blue';
        for(var i =0; i<div.length;i++){
            div[i].style.color = 'blue';
        }
        for(var i =0; i<button.length;i++){
            button[i].style.backgroundColor = 'blue';
            button[i].style.color = 'black';
        }
    }else{
        //chkbox.checked = true;
        mainLogo.style.backgroundColor='black';
        for(var i =0; i<div.length;i++){
            div[i].style.color = 'black';
        }
        for(var i =0; i<button.length;i++){
            button[i].style.backgroundColor = 'black';
            button[i].style.color = 'blue';
        }
    }
}

radioBtn.forEach((nation)=>{
    nation.addEventListener("click",(e)=>{
        const nation = getNation();
        const date = getDate(now);
        const url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=85ef7bd4e0f94ce78f0ba83e1cc343e7&targetDt='+date+nation;
        dateDiv.innerHTML = date;

        ajax(url)
        .then((res)=>{
            movieRankRender(res);
        })
    })
})
yesterdayBtn.addEventListener('click',(e)=>{
    changeDate(false);
    const nation = getNation();
    const date = getDate(now);
    const url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=85ef7bd4e0f94ce78f0ba83e1cc343e7&targetDt='+date+nation;
    dateDiv.innerHTML = date;

    ajax(url)
    .then((res)=>{
        movieRankRender(res);
    })
});
tomorrowBtn.addEventListener('click',(e)=>{
    changeDate(true);
    const nation = getNation();
    const date = getDate(now);
    const url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=85ef7bd4e0f94ce78f0ba83e1cc343e7&targetDt='+date+nation;
    dateDiv.innerHTML = date;

    ajax(url)
    .then((res)=>{
        movieRankRender(res);
    })
});
modalClose.addEventListener("click",(e)=>{
    closeModal();
})
window.addEventListener("click",(e)=>{
    e.target === modal ? closeModal() : false
})
/*
const ajax = (url) =>{
    return new Promise((resolve,reject)=>{
        const xhr = new XMLHttpRequest();
        xhr.open('GET',url,true);
        xhr.onload = () =>{
            if(xhr.status == 200 || xhr.status == 201){
                resolve(JSON.parse(xhr.responseText));
            }else{
                console.error(xhr.responseText);
            }
        }
        xhr.send();
    });
}*/

const ajax = async (url) =>{
    let data = await fetch(url)
    data = data.json()
    return data;
}

const movieRankRender = (res) => {
    console.log(res);
    const rank = res.boxOfficeResult.dailyBoxOfficeList;
    console.log(rank);
    movieRank.innerHTML = "";
    const url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=85ef7bd4e0f94ce78f0ba83e1cc343e7&movieCd=';
    rank.forEach((movie) =>{
        const movieName = document.createElement('div');
        movieName.style.cursor="pointer";
        movieName.addEventListener('click', ()=>{
            modal.classList.add('show-modal')
            ajax(url+movie.movieCd)
            .then((res)=>{
                const movieInfo = res.movieInfoResult.movieInfo;
                const companys = movieInfo.companys;
                companys.forEach((company)=>{
                    const div = document.createElement('div');
                    div.innerHTML = company.companyNm;
                    modalContent.appendChild(div);
                })
            })
        })
        
        movieName.innerHTML = movie.movieNm;
        movieRank.appendChild(movieName);
    })
}
ajax(main_url+getDate(now))
.then((res)=>{
    movieRankRender(res);
})

darkMode.addEventListener("click",DarkMode);