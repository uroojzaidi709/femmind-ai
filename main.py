# main.py

from app.routes import app

def print_summary():
    print("=" * 50)
    print("FemMind AI - Project Complete!")
    print("=" * 50)
    print()
    print("LIVE DEMO: https://uroojzaidi.pythonanywhere.com")
    print()
    print("Features Implemented:")
    print("- 5 Specialized AI Wellness Agents")
    print("- Multi-Agent Coordination System")
    print("- Gemini AI Integration")
    print("- Pandas/NumPy Analytics")
    print("- Beautiful Flask Web UI")
    print()
    print("Thank you for reviewing FemMind AI!")
    print("=" * 50)

if __name__ == "__main__":
    # Print project summary in console
    print_summary()
    
    # Run Flask app locally for testing
    app.run(debug=True)

