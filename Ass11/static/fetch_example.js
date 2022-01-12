function get_user(index){
    console.log("clicked");
    fetch(`https://reqres.in/api/users/${index}`).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(data){
    const curr_main = document.querySelector("assignment11");
    const section = document.createElement('section');
    section.innerHTML = `
        <img src="${data.avatar}" alt="profile pic"/>
        <div>
            <span>${data.first_name} ${data.last_name}</span>
            <br>
            <a href="mailto:${data.email}">send email</a>
        </div>
        `;
    curr_main.appendChild(section);
}