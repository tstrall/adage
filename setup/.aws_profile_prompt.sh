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

alias aws-login='aws sso login --profile management'

# Set '${AWS_PROFILE}' env variable
aws-profile() {
  export AWS_PROFILE="$1"
  echo "AWS_PROFILE set to $AWS_PROFILE"
}
