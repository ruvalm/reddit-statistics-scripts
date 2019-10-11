# reddit-statistics-scripts
Collection of scripts that count basic stats from Reddit threads and subs.

## Preparation / Requirements
1. Go to your Reddit account -> Preferences -> apps tab -> click on Create another app button.
2. Fill in the form fields, submit it.
3. Go to this project's config.py file and fill in:
```python
USER_AGENT = <anything that identifies you>
CLIENT_ID = <your client_id that step 2 provided in Reddit>
CLIENT_SECRET = <your client secret that step 2 provided in Reddit>
USERNAME = <your Reddit username>
PASSWORD = <your Reddit password>
```
4. Open your local terminal/console and install praw (via pip, for instance: `pip install praw`).

## Command Line Usage

### count_from_thread.py

Counts upvotes, comments and unique participants from one Reddit Thread:

`python count_from_thread.py <thread_url>`

### count_unique_overlap.py

Counts number of users that participated in 2 distinct Reddit Threads:

`python count_unique_overlap.py <thread_url_1> <thread_url_2>`

### count_all_sub_statistics.py

Counts a sub's number of posts, comments, upvotes and unique participants (up to the latest 1000 threads).

`python count_all_sub_statistics.py <sub_reddit_name>`


## Examples

### count_from_thread.py

```bash
python count_from_thread.py https://www.reddit.com/r/ethfinance/comments/dftses/daily_general_discussion_october_10_2019/
```

### count_unique_overlap.py

```bash
python count_unique_overlap.py https://www.reddit.com/r/ethfinance/comments/dgaxra/daily_general_discussion_october_11_2019/ https://www.reddit.com/r/ethfinance/comments/dd7caw/devcon_v_megathread_is_live/
```

### count_all_sub_statistics.py

```bash
python count_all_sub_statistics.py ethfinance
```
