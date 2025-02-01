import sqlite3

from _socket import gethostname


def auto_login():
    con = sqlite3.connect('data/user_data.db')
    cur = con.cursor()
    num_id = gethostname()
    if num_id in [i[0] for i in cur.execute("SELECT num_id FROM users_scores").fetchall()]:
        scores = cur.execute(f"SELECT level_1, level_2, level_3 FROM users_scores WHERE num_id = '{num_id}'").fetchone()
    else:
        cur.execute(f"Insert into users_scores (num_id, level_1, level_2, level_3) VALUES ('{num_id}',"
                    f" '[0, 0/120]', '[0, 0/240]', '[0, 0/360]')")
        con.commit()
        scores = cur.execute(f"SELECT level_1, level_2, level_3 FROM users_scores WHERE num_id = '{num_id}'").fetchone()
    return scores


def save_results_in_db(level, level_stats):
    score = level_stats[0]
    time = level_stats[1]
    con = sqlite3.connect('data/user_data.db')
    cur = con.cursor()
    num_id = gethostname()
    curr_max_score = cur.execute(f"SELECT level_{level} FROM users_scores WHERE num_id = '{num_id}'").fetchone()
    if (eval(curr_max_score[0])[0] < score or
            (eval(curr_max_score[0])[0] == score and eval(curr_max_score[0])[1] > int(time.split('/')[0]) / int(
                time.split(
                    '/')[1]))):
        cur.execute(f"UPDATE users_scores SET level_{level} = '[{score}, {time}]' WHERE num_id = '{num_id}'")
    con.commit()
