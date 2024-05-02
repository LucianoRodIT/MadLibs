document.getElementById("UserInputForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch("/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        var story = data.story;
        document.getElementById("madlibsStory").innerHTML = "<p>" + story + "</p>";
    })
    .catch(error => console.error("Error:", error));
});
