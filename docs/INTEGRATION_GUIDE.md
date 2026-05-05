# Microsoft Defender for Cloud Integration Guide

This guide walks you through connecting your GitHub repository to Microsoft Defender for Cloud for centralized security monitoring and alert management.

## Prerequisites

- ✅ Azure subscription with Microsoft Defender for Cloud enabled
- ✅ GitHub organization with Admin access
- ✅ GitHub Advanced Security enabled on your repository
- ✅ Appropriate permissions in both environments

## Step-by-Step Integration

### Step 1: Enable GitHub Advanced Security

First, ensure GHAS is enabled on your repository:

1. Navigate to: https://github.com/leandroer/GHAS-MDC-demo/settings/security_analysis
2. Enable the following:
   - ✅ **Dependabot alerts** - Vulnerability detection in dependencies
   - ✅ **Dependabot security updates** - Auto-remediation PRs
   - ✅ **Secret scanning** - Detection of exposed credentials
   - ✅ **Advanced security** - CodeQL and other advanced features

### Step 2: Connect to Microsoft Defender for Cloud

#### 2.1 Open Microsoft Defender for Cloud

1. Go to [Azure Portal](https://portal.azure.com/)
2. Search for **"Microsoft Defender for Cloud"**
3. Click on it to open

#### 2.2 Access Environment Settings

1. In the Defender for Cloud sidebar, find **"Environment settings"**
2. Click on **"Add environment"** (top button)
3. Select **"GitHub"** from the dropdown

#### 2.3 Authorize GitHub

1. Click **"Connect GitHub Account"**
2. You'll be redirected to GitHub to authorize the **Microsoft Security DevOps** app
3. Review and accept the permissions requested
4. The app will request access to:
   - Repository metadata
   - Code scanning results
   - Dependabot alerts
   - Secret scanning findings

#### 2.4 Select Your Organization and Repository

1. After authorization, select your GitHub **organization**
2. Under "Repositories", select:
   - ✅ **GHAS-MDC-demo** (or specify all repositories)
3. Click **"Create"** or **"Connect"**

### Step 3: Configure Defender Settings

Once connected:

1. Return to **Environment settings** in Defender for Cloud
2. Select your GitHub environment
3. Configure:
   - **Data collection**: Enable to pull alerts from GitHub
   - **Alerts and recommendations**: Choose severity levels to monitor
   - **Logging**: Configure diagnostic settings if needed

### Step 4: Trigger Initial Scans

For faster results, manually trigger security scans:

1. Go to your repository: https://github.com/leandroer/GHAS-MDC-demo/actions
2. Under **Workflows**, click:
   - **CodeQL Analysis** → **Run workflow**
   - **Security Audit** → **Run workflow**
3. Wait 5-10 minutes for scans to complete

### Step 5: View Alerts in Defender for Cloud

Once scans complete and data syncs (can take 5-15 minutes):

1. In Microsoft Defender for Cloud, navigate to:
   - **DevOps Security** (sidebar)
   - Or **Settings** → **DevOps Resources**

2. Click on your **GitHub organization**

3. View findings by category:
   - **Secrets** - Exposed credentials found
   - **Dependencies** - Vulnerable packages (from Dependabot)
   - **Code** - Vulnerabilities found by CodeQL
   - **Infrastructure** - Other security issues

## Using Defender for Cloud Dashboard

### Alert Management

The DevOps Security dashboard allows you to:

#### Triage Alerts
- **Review**: Click each alert to see details
- **Assign**: Assign to team members
- **Set Status**: Mark as "Active", "Acknowledged", "Dismissed", "Resolved"
- **Severity**: Filter by Critical, High, Medium, Low

#### Export Findings
- Use **Export** to generate reports for compliance
- Supports CSV, Excel, JSON formats
- Schedule automated exports

#### Set Remediation Priority
1. View recommended remediations
2. Prioritize by:
   - Severity level
   - Attack vector
   - CVSS score
   - Business impact

### Link to Source Code

Each alert includes:
- Direct link to the repository
- Line number where issue was found
- Code snippet showing the vulnerability
- Recommended fix

Click the GitHub link to jump directly to the code in your repository.

## Automating with Workflows

### GitHub Actions Integration

Defender for Cloud can trigger GitHub Actions workflows:

1. Create a workflow file in `.github/workflows/`
2. Configure it to trigger on Defender alerts
3. Example: Auto-create Jira tickets, notify teams, etc.

### Remediation Process

For each vulnerability:

1. **Dependabot Alerts**:
   - Dependabot automatically creates PRs with fixes
   - Review and merge to update dependencies

2. **Code Scanning Alerts**:
   - Review findings in Security tab
   - Fix code vulnerabilities manually
   - Re-run CodeQL to verify

3. **Secret Alerts**:
   - Rotate compromised credentials
   - Remove secrets from code
   - Add to `.gitignore`

## Alert Types You'll See

### Dependabot Findings
- Django 1.11.0 - EOL, multiple CVEs
- requests 2.18.4 - SSL vulnerabilities
- Flask 0.12.0 - Outdated with issues
- PyYAML 3.11 - Code execution vulnerability
- Others from requirements.txt

### CodeQL Findings
- SQL Injection patterns
- Command Injection risks
- Insecure deserialization
- Use of eval/exec
- Hardcoded credentials
- Cross-site scripting (XSS)

### Secret Scanning Findings
- API keys in code
- Database credentials
- Tokens and secrets
- Private key fragments

## Best Practices

### 1. Review Regularly
- Check Defender dashboard weekly
- Don't ignore low-severity findings
- Track remediation progress

### 2. Automate Where Possible
- Enable Dependabot security updates for auto-remediation
- Use GitHub Actions for automated scanning
- Set up notifications for critical findings

### 3. Prioritize Remediation
- Critical and High severity first
- Actively exploited vulnerabilities ASAP
- Address code issues before dependencies

### 4. Track Compliance
- Use exports for audit trails
- Document remediation actions
- Keep compliance teams informed

### 5. Team Communication
- Assign findings to relevant team members
- Use GitHub Issues for remediation tracking
- Set SLAs for fix timelines

## Troubleshooting

### Findings Not Appearing

**Problem**: No alerts showing in Defender for Cloud after 15+ minutes

**Solutions**:
1. Verify GitHub Advanced Security is enabled
2. Check that Dependabot/CodeQL workflows have run
3. Confirm repository was selected during GitHub connection
4. Wait another 10-15 minutes for sync
5. Check Azure Portal for any service health alerts

### Missing Vulnerabilities

**Problem**: Expected vulnerabilities not detected

**Solutions**:
1. Verify requirements.txt has outdated packages
2. Run CodeQL workflow manually
3. Check Dependabot is enabled for pip
4. Review CodeQL configuration
5. Ensure branch protection rules aren't blocking scans

### Authorization Issues

**Problem**: Cannot connect GitHub to Defender

**Solutions**:
1. Verify GitHub organization admin access
2. Check Azure subscription permissions
3. Ensure Microsoft Security DevOps app is authorized
4. Re-authenticate if token expired
5. Check for any organization policies blocking integration

## Advanced Configuration

### Custom Security Policies

Set up custom policies in Defender for Cloud:

1. Go to **Environment settings**
2. Select GitHub environment
3. Configure policy:
   - Alert thresholds
   - Alert types to monitor
   - Auto-remediation rules

### Integration with Other Services

Connect Defender findings to:
- **Microsoft Teams** - Notifications
- **Azure DevOps** - Work items
- **Jira** - Issue tracking
- **Slack** - Team notifications
- **ServiceNow** - ITSM integration

### Reporting

Generate compliance reports:

1. **Security Score** - Overall security posture
2. **Risk Dashboard** - Critical vulnerabilities
3. **Remediation Progress** - Tracking fixes
4. **Trend Analysis** - Security improvements over time

## Resources

- [Microsoft Defender for DevOps Documentation](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction)
- [GitHub Advanced Security Docs](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
- [Dependabot Documentation](https://docs.github.com/en/code-security/dependabot)
- [CodeQL Analysis](https://codeql.github.com/)

## Support

- GitHub Support: https://github.com/support
- Azure Support: https://support.microsoft.com/
- Community Forum: https://github.community/

---

**Last Updated**: 2026-05-05  
**Repository**: GHAS-MDC-demo  
**Owner**: leandroer
