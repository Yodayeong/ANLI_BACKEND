function KindOfHome() {
    var click= document.getElementById('kindofhome');
    
    if(click.style.display === "none"){
        click.style.display = "block";

    }else{
        click.style.display = "none";                 
    }
}

document.getElementById('kindofhome').addEventListener('change', function() {
    console.log('You selected: ', this.value);
});


function InputDays() {
    var click= document.getElementById('inputdays');

    if(click.style.display === "none"){
        click.style.display = "block";

    }else{
        click.style.display = "none";                 
    }
}

function InputInfo() {
    var click= document.getElementById('inputinfo');

    if(click.style.display === "none"){
        click.style.display = "block";

    }else{
        click.style.display = "none";                 
    }
}

function readInputFile(e){
    var sel_files = [];
    
    sel_files = [];

    var files = e.target.files;
    var fileArr = Array.prototype.slice.call(files);
    var index = 0;
    
    fileArr.forEach(function(f){
    	if(!f.type.match("image/.*")){
        	alert("이미지 확장자만 업로드 가능합니다.");
            return;
        };
        if(files.length < 11){
        	sel_files.push(f);
            var reader = new FileReader();
            reader.onload = function(e){
                var img = document.createElement("img");
                img.setAttribute("src", e.target.result);
                img.style.width = "30%";
                document.querySelector("div#image").appendChild(img);
                index++;
            };
            reader.readAsDataURL(f);
        }
    })
    if(files.length > 4){
    	alert("최대 10장까지 업로드 할 수 있습니다.");
    }
}
