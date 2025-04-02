# 💰 Cost Management: Budgets, Alerts & Cost Visibility

This guide walks through setting up **spending controls and cost visibility** for a secure AWS account using the Free Tier. These steps help avoid unexpected charges and prepare you for multi-account cost tracking.

---

## 🎯 Goal

- Enable billing alerts
- Create a monthly budget (e.g., $5–$10)
- Turn on Free Tier and usage alerts
- Enable Cost Explorer
- (Optional) Set up cost allocation tagging

---

## ✅ Step 1: Enable Billing Alerts

1. Go to the AWS Console and search for **Billing**
2. In the left menu, click **Billing preferences**
3. Check the boxes:
   - ✅ Receive **Free Tier Usage Alerts**
   - ✅ Receive **Billing Alerts**
4. Save preferences

✅ You’ll now receive email alerts when your usage exceeds Free Tier or budget thresholds.

---

## 💵 Step 2: Create a Monthly Budget

1. In the Billing console, go to **Budgets** → **Create budget**
2. Select **Cost budget**
3. Set:
   - **Name:** `monthly-budget`
   - **Amount:** `$5` or `$10` (whatever level you're comfortable with)
   - **Period:** Monthly
4. Click **Configure alerts**:
   - Alert at 80% and 100% of the budget
   - Enter your email address for notifications

✅ You’ll be notified if your AWS usage exceeds your set budget.

---

## 📈 Step 3: Enable Cost Explorer

1. In the Billing console, click **Cost Explorer**
2. Click **Enable Cost Explorer**

This unlocks visual reports of your AWS usage by service, linked account, and tag.

✅ You can now explore and analyze your AWS costs over time.

---

## 🏷️ Step 4: Enable Cost Allocation Tags (Optional but Recommended)

If you're tagging resources, you can track costs per tag (e.g., `Environment`, `Project`, `Owner`).

1. In the Billing console, go to **Cost allocation tags**
2. You'll see AWS-generated and user-defined tags
3. For each relevant tag (e.g., `Environment`, `Owner`, `CostCenter`), click **Activate**

✅ These tags will appear in billing and Cost Explorer reports within 24 hours.

---

## 🛠️ Optional Advanced: Set up Consolidated Billing for Multiple Accounts

Once you enable AWS Organizations:
- All sub-accounts (`dev`, `prod`) roll up to the **management account**
- Budgets and alerts can be set **per-account** or **globally**

You can:
- Track cost per account
- Use **linked account filtering** in Cost Explorer

---

## 🧩 Optional Tools

- **AWS Budgets Actions:** Can auto-disable services if thresholds are met (e.g., turn off EC2 if over budget)
- **Trusted Advisor:** Shows cost-saving opportunities
- **Third-party tools:** You can integrate with tools like CloudZero or Harness for richer analysis later

---

## ✅ Summary

You now have:
- Free Tier and billing alerts enabled
- A monthly budget with email notifications
- Cost Explorer ready to visualize service usage
- Tag-based cost tracking (if tagging is used)

This setup ensures visibility and control as your AWS usage grows — especially in a multi-account environment.

**Last Updated:** April 2025

