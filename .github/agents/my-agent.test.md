Checklist to verify enterprise structure and confirm your automation plan is active

Confirm enterprise policies for automation and security
In the top-right, click your profile picture → Enterprise (or Enterprises → select your enterprise) → Policies.
Under "Policies" → Advanced Security, verify settings that affect repository admins (for example, whether repo admins can enable/disable Secret Protection, GitHub Advanced Security, AI detection in secret scanning, Copilot Autofix). These policies control what automated security/analysis features can be turned on across orgs.
Verify GitHub Actions governance and rollout settings
Ensure your enterprise plan for Actions (governance and compliance) is documented: decide allowed third‑party actions, verified creators or specific whitelists, and whether to allow only GitHub actions.
Confirm organization/repository level Actions controls are set according to that plan (the docs reference configuring allowed actions at repo/org/enterprise levels).
Confirm your runner strategy (GitHub-hosted vs self-hosted) and any private networking (Azure VNET) is in place as planned.
Ensure audit log/exporting of Actions activity is configured if you need longer retention.
Check that required repository workflows are enforced (dependency review example)
If you require a workflow (for example, the dependency-review-action) to pass before merging, verify a repository ruleset exists:
Organization → Settings → Repository → Rulesets → Create or edit a branch ruleset.
Set Enforcement status to Active, add the rule "Require workflows to pass before merging", click Add workflow and select the repository, branch, and workflow file for the dependency review action.
Confirm the workflow file exists in the referenced repo/branch and is configured correctly.
Verify Projects built-in automations are enabled
Open the project → click the menu icon (top-right) → Workflows.
Under "Default workflows" open each workflow you depend on, click Edit, adjust fields if needed, then click Save and turn on workflow.
Confirm initial defaults are active (projects enable workflows that set Status to Done when issues/PRs are closed/merged) and any configured automatic adding or archiving rules are set.
Confirm deployment and environment protections
Ensure secrets storage and environment protections for sensitive deployments are aligned with your plan (use repo/org secrets and consider manual approvals for environments).
Quick validation steps you can run now

Open Enterprise → Policies → Advanced Security and read each setting to confirm they match your intended enforcement.
Pick a sample org → Settings → Actions to confirm allowed actions/runners configuration.
Pick a repository with a required workflow (e.g., dependency review) and confirm the workflow exists and passes on a test PR.
Open a project and check Workflows → ensure required built-in automations are turned on.
If any of these checks do not match your plan, update the relevant enterprise policy, organization/repository Actions settings, ruleset, workflow file, or project workflow via the UI flows described above.

