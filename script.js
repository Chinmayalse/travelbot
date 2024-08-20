// static/script.js
function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;
    document.getElementById('chat-box').style.color='black';
    appendMessage('You', userInput);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(userInput)}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chat-box').style.color='black';
        appendMessage('Bot', data.response);
    });

    document.getElementById('user-input').value = '';
    scrollChatToBottom();
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.innerHTML = `<strong>${sender}: </strong> ${message}`;
    chatBox.appendChild(messageElement);
}

function scrollChatToBottom() {
    const chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
}
