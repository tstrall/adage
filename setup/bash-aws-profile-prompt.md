## AWS CLI Profile Prompt & Terminal Title Setup (for Bash)

This guide shows how to enhance your Bash prompt and terminal title bar with the current `AWS_PROFILE` and active Git branch (if inside a Git repo).

You’ll always know which AWS account you're working in, and avoid accidental deployments to the wrong environment.

---

### 1. Copy the Helper Script

Copy the file named `.aws_profile_prompt.sh` to your home directory

```bash
cp .aws_profile_prompt.sh ~
```

---

### 2. Enable It in Your Bash Configuration

Edit your `~/.bashrc` and add the following line at the bottom:

```bash
# Enable AWS_PROFILE + Git-aware prompt
[ -f ~/.aws_profile_prompt.sh ] && source ~/.aws_profile_prompt.sh
```

---

### 3. Apply Immediately

To apply the change without restarting your shell:

```bash
source ~/.aws_profile_prompt.sh
```

---

### 4. Log into AWS using the management profile
```bash
~> aws-login
```

---

### 5. Set `AWS_PROFILE` environment variable

```bash
~> aws-profile dev-iac
AWS_PROFILE set to dev-iac
[dev-iac]~> 
```

---

### Example Prompt

```bash
[dev-iac]~/workspace/aws-config (main)>
```

- `dev-iac` comes from your `AWS_PROFILE`
- `main` is the Git branch
- `~/workspace/aws-config` is your current working directory

The terminal title bar will also reflect your current profile and path.
