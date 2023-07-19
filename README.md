# relevant-jobs
More quickly find jobs that require or don't require a security clearance

Run with
```
python3 job-getter.py
```

(Or however you run your python scripts locally).

## Explanation

Deloitte has hundreds of job results when you search for 'data engineer' for example. Many require a security clearance and I have had to click into most pages and scan the text to look for that requirement. It's very time consuming and makes it difficult for someone who hasn't had their first clearance yet. This script helps you find the needle in the haystack (jobs that don't require an active security clearance).

It is setup to search for 'python' roles, but you could change the initial url with different search terms. Once it gets results, it accesses each one and saves some details to a CSV file, including the word clearance and some surrounding characters. That way you can look at the CSV in a spreadsheet program and see which jobs require a security clearance or not all on one page (without having to open every job description).

Still being improved. It gives some false negatives (says some jobs don't require a clearance when they do).
