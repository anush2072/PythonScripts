Use this alias once:
```bash
git config --global alias.od '!f(){ base="${1:-develop}"; git fetch origin "$base" && git rebase --autostash "origin/$base"; }; f "$@"' && git config --global --get alias.od
```

Then every time on your feature branch:
```bash
git od
```


Why this is the best fit:
- Always gets latest code from develop.
- Keeps your feature branch history clean (no extra merge commits).
- No manual commit created for “sync with develop.”

What it runs internally:
- git fetch origin <branch>
- git rebase --autostash origin/branch_name

What this means:
global alias is parameterized: default develop, but accepts a branch argument when needed
- git od → uses develop by default
- git od dev → rebases onto origin/dev
- git od main → rebases onto origin/main
