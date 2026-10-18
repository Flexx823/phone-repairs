
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FixPoint Phone Repairs</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #f4f6f8;
                color: #222;
            }

            header {
                background-color: #123456;
                color: white;
                text-align: center;
                padding: 25px;
            }

            nav {
                background-color: #0b2239;
                padding: 12px;
                text-align: center;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin: 12px;
            }

            .hero {
                text-align: center;
                padding: 45px 15px;
                background-color: #dcecff;
            }

            .hero h2 {
                color: #123456;
            }

            .button {
                display: inline-block;
                background-color: #ff9800;
                color: #111;
                padding: 12px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }

            .services {
                padding: 25px;
                text-align: center;
            }

            .service {
                background: white;
                padding: 18px;
                margin: 12px auto;
                max-width: 400px;
                border-radius: 8px;
                box-shadow: 0 2px 6px #ddd;
            }

            footer {
                background-color: #123456;
                color: white;
                text-align: center;
                padding: 18px;
                margin-top: 25px;
            }
        </style>
    </head>

    <body>
        <header>
            <h1>FixPoint Mobile Repairs</h1>
            <p>Your phone, our priority!</p>
        </header>

        <nav>
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
        </nav>

        <section class="hero" id="home">
            <h2>We Fix Phones Fast!</h2>
            <p>Reliable and affordable repairs for your mobile devices.</p>
            <p>Screen repairs, battery replacement, charging issues and more.</p>
            <a class="button" href="#contact">Request a Repair</a>
        </section>

        <section class="services" id="services">
            <h2>Our Services</h2>

            <div class="service">
                <h3>📱 Screen Replacement</h3>
                <p>Cracked or damaged screen repairs.</p>
                <strong>From ₦15,000</strong>
            </div>

            <div class="service">
                <h3>🔋 Battery Replacement</h3>
                <p>Replace weak batteries and improve battery life.</p>
                <strong>From ₦10,000</strong>
            </div>

            <div class="service">
                <h3>🔌 Charging Port Repair</h3>
                <p>Fix charging problems and loose ports.</p>
                <strong>From ₦8,000</strong>
            </div>
        </section>

        <section class="services" id="contact">
            <h2>Contact Us</h2>
            <p>Need your phone repaired? Contact us today.</p>
            <p>Phone: +234 800 000 0000</p>
            <p>Location: Your City, Nigeria</p>
            <a class="button"
               href="https://wa.me/2348000000000">
               Chat on WhatsApp
            </a>
        </section>

        <footer>
            <p>&copy; 2026 FixPoint Mobile Repairs</p>
            <p>Quality repairs. Reliable service.</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
