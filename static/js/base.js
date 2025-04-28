document.getElementById('loginform').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log(username,password);
    
  
    if (username === 'ni' && password === '123') {
        alert("Login successful!")
        window.location.href = "/rental/home/";
    } else {
      alert("Try again")
    }
});