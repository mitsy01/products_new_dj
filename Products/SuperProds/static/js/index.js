var count = 0 
document.querySelector(".myButton").addEventListener("mouseover", function() {
    var messageDiv = document.querySelector(".message");
    messageDiv.innerHTML = `Тицьнув ${count}` ;
    messageDiv.style.color = "green";
    count += 1;
})