document.getElementById('linkForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const content = document.getElementById('content').value;
    const alias = document.getElementById('alias').value;

    fetch('/create_link', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: content, alias: alias })
    })
    .then(response => response.json())
    .then(data => {
        if (data.link) {
            document.getElementById('result').innerHTML = `<p>Link created: <a href="${data.link}">${data.link}</a></p>`;
        } else {
            document.getElementById('result').innerHTML = `<p>Error: ${data.error}</p>`;
        }
    });
});
