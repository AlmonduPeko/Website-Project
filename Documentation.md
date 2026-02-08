## Requirements to run this Flask App

- *Python* -> `python -m pip install --upgrade pip`
- *Flask* -> `python -m pip install flask`

📚 **Helpful Resource:** `https://www.reddit.com/r/flask/comments/ylu1a9/1_setting_up_your_vscode_for_a_flask_app_for`

## Optional lybrary for self signed SSl Certificate

- *pyopenssl* -> `pip install pyopenssl` -> allow for self signed secure certificate connection.
    Source: `https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https`

- *Jinja* documentation -> `https://jinja.palletsprojects.com/en/stable/templates`

## Configuring Custom Domain for GitHub Pages

### 1. A Records Configuration
Add these four A records:

| Type | Host | Answer |
|------|------|--------|
| A | yourdomain.com | 185.199.108.153 |
| A | yourdomain.com | 185.199.109.153 |
| A | yourdomain.com | 185.199.110.153 |
| A | yourdomain.com | 185.199.111.153 |

### 2. CNAME Record
| Type | Host | Answer |
|------|------|--------|
| CNAME | www.yourdomain.com | username.github.io |

### 3. Repository Setup
Create a `CNAME` file in your repository root containing your naked domain (e.g., `yourdomain.com`)

📖 **Source:** [GitHub Pages Custom Domain Documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain)