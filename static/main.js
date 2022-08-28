var output = document.getElementById('output');             
var header = document.getElementById("myHeader");
var sticky = header.offsetTop;
var xhr = new XMLHttpRequest();
console.log("new XMLHttpRequest()");

xhr.open('GET', 'stream');
xhr.send();
console.log("Connected to /stream");
                
var setIntervalId = setInterval(function() {                        
        output.textContent = "\n"+xhr.responseText+"\n";
        console.log("dataLen: " + xhr.responseText.length);
    }, 900);

console.log("XMLHttpRequest ThreadID "+setIntervalId);

function xhrStop(setIntervalId){
    xhr.abort();
    clearInterval(setIntervalId);
    console.log("xhrStop -> XMLHttpRequest.Abort()");
    console.log("Disconnected from /stream");
    console.log("xhrStop -> clearInterval("+setIntervalId+")");
}
                
document.body.addEventListener('DOMSubtreeModified', function () {
    window.scrollTo(0, document.body.scrollHeight);
}, false);

window.onscroll = function() {stickyHeader()};

function stickyHeader() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}