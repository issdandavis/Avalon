# Testing the AI Inbox Management System

## Quick Test (5 Minutes)

### Test 1: Create a Test Issue

1. **Go to your repository**
   ```
   https://github.com/issdandavis/Avalon
   ```

2. **Create a new issue:**
   - Click "Issues" tab
   - Click "New Issue"
   - Title: `Test: AI Inbox Auto-Reply System`
   - Description:
     ```
     This is a test issue to verify the AI inbox management system is working correctly.

     Expected behavior:
     - Auto-reply within 30 seconds
     - Labels applied automatically
     - Issue categorized

     Test created at: [current timestamp]
     ```
   - Click "Submit new issue"

3. **Watch for auto-reply:**
   - Within 30 seconds, you should see an automated comment
   - The comment should include:
     - Category classification
     - Priority level
     - Next steps information

4. **Check labels:**
   - Labels should be applied automatically:
     - `automated:inbox-managed`
     - `question` (or appropriate category)
     - Possibly `priority:high` or `priority:medium`

5. **Result:**
   - ✅ PASS: Auto-reply received, labels applied
   - ❌ FAIL: No auto-reply or labels

---

### Test 2: View Workflow Execution

1. **Go to Actions tab**
   ```
   https://github.com/issdandavis/Avalon/actions
   ```

2. **Find the workflow:**
   - Look for "AI Inbox Management System"
   - Click on the latest run (should be from your test issue)

3. **Check the jobs:**
   - ✅ "Categorize & Auto-Respond" should be green
   - Expand the steps to see:
     - Categorization results
     - Auto-reply sent confirmation
     - Labels applied confirmation

4. **Review logs:**
   - Click on "Categorize GitHub notification"
   - Should show: Category, Priority, Auto-reply decision
   - Click on "Send auto-reply"
   - Should show: "Auto-reply sent to issue"

---

### Test 3: Create a Test PR (Optional)

1. **Create a simple PR:**
   - Create a new branch:
     ```bash
     git checkout -b test/ai-inbox-pr
     echo "# Test PR for AI Inbox" > test-pr.md
     git add test-pr.md
     git commit -m "Test: AI inbox PR auto-reply"
     git push origin test/ai-inbox-pr
     ```

2. **Open PR on GitHub:**
   - Go to "Pull requests" tab
   - Click "New pull request"
   - Select your test branch
     - Title: `Test: AI Inbox PR Auto-Reply`
   - Click "Create pull request"

3. **Watch for auto-reply:**
   - Should receive automated comment within 30 seconds
   - Different template than issue auto-reply
   - Should mention PR review process

4. **Check labels:**
   - `automated:inbox-managed` should be applied
   - Possibly `priority:high`

---

### Test 4: Trigger Manual Inbox Review

1. **Go to Actions tab**

2. **Run workflow manually:**
   - Select "AI Inbox Management System"
   - Click "Run workflow"
   - Select branch: `main`
   - Leave "Force reply" unchecked
   - Click "Run workflow"

3. **Wait for completion** (should take 1-2 minutes)

4. **Download artifacts:**
   - Click on the completed run
   - Scroll to "Artifacts" section
   - Download:
     - `inbox-summary-[number]`
     - `email-templates-[number]`
     - `multi-account-status-[number]` (if scheduled run)

5. **Review artifacts:**
   - Open `inbox-summary.md` → Should show current inbox status
   - Open `email-templates/` → Should contain 3 template files
   - Open `account_status.json` → Should show GitHub account status

---

## Expected Results

### ✅ All Systems Working:

```
Test Issue Created
  ↓
Auto-Reply Received (< 30 seconds)
  ↓
Labels Applied:
  - automated:inbox-managed ✅
  - question ✅
  - priority:medium ✅
  ↓
Workflow Execution: SUCCESS ✅
  ↓
Logs Show:
  - Category: question
  - Priority: medium
  - Auto-reply: sent
  - Labels: applied
```

### ⚠️ Troubleshooting:

If auto-reply doesn't arrive:

1. **Check workflow permissions:**
   - Repository Settings → Actions → General
   - Ensure "Read and write permissions" is enabled

2. **Check if workflow ran:**
   - Actions tab → Recent runs
   - If no run triggered, check workflow file syntax

3. **Check for errors:**
   - Actions tab → Failed runs
   - Review error logs

4. **Check labels exist:**
   - Issues → Labels
   - Create missing labels:
       - `automated:inbox-managed`
       - `bug`
       - `enhancement`
       - `question`
       - `priority:high`
       - `priority:critical`

---

## Advanced Tests

### Test 5: Multi-Platform Sync (If Configured)

1. **Requires GitLab/Bitbucket setup**
2. **Create issue on GitLab**
3. **Wait for daily sync (or trigger manually)**
4. **Check multi-account-status artifact**
5. **Verify cross-platform synchronization**

### Test 6: Email Integration (If Configured)

1. **Requires email API setup**
2. **Send test email to configured address**
3. **Check for auto-reply**
4. **Verify email forwarding to GitHub**

### Test 7: Scheduled Monitoring

1. **Wait for scheduled run (every 6 hours)**
2. **Or adjust schedule in workflow for testing:**
   ```yaml
   schedule:
     - cron: '*/15 * * * *'  # Every 15 minutes for testing
   ```
3. **Review inbox-summary artifacts**
4. **Check for stale item detection**

---

## Performance Benchmarks

### Expected Performance:

| Metric | Target | Acceptable | Needs Improvement |
|--------|--------|------------|-------------------|
| Auto-reply time | < 30 sec | < 60 sec | > 60 sec |
| Workflow run time | < 2 min | < 5 min | > 5 min |
| Label application | 100% | 90%+ | < 90% |
| Categorization accuracy | 95%+ | 85%+ | < 85% |

---

## Test Checklist

### Before Deployment:
- [ ] Create test issue → Verify auto-reply
- [ ] Check labels applied correctly
- [ ] Review workflow logs for errors
- [ ] Verify auto-reply message is professional
- [ ] Test manual workflow trigger
- [ ] Download and review artifacts
- [ ] Create test PR → Verify auto-reply
- [ ] Check categorization accuracy

### Optional Tests:
- [ ] Test with different issue types (bug, feature, question)
- [ ] Test with different label scenarios
- [ ] Test scheduled monitoring (wait 6 hours)
- [ ] Test multi-account sync (if configured)
- [ ] Test email integration (if configured)
- [ ] Performance testing (multiple issues rapidly)
- [ ] Error handling (invalid labels, permissions issues)

---

## Cleanup After Testing

1. **Close test issues:**
   ```
   Label with "test" and close
   ```

2. **Delete test PR:**
   ```bash
   git branch -D test/ai-inbox-pr
   git push origin --delete test/ai-inbox-pr
   ```

3. **Delete test file (if merged):**
   ```bash
   git rm test-pr.md
   git commit -m "Clean up: Remove test file"
   git push
   ```

4. **Adjust schedule back (if changed):**
   ```yaml
   schedule:
     - cron: '0 */6 * * *'  # Back to every 6 hours
   ```

---

## Success Criteria

✅ **System is working if:**
- Auto-replies are sent within 60 seconds
- Labels are applied correctly
- Workflow runs without errors
- Artifacts are generated successfully
- Categorization is accurate
- Messages are professional and helpful

🎉 **Ready for production!**

---

## Monitoring in Production

### Daily Checks:
1. Review inbox-summary artifacts
2. Check for failed workflow runs
3. Verify auto-reply quality
4. Monitor response times

### Weekly Checks:
1. Review categorization accuracy
2. Check stale item reports
3. Verify multi-account sync (if configured)
4. Review and update templates if needed

### Monthly Checks:
1. Audit all auto-replies for quality
2. Update templates based on feedback
3. Review performance metrics
4. Optimize workflow if needed

---

## Getting Help

If tests fail:

1. **Review logs:** Actions tab → Failed runs → Expand steps
2. **Check permissions:** Settings → Actions → Permissions
3. **Verify labels:** Issues → Labels → Create missing
4. **Check syntax:** Validate YAML file
5. **Consult docs:** `docs/INBOX_MANAGEMENT.md`

---

**Once all tests pass, your AI inbox management system is ready to handle all your notifications automatically!** 🎉

---

*Last Updated: 2025-11-25*
