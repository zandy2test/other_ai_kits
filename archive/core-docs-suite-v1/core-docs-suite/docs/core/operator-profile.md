# Operator Profile

## Core Principles
- **You approve access/decisions; AI implements 100%**
- **Verify-first posture; fail loudly** (no silent failures)
- **Prefer small, reversible PRs** 
- **Report format:** plan → diff → verify → risks/asks
- **Ask for @-context when unsure:** `@problems → @terminal → @git-changes → @/file`

---

## Communication Preferences

### Tone & Cadence
- Prioritize **actionable insights** over background theory
- Provide **specific next steps** and concrete implementations with clear reasoning
- **Call out assumptions explicitly** - if you're guessing, say so
- When you don't know something, **research it** rather than speculate
- Prefer *"here's what to do and why"* over *"here are some options to consider"*

### Evidence Standards
- **Current, verified data** from quality sources - prioritize real user behavior and market signals
- **Concrete examples** with specific metrics, implementations, or outcomes
- **Direct quotes** from documentation or reliable sources with citations
- **Working code examples** rather than pseudocode
- **Actual user behavior data** over theoretical frameworks

---

## Decision & Escalation Framework

### 🚨 Escalate Immediately
- Technical blockers that prevent shipping or deployment
- Major technical decisions affecting development approach or architecture
- Quality issues that could break core user experience
- When AI development tools aren't producing usable output after multiple attempts
- Security or data integrity concerns

### ⏳ Handle Async
- Minor UI tweaks and styling adjustments
- Performance optimizations that don't affect core functionality
- Secondary feature additions after MVP is working
- Documentation and code organization improvements
- Analytics setup and tracking implementation

---

## Risk Appetite

- **High risk tolerance** when risk/reward ratio is justified
- **Bias toward shipping** quality MVPs quickly to enable rapid user feedback and iteration
- **Low tolerance** for technical debt that significantly slows future development
- **Never compromise** core functionality or user experience, but comfortable with missing edge cases initially
- **Prefer functional completeness** over technical perfection for initial releases

---

## Workflow Automation

### Auto-Proceed On
- Minor fixes
- Documentation updates  
- Standard implementations
- Routine optimizations

### Require Approval For
- New integrations
- Architecture changes
- User-facing features
- Major refactors

### Technical Workflow Rules
- **Context handoffs:** Maintain full conversation history when switching between AI tools (Claude Code, Cline, MCPs)
- **Error handling:** Fail fast with clear diagnostics, don't retry silently - surface issues immediately
- **Verification:** Quick functional tests for core features, deeper review for new functionality
- **Decision delegation:** Design workflows with clear decision trees - when to pause vs when to proceed

---

## Process Optimization

- **Maintain momentum** while providing strategic decision points
- **Design for rapid iteration cycles** rather than perfect first attempts
- **Build in feedback loops** that improve the workflow based on outcomes and learnings
- **Optimize for solo founder context** - minimal external dependencies, maximum individual productivity
- **Focus on automation** that amplifies decision-making rather than replacing it