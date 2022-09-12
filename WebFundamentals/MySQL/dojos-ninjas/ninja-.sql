INSERT INTO dojos (name)
 VALUES ("onsite");

INSERT INTO dojos (name)
 VALUES ("online");

INSERT INTO dojos (name)
 VALUES ("part-time");

DELETE FROM dojos
WHERE id = 1;

 INSERT INTO dojos (name)
 VALUES ("onsite1");
 
  INSERT INTO dojos (name)
 VALUES ("online1");
 
   INSERT INTO dojos (name)
 VALUES ("part-time1");
 
  INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
  VALUES ("Jumana","Saad",26,1);
  INSERT INTO ninjas (first_name, last_name, age, dojo_id)
   VALUES ("Dana","Alhaji",27,1);
    INSERT INTO ninjas (first_name, last_name, age, dojo_id)
   VALUES ("Hanin","Kindah",23,1);
   
   INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
  VALUES ("Sara","Khalil",30,2);
  INSERT INTO ninjas (first_name, last_name, age, dojo_id)
   VALUES ("Hiba","Badir",20,2);
    INSERT INTO ninjas (first_name, last_name, age, dojo_id)
   VALUES ("Bushra","Rahma",29,2);
   
   INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
  VALUES ("Nida","Natsha",35,3);
  INSERT INTO ninjas (first_name, last_name, age, dojo_id)
   VALUES ("Mai","Hamori",39,3);
    INSERT INTO ninjas (first_name, last_name, age, dojo_id)
   VALUES ("Alaa","Jubeh",40,3);
   
 SELECT * FROM dojos 
 LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id  
 WHERE dojos.id = 1; 
 
 SELECT * FROM dojos 
 LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id 
 WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1); 
 
 SELECT * FROM dojos 
 WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1); 


   
   
   
  
  
 
 
