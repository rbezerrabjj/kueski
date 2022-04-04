from sqlalchemy import create_engine
import pandas as pd

import boto3, os s3 \= boto3.resource('s3')

path = "/home/ricardo.santos/"

import sys
sys.path.append(f'{path}credentials/')
import credentials as cd
cd = cd.credentials()

from datetime import date, timedelta, datetime


def s3_to_redshift():
    engine = create_engine(f'{driver_postgres}//{user_postgres}:{password_postgres}@{host_postgres}:{port_postgres}/{dbname_postgres}')

# id		flag_own_car	birthday	job_start_date	loan_date	loan_amount
# 5044500	N		1955-08-04	3021-09-18	2019-01-01	133.714973572794

    engine.execute(f"""
                        DROP TABLE IF EXISTS {cd.schema_postgres}.{cd.creditanalysis};
                        CREATE TABLE IF NOT EXISTS {cd.schema_postgres}.{cd.creditanalysis}
                        (
                          {cd.pm_id} integer,
                          {cd.pm_age} integer,
                          {cd.pm_years_on_the_job} integer,
                          {cd.pm_nb_previous_loans} VARCHAR,
                          {cd.pm_avg_amount_loans_previous} VARCHAR,
                          {cd.pm_flag_own_car} VARCHAR,
                          {cd.pm_status} VARCHAR
                        );
                        copy {cd.schema_postgres}.{cd.creditanalysis}
                        from 's3://bucket_analytics/csv_files/train_model.csv'
                        credentials 'aws_access_key_id={cd.aws_access_key};aws_secret_access_key={cd.aws_secret_access_key}'
                        csv
                        delimiter ','
                        IGNOREHEADER 1;
