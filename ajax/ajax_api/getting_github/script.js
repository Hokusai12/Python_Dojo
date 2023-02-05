async function getData() {
    var response = await fetch("https://api.github.com/users/");
    var coderData = await response.json();
    document.querySelector("#github-data").innerHTML += "<h3>" + coderData.name + " has " + coderData.followers + " followers</h3><img src=\"" + coderData.avatar_url + "\">";
    console.log(coderData);
}