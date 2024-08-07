// Function to add messages to the chatbox
function addMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${sender}-message`;
    messageElement.textContent = message;
    document.getElementById('messages').appendChild(messageElement);
    document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight;
}

// Function to handle sending queries
async function sendQuery() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return;

    // Add user message to chatbox
    addMessage('user', userInput);

    // Show loader
    const loader = document.getElementById('loader');
    const loadingDots = document.getElementById('loading-dots');
    loader.style.display = 'inline-block';
    loadingDots.style.display = 'inline-block';

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
        const mistralResponse = data.mistral || 'No response from Mistral';

        // Add bot messages to chatbox
        addMessage('bot', `Mistral says: ${mistralResponse}`);

    } catch (error) {
        console.error('Error:', error);
        addMessage('bot', 'Sorry, there was an error processing your request.');
    } finally {
        // Hide loader
        loader.style.display = 'none';
        loadingDots.style.display = 'none';
        document.getElementById('user-input').value = ''; // Clear input
    }
}

// Function to log mood
function logMood() {
    const moodInput = document.getElementById('mood-input').value;
    if (!moodInput.trim()) return;

    // Show progress bar
    const progressBar = document.getElementById('progress-bar');
    progressBar.style.width = '100%';

    // Generate mood-based message
    const moodMessage = generateMoodMessage(moodInput);

    // Display mood message
    const moodMessageElement = document.getElementById('mood-message');
    moodMessageElement.textContent = moodMessage;

    // Clear mood input
    document.getElementById('mood-input').value = '';

    // Hide progress bar after 1 second
    setTimeout(() => {
        progressBar.style.width = '0%';
    }, 1000);
}

// Function to generate mood-based message
function generateMoodMessage(mood) {
    let message;
    switch (true) {
        case /happy|joy|excited/i.test(mood):
            message = "That's great to hear! Keep spreading the positivity.";
            break;
        case /sad|down|unhappy/i.test(mood):
            message = "I'm sorry you're feeling this way. Remember, it's okay to seek help.";
            break;
        case /angry|frustrated/i.test(mood):
            message = "Take a deep breath. It's important to stay calm.";
            break;
        default:
            message = "Thanks for sharing your mood. How can I assist you further?";
    }
    return message;
}
