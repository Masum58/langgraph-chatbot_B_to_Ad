# Git Workflow Guide (GitHub + Feature Branch + Pull Request)

এক নজরে পুরো চক্র:

```
প্রথমবার: repo বানাও → .gitignore → প্রথম commit → main push
প্রতিটি feature: branch → code → test → commit → push → PR → merge → clean up
```

---

## ধাপ ০: প্রথমবারের Setup (একবারই করতে হয়)

### 0.1 GitHub-এ নতুন repo বানাও
- GitHub → **New repository**
- নাম দাও (যেমন `langgraph-chatbot`), **Private** রাখো
- **README, .gitignore, license কিছুই টিক দিও না** (repo খালি থাকবে, নইলে push-এ গোলমাল হয়)

### 0.2 `.gitignore` বানাও (push-এর আগে, খুবই জরুরি)
Project root-এ `.gitignore` ফাইলে:
```
# Secrets
.env

# Virtual environment
.venv/
venv/

# Python
__pycache__/
*.pyc
.pytest_cache/

# VS Code
.vscode/
```
> `.env` (API key) যেন কখনো GitHub-এ না যায়। `.env.example` (ফাঁকা মান সহ) commit করা যায়।

### 0.3 Local repo তৈরি ও প্রথম commit
```bash
git init
git status                      # .env বা venv দেখা গেলে .gitignore ঠিক করো
git add .
git commit -m "docs: add CLAUDE.md and .gitignore"
```

### 0.4 GitHub-এর সাথে যুক্ত করো ও প্রথম push
```bash
git branch -M main
git remote add origin https://github.com/<তোমার-username>/<repo-name>.git
git push -u origin main
```
> প্রথম push অবশ্যই **`main`**-এ। `main` না থাকলে পরে Pull Request বানানো যায় না।

### 0.5 GitHub-এ default branch যাচাই
Repo → **Settings → General → Default branch** → `main` আছে কিনা দেখো।

---

## ধাপ ১: নতুন Feature শুরু (প্রতিটি feature-এ)

### 1.1 `main` থেকে নতুন branch নাও
```bash
git checkout main
git pull
git checkout -b feature/<feature-name>
```
উদাহরণ: `feature/simple-chatbot`, `feature/rag`, `feature/tools`

### 1.2 Claude Code দিয়ে কাজ
1. `claude` চালাও
2. `Shift+Tab` দিয়ে **plan mode**
3. Plan চাও → পড়ো → approve করো
4. Code হলে **নিজে চালিয়ে test করো**

---

## ধাপ ২: Commit ও Push

```bash
git status                      # কী কী বদলেছে, .env যাচ্ছে না তো?
git add .
git commit -m "feat: <কী যোগ করলে>"
git push -u origin feature/<feature-name>
```
> `-u` শুধু প্রথম push-এ লাগে। পরে শুধু `git push`।
> সঠিক ক্রম: `git push -u origin <branch>` (`git -u origin push` ভুল)।

### Commit message-এর ধরন
| Prefix | কখন |
|---|---|
| `feat:` | নতুন feature |
| `fix:` | bug ঠিক করা |
| `docs:` | documentation / CLAUDE.md |
| `refactor:` | structure বদল, আচরণ একই |
| `test:` | test যোগ |

---

## ধাপ ৩: Pull Request (PR) বানাও ও Merge করো

1. GitHub-এ Repo-তে **Compare & pull request** বাটন আসবে (না এলে নিচের পথ)
2. **Pull requests → New pull request**
   - **base:** `main`
   - **compare:** `feature/<feature-name>`
3. Title দাও → **Create pull request**
4. **Merge pull request → Confirm merge**
5. **Delete branch** চাপো (GitHub থেকে branch মুছে যাবে)

---

## ধাপ ৪: Merge-এর পর Clean up

### 4.1 `main` আপডেট করো ও local branch মোছো
```bash
git checkout main
git pull
git branch -d feature/<feature-name>
```
> `-d` নিরাপদ মোছা। merge না হলে Git আপত্তি করবে।

### 4.2 যাচাই করো
```bash
git branch -a
```

### 4.3 GitHub-এ মোছা branch-এর পুরোনো রেফারেন্স সাফ করো
```bash
git fetch --prune
```

### 4.4 আবার যাচাই করো
```bash
git branch -a
```
এখন শুধু `main` আর `remotes/origin/main` দেখা উচিত।

---

## ধাপ ৫: পরের Feature
- `CLAUDE.md`-এ `Current phase: N` বদলাও
- Claude Code-এ `/clear`
- আবার **ধাপ ১** থেকে শুরু

---

## দ্রুত Cheat Sheet

```bash
# নতুন feature
git checkout main && git pull
git checkout -b feature/<name>

# কাজ শেষে
git add .
git commit -m "feat: ..."
git push -u origin feature/<name>

# GitHub-এ PR → Merge → Delete branch

# Merge-এর পর
git checkout main && git pull
git branch -d feature/<name>
git fetch --prune
git branch -a
```

## সাধারণ সমস্যা ও সমাধান

| সমস্যা | কারণ / সমাধান |
|---|---|
| "Compare & pull request" আসছে না | repo-তে `main` নেই, বা দুই branch একই commit-এ। `main` আগে push করো |
| `LF will be replaced by CRLF` warning | Windows-এর স্বাভাবিক warning, উপেক্ষা করা যায় |
| push করার পর নতুন file GitHub-এ নেই | `git commit` করোনি, শুধু `git add` করেছ |
| `.env` ভুলে commit হয়ে গেছে | API key বাতিল করে নতুন বানাও, তারপর `.gitignore` ঠিক করো |
| `git branch -d` আপত্তি করছে | আগে `git checkout main`, তারপর `git pull` |
| `fatal: ... does not appear to be a git repository` | `origin` বানান ভুল (যেমন `oringin`) |