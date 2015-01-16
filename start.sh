#! /bin/bash
source bin/activate 
python saposki/saposki.py
rm -r sblog.db
python saposki/sblog1.py