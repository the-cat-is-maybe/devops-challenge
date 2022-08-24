db.createUser(
    {
        user: "devopsC",
        pwd: "dev0psUs3r",
        roles: [
            {
                role: "readWrite",
                db: "devops-challenge-db"
            }
        ]
    }
);