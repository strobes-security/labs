document.addEventListener('DOMContentLoaded', function() {
    const accountDetailsElement = document.getElementById('accountDetails');
    const showDetailsBtn = document.getElementById('showDetailsBtn');
    const analyticsFrame = document.getElementById('analyticsFrame');
    
    // Fetch secret account details when the button is clicked
    showDetailsBtn.addEventListener('click', async function() {
        try {
            const response = await fetch('/api/secret');
            const data = await response.json();
            
            if (data.secret) {
                // Show the sensitive information
                accountDetailsElement.innerHTML = `
                    <div class="secret-details">
                        <h3>Secret Account Details</h3>
                        <p class="secret-code">Your secret code: ${data.secret}</p>
                        <p class="note">Keep this information secure and do not share it.</p>
                    </div>
                `;
                accountDetailsElement.classList.remove('hidden');
                
                // VULNERABILITY: Send sensitive information using postMessage with wildcard origin
                // This allows any domain to receive this message
                analyticsFrame.contentWindow.postMessage({
                    type: 'accountDetails',
                    secret: data.secret
                }, '*');  // Using '*' instead of specific origin is the vulnerability
                
                console.log('Sent secret to analytics widget');
            }
        } catch (error) {
            console.error('Error fetching secret:', error);
        }
    });
    
    // Listen for messages from the iframe
    window.addEventListener('message', function(event) {
        // VULNERABILITY: No origin check before processing message
        console.log('Received message from iframe:', event.data);
        
        if (event.data.type === 'analytics-ready') {
            console.log('Analytics widget is ready');
        }
    });
});
