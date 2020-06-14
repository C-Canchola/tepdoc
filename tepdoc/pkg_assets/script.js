let btns = document.getElementsByClassName("file-btn");
let fileLists = document.getElementsByClassName("file-list-initial");

hiddenToggle = {
    false:"visible",
    true: "file-list",

}
btnToggle = {
    true:"file-btn btn-toggle-off",
    false:"file-btn btn-toggle-on",
}

function addListenerToButton(btn, fileList){

    let toggle = true;

    btn.addEventListener('click', function(){
        toggle = !toggle;
        fileList.className = hiddenToggle[toggle];
        btn.className = btnToggle[toggle];
    });
}

for (let i = 0; i<btns.length; i++){
    addListenerToButton(btns[i], fileLists[i]);
}
