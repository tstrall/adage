## AWS CLI Profile Prompt & Terminal Title Setup (for Bash)

This guide shows how to enhance your Bash prompt and terminal title bar with the current `AWS_PROFILE` and active Git branch (if inside a Git repo).

You’ll always know which AWS account you're working in, and avoid accidental deployments to the wrong environment.

---

### 1. Save the Script

Create a file named `~/.aws_profile_prompt.sh` and paste the following contents:

```bash
# ~/.aws_profile_prompt.sh

# Show Git branch if in a repo
parse_git_branch() {
  git rev-parse --is-inside-work-tree &>/dev/null || return
  git symbolic-ref --short HEAD 2>/dev/null | awk '{print " (" $0 ")"}'
}

# Build the prompt string
build_prompt() {
  local aws=""
  [ -n "$AWS_PROFILE" ] && aws="[$AWS_PROFILE]"
  local git_branch="$(parse_git_branch)"
  PS1="${aws}\w${git_branch}> "
}

# Set terminal title and prompt
update_prompt_and_title() {
  build_prompt
  local title=""
  [ -n "$AWS_PROFILE" ] && title="[$AWS_PROFILE] "
  title+="$(dirs +0)"  # keeps ~ intact
  echo -ne "\033]0;${title}\007"
}

PROMPT_COMMAND="update_prompt_and_title"
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

### Example Prompt

```bash
[dev-iac]~/workspace/aws-config (main)>
```

- `dev-iac` comes from your `AWS_PROFILE`
- `main` is the Git branch
- `~/workspace/aws-config` is your current working directory

The terminal title bar will also reflect your current profile and path.
