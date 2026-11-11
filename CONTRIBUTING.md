# Contributing

1. One PR per entry (or a small batch of related entries) — keeps review easy.
2. Format for each entry:
   ```
   - [Name](link) — one-line description of what it does.
   ```
3. Put it under the right category heading in `README.md`. If none fit, propose a new
   category in the PR description.
4. Only add servers that are maintained — check the repo's last commit isn't ancient and
   it has at least a minimal README.
5. No self-promotion spam: if you're the author of a server you're adding, say so in the
   PR description. That's fine, just be upfront about it.
6. Keep descriptions factual, not marketing copy — what it does, not why it's the best.

## Claude skill contributions

Claude skills are separate from the MCP-server catalog entries. Place each skill at
`.claude/skills/<skill-name>/SKILL.md`, using a lowercase, hyphen-separated directory name
that matches the frontmatter `name` field. Each `SKILL.md` must have non-empty `name` and
`description` fields in YAML frontmatter. Keep reusable supporting material beside the
skill (for example, in a `templates/` subdirectory) and use relative Markdown links so the
skill remains portable when packaged on its own.

Keep skill instructions tool-aware: distinguish the QA method from actions that require an
available tool, environment access, or explicit authorization. Never claim that tests ran
or evidence was collected unless that actually happened. Do not commit credentials, tokens,
customer data, or other secrets in skills or examples.

Before opening a skill PR, run these checks from the repository root (Python 3.10+; no
third-party packages are required):

~~~bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
~~~

The skill validator checks required skill frontmatter fields, skill-name/directory consistency,
duplicate skill names, and inline relative Markdown links inside `.claude/skills/`. It does
not perform a full YAML parse, verify external URLs, or judge whether a skill's QA guidance
is correct.\n\nThe evaluation-matrix validator checks unique case IDs, the required Prompt, Mandatory\nobservations, and Hard failure sections, plus exact coverage between regression cases and\nresult-log rows. It also checks that each result uses PASS, PARTIAL, FAIL, or NOT EVALUATED.\nThese checks validate matrix structure only: they do not run prompts against a model or\ngrade assistant responses. Reviewers must still assess the quality of the scenarios and\nrecorded evaluation evidence.
