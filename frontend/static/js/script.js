async function sendQuery() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return;

    // Add user message to chatbox
    addMessage('user', userInput);

    try {
        // Send request to backend
        const response = await fetch('/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: userInput })
        });

        // Check if the response is OK
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();
        console.log('Response Data:', data);

        // Ensure data contains expected fields
        const llamaResponse = data.llama || 'No response from LLaMA';
        const chatgptResponse = data.chatgpt || 'No response from ChatGPT';

        // Add bot messages to chatbox
        // addMessage('bot', `LLaMA says: ${llamaResponse}`);
        addMessage('bot', `ChatGPT says: ${chatgptResponse}`);

    } catch (error) {
        console.error('Error:', error);
        addMessage('bot', 'Sorry, there was an error processing your request.');
    }

    // Clear user input
    document.getElementById('user-input').value = '';
}

function addMessage(role, text) {
    const messages = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}-message`;
    messageDiv.textContent = text;
    messages.appendChild(messageDiv);
    messages.scrollTop = messages.scrollHeight;
}
