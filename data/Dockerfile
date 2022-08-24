FROM mongo
COPY restaurant.json /restaurant.json
COPY mongo-init.js /mongo-init.js
CMD mongoimport --host mongodb --db devops-challenge-db --username devopsC --password dev0psUs3r --collection restaurant --type json --file /restaurant.json