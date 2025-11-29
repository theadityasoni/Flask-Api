from flask import Flask
app = Flask(__name__)

@app.route("/")
def profile():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nakul — Portfolio</title>
  <style>
    body { font-family: Arial, sans-serif; margin:0; background:#f4f4f9; color:#333; }
    header { background:#4a90e2; color:white; padding:30px; text-align:center; }
    header h1 { margin:0; }
    nav { margin-top:15px; }
    nav a { color:white; margin:0 12px; text-decoration:none; font-weight:bold; }
    nav a:hover { text-decoration:underline; }
    section { padding:40px; max-width:900px; margin:auto; }
    h2 { color:#4a90e2; }
    .card { background:white; padding:20px; margin:20px 0; border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.1); }
    ul { padding-left:20px; }
    footer { background:#333; color:white; text-align:center; padding:15px; margin-top:30px; }
  </style>
</head>
<body>
  <header>
    <h1>Nakul's Portfolio</h1>
    <p>College Student • Python Developer • Tech Enthusiast</p>
    <nav>
      <a href="#profile">Profile</a>
      <a href="#about">About</a>
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <!-- Profile Section -->
  <section id="profile">
    <div class="card">
      <h2>Profile</h2>
      <p>Hello, I’m Nakul — a motivated college student actively involved in technical projects and strategic analysis for an AI startup. I enjoy hands‑on coding in Python, VBA, and React, and love building original, plagiarism‑free work that communicates ideas clearly.</p>
    </div>
  </section>

  <!-- About Section -->
  <section id="about">
    <div class="card">
      <h2>About Me</h2>
      <p>I’m detail‑oriented, methodical, and proactive. I value clarity, originality, and incremental progress, balancing academic rigor with practical skill development. My focus is on building projects step‑by‑step, testing each phase, and presenting ideas visually and effectively.</p>
    </div>
  </section>

  <!-- Skills Section -->
  <section id="skills">
    <div class="card">
      <h2>Technical Skills</h2>
      <ul>
        <li>Python programming — data structures, file handling, project design</li>
        <li>VBA — PowerPoint automation and slide creation</li>
        <li>React — state, props, and component structure</li>
        <li>Automation — building original tools and scripts</li>
      </ul>
    </div>

    <div class="card">
      <h2>Soft Skills</h2>
      <ul>
        <li>Clear communication of technical ideas</li>
        <li>Structured presentations and reports</li>
        <li>Methodical, detail‑oriented approach</li>
        <li>Originality and creativity in projects</li>
      </ul>
    </div>
  </section>

  <!-- Projects Section -->
  <section id="projects">
    <div class="card">
      <h2>Python Projects</h2>
      <ul>
        <li><strong>ATM Transaction System</strong> — Simulates deposits, withdrawals, and balance checks with secure PIN validation.</li>
        <li><strong>Calculator</strong> — Performs arithmetic operations with a simple interface.</li>
        <li><strong>Jarvis Voice Assistant</strong> — Voice‑controlled assistant that can open apps, search the web, and respond to commands.</li>
      </ul>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact">
    <div class="card">
      <h2>Contact</h2>
      <p>Email: nakul@example.com</p>
      <p>Location: Jaipur, Rajasthan</p>
    </div>
  </section>

  <footer>
    <p>© 2025 Nakul | Portfolio</p>
  </footer>
</body>
</html>
    """
    
if __name__=='__main__':
    app.run()
