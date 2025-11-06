# GitHub Setup Guide

Follow these steps to push your Writer Notes app to GitHub.

## Step 1: Configure Git

Set your GitHub username and email:

```bash
git config --global user.name "Your GitHub Username"
git config --global user.email "your-email@example.com"
```

## Step 2: Add and Commit Files

Add all files and create your first commit:

```bash
git add .
git commit -m "Initial commit: Writer Notes Android app"
```

## Step 3: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `writer-notes-app` (or your preferred name)
3. Description: `A note-taking Android app built with Python and Kivy`
4. **Important**: Do NOT initialize with README, .gitignore, or license
5. Click "Create repository"

## Step 4: Connect and Push

### Option A: Using SSH (Recommended)

```bash
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/writer-notes-app.git
git push -u origin main
```

### Option B: Using HTTPS

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/writer-notes-app.git
git push -u origin main
```

**Note**: Replace `YOUR_USERNAME` with your actual GitHub username.

## Troubleshooting

### If you need to set up SSH keys:

1. Generate a new SSH key:
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

2. Start the ssh-agent:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

3. Copy your public key:
```bash
cat ~/.ssh/id_ed25519.pub
```

4. Add the key to GitHub:
   - Go to https://github.com/settings/keys
   - Click "New SSH key"
   - Paste your public key
   - Click "Add SSH key"

### If you get authentication errors with HTTPS:

GitHub no longer accepts password authentication. You'll need to use a Personal Access Token:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name and select scopes (at least `repo`)
4. Copy the token and use it as your password when pushing

## Success!

Once pushed, your repository will be available at:
`https://github.com/YOUR_USERNAME/writer-notes-app`
