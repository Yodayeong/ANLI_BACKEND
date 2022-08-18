function KindOfHome() {
    var click= document.getElementById('drop-content');

    if(click.style.display === "none"){
        click.style.display = "block";

    }else{
        click.style.display = "none";                 
    }
}

function loadFile(event) {
    var reader = new FileReader();

    reader.onload = function(event) {
      var img = document.createElement("img");
      img.setAttribute("src", event.target.result);
      document.querySelector("div#image_container").appendChild(img);
    };

    reader.readAsDataURL(event.target.files[0]);
}
