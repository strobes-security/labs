document.addEventListener('DOMContentLoaded', function() {
    const widgetContent = document.getElementById('widget-content');
    
    // Notify the parent window that the analytics widget is ready
    window.parent.postMessage({
        type: 'analytics-ready'
    }, '*');
    
    // Listen for messages from parent window
    window.addEventListener('message', function(event) {
        // The widget is not checking the origin of the message (vulnerability)
        if (event.data && event.data.type === 'accountDetails') {
            // Update the widget with the received data
            widgetContent.innerHTML = `
                <p>Analytics data processed successfully!</p>
                <p>User activity score: 87/100</p>
                <p>Last login: Today at 10:32 AM</p>
            `;
            
            console.log('Received account details from parent:', event.data);
        }
    });
});
