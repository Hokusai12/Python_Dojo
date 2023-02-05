var addUserForm = document.getElementById("add-user-form");
console.log("I swear to got im here bro");

addUserForm.onsubmit = function(e) {
    e.preventDefault();
    
    var formData = new FormData(addUserForm);
    console.log("got here");
    fetch("http://localhost:5000/create_user", { method : 'POST', body : formData })
        .then( response => response.json() )
        .then( data => { console.log(data); } )


    console.log("User JSON: " +  user.email);

    var userTableBody = document.getElementById("user-table").querySelector("tbody");
    userTableBody.innerHTML += 
    `<tr>
        <td>${user.id}</td>
        <td>${user.firstName}</td>
        <td>${user.lastName}</td>
        <td>${user.email}</td>
    </tr>`;
}