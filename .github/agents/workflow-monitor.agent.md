# Workflow Monitor Agent

## Purpose
The Workflow Monitor Agent actively monitors the health and status of all GitHub Actions workflows in the repository, catalogues failures, detects output formatting issues, and provides actionable recommendations for maintaining workflow reliability.

## Capabilities

### 1. Workflow Health Monitoring
- **Real-time Status Tracking**: Monitors all workflows using GitHub API
- **Success/Failure Rates**: Calculates success rates across all workflows
- **Recent Run Analysis**: Reviews last 24 hours of workflow activity
- **Trend Detection**: Identifies patterns in workflow failures

### 2. Failure Cataloging
- **Detailed Failure Tracking**: Records workflow name, run ID, and timestamp for each failure
- **Root Cause Analysis**: Examines job logs to identify common failure patterns
- **Historical Reports**: Maintains artifact-based records of all failures
- **Priority Classification**: Flags critical vs. warning-level issues

### 3. Output Formatting Issue Detection
- **Empty Output Detection**: Identifies workflow steps that fail due to empty grep/wc outputs
- **Variable Safety Checks**: Detects missing fallback patterns in bash scripts
- **GITHUB_OUTPUT Validation**: Ensures all outputs follow safety patterns
- **Preventive Recommendations**: Suggests fixes before failures occur

### 4. Automated Recommendations
- **Actionable Guidance**: Provides specific steps to resolve detected issues
- **Best Practices**: Documents workflow output safety patterns
- **Priority Ranking**: Orders recommendations by criticality
- **Status Reports**: Generates comprehensive health reports as artifacts

## Workflow Output Safety Pattern

To prevent workflow failures from empty command outputs, all bash variables that feed into `$GITHUB_OUTPUT` or job outputs should follow this safety pattern:

```bash
# SAFETY: Apply fallback to prevent empty output
VAR=$(command | grep something || echo "0")
VAR=${VAR:-0}
echo "var=$VAR" >> $GITHUB_OUTPUT
```

This triple-layer protection ensures:
1. **First Layer**: `|| echo "0"` provides immediate fallback if command fails
2. **Second Layer**: `${VAR:-0}` applies parameter expansion fallback if variable is empty
3. **Third Layer**: Ensures output is always valid for workflow processing

## Monitoring Schedule

The Workflow Monitor runs:
- **Scheduled**: Twice daily at 6 AM and 6 PM UTC
- **On-Demand**: Via `workflow_dispatch` for immediate health checks
- **After Changes**: Automatically after workflow file modifications

## Output Artifacts

The agent generates several artifacts for each run:

### 1. workflow_summary.md
Complete health report showing:
- All workflows and their recent runs
- Success/failure status for each run
- Detection of output formatting issues
- Summary statistics and success rates

### 2. recommendations.md
Actionable recommendations including:
- Critical issues requiring immediate attention
- Warning-level issues for review
- Best practices documentation
- Workflow failure prevention guidance
- Recent failure analysis

### 3. workflow_failures.txt
Structured log of all failures:
```
workflow_name|run_id|timestamp
ai-scene-writer.yml|12345678|2024-01-29T10:30:00Z
```

## Integration with Other Systems

The Workflow Monitor integrates with:
- **Agent Management Dashboard**: Provides workflow health scores
- **Enterprise Monitoring**: Feeds into overall system health metrics
- **Notification Systems**: Can trigger alerts for critical failures
- **CI/CD Pipeline**: Ensures workflow reliability before merges

## Failure Prevention Features

### Proactive Detection
- Scans all workflow files for unsafe output patterns
- Identifies potential issues before they cause failures
- Provides automated suggestions for improvements

### Safety Enforcement
- Documents required safety patterns
- Generates examples of correct implementations
- Tracks compliance with best practices

### Continuous Improvement
- Learns from past failures
- Updates recommendations based on trends
- Maintains historical data for analysis

## Usage Examples

### Manual Health Check
```bash
gh workflow run agent-management.yml
```

### Check After Workflow Changes
The monitor automatically runs when workflow files are modified, ensuring new workflows follow safety patterns.

### Review Historical Failures
Download artifacts from previous runs to analyze failure trends:
```bash
gh run download <run-id> --name agent-management-reports
```

## Recommendations Output Format

The agent provides recommendations in priority order:

1. **🔴 CRITICAL**: Issues requiring immediate action (e.g., authentication failures, multiple workflow failures)
2. **⚠️ WARNING**: Issues needing attention (e.g., single workflow failure, coordination conflicts)
3. **💡 SUGGESTION**: Best practice improvements (e.g., missing safety patterns)
4. **✅ SUCCESS**: Confirmation of healthy operations

## Technical Details

### API Requirements
- **GitHub Token**: Requires `GITHUB_TOKEN` with `actions: read` permission
- **Rate Limiting**: Respects GitHub API rate limits (5000 requests/hour)
- **Pagination**: Handles large numbers of workflow runs efficiently

### Safety Patterns Applied
All variables in the monitor itself follow the safety pattern to ensure reliable operation:
```bash
VAR=${VAR:-default_value}
```

This ensures the monitor never fails due to its own output issues.

## Maintenance

The Workflow Monitor requires minimal maintenance:
- **Self-Monitoring**: Detects its own potential issues
- **Artifact Retention**: Keeps 30 days of historical reports
- **Automatic Cleanup**: GitHub Actions handles artifact lifecycle
- **Version Control**: All changes tracked in git history

## Future Enhancements

Planned improvements:
- Machine learning-based failure prediction
- Integration with external monitoring services
- Automated PR creation for safety fixes
- Slack/Discord notifications for critical issues
- Custom failure pattern definitions
- Workflow performance benchmarking

## Support

For issues or questions about the Workflow Monitor:
1. Check artifact reports for detailed information
2. Review workflow run logs in GitHub Actions
3. Consult the workflow output safety documentation
4. Open an issue with the `workflow-monitor` label

---

**Last Updated**: 2024-01-29
**Version**: 1.0.0
**Maintainer**: Agent Management System
