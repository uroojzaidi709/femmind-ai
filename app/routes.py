from flask import Blueprint, request, render_template_string
from app.models.agents import WellnessAgents, AgentCoordinator
from app.models.memory import MemorySystem

main_routes = Blueprint('main', __name__)

# Initialize components
memory_system = MemorySystem()
wellness_agents = WellnessAgents()
coordinator = AgentCoordinator(wellness_agents, memory_system)

@main_routes.route('/')
def home():
    """Beautiful homepage with premium health app design"""
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>FemMind AI - Women''s Wellness Companion</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Inter', sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            
            .app-container {
                max-width: 428px;
                margin: 0 auto;
                background: white;
                border-radius: 24px;
                overflow: hidden;
                box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            }
            
            .header {
                background: linear-gradient(135deg, #FF6B8B 0%, #FF8E53 100%);
                color: white;
                padding: 40px 30px 30px;
                text-align: center;
                position: relative;
            }
            
            .app-icon {
                width: 80px;
                height: 80px;
                background: rgba(255,255,255,0.2);
                border-radius: 20px;
                margin: 0 auto 15px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 36px;
                backdrop-filter: blur(10px);
            }
            
            .user-greeting {
                background: rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
                padding: 20px;
                border-radius: 16px;
                margin-top: 20px;
                text-align: left;
            }
            
            .user-avatar {
                width: 50px;
                height: 50px;
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                border-radius: 25px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                margin-bottom: 10px;
            }
            
            .stats-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                padding: 20px;
                background: white;
            }
            
            .stat-card {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                padding: 20px;
                border-radius: 16px;
                text-align: center;
            }
            
            .stat-card.blue {
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            }
            
            .stat-icon {
                width: 50px;
                height: 50px;
                background: rgba(255,255,255,0.2);
                border-radius: 15px;
                margin: 0 auto 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
            }
            
            .feature-grid {
                padding: 20px;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
            }
            
            .feature-card {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 16px;
                text-align: center;
                border: 1px solid #e9ecef;
                transition: transform 0.2s;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
            }
            
            .feature-icon {
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px;
                margin: 0 auto 15px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                color: white;
            }
            
            .chat-section {
                padding: 20px;
                background: white;
            }
            
            .chat-input-container {
                display: flex;
                gap: 10px;
                margin-top: 20px;
            }
            
            .chat-input {
                flex: 1;
                padding: 15px 20px;
                border: 2px solid #e9ecef;
                border-radius: 25px;
                font-size: 14px;
                outline: none;
                transition: border-color 0.3s;
            }
            
            .chat-input:focus {
                border-color: #667eea;
            }
            
            .send-button {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 15px 25px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: 600;
            }
            
            .agent-tags {
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
                margin-top: 15px;
            }
            
            .agent-tag {
                background: linear-gradient(135deg, #FF6B8B 0%, #FF8E53 100%);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
            }
            
            .nav-bottom {
                display: grid;
                grid-template-columns: 1fr 1fr 1fr;
                background: white;
                border-top: 1px solid #e9ecef;
                padding: 15px;
            }
            
            .nav-item {
                text-align: center;
                color: #6c757d;
                text-decoration: none;
                font-size: 12px;
                font-weight: 500;
            }
            
            .nav-item.active {
                color: #667eea;
            }
            
            .nav-icon {
                font-size: 20px;
                margin-bottom: 5px;
            }
            
            /* Wellness Image Section */
            .wellness-image {
                width: 100%;
                height: 120px;
                background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                border-radius: 16px;
                margin: 20px 0;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow: hidden;
            }
            
            .wellness-image::before {
                content: "🌸";
                font-size: 60px;
                opacity: 0.3;
            }
            
            .wellness-text {
                position: absolute;
                color: #333;
                font-weight: 600;
                font-size: 18px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="app-container">
            <!-- Header Section -->
            <div class="header">
                <div class="app-icon">🌺</div>
                <h1>FemMind AI</h1>
                <p>Your Personal Wellness Companion</p>
                
                <div class="user-greeting">
                    <div class="user-avatar">👩</div>
                    <h3>Welcome Back! 👋</h3>
                    <p>Ready for your wellness journey?</p>
                </div>
            </div>
            
            <!-- Wellness Image Banner -->
            <div class="wellness-image">
                <div class="wellness-text">Your Wellness Journey Starts Here 🌟</div>
            </div>
            
            <!-- Stats Grid -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon">🤖</div>
                    <h3>5 AI Experts</h3>
                    <p>Always Available</p>
                </div>
                <div class="stat-card blue">
                    <div class="stat-icon">💬</div>
                    <h3>24/7 Support</h3>
                    <p>Always Listening</p>
                </div>
            </div>
            
            <!-- Feature Grid -->
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">🍎</div>
                    <h4>Nutrition</h4>
                    <p>Diet Plans</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💪</div>
                    <h4>Fitness</h4>
                    <p>Workout Routines</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">😊</div>
                    <h4>Mental Health</h4>
                    <p>Emotional Support</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🌸</div>
                    <h4>Reproductive</h4>
                    <p>Women''s Health</p>
                </div>
            </div>
            
            <!-- Chat Section -->
            <div class="chat-section">
                <h3>💬 Chat with FemMind AI</h3>
                <p style="color: #6c757d; margin-bottom: 15px;">Ask anything about women''s wellness</p>
                
                <form action="/chat" method="post">
                    <div class="chat-input-container">
                        <input type="text" name="message" class="chat-input" 
                               placeholder="How can I support your wellness today?" required>
                        <button type="submit" class="send-button">Send</button>
                    </div>
                </form>
                
                <div class="agent-tags">
                    <span class="agent-tag">Wellness Coach</span>
                    <span class="agent-tag">Nutrition Expert</span>
                    <span class="agent-tag">Fitness Trainer</span>
                    <span class="agent-tag">Mental Health</span>
                    <span class="agent-tag">Reproductive Health</span>
                </div>
            </div>
            
            <!-- Bottom Navigation -->
            <div class="nav-bottom">
                <a href="/" class="nav-item active">
                    <div class="nav-icon">🏠</div>
                    Home
                </a>
                <a href="/analytics" class="nav-item">
                    <div class="nav-icon">📊</div>
                    Analytics
                </a>
                <a href="/chat" class="nav-item">
                    <div class="nav-icon">💬</div>
                    Chat
                </a>
            </div>
        </div>
    </body>
    </html>
    ''')

@main_routes.route('/chat', methods=['POST'])
def chat():
    """Beautiful chat response page with images"""
    user_message = request.form['message']
    user_id = "user_001"
    
    # Process with multi-agent system
    result = coordinator.process_query(user_id, user_message)
    
    # Create agent tags
    agent_tags = ''.join([f'<span class="agent-tag">{agent}</span>' for agent in result['agents_used']])
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>FemMind AI Response</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Inter', sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            
            .app-container {
                max-width: 428px;
                margin: 0 auto;
                background: white;
                border-radius: 24px;
                overflow: hidden;
                box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            }
            
            .header {
                background: linear-gradient(135deg, #FF6B8B 0%, #FF8E53 100%);
                color: white;
                padding: 30px;
                text-align: center;
                position: relative;
            }
            
            .ai-avatar {
                width: 80px;
                height: 80px;
                background: rgba(255,255,255,0.2);
                border-radius: 20px;
                margin: 0 auto 15px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 36px;
                backdrop-filter: blur(10px);
            }
            
            .back-button {
                position: absolute;
                left: 20px;
                top: 30px;
                background: rgba(255,255,255,0.2);
                border: none;
                color: white;
                padding: 10px 15px;
                border-radius: 12px;
                cursor: pointer;
                text-decoration: none;
            }
            
            .chat-container {
                padding: 20px;
                max-height: 60vh;
                overflow-y: auto;
            }
            
            .user-message {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px 20px;
                border-radius: 18px 18px 4px 18px;
                margin: 10px 0;
                max-width: 80%;
                margin-left: auto;
            }
            
            .ai-response {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 18px 18px 18px 4px;
                margin: 10px 0;
                border: 1px solid #e9ecef;
                white-space: pre-wrap;
                line-height: 1.6;
            }
            
            .response-avatar {
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 18px;
                color: white;
                margin-bottom: 10px;
            }
            
            .agents-section {
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                color: white;
                padding: 20px;
                text-align: center;
            }
            
            .agent-tags {
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
                justify-content: center;
                margin-top: 10px;
            }
            
            .agent-tag {
                background: rgba(255,255,255,0.2);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
                backdrop-filter: blur(10px);
            }
            
            .action-buttons {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                padding: 20px;
            }
            
            .action-button {
                padding: 15px;
                border: none;
                border-radius: 12px;
                font-weight: 600;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
                display: block;
            }
            
            .primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            
            .secondary {
                background: #f8f9fa;
                color: #333;
                border: 1px solid #e9ecef;
            }
        </style>
    </head>
    <body>
        <div class="app-container">
            <!-- Header -->
            <div class="header">
                <a href="/" class="back-button">← Back</a>
                <div class="ai-avatar">🤖</div>
                <h2>FemMind AI</h2>
                <p>Wellness Response</p>
            </div>
            
            <!-- Chat Content -->
            <div class="chat-container">
                <div class="user-message">
                    <strong>You:</strong> {{ user_message }}
                </div>
                
                <div class="ai-response">
                    <div class="response-avatar">💡</div>
                    <strong>FemMind AI:</strong><br><br>
                    {{ result.response }}
                </div>
            </div>
            
            <!-- Agents Section -->
            <div class="agents-section">
                <h4>Expert Team Involved</h4>
                <div class="agent-tags">
                    {{ agent_tags | safe }}
                </div>
                <p style="margin-top: 10px; font-size: 12px; opacity: 0.8;">
                    {{ result.agent_count }} specialists collaborated on this response
                </p>
            </div>
            
            <!-- Action Buttons -->
            <div class="action-buttons">
                <a href="/" class="action-button secondary">🏠 Home</a>
                <a href="/analytics" class="action-button primary">📊 Analytics</a>
            </div>
        </div>
    </body>
    </html>
    ''', user_message=user_message, result=result, agent_tags=agent_tags)

@main_routes.route('/analytics')
def analytics():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>FemMind AI Analytics</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 428px;
                margin: 0 auto;
                background: white;
                border-radius: 24px;
                overflow: hidden;
                box-shadow: 0 20px 60px rgba(0,0,0,0.2);
            }
            .header {
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                color: white;
                padding: 30px;
                text-align: center;
            }
            .analytics-content {
                padding: 20px;
            }
            .metric-card {
                background: #f8f9fa;
                padding: 20px;
                margin: 15px 0;
                border-radius: 10px;
                border-left: 5px solid #667eea;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>📊 Analytics Dashboard</h2>
                <p>Your Wellness Journey</p>
            </div>
            <div class="analytics-content">
                <div class="metric-card">
                    <h3>System Status</h3>
                    <p>✅ Multi-agent system active</p>
                    <p>✅ 5 AI experts ready</p>
                    <p>✅ Memory system working</p>
                    <p>✅ Real-time analytics</p>
                </div>
                <div style="text-align: center; margin-top: 20px;">
                    <a href="/" style="color: #667eea; text-decoration: none; font-weight: bold;">← Back to Home</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')
