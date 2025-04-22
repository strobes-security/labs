from flask import Flask, request, render_template_string
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CustomCards - Personal Greeting Card Generator</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .form-group { margin-bottom: 20px; }
            textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
            input[type="text"] { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
            button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #45a049; }
            .preview { margin-top: 20px; padding: 20px; border: 1px solid #ddd; border-radius: 5px; background-color: #fafafa; }
            .examples { font-size: 0.9em; color: #666; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CustomCards - Personal Greeting Card Generator</h1>
            <p>Create beautiful personalized greeting cards with our easy-to-use generator.</p>
            
            <form method="POST" action="/preview">
                <div class="form-group">
                    <label for="name">Recipient Name:</label>
                    <input type="text" id="name" name="name" placeholder="Enter recipient's name">
                </div>
                
                <div class="form-group">
                    <label for="message">Your Message (supports dynamic content with {{ name }} syntax):</label>
                    <textarea id="message" name="message" rows="5" placeholder="Dear {{ name }}, wishing you a wonderful day!"></textarea>
                    <div class="examples">
                        <p>Examples:</p>
                        <ul>
                            <li>Happy Birthday {{ name }}!</li>
                            <li>Congratulations on your achievement, {{ name }}!</li>
                            <li>Thank you {{ name }} for your support!</li>
                        </ul>
                    </div>
                </div>
                
                <button type="submit">Preview Card</button>
            </form>
            
            <div id="info">
                <h3>Tips for Great Cards:</h3>
                <ul>
                    <li>Use {{ name }} to personalize your message</li>
                    <li>Keep your message concise and meaningful</li>
                    <li>Review your preview before finalizing</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/preview', methods=['POST'])
def preview():
    name = request.form.get('name', 'Friend')
    message = request.form.get('message', 'Have a wonderful day!')
    
    # Vulnerable template rendering - no sanitation of user input
    template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Card Preview</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
            .card {{ background: white; padding: 40px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); text-align: center; }}
            .card h2 {{ color: #333; font-size: 24px; }}
            .card p {{ color: #666; font-size: 18px; line-height: 1.6; }}
            .buttons {{ margin-top: 30px; }}
            .button {{ background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; margin: 0 10px; display: inline-block; }}
            .button.secondary {{ background-color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Card Preview</h1>
            <div class="card">
                <h2>To: {name}</h2>
                <p>{message}</p>
            </div>
            <div class="buttons">
                <a href="/" class="button secondary">Edit Card</a>
                <button onclick="alert('Card would be generated!');" class="button">Generate Card</button>
            </div>
        </div>
    </body>
    </html>
    '''
    
    # Vulnerable rendering without proper sanitation
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
