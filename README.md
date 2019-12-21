# database
Database migrations and seeds

---

## To run:
1) Make an `.env` file with a `DATABASE_URL` variable.
    - This should look something like `dialect+driver://username:password@host:port/database`
    
2) Run `pipenv shell`

3) Once the pipenv env is set up run `pipenv install` to install all the
 dependencies.
 
4) In the command line from the root folder run `python migrate_and_seed.py`