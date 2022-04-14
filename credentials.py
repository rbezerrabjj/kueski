class Credentials():
    def credentials(self,
                    driver_postgres,
                    host_postgres,
                    user_postgres,
                    dbname_postgres,
                    password_postgres,
                    sslmode_postgres,
                    port_postgres
                    ):

        self.driver_postgres = driver_postgres
        self.host_postgres = host_postgres
        self.user_postgres = user_postgres
        self.dbname_postgres = dbname_postgres
        self.password_postgres = password_postgres
        self.sslmode_postgres = sslmode_postgres
        self.port_postgres = port_postgres

# Redshift
driver_postgres = "postgresql+psycopg2"
host_postgres = "localhost"
user_postgres = input("User_postgres: ") # user
password_postgres = pwinput.pwinput(prompt="Password_postgres: ", mask='*') # password
dbname_postgres = "pocdw"
sslmode_postgres = "require"
port_postgres = "5432"
schema_pstgres = "poc"

# Table creditanalysis
pm_id = "id"
pm_age = "age"
pm_years_on_the_job = "years_on_the_job"
pm_nb_previous_loans = "nb_previous_loans"
pm_avg_amount_loans_previous  = "avg_amount_loans_previous"
pm_flag_own_car = "flag_own_car"
pm_status = "status"
pm_tb_ft_pd = "creditanalysis"

# AWS - fake credentials
aws_access_key_id = ASIARQ6XJZGSIMXLH65K
aws_secret_access_key = shtNlwpC5pSyM4mGQ1Y9EaFqMTbkDUNd2hPa9Grh
aws_session_token = FeU26DXyu+COuadfCL+Ac+2w0+zTli0oHrkHSE396in95aPdeh3nrHDebkZCLhv8+A2sGQx7trZjn/OZwZTsDm2vapA79n5JtYgpPT7Fev+E7B78ie5Z/Ul8+xB7h1fhJLmzKAmX/D0DMfkknqx8fNIf6UCNVbxpPuVTHOGFUoxHyXJ4CqrTlpNQFm+yLbcZ8q1sk1+RrMoB9oMcyc9ByAvHfH6FZWqq28pODokfyePOOa0Og/owGx83+BpB7KOuXmJIGMiusr3RU2uKpoHHwwbWkgfkqPkB30JRihH9BFpcjK35k/gAiMgEPICgMbtx8
aws_security_token = FwoGZXIvYXdzEJb///////ZCLhv8+A2sGQx7trZjn/OZwZTsDm2vapA79n5JtYgpPT7Fev+E7B78ie5Z/Ul8+xB7h1fhJLmzKAmX/D0DMfkknqx8fNIf6UCNVbxpPuVTHJZcMq5DQxIdZDPHjAV2Ct17OhO2bvb8uxMu805F7NJ8QjUJ1IjjjrmwTp575eDy5HCXshwo8P6JBJUOVXA7m2RFpcjK35k/EPICx8

def main():
    pass

if __name__ == "__main__":
    main()
