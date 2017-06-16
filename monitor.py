#!/usr/bin/env python3

import json
import os
import psycopg2
import time


settings = {
    'database': os.environ.get('DATABASE_NAME'),
    'user': os.environ.get('DATABASE_USER'),
    'password': os.environ.get('DATABASE_PASSWORD'),
    'host': os.environ.get('POSTGRESQL_SERVICE_HOST'),
    'port': os.environ.get('POSTGRESQL_SERVICE_PORT'),
}

REFRESH_TIME = os.environ.get('REFRESH_TIME', 60)

conn1 = psycopg2.connect(**settings)
cur = conn1.cursor()


def get_tx_stat():
    sql = """
    SELECT xact_commit+xact_rollback FROM pg_stat_database WHERE datname = '{}'
    """.format(settings['database'])
    cur.execute(sql)
    conn1.commit()
    return int(cur.fetchone()[0])


def main():
    out = {}
    prev_val = get_tx_stat()
    while True:
        time.sleep(REFRESH_TIME)
        new_val = get_tx_stat()
        tps = (new_val - prev_val) / REFRESH_TIME
        out = {
            'metric_namespace': 'postgres',
            'database_name': settings['database'],
            'refresh_time': REFRESH_TIME,
            'tps': tps
        }
        print(json.dumps(out))


if __name__ == "__main__":
    main()
