# Git Scripts Documentation

## stale_branches.txt

**Purpose**: Lists stale branches in a Git repository that haven't had commits in the last 10 days.

**Script**:
```bash
git ls-remote --heads origin | while read -r commit ref; do if [[ -z $(git log -1 --since='10 days ago' --branches="$ref") ]]; then printf "%-30s %s\n" "$(git log -1 --pretty='%an' "$commit")" "$(basename "$ref")"; fi; done
```

**How it works**:
1. `git ls-remote --heads origin` - Lists all remote branches with their commit hashes
2. `while read -r commit ref` - Reads each line, splitting into commit hash and reference
3. `git log -1 --since='10 days ago' --branches="$ref"` - Checks if the branch has any commits in the last 10 days
4. If no recent commits found (`-z` condition), prints the author name and branch name
5. `printf "%-30s %s\n"` - Formats output with author name (30 chars, left-aligned) and branch name

**Output format**:
```
Author Name                     Branch Name
```

**Usage**:
- Run from within any Git repository
- Shows branches that haven't been updated in 10+ days
- Useful for identifying cleanup candidates
- Requires access to remote repository

**Customization**:
- Change `--since='10 days ago'` to adjust the time threshold
- Modify `printf` format to change output formatting