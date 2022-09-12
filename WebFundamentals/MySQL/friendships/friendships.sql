
INSERT INTO users (first_name,last_name)
VALUES ("Rana","Zaro");
INSERT INTO users (first_name,last_name)
VALUES ("Dana","Alhaji");
INSERT INTO users (first_name,last_name)
VALUES ("Sara","Alama");
INSERT INTO users (first_name,last_name)
VALUES ("Mai","Hamori");
INSERT INTO users (first_name,last_name)
VALUES ("Amal","Jubeh");
INSERT INTO users (first_name,last_name)
VALUES ("Nida","Natsha");

INSERT INTO friendships (user_id,friend_id)
VALUES (1,2),(1,4),(1,6);
INSERT INTO friendships (user_id,friend_id)
VALUES (2,1),(2,3),(2,5);
INSERT INTO friendships (user_id,friend_id)
VALUES (3,2),(3,5);
INSERT INTO friendships (user_id,friend_id)
VALUES (4,3);
INSERT INTO friendships (user_id,friend_id)
VALUES (5,1),(5,6);
INSERT INTO friendships (user_id,friend_id)
VALUES (6,2),(6,3);

SELECT users.first_name as first_name, users.last_name as last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users users2 ON users2.id = friendships.friend_id
WHERE users.id = 1;

SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users users2 ON users2.id = friendships.friend_id
ORDER BY first_name;





