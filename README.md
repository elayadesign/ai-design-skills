# AI Design Skills

[![skills.sh](https://skills.sh/b/elayadesign/ai-design-skills)](https://skills.sh/elayadesign/ai-design-skills)

A growing collection of design skills for AI coding tools — Claude Code, Cursor, Codex, Windsurf, and anything else that reads a markdown rules file.

Each skill is a self-contained folder. Install the ones you need.

---

## Skills

| Skill | What it does |
|---|---|
| [`landing-page-design`](./skills/landing-page-design/SKILL.md) | Builds a landing page from scratch — intake questions, page structure, conversion copy, plus a full visual system (type, spacing, radius, motion) |
| [`design-to-motion`](./skills/design-to-motion/SKILL.md) | Turns a static design into a pixel exact animated showcase — empty state to loaded, every visual acting out its story on a loop, background kept untouched, exported as an MP4 for X plus website and 800×500 GIFs |

More on the way. [Upgrading an existing site instead of building new?](https://github.com/elayadesign/redesign-skill) That one lives in its own repo since it predates this collection.

---

## Install

Uses the [skills CLI](https://skills.sh). Needs Node.js.

```bash
npx skills add elayadesign/ai-design-skills
```

It lists the skills in this repo and asks which ones to install and for which agents. Add flags to skip the prompts:

```bash
# one skill
npx skills add elayadesign/ai-design-skills --skill landing-page-design

# pick agents
npx skills add elayadesign/ai-design-skills -a claude-code -a cursor

# user-level instead of project-level
npx skills add elayadesign/ai-design-skills -g

# see what's available without installing
npx skills add elayadesign/ai-design-skills --list
```

Add `-y` to skip confirmations. Skills land in `.claude/skills/` for Claude Code and `.agents/skills/` for Cursor, Codex and other agents. Run `npx skills update` later to pull changes.

Then just ask, in plain language, for what the skill covers.

<details>
<summary><b>Manual install</b></summary>

Claude Code:

```bash
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

Cursor:

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

Codex, Windsurf, other: copy the skill's `SKILL.md` into your tool's rules file.

| Tool | Path |
|---|---|
| Codex | `AGENTS.md` |
| Windsurf | `.windsurfrules` |
| Cline | `.clinerules` |
| Generic | paste into your system prompt |
</details>

<details>
<summary><b>Claude.ai (no terminal)</b></summary>

Download the skill's `SKILL.md` and upload it to a Project, or attach it to a chat and say *"follow this."*
</details>

---

## Make it yours

Every skill's design values (fonts, colors, spacing, motion) live in one section near the bottom of its file. Fork this repo, edit that section, and the rest of the skill follows automatically.

---

## Credits

`design-to-motion` adapts a few general motion rules from [emilkowalski/skills](https://github.com/emilkowalski/skills), [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills), and [dylantarre/animation-principles](https://github.com/dylantarre/animation-principles), all MIT licensed. Details are at the end of [its SKILL.md](./skills/design-to-motion/SKILL.md#credits).

---

## License

MIT. Use it, fork it, ship it, sell what you build with it. No attribution needed.
