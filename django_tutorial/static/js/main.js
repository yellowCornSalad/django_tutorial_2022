// navbar 높이 + container높이(#content) + footer높이가 > viewport(창) 
// viewport의 높이보다 크다면
// footer태그의 .fixed-bottom를 삭제

let nav_h = document.querySelector('div.nav').clientHeight;
let con_h = document.querySelector('div#content').clientHeight;
let footer_h = document.querySelector('footer').clientHeight;
console.log(nav_h, con_h, footer_h)
console.log(window.innerHeight)
doc_h = nav_h + con_h + footer_h
if (doc_h >= window.innerHeight) {
    document.querySelector('footer').classList.remove('fixed-bottom')
}